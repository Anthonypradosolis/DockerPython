# Script para crear el archivo comprimido .tgz

Write-Host "Creando archivo comprimido apelido_nome_docker1.tgz..." -ForegroundColor Green

# Ir al directorio padre
Set-Location -Path "C:\Users\a25anthonyps\ASIGNATURAS\DAW\2TRIMESTRE"

# Crear archivo tar.gz usando tar (disponible en Windows 10+)
tar -czf apelido_nome_docker1.tgz -C aplicacionDocker Dockerfile juego_sumar.py readme.txt

Write-Host ""
Write-Host "¡Archivo creado exitosamente!" -ForegroundColor Green
Write-Host "Ubicación: C:\Users\a25anthonyps\ASIGNATURAS\DAW\2TRIMESTRE\apelido_nome_docker1.tgz" -ForegroundColor Cyan
Write-Host ""
Write-Host "Contenido del archivo:" -ForegroundColor Yellow
tar -tzf apelido_nome_docker1.tgz

Write-Host ""
Write-Host "Para probar el juego, ejecuta desde el directorio aplicacionDocker:" -ForegroundColor Yellow
Write-Host "  1. docker build -t juego-sumar ." -ForegroundColor White
Write-Host "  2. docker run -it --rm juego-sumar" -ForegroundColor White
