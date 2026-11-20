from flask import Blueprint, request, jsonify
from services.tarea_service import TareaService

tarea_bp = Blueprint(
    "tareas",
    __name__,
    url_prefix="/api/tasks"
)

# RF-04 Consultar tareas
# RF-06 Filtrar por estado y prioridad

@tarea_bp.route("", methods=["GET"])
def listar_tareas():

    prioridad = request.args.get("prioridad")
    estado = request.args.get("estado")

    tareas = TareaService.obtener_todas(
        prioridad,
        estado
    )

    return jsonify(
        [tarea.to_dict() for tarea in tareas]
    )


# RF-04 Consultar tarea por id

@tarea_bp.route("/<int:id_tarea>", methods=["GET"])
def obtener_tarea(id_tarea):

    tarea = TareaService.obtener_por_id(
        id_tarea
    )

    if not tarea:
        return jsonify(
            {"error": "Tarea no encontrada"}
        ), 404

    return jsonify(
        tarea.to_dict()
    )


# RF-01 Registrar tarea

@tarea_bp.route("", methods=["POST"])
def crear_tarea():

    data = request.get_json()

    if not data.get("titulo"):
        return jsonify(
            {"error": "El título es obligatorio"}
        ), 400

    tarea = TareaService.crear(data)

    return jsonify(
        tarea.to_dict()
    ), 201


# RF-02 Modificar tarea

@tarea_bp.route("/<int:id_tarea>", methods=["PUT"])
def actualizar_tarea(id_tarea):

    data = request.get_json()

    tarea = TareaService.actualizar(
        id_tarea,
        data
    )

    return jsonify(
        tarea.to_dict()
    )


# RF-05 Cambiar estado

@tarea_bp.route(
    "/<int:id_tarea>/estado",
    methods=["PATCH"]
)
def cambiar_estado(id_tarea):

    data = request.get_json()

    estado = data.get("estado")

    estados_validos = [
        "Pendiente",
        "En Progreso",
        "Completada"
    ]

    if estado not in estados_validos:
        return jsonify(
            {"error": "Estado inválido"}
        ), 400

    tarea = TareaService.cambiar_estado(
        id_tarea,
        estado
    )

    return jsonify(
        tarea.to_dict()
    )


# RF-03 Eliminar tarea

@tarea_bp.route("/<int:id_tarea>", methods=["DELETE"])
def eliminar_tarea(id_tarea):

    TareaService.eliminar(id_tarea)

    return jsonify(
        {"mensaje": "Tarea eliminada"}
    )
