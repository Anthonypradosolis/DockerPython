#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Juego de sumar - Practica matemáticas sumando números
"""

import random
import sys


def generar_suma():
    """Genera dos números aleatorios para sumar"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2


def jugar():
    """Función principal del juego"""
    print("=" * 50)
    print("   ¡BIENVENIDO AL JUEGO DE SUMAR!")
    print("=" * 50)
    print("\nPractica tus habilidades de suma.")
    print("Escribe 'salir' para terminar el juego.\n")
    
    puntos = 0
    intentos = 0
    
    while True:
        # Generar una nueva suma
        num1, num2 = generar_suma()
        resultado_correcto = num1 + num2
        
        # Mostrar la pregunta
        print(f"\n¿Cuánto es {num1} + {num2}?")
        respuesta = input("Tu respuesta: ").strip()
        
        # Verificar si el usuario quiere salir
        if respuesta.lower() in ['salir', 'exit', 'quit', 'q']:
            print("\n" + "=" * 50)
            print("   JUEGO TERMINADO")
            print("=" * 50)
            if intentos > 0:
                porcentaje = (puntos / intentos) * 100
                print(f"\nEstadísticas finales:")
                print(f"  - Respuestas correctas: {puntos}/{intentos}")
                print(f"  - Porcentaje de acierto: {porcentaje:.1f}%")
            else:
                print("\n¡No has jugado ninguna ronda!")
            print("\n¡Gracias por jugar!\n")
            break
        
        # Verificar la respuesta
        try:
            respuesta_numerica = int(respuesta)
            intentos += 1
            
            if respuesta_numerica == resultado_correcto:
                puntos += 1
                print(f"✓ ¡Correcto! Llevas {puntos} puntos.")
            else:
                print(f"✗ Incorrecto. La respuesta correcta era {resultado_correcto}.")
                print(f"  Llevas {puntos} puntos.")
        
        except ValueError:
            print("Por favor, introduce un número válido o 'salir' para terminar.")


def main():
    """Punto de entrada del programa"""
    try:
        jugar()
    except KeyboardInterrupt:
        print("\n\n¡Juego interrumpido! Hasta pronto.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
