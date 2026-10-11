export default function DeviceStatus({ status }) {
  return (
    <div className="device-status">
      <h3>Estado del dispositivo</h3>
      <p>Conectado: {status.connected ? "Sí" : "No"}</p>
      <p>Última actualización: {status.lastUpdate}</p>
    </div>
  );
}
