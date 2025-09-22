from typing import Optional

import peewee

from iam.domain.entities import Device
from iam.infrastructure.models import Device as DeviceModel


class DeviceRepository:
    """
    Repository for managing Device entities in the IAM context.
    """
    @staticmethod
    def find_by_id_and_api_key(device_id: str, api_key: str) -> Optional[Device]:
        """
        Finds a device by its ID and API key.
        :param device_id: The device ID
        :param api_key: The API key
        :return: Device if found, None otherwise
        """
        try:
            device = DeviceModel.get((DeviceModel.device_id == device_id) & (DeviceModel.api_key == api_key))
            return Device(device_id=device.device_id, api_key=device.api_key, created_at=device.created_at)
        except peewee.DoesNotExist:
            return None

    @staticmethod
    def get_or_create_test_device()->Device:
        """
        Creates or retrieves a test device for testing purposes.
        :return: A test Device instance
        """
        device, _ = DeviceModel.get_or_create(
            device_id="smart-band-001",
            defaults={ "api_key": "test-api-key-123", "created_at": "2025-09-22T10:00:00Z" }
        )
        return Device(device_id=device.device_id, api_key=device.api_key, created_at=device.created_at)