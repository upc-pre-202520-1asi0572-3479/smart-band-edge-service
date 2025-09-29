"""
Database initialization for the Smart Band Edge Service

This module sets up the database connection and initializes the database schema.
Sets up the SQLite database and creates required tables for devices and health records
"""

from peewee import SqliteDatabase

# Initialize the SQLite database
db = SqliteDatabase('smart_band.db')

def init_db() -> None:
    """
    Initialize the database and create tables for Device and HealthRecord models.
    """
    db.connect()
    from iam.infrastructure.models import Device
    from health.infrastructure.models import HealthRecord
    db.create_tables([Device, HealthRecord], safe=True)
    db.close()