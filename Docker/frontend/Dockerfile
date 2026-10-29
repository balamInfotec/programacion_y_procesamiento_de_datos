# ============================
# Etapa 1: Construcción con Node
# ============================
FROM node:20-alpine AS build

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de dependencias
COPY package.json package-lock.json ./

# Instalamos dependencias
RUN npm install

# Copiamos el resto del proyecto
COPY . .

# Ejecutamos el build de producción
RUN npm run build


# ============================
# Etapa 2: Servir con Nginx
# ============================
FROM nginx:1.25-alpine

# Eliminamos la configuración por defecto de Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copiamos nuestra configuración personalizada
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiamos el build generado por Vite
COPY --from=build /app/dist /usr/share/nginx/html

# Exponemos el puerto estándar de Nginx
EXPOSE 80

# Iniciamos Nginx en modo foreground
CMD ["nginx", "-g", "daemon off;"]
