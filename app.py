"""
Archivo: app.py

Proyecto: TaskFlow IA - Gestor Inteligente de Tareas

Responsabilidades:
- Inicializar la aplicación Flask.
- Configurar SQLite mediante SQLAlchemy.
- Registrar la API REST de tareas.
- Crear las tablas automáticamente.
- Exponer la interfaz web principal.

Versión consolidada para la actividad:
"Desarrollo de aplicaciones con asistentes de programación basados en IA".
"""

# =====================================================
# IMPORTACIONES
# =====================================================

# Framework principal
from flask import Flask, render_template

# Configuración de la aplicación
# Cambio incorporado durante la evolución de la arquitectura
# para centralizar parámetros técnicos.
from config import Config

# Instancia SQLAlchemy definida en models/tarea.py
from models.tarea import db

# Blueprint con los endpoints REST
# Cambio incorporado al implementar RF-01 al RF-06.
from routes.tarea_routes import tarea_bp


# =====================================================
# CREACIÓN DE LA APLICACIÓN
# =====================================================

app = Flask(__name__)


# =====================================================
# CONFIGURACIÓN
# =====================================================

# Cambio de arquitectura:
# Se sustituye la configuración embebida por una
# configuración centralizada en config.py.
app.config.from_object(Config)


# =====================================================
# INICIALIZACIÓN DEL ORM
# =====================================================

# Asociación entre Flask y SQLAlchemy.
db.init_app(app)


# =====================================================
# REGISTRO DE BLUEPRINTS
# =====================================================

# Cambio incorporado durante la implementación
# de la API REST para desacoplar las rutas
# del archivo principal.
app.register_blueprint(tarea_bp)


# =====================================================
# CREACIÓN AUTOMÁTICA DE TABLAS
# =====================================================

with app.app_context():

    # Cambio incorporado durante la integración
    # de SQLite y SQLAlchemy.
    #
    # Si las tablas no existen se crean automáticamente.
    # Si ya existen, no se modifican.
    db.create_all()


# =====================================================
# RUTA PRINCIPAL
# =====================================================

@app.route("/")
def home():
    """
    Cambio incorporado durante el desarrollo
    del frontend.

    En lugar de mostrar un JSON de prueba,
    se renderiza la interfaz principal de
    TaskFlow IA.
    """

    return render_template("index.html")


# =====================================================
# ENDPOINT DE SALUD DE LA APLICACIÓN
# =====================================================

@app.route("/health")
def health():
    """
    Endpoint técnico para validar rápidamente
    que el backend está operativo.

    Puede utilizarse durante las pruebas,
    monitoreo o depuración.
    """

    return {
        "application": "TaskFlow IA",
        "status": "UP",
        "database": "SQLite",
        "version": "1.0"
    }, 200


# =====================================================
# PUNTO DE INICIO
# =====================================================

if __name__ == "__main__":

    # Configuración para entorno local de desarrollo.
    # El host 0.0.0.0 permite acceder desde otras
    # máquinas de la misma red si fuese necesario.

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )