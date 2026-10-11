import { useTelemetry } from "../context/TelemetryContext";
import GaugeChart from "../components/charts/GaugeChart";

export default function TelemetryPage() {
  const { metrics } = useTelemetry();

  if (!metrics || Object.keys(metrics).length === 0) {
    return <p className="text-slate-400">Esperando datos de telemetría...</p>;
  }

  return (
    <div className="space-y-8">
      <h2 className="text-2xl font-bold text-white">Telemetría</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {Object.entries(metrics).map(([metric, value]) => (
          <GaugeChart
            key={metric}
            metricName={metric}
            value={value}
            min={0}
            max={metric === "voltage" ? 5 : 100} // ejemplo
          />
        ))}
      </div>
    </div>
  );
}
