import requests
import json
import os
from datetime import datetime

class Pokedex:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.data_folder = "pokedex_json"  # Nombre actualizado
        
        # Crear carpeta si no existe
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            print(f"📁 Carpeta '{self.data_folder}' creada exitosamente")
    
    def buscar_pokemon(self, nombre):
        """
        Busca un Pokémon por nombre en la PokeAPI
        Returns: dict con datos del Pokémon o None si hay error
        """
        try:
            print(f"🔍 Buscando '{nombre}' en la PokeAPI...")
            response = requests.get(f"{self.base_url}{nombre.lower()}")
            
            # Manejar diferentes status codes
            if response.status_code == 404:
                print(f"❌ Error: Pokémon '{nombre}' no encontrado")
                return None
            elif response.status_code == 200:
                print("✅ Pokémon encontrado!")
                datos = response.json()
                return self._procesar_datos_pokemon(datos)
            else:
                print(f"❌ Error en la API: Código {response.status_code}")
                return None
            
        except requests.exceptions.ConnectionError:
            print("❌ Error de conexión: Verifica tu internet")
            return None
        except requests.exceptions.Timeout:
            print("❌ Error: Tiempo de espera agotado")
            return None
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return None
    
    def _procesar_datos_pokemon(self, datos):
        """
        Procesa los datos crudos de la API y los estructura
        """
        pokemon_info = {
            'id': datos['id'],
            'nombre': datos['name'],
            'peso': datos['weight'] / 10,  # Convertir a kg
            'altura': datos['height'] / 10,  # Convertir a metros
            'tipos': [tipo['type']['name'] for tipo in datos['types']],
            'habilidades': [habilidad['ability']['name'] for habilidad in datos['abilities']],
            'movimientos': [movimiento['move']['name'] for movimiento in datos['moves'][:10]],
            'imagen_frontal': datos['sprites']['front_default'],
            'stats': {
                'hp': datos['stats'][0]['base_stat'],
                'ataque': datos['stats'][1]['base_stat'],
                'defensa': datos['stats'][2]['base_stat'],
                'ataque_especial': datos['stats'][3]['base_stat'],
                'defensa_especial': datos['stats'][4]['base_stat'],
                'velocidad': datos['stats'][5]['base_stat']
            },
            'fecha_consulta': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return pokemon_info
    
    def mostrar_informacion(self, pokemon_info):
        """
        Muestra la información del Pokémon de forma legible
        """
        print(f"\n{'='*60}")
        print(f"🎯 POKÉDEX - {pokemon_info['nombre'].upper()} (#{pokemon_info['id']})")
        print(f"{'='*60}")
        print(f"⚖️  Peso: {pokemon_info['peso']} kg")
        print(f"📏 Altura: {pokemon_info['altura']} m")
        print(f"🎨 Tipos: {', '.join(pokemon_info['tipos'])}")
        print(f"💪 Habilidades: {', '.join(pokemon_info['habilidades'])}")
        
        print(f"\n🎯 ESTADÍSTICAS:")
        stats = pokemon_info['stats']
        print(f"   ❤️  HP: {stats['hp']}")
        print(f"   ⚔️  Ataque: {stats['ataque']}")
        print(f"   🛡️  Defensa: {stats['defensa']}")
        print(f"   🔥 Ataque Especial: {stats['ataque_especial']}")
        print(f"   ❄️  Defensa Especial: {stats['defensa_especial']}")
        print(f"   🏃 Velocidad: {stats['velocidad']}")
        
        print(f"\n👊 MOVIMIENTOS (primeros 10):")
        for i, movimiento in enumerate(pokemon_info['movimientos'], 1):
            print(f"   {i:2d}. {movimiento}")
        
        if pokemon_info['imagen_frontal']:
            print(f"\n🖼️  Imagen frontal: {pokemon_info['imagen_frontal']}")
            print("   💡 Copia esta URL en tu navegador para ver la imagen")
        print(f"{'='*60}")
    
    def guardar_json(self, pokemon_info):
        """
        Guarda la información del Pokémon en un archivo JSON
        """
        try:
            filename = f"{self.data_folder}/{pokemon_info['nombre']}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(pokemon_info, f, indent=2, ensure_ascii=False)
            return filename
        except Exception as e:
            print(f"❌ Error al guardar archivo: {e}")
            return None
    
    def ejecutar(self):
        """
        Función principal que ejecuta la Pokédex
        """
        print("🌟" + "="*50)
        print("           BIENVENIDO A LA POKÉDEX")
        print("🌟" + "="*50)
        print("📚 Busca información de cualquier Pokémon")
        print("💾 Los datos se guardan en la carpeta 'pokedex_json'")
        print("🚪 Escribe 'salir' para terminar el programa")
        print("-"*50)
        
        while True:
            # Obtener entrada del usuario
            entrada = input("\n🔍 Ingresa el nombre de un Pokémon: ").strip()
            
            # Verificar si quiere salir
            if entrada.lower() in ['salir', 'exit', 'quit', 'q']:
                print("\n👋 ¡Gracias por usar la Pokédex! ¡Hasta pronto!")
                break
            
            if not entrada:
                print("⚠️  Por favor ingresa un nombre válido")
                continue
            
            # Buscar el Pokémon
            pokemon_info = self.buscar_pokemon(entrada)
            
            if pokemon_info:
                # Mostrar información
                self.mostrar_informacion(pokemon_info)
                
                # Preguntar si guardar
                guardar = input("\n💾 ¿Quieres guardar esta información en JSON? (s/n): ").lower().strip()
                if guardar in ['s', 'si', 'sí', 'y', 'yes']:
                    archivo_guardado = self.guardar_json(pokemon_info)
                    if archivo_guardado:
                        print(f"✅ ¡Guardado exitoso en: {archivo_guardado}!")
                    else:
                        print("❌ No se pudo guardar el archivo")
                else:
                    print("ℹ️  Información no guardada")
            
            print("\n" + "-"*50)

def main():
    """
    Función principal del programa
    """
    try:
        pokedex = Pokedex()
        pokedex.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()