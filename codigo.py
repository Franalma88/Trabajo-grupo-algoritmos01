import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
file_path = "datos.csv"  

# Cargar el archivo CSV con el separador correcto
df = pd.read_csv(file_path, sep=';')

# Convertir a lista de diccionarios
jugadores = df.to_dict(orient='records')

# Funcion listar jugadores --> Muestra todos los  elementos 
def listar_jugadores():
    for jugador in jugadores:
        print(jugador["Jugador"])


def mostrar_estadisticas(nombre):
    for jugador in jugadores:
        if jugador['Jugador'].lower() == nombre.lower():
            print(f"\nEstadísticas de {jugador['Jugador']}:")
            for clave, valor in jugador.items():
                print(f"  {clave}: {valor}")
            return
    print(f"No se encontró ningún jugador con el nombre '{nombre}'.")
    
def valor_estadistica(nombre, estadistica):
    for jugador in jugadores:
        if jugador['Jugador'].lower() == nombre.lower():
            if estadistica in jugador:
                valor = jugador[estadistica]
                print(f"{estadistica} de {jugador['Jugador']}: {valor}")
                return valor
            else:
                print(f"La estadística '{estadistica}' no existe para este jugador.")
                return None
    print(f"No se encontró ningún jugador con el nombre '{nombre}'.")
    return None
  
def actualizar_estadisticas(nombre, estadistica, valor):
    for jugador in jugadores:
        if jugador['Jugador'].lower() == nombre.lower():
            if estadistica in jugador:
                try:
                    # Si la estadística es numérica, actualizamos sumando el valor
                    jugador[estadistica] = type(jugador[estadistica])(valor)
                    print(f"{estadistica} de {jugador['Jugador']} actualizada a {jugador[estadistica]}")
                except Exception as e:
                    print(f"Error al actualizar la estadística: {e}")
            else:
                print(f"La estadística '{estadistica}' no existe para este jugador.")
            return
    print(f"No se encontró ningún jugador con el nombre '{nombre}'.")

def mejor_jugador(estadistica):
    mejor = None
    max_valor = float('-inf')

    for jugador in jugadores:
        if estadistica in jugador:
            try:
                valor = jugador[estadistica]
                if isinstance(valor, (int, float)) and valor > max_valor:
                    max_valor = valor
                    mejor = jugador
            except:
                continue

    if mejor:
        print(f"El mejor jugador en '{estadistica}' es {mejor['Jugador']} con un valor de {max_valor}")
        return mejor
    else:
        print(f"No se pudo calcular el mejor jugador en la estadística '{estadistica}'.")
        return None

def ordenar_jugadores(estadistica, descendente):
    try:
        if descendente.lower() == "a":
            descendente=False
        else:
             descendente=True   
        jugadores_ordenados = sorted(
            jugadores,
            key=lambda j: int(j.get(estadistica, 0)),
            reverse=descendente
        )
        print(f"\nJugadores ordenados por '{estadistica}' ({'descendente' if descendente else 'ascendente'}):")
        for jugador in jugadores_ordenados:
            print(f"{jugador['Jugador']}: {jugador.get(estadistica, 'N/A')}")
        return jugadores_ordenados
    except Exception as e:
        print(f"Error al ordenar por '{estadistica}': {e}")
        return []

def promedio_puntos():
    total_puntos = 0
    total_jugadores = 0

    for jugador in jugadores:
        try:
            puntos = float(jugador.get('PTS', 0))
            total_puntos += puntos
            total_jugadores += 1
        except:
            continue

    if total_jugadores > 0:
        promedio = total_puntos / total_jugadores
        print(f"Promedio de puntos por jugador en la temporada es : {promedio:.2f}")
        return promedio
    else:
        print("No hay jugadores válidos para calcular el promedio.")
        return 0

def grafico_puntos_vs_minutos():
    nombres = [j['Jugador'] for j in jugadores]
    minutos = [j['MinutosJugados'] for j in jugadores]
    puntos = [j['PTS'] for j in jugadores]

    plt.figure(figsize=(10, 6))
    plt.scatter(minutos, puntos)

    plt.title("Puntos (PTS) vs Minutos Jugados ")
    plt.xlabel("Minutos Jugados Totales ")
    plt.ylabel("Puntos Anotados totales (PTS)")
    plt.grid(True)

    # Etiquetas para algunos puntos
    for nombre, x, y in zip(nombres, minutos, puntos): 
             
        plt.text(x, y, f"{nombre}/{y}", fontsize=8)

    plt.tight_layout()
    plt.show()

def salir():
    print("Saliendo del programa. ¡Hasta luego!")
    exit()
    
# Menú principal
def menu():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Mostrar estadísticas de un jugador")
        print("2. Listar todos los jugadores")
        print("3. Actualizar estadisticas de un jugador")
        print("4. Mejor Jugador en Base a estadistica")
        print("5. Ordenar Jugadores por estadistica")
        print("6. Promedio")
        print("7. Graficas")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")
        if opcion == '1':
            nombre = input("Nombre del jugador: ")
            mostrar_estadisticas(nombre)
        elif opcion == '2':
            listar_jugadores()
        elif opcion == '3':
              nombre = input("Nombre del jugador: ")
              estadistica=input("Nombre de la estadistica: ")
              valor_estadistica(nombre, estadistica)
              valor=input("Valor a cambiar: ")
              actualizar_estadisticas(nombre, estadistica, valor)
        elif opcion == '4':
             estadistica=input("Nombre de la estadistica: ")
             mejor_jugador(estadistica)   
        elif opcion == '5':
             estadistica=input("Nombre de la estadistica: ")
             orden=input("Ascendente -->(A) / Descendente -->(D): ")
             ordenar_jugadores(estadistica, orden)
        elif opcion == '6':   
             promedio_puntos()
        elif opcion == '7':
             grafico_puntos_vs_minutos()
        elif opcion == '8':
            salir()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()
