"""
Description: Base manager class
Developer: Jevin Evans
Date: 10.8.2023
"""


class BaseManager:
    """
    A base manager class that other managers can inherit from.
    """

    @staticmethod
    def load_data():
        raise NotImplementedError

    @staticmethod
    def update_data():
        raise NotImplementedError

    @staticmethod
    def export_data():
        raise NotImplementedError