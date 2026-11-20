from app import app
from models.tarea import db, Tarea
from datetime import date

with app.app_context():

    nueva_tarea = Tarea(
        titulo="Actividad UNIR",
        descripcion="Prueba de SQLAlchemy",
        prioridad="Alta",
        estado="Pendiente",
        fecha_vencimiento=date(2026, 11, 30)
    )

    db.session.add(nueva_tarea)
    db.session.commit()

    print("Registro insertado correctamente")