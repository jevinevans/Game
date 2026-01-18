"""
Description: Base manager class
Developer: Jevin Evans
Date: 10.8.2023
"""

import funclg.utils.data_mgmt as db
from funclg.utils.input_validation import confirmation, selection_validation, string_validation
import threading


class BaseManager:
    """
    A base manager class that other managers can inherit from.
    """

    def __init__(self, name: str, filename: str):
        """Initialize the base manager."""
        self.name = name
        self.filename = filename
        self.menu = {
            "name": f"Manage {self.name}",
            "description": f"The following are settings to manage {self.name}",
            "menu_items": [],
        }
        self.data = {}
        self.objects = {}

    def load_data(self):
        """Load data from the data source."""
        self.data = db.load_data(self.filename, self.data)
        self.update_data()

    def update_data(self):
        """Update internal data structures."""
        db.update_data(self.filename, self.data)

    def export_data(self):
        """Export data to the data source."""
        db.update_data(self.filename, self.data)

    @staticmethod
    def get_confirmation(prompt: str) -> bool:
        """Get a confirmation from the user."""
        return confirmation(prompt)

    @staticmethod
    def get_selection(
        prompt: str, options: list, display_attr: str = None, return_attr: str = None
    ):
        """Get a selection from the user."""
        return selection_validation(prompt, options, display_attr, return_attr)

    @staticmethod
    def get_string(prompt: str, field_name: str) -> str:
        """Get a validated string input from the user."""
        return string_validation(prompt, field_name)


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with SingletonMeta._lock:
            if cls not in SingletonMeta._instances:
                SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)
        return SingletonMeta._instances[cls]
