import datetime
from zoneinfo import ZoneInfo


class Static:
    """Set the Static variables here."""

    GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"  # noqa: S105
    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
    KEY_TOKEN_EXPIRE_TIME = datetime.timedelta(minutes=15)
    TIME_ZONE = ZoneInfo("Asia/Tokyo")


static = Static()
