from django.conf import settings
from datetime import datetime, timedelta
import random


def get_auth_username(request):
    user = request.user
    username = user.username
    return username


def get_notauth_name(request):

    current_time = datetime.now()

    if "username" in request.session and "uname_timestamp" in request.session:

        stored_timestamp = datetime.fromisoformat(request.session["uname_timestamp"])

        if current_time - stored_timestamp < timedelta(seconds=42):
            return request.session["username"]

    new_username = random.choice(settings.NAMES)

    request.session["username"] = new_username
    request.session["uname_timestamp"] =current_time.isoformat()

    return new_username