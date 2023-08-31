from typing import Dict


def json_err_content(
    status_code: int,
    error_name: str,
    message: str,
) -> Dict[str, str | int]:
    """Function to create json error response.

    Example:
        >>> json_err_content(404, "Not Found", "Not found the page.")
        >>> {
            "status": 404,
            "error": "Not Found",
            "message": "Not found the page."
        }

    :param status_code: Status code of response
    :param error_name: Name of the error
    :param message: Message of the error response
    :returns: Return dict with status_code, error_name, message
    """
    return {
        "status": status_code,
        "error": error_name,
        "message": message,
    }
