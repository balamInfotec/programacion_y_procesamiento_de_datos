import Card from "../Card/Card"
import { useDashboard } from "./useDashboard"

function Dashboard() {
    const {
        temperatura,
        conectar,
        desconectar
    } = useDashboard()

    return (
        <>
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <button onClick={conectar}>Conectar</button>
                <button onClick={desconectar}>Desconectar</button>
            </div>
            <Card titulo="Temperatura" valor={temperatura} />
        </>
    )
}

export default Dashboard