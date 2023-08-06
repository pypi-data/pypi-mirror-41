from calendar import timegm
from datetime import datetime, timedelta

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from jwt_auth import settings
from jwt_auth.core import User
from jwt_auth.utils import jwt_get_user_id_from_payload_handler

jwt_payload_handler = settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = settings.JWT_ENCODE_HANDLER
jwt_decode_handler = settings.JWT_DECODE_HANDLER
jwt_get_user_id_from_payload = settings.JWT_PAYLOAD_GET_USER_ID_HANDLER


def json_web_token_encode_payload(user, orig_iat=None):
    payload = jwt_payload_handler(user)

    if orig_iat is None:
        if settings.JWT_ALLOW_REFRESH:
            # Include original issued at time for a brand new token, to
            # allow token refresh
            payload["orig_iat"] = timegm(datetime.utcnow().utctimetuple())
    else:
        payload["orig_iat"] = orig_iat

    return jwt_encode_handler(payload)


class JSONWebTokenForm(forms.Form):
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(JSONWebTokenForm, self).__init__(*args, **kwargs)

        # Dynamically add the USERNAME_FIELD to self.fields.
        self.fields[self.username_field] = forms.CharField()
        self.object = None

    @property
    def username_field(self):
        try:
            return User.USERNAME_FIELD
        except AttributeError:
            return "username"

    def clean(self):
        cleaned_data = super(JSONWebTokenForm, self).clean()
        credentials = {
            self.username_field: cleaned_data.get(self.username_field),
            "password": cleaned_data.get("password"),
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    raise forms.ValidationError(_("User account is disabled."))

                self.object = {"token": json_web_token_encode_payload(user)}
            else:
                raise forms.ValidationError(
                    _("Unable to login with provided credentials.")
                )
        else:
            raise forms.ValidationError(_("Must include 'username' and 'password'."))


class JSONWebTokenRefreshForm(forms.Form):
    token = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(JSONWebTokenRefreshForm, self).__init__(*args, **kwargs)
        self.object = None

    def clean(self):
        cleaned_data = super(JSONWebTokenRefreshForm, self).clean()

        old_payload = jwt_decode_handler(cleaned_data.get("token"))
        user_id = jwt_get_user_id_from_payload_handler(old_payload)

        # Verify user
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("Unable to login with provided credentials."))

        if not user.is_active:
            raise forms.ValidationError(_("User account is disabled."))

        # Verify orig_iat
        orig_iat = old_payload.get("orig_iat")
        if not orig_iat:
            raise forms.ValidationError(_("orig_iat was missing from payload."))

        # Verify expiration
        refresh_limit = settings.JWT_REFRESH_EXPIRATION_DELTA

        if isinstance(refresh_limit, timedelta):
            refresh_limit = refresh_limit.days * 24 * 3600 + refresh_limit.seconds

        expiration_timestamp = orig_iat + int(refresh_limit)
        now_timestamp = timegm(datetime.utcnow().utctimetuple())

        if now_timestamp > expiration_timestamp:
            raise forms.ValidationError(_("Refresh has expired."))

        # Re-issue new token
        # Include original issued at time for a brand new token,
        # to allow token refresh
        self.object = {"token": json_web_token_encode_payload(user, orig_iat)}
