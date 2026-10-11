import { useState } from "react"
import { createWebSocket } from "../services/websocketService";

export function useDashboard() {
    const [websocket, setWebsocket] = useState(null);
    const [temperatura, setTemperatura] = useState(null);

    function mensajeRecibido(data) {
        console.log("Mensaje recibido del websocket:", data);
        // PASO 8: Actualizamos el estado de la temperatura con los datos recibidos
        setTemperatura(data.metrics.temperature);
    }

    function conectar() {
        console.log("Click en el botón Conectar");

        // PASO 7: Agregar la conexión al websocket, usando la función createWebSocket del servicio websocketService.js
        const ws = createWebSocket(mensajeRecibido);
        setWebsocket(ws);
    }

    function desconectar() {
        if(websocket) {
            websocket.close();
            setWebsocket(null);
            console.log("Conexión del websocket cerrada");
        }
    }

    return {
        temperatura,
        conectar,
        desconectar
    }
}