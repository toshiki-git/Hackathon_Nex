import datetime
from zoneinfo import ZoneInfo


class Static:
    """Set the Static variables here."""

    GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"  # noqa: S105
    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
    MAGIC_LINK_EXPIRE_TIME = datetime.timedelta(minutes=15)
    ACCESS_TOKEN_EXPIRE_TIME = datetime.timedelta(minutes=15)
    REFRESH_TOKEN_EXPIRE_TIME = datetime.timedelta(days=90)
    TIME_ZONE = ZoneInfo("Asia/Tokyo")


static = Static()
