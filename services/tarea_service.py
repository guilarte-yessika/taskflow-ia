"""
Archivo: services/tarea_service.py

Responsabilidad:
Centralizar la lógica de negocio asociada a la entidad Tarea.

Incidencia corregida:
------------------------------------------------------------
Error:
SQLite Date type only accepts Python date objects as input.

Causa:
La API recibía el campo fecha_vencimiento como string
desde el JSON del request y se intentaba guardar
directamente en una columna SQLAlchemy de tipo Date.

Solución:
Se agrega una función interna para convertir la fecha
recibida en formato YYYY-MM-DD a un objeto date de Python
antes de persistirla en SQLite.
------------------------------------------------------------
"""

from datetime import datetime

from models.tarea import db, Tarea


class TareaService:

    @staticmethod
    def convertir_fecha(fecha_str):
        """
        Convierte una fecha recibida desde JSON
        al tipo date requerido por SQLAlchemy.

        Ejemplo de entrada:
        "2026-11-30"

        Resultado:
        datetime.date(2026, 11, 30)

        Se agrega debido a la incidencia:

        SQLite Date type only accepts Python date objects
        as input.
        """

        if not fecha_str:
            return None

        return datetime.strptime(
            fecha_str,
            "%Y-%m-%d"
        ).date()

    @staticmethod
    def obtener_todas(prioridad=None, estado=None):
        """
        Obtiene todas las tareas.

        Permite aplicar filtros opcionales
        por prioridad y estado.
        """

        query = Tarea.query

        if prioridad:
            query = query.filter_by(
                prioridad=prioridad
            )

        if estado:
            query = query.filter_by(
                estado=estado
            )

        return query.all()

    @staticmethod
    def obtener_por_id(id_tarea):
        """
        Consulta una tarea específica
        mediante su identificador.
        """

        return Tarea.query.get(id_tarea)

    @staticmethod
    def crear(data):
        """
        Registra una nueva tarea.

        Corrección aplicada:
        Se convierte fecha_vencimiento
        de string a objeto date antes
        de realizar el INSERT.
        """

        fecha_vencimiento = (
            TareaService.convertir_fecha(
                data.get("fecha_vencimiento")
            )
        )

        tarea = Tarea(
            titulo=data["titulo"],
            descripcion=data.get("descripcion"),
            prioridad=data.get(
                "prioridad",
                "Media"
            ),
            estado="Pendiente",
            fecha_vencimiento=fecha_vencimiento
        )

        db.session.add(tarea)
        db.session.commit()

        return tarea

    @staticmethod
    def actualizar(id_tarea, data):
        """
        Actualiza los datos de una tarea existente.

        Corrección aplicada:
        Se convierte fecha_vencimiento
        de string a objeto date antes
        de realizar el UPDATE.
        """

        tarea = Tarea.query.get_or_404(
            id_tarea
        )

        tarea.titulo = data.get(
            "titulo",
            tarea.titulo
        )

        tarea.descripcion = data.get(
            "descripcion",
            tarea.descripcion
        )

        tarea.prioridad = data.get(
            "prioridad",
            tarea.prioridad
        )

        if "fecha_vencimiento" in data:

            tarea.fecha_vencimiento = (
                TareaService.convertir_fecha(
                    data.get("fecha_vencimiento")
                )
            )

        db.session.commit()

        return tarea

    @staticmethod
    def cambiar_estado(id_tarea, estado):
        """
        Modifica el estado de una tarea.

        Estados válidos:
        - Pendiente
        - En Progreso
        - Completada
        """

        tarea = Tarea.query.get_or_404(
            id_tarea
        )

        tarea.estado = estado

        db.session.commit()

        return tarea

    @staticmethod
    def eliminar(id_tarea):
        """
        Elimina una tarea de la base de datos.
        """

        tarea = Tarea.query.get_or_404(
            id_tarea
        )

        db.session.delete(tarea)
        db.session.commit()

        return True