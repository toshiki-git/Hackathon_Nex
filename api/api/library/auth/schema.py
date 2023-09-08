from typing import Optional

from api.web.api.users.schema import UserModelDTO


class AuthenticatedUser(UserModelDTO):
    session_cert: Optional[str] = None

    def __init__(self) -> None:
        super().__init__()

    def __new__(cls):
        return super().__new__(cls)
