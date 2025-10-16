import requests
import json
import os
from pathlib import Path

def obtener_datos_pokemon(nombre_pokemon):
    """
    Obtiene los datos de un Pokémon desde la PokeAPI
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    
    try:
        respuesta = requests.get(url)
        print(f"🔍 Buscando: {url}")  # Debug para ver la URL
        
        if respuesta.status_code == 200:
            print("✅ Pokémon encontrado")
            return respuesta.json()
        elif respuesta.status_code == 404:
            print(f"❌ Error: El Pokémon '{nombre_pokemon}' no existe.")
            return None
        else:
            print(f"❌ Error en la API: Código {respuesta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def mostrar_informacion_pokemon(datos_pokemon):
    """
    Muestra la información del Pokémon en la consola
    """
    print(f"\n{'='*50}")
    print(f"📊 INFORMACIÓN DE {datos_pokemon['name'].upper()}")
    print(f"{'='*50}")
    
    # Imágenes - probamos diferentes fuentes
    imagen_frontal = datos_pokemon['sprites']['front_default']
    imagen_hd = datos_pokemon['sprites']['other']['official-artwork']['front_default']
    
    print(f"🖼️  Imagen frontal: {imagen_frontal}")
    if imagen_hd:
        print(f"🖼️  Imagen HD: {imagen_hd}")
    else:
        print("🖼️  Imagen HD: No disponible")
    
    print(f"📏 Altura: {datos_pokemon['height'] / 10} m")
    print(f"⚖️  Peso: {datos_pokemon['weight'] / 10} kg")
    
    # Tipos
    tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]
    print(f"🎨 Tipos: {', '.join(tipos)}")
    
    # Habilidades - todas
    habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
    print(f"🌟 Habilidades: {', '.join(habilidades)}")
    
    # Movimientos - TODOS sin límite
    movimientos = [movimiento['move']['name'] for movimiento in datos_pokemon['moves']]
    print(f"⚡ Movimientos ({len(movimientos)}): {', '.join(movimientos)}")
    
    # Estadísticas base
    print("\n📈 ESTADÍSTICAS BASE:")
    for stat in datos_pokemon['stats']:
        nombre_stat = stat['stat']['name'].replace('-', ' ').title()
        print(f"   {nombre_stat}: {stat['base_stat']}")

def guardar_en_json(datos_pokemon):
    """
    Guarda la información del Pokémon en un archivo JSON
    """
    # Creamos la carpeta si no existe
    carpeta_pokedex = Path("pokedex_json")
    carpeta_pokedex.mkdir(exist_ok=True)
    
    # Preparamos los datos que vamos a guardar
    datos_guardar = {
        "id": datos_pokemon["id"],
        "nombre": datos_pokemon["name"],
        "altura": datos_pokemon["height"] / 10,
        "peso": datos_pokemon["weight"] / 10,
        "tipos": [tipo["type"]["name"] for tipo in datos_pokemon["types"]],
        "habilidades": [habilidad["ability"]["name"] for habilidad in datos_pokemon["abilities"]],
        "movimientos": [movimiento["move"]["name"] for movimiento in datos_pokemon["moves"]],  # TODOS los movimientos
        "estadisticas": {stat["stat"]["name"]: stat["base_stat"] for stat in datos_pokemon["stats"]},
        "imagen_frontal": datos_pokemon['sprites']['front_default'],
        "imagen_hd": datos_pokemon['sprites']['other']['official-artwork']['front_default']
    }
    
    # Creamos el nombre del archivo
    nombre_archivo = carpeta_pokedex / f"{datos_pokemon['name']}.json"
    
    # Guardamos en formato JSON
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos_guardar, archivo, indent=4, ensure_ascii=False)
    
    print(f"💾 Datos guardados en: {nombre_archivo}")

def main():
    """
    Función principal del programa
    """
    print("🎮 BIENVENIDO A TU POKÉDEX")
    print("🔍 Busca información de cualquier Pokémon")
    
    while True:
        print(f"\n{'─'*30}")
        nombre_pokemon = input("Ingresa el nombre del Pokémon (o 'salir' para terminar): ").strip()
        
        if nombre_pokemon.lower() == 'salir':
            print("👋 ¡Hasta luego, entrenador Pokémon!")
            break
            
        if not nombre_pokemon:
            print("⚠️  Por favor ingresa un nombre válido.")
            continue
        
        # Obtenemos los datos del Pokémon
        datos = obtener_datos_pokemon(nombre_pokemon)
        
        if datos:
            # Mostramos la información
            mostrar_informacion_pokemon(datos)
            
            # Preguntamos si quiere guardar
            guardar = input("\n¿Quieres guardar esta información? (s/n): ").lower()
            if guardar == 's':
                guardar_en_json(datos)
                print("✅ ¡Pokémon guardado exitosamente!")
            
            # Preguntamos si quiere continuar
            continuar = input("\n¿Quieres buscar otro Pokémon? (s/n): ").lower()
            if continuar != 's':
                print("👋 ¡Hasta luego, entrenador Pokémon!")
                break
        else:
            # Si no encontró el Pokémon, preguntar si quiere intentar con otro
            continuar = input("\n¿Quieres buscar otro Pokémon? (s/n): ").lower()
            if continuar != 's':
                print("👋 ¡Hasta luego, entrenador Pokémon!")
                break

if __name__ == "__main__":
    main()