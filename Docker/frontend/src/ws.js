export function connectWS() {
  const ws = new WebSocket("ws://localhost:8000/ws");

  ws.onopen = () => {
    console.log("WebSocket conectado");
  };

  ws.onmessage = (event) => {
    console.log("Mensaje recibido:", event.data);
  };

  ws.onerror = (err) => {
    console.error("Error en WebSocket:", err);
  };

  ws.onclose = () => {
    console.log("WebSocket cerrado");
  };

  return ws;
}
