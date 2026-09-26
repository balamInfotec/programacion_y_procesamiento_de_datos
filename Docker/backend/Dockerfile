# Usa la imagen base oficial de Python 3.11 en una versión ligera
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias al directorio actual
COPY requirements.txt .

# Instala las dependencias de Python sin dejar caché para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY ./app ./app

# Expone el puerto 8000 para que la aplicación sea accesible desde fuera del contenedor
EXPOSE 8000

# Inicia la aplicación con Uvicorn en la dirección 0.0.0.0 y puerto 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
