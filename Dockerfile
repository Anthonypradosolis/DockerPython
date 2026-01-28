FROM alpine:latest

RUN apk add --no-cache python3

# Crear directorio de trabajo
WORKDIR /app

# Copiar el juego al contenedor
COPY juego_sumar.py /app/

# Hacer el script ejecutable
RUN chmod +x juego_sumar.py

# Comando para ejecutar el juego cuando se inicie el contenedor
CMD ["python3", "juego_sumar.py"]
