"""
Peewee ORM models for health records

Defines the HealthRecord database table structure for storing health-related data.
"""
from peewee import Model, AutoField, CharField, FloatField, DateTimeField

from shared.infrastructure.database import db


class HealthRecord(Model):
    """
    ORM Model for the health_records table.
    Represents a health record entry in the database.
    """
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'health_records'