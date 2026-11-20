const API_URL = "/api/tasks";

async function obtenerTareas(filtros = "") {

    const response =
        await fetch(`${API_URL}${filtros}`);

    return await response.json();
}

async function crearTarea(data) {

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return await response.json();
}

async function actualizarTarea(id, data) {

    const response =
        await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

    return await response.json();
}

async function eliminarTarea(id) {

    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });
}

async function cambiarEstado(id, estado) {

    const response =
        await fetch(
            `${API_URL}/${id}/estado`,
            {
                method: "PATCH",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    estado
                })
            }
        );

    return await response.json();
}