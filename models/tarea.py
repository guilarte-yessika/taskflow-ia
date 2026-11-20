"""
Archivo: models/tarea.py

Modelo de datos para la entidad Tarea utilizando
Flask, SQLAlchemy y SQLite.

Este modelo representa la estructura principal
de la aplicación TaskFlow IA.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Instancia global de SQLAlchemy
db = SQLAlchemy()


class Tarea(db.Model):
    """
    Entidad Tarea.

    Cada registro almacenará la información
    de una tarea gestionada por el usuario.
    """

    # Nombre de la tabla en SQLite
    __tablename__ = "tareas"

    # Identificador único de la tarea
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Título de la tarea
    # Campo obligatorio
    titulo = db.Column(
        db.String(150),
        nullable=False
    )

    # Descripción detallada
    descripcion = db.Column(
        db.Text,
        nullable=True
    )

    # Prioridad de la tarea
    # Valores permitidos:
    # Alta, Media, Baja
    prioridad = db.Column(
        db.String(20),
        nullable=False,
        default="Media"
    )

    # Estado actual de la tarea
    # Valores permitidos:
    # Pendiente
    # En Progreso
    # Completada
    estado = db.Column(
        db.String(20),
        nullable=False,
        default="Pendiente"
    )

    # Fecha de creación automática
    fecha_creacion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    # Fecha límite para completar la tarea
    fecha_vencimiento = db.Column(
        db.Date,
        nullable=True
    )

    def to_dict(self):
        """
        Convierte el objeto Tarea en un
        diccionario para respuestas JSON
        de la API REST.
        """

        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "estado": self.estado,
            "fecha_creacion": (
                self.fecha_creacion.isoformat()
                if self.fecha_creacion else None
            ),
            "fecha_vencimiento": (
                self.fecha_vencimiento.isoformat()
                if self.fecha_vencimiento else None
            )
        }

    def __repr__(self):
        """
        Representación legible para
        depuración y logs.
        """

        return (
            f"<Tarea "
            f"id={self.id}, "
            f"titulo='{self.titulo}', "
            f"estado='{self.estado}'>"
        )