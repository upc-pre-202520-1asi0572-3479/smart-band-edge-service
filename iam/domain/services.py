from typing import Optional

from iam.domain.entities import Device


class AuthService:
    """
    Service for authenticating devices in the IAM context.
    """
    def __init__(self):
        """
        Constructor for AuthService.
        """
        pass

    @staticmethod
    def authenticate(device: Optional[Device])->bool:
        """
        Authenticates a device based on its presence.
        :param device: Device or None
        :return: True if device is valid, False otherwise
        """
        return device is not None