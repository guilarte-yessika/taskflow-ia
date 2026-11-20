const tableBody =
    document.getElementById("taskTableBody");

const form =
    document.getElementById("taskForm");

let tareaEditando = null;


document.addEventListener(
    "DOMContentLoaded",
    cargarTareas
);


async function cargarTareas() {

    const tareas =
        await obtenerTareas();

    renderizarTabla(tareas);
}


function renderizarTabla(tareas) {

    tableBody.innerHTML = "";

    tareas.forEach(tarea => {

        let prioridadClass = "";

        if (tarea.prioridad === "Alta")
            prioridadClass = "priority-high";

        if (tarea.prioridad === "Media")
            prioridadClass = "priority-medium";

        if (tarea.prioridad === "Baja")
            prioridadClass = "priority-low";

        let statusClass = "";

        if (tarea.estado === "Pendiente")
            statusClass = "status-pending";

        if (tarea.estado === "En Progreso")
            statusClass = "status-progress";

        if (tarea.estado === "Completada")
            statusClass = "status-done";

        tableBody.innerHTML += `
        <tr>

            <td>${tarea.id}</td>

            <td>${tarea.titulo}</td>

            <td>
                <span class="${prioridadClass}">
                    ${tarea.prioridad}
                </span>
            </td>

            <td class="${statusClass}">
                ${tarea.estado}
            </td>

            <td>
                ${tarea.fecha_vencimiento || ""}
            </td>

            <td>

                <button
                    class="action-btn edit-btn"
                    onclick="editarTarea(${tarea.id})">
                    Editar
                </button>

                <button
                    class="action-btn delete-btn"
                    onclick="borrarTarea(${tarea.id})">
                    Eliminar
                </button>

            </td>
        </tr>`;
    });
}


form.addEventListener(
    "submit",
    async (e) => {

        e.preventDefault();

        const tarea = {

            titulo:
                document
                .getElementById("titulo")
                .value,

            descripcion:
                document
                .getElementById("descripcion")
                .value,

            prioridad:
                document
                .getElementById("prioridad")
                .value,

            fecha_vencimiento:
                document
                .getElementById("fecha_vencimiento")
                .value
        };

        if (tareaEditando) {

            await actualizarTarea(
                tareaEditando,
                tarea
            );

            tareaEditando = null;

        } else {

            await crearTarea(tarea);
        }

        form.reset();

        cargarTareas();
    }
);


async function borrarTarea(id) {

    if (
        confirm(
            "¿Desea eliminar la tarea?"
        )
    ) {

        await eliminarTarea(id);

        cargarTareas();
    }
}


async function editarTarea(id) {

    const tareas =
        await obtenerTareas();

    const tarea =
        tareas.find(
            t => t.id === id
        );

    document.getElementById("titulo").value =
        tarea.titulo;

    document.getElementById("descripcion").value =
        tarea.descripcion;

    document.getElementById("prioridad").value =
        tarea.prioridad;

    document.getElementById("fecha_vencimiento").value =
        tarea.fecha_vencimiento;

    tareaEditando = id;
}


document
.getElementById("btnFiltrar")
.addEventListener(
    "click",
    async () => {

        const prioridad =
            document.getElementById(
                "filterPrioridad"
            ).value;

        const estado =
            document.getElementById(
                "filterEstado"
            ).value;

        let filtros = "?";

        if (prioridad)
            filtros +=
                `prioridad=${prioridad}&`;

        if (estado)
            filtros +=
                `estado=${estado}`;

        const tareas =
            await obtenerTareas(
                filtros
            );

        renderizarTabla(tareas);
    }
);