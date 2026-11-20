"""
Archivo: config.py

Configuración centralizada de la aplicación.
"""

class Config:

    # Base de datos SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///taskflow.db"

    # Desactiva eventos innecesarios
    SQLALCHEMY_TRACK_MODIFICATIONS = False