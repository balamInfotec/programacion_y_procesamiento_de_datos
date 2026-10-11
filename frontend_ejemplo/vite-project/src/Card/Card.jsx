function Card({
    titulo,
    valor
}) {
    return (
        <>
            <div>
                <h1 style={{ backgroundColor: '#1e293b', color: 'white', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                    {titulo}
                </h1>
                <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <h2>{valor}</h2>
                </div>
            </div>
        </>
    )
}

export default Card