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
Consumo de APIs REST: Aprendí a hacer peticiones HTTP a APIs externas usando la librería requests

Manejo de JSON: Cómo procesar y trabajar con datos en formato JSON

Manejo de errores: Cómo lidiar con diferentes status codes y excepciones

Manipulación de archivos: Crear, escribir y organizar archivos en el sistema

Programación orientada a objetos: Organizar el código en clases y métodos

Manejo de dependencias: Usar requirements.txt para gestionar librerías externas

🛠️ Tecnologías Utilizadas
Python 3

Requests (para peticiones HTTP)

JSON (manipulación de datos)

OS (manejo de archivos y directorios)

📄 Licencia
Este proyecto es con fines educativos como parte del módulo 4.