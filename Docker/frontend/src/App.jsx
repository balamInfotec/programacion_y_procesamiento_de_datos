import DashboardLayout from "./components/layout/DashboardLayout";

function App() {
  return (
    <DashboardLayout>
      <h2 className="text-2xl font-bold mb-4 text-white">Bienvenido al Dashboard IoT</h2>
      <p className="text-slate-300">Aquí mostraremos telemetría, comandos, logs y estado del dispositivo.</p>
    </DashboardLayout>
  );
}

export default App;

