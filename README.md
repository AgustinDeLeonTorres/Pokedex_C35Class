# Pokédex en Python

Una aplicación de consola que consume la PokeAPI para obtener información detallada de Pokémon.

## 🚀 Características

- Buscar Pokémon por nombre
- Mostrar información detallada (peso, altura, tipos, habilidades, movimientos, estadísticas)
- Guardar información en archivos JSON en la carpeta `pokedex_json`
- Manejo de errores y validaciones
- Interfaz amigable de consola

## 📋 Requisitos

- Python 3.6+
- Librería `requests`

## 🔧 Instalación

1. Navega a la carpeta del proyecto:
   cd Pokedex
3. Instala las dependencias:
pip install -r requirements.txt

🎮 Uso
Ejecuta el programa:
python pokedexcodigo.py

📁 Estructura del Proyecto

Pokedex/
├── pokedexcodigo.py   # Código principal
├── requirements.txt   # Dependencias
├── README.md         # Este archivo
└── pokedex_json/     # Carpeta para JSONs (se crea automáticamente)
    ├── pikachu.json  # Ejemplo de archivo guardado
    └── charmander.json

🔍 Ingresa el nombre de un Pokémon: pikachu
🔍 Buscando 'pikachu' en la PokeAPI...
✅ Pokémon encontrado!

============================================================
🎯 POKÉDEX - PIKACHU (#25)
============================================================
⚖️  Peso: 6.0 kg
📏 Altura: 0.4 m
🎨 Tipos: electric
💪 Habilidades: static, lightning-rod

🎯 ESTADÍSTICAS:
   ❤️  HP: 35
   ⚔️  Ataque: 55
   🛡️  Defensa: 40
   🔥 Ataque Especial: 50
   ❄️  Defensa Especial: 50
   🏃 Velocidad: 90

📚 Lo que aprendí en este módulo
Consumo de APIs REST:
Aprendí a hacer peticiones HTTP a APIs externas usando la librería requests. En el código, la función buscar_pokemon() hace peticiones GET a la PokeAPI y maneja diferentes respuestas HTTP.

Manejo de JSON:
Aprendí a procesar y trabajar con datos en formato JSON. La función _procesar_datos_pokemon() toma la respuesta JSON de la API y extrae la información específica que necesitamos como nombre, tipos, movimientos, etc.

Manejo de errores:
Aprendí a lidiar con diferentes status codes y excepciones. El código maneja errores como:

Status 404 (Pokémon no encontrado)

Status 200 (éxito)

Errores de conexión

Excepciones generales con try-except

Manipulación de archivos:
Aprendí a crear, escribir y organizar archivos en el sistema. La función guardar_json() crea archivos JSON en la carpeta pokedex_json y la función _crear_carpeta_json() asegura que la carpeta exista.

Programación orientada a objetos:
Aprendí a organizar el código en clases y métodos. La clase Pokedex encapsula toda la funcionalidad con métodos específicos para cada tarea: buscar, procesar, mostrar y guardar información.

Manejo de dependencias:
Aprendí a usar requirements.txt para gestionar librerías externas y asegurar que otros desarrolladores puedan ejecutar el proyecto.

Estructura de programas Python:
Aprendí la importancia del if __name__ == "__main__": al final del código. Esto permite que el programa se ejecute cuando es llamado directamente, pero no cuando es importado como módulo en otro programa.

🔧 Explicación de las funciones principales:
__init__(self)
Constructor de la clase - Se ejecuta al crear una nueva instancia de Pokedex

Inicializa variables como la URL base y la carpeta para JSONs

Asegura que la carpeta existe llamando a _crear_carpeta_json()

buscar_pokemon(nombre)
Hace la petición HTTP a la PokeAPI usando requests.get()

Maneja los status codes: 200 (éxito), 404 (no encontrado), otros errores

Retorna los datos procesados o None si hay error

_procesar_datos_pokemon(datos)
Extrae y estructura la información del JSON de la API

Convierte unidades (peso y altura de decímetros a metros/kg)

Organiza estadísticas, tipos, habilidades y movimientos en un diccionario

mostrar_informacion(pokemon_info)
Presenta la información de forma legible en la consola

Muestra todos los datos: stats, movimientos, tipos, etc.

Formatea la salida con emojis y separadores para mejor visualización

guardar_json(pokemon_info)
Guarda los datos en archivo JSON con encoding UTF-8

Usa indentación para que el JSON sea legible

Maneja errores de permisos o escritura de archivos

ejecutar()
Función principal del flujo - Controla la interacción con el usuario

Maneja el bucle principal de búsquedas

Pregunta al usuario si quiere guardar los resultados

main()
Punto de entrada del programa - Crea la instancia de Pokedex y la ejecuta

Maneja excepciones globales y la interrupción por teclado (Ctrl+C)

if __name__ == "__main__": main()
Patrón estándar en Python - Asegura que main() solo se ejecute cuando el archivo es run directamente

Permite que el código sea importado como módulo sin ejecutar automáticamente

🎯 Conceptos técnicos implementados:
Clases y objetos: La clase Pokedex como molde para crear instancias

Métodos públicos y privados: _crear_carpeta_json() con _ indica método interno

Manejo de excepciones: Try-except para errores de red y archivos

Formato de strings: f-strings para interpolación de variables

List comprehensions: Para procesar listas de movimientos y tipos

Context managers: with open() para manejo seguro de archivos

Módulo datetime: Para registrar fecha y hora de las consultas

Esta estructura me permitió crear una aplicación funcional, mantenible y que cumple con todos los requisitos del proyecto mientras aplico las mejores prácticas de programación Python.

🛠️ Tecnologías Utilizadas
Python 3

Requests (para peticiones HTTP)

JSON (manipulación de datos)

OS (manejo de archivos y directorios)

📄 Licencia
Este proyecto es con fines educativos como parte del módulo 4.