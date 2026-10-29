import DeviceStatus from "../components/device/DeviceStatus";
import { useDevice } from "../context/DeviceContext";

export default function DevicePage() {
  const { status } = useDevice();

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4 text-white">Estado del Dispositivo</h2>
      <DeviceStatus status={status} />
    </div>
  );
}
