                    JUEGO DE SUMAR - DOCKER

DESCRIPCIÓN:

Este proyecto contiene un juego simple de sumar números implementado en Python,
configurado para ejecutarse en un contenedor Docker basado en Alpine Linux.

CONTENIDO DEL PAQUETE:

- juego_sumar.py : Código fuente del juego en Python
- Dockerfile     : Archivo de configuración para construir la imagen Docker
- readme.txt     : Este archivo con las instrucciones

REQUISITOS PREVIOS:

- Docker instalado y funcionando en tu sistema
- Permisos para ejecutar comandos Docker


INSTRUCCIONES DE USO:

1. CONSTRUIR LA IMAGEN DOCKER:
   
   Desde el directorio que contiene el Dockerfile, ejecuta:
   
   docker build -t juego-sumar .
   
   Esto creará una imagen llamada "juego-sumar" basada en Alpine Linux
   con Python 3 y el juego instalado.


2. EJECUTAR EL CONTENEDOR:
   
   Para iniciar el juego, ejecuta:
   
   docker run -it --rm juego-sumar
   
   Explicación de los parámetros:
   -i  : Modo interactivo (permite la entrada del usuario)
   -t  : Asigna una pseudo-TTY (terminal)
   --rm: Elimina el contenedor automáticamente al salir
   
   ¡IMPORTANTE! --> Los flags -it son necesarios para poder interactuar con el juego.


CÓMO JUGAR:
----------
1. El juego te presentará sumas aleatorias de números del 1 al 100
2. Escribe la respuesta correcta y pulsa Enter
3. El juego te dirá si acertaste y mostrará tu puntuación
4. Para salir, escribe "salir" o presiona Ctrl+C
5. Al finalizar verás tus estadísticas finales
