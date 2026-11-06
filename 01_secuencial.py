import time

# Ejecucion secuencial: recorrido de un pedido de comida a domicilio.
# Cada etapa depende de la anterior, por eso no puede empezar
# hasta que la anterior termine.


def realizar_etapa(descripcion, segundos):
    print(f"{descripcion}...")
    time.sleep(segundos)  # Simula el tiempo que toma la etapa
    print(f"Listo ({segundos} s)\n")


def main():
    print("=== Pedido de comida a domicilio ===\n")

    inicio = time.perf_counter()

    realizar_etapa("1. El restaurante confirma el pedido", 1)
    realizar_etapa("2. El restaurante prepara la comida", 4)
    realizar_etapa("3. Se empaca el pedido", 1)
    realizar_etapa("4. El repartidor lleva el pedido", 3)
    realizar_etapa("5. El cliente recibe el pedido", 1)

    fin = time.perf_counter()

    # Los tiempos se suman: 10 segundos
    print(f"Pedido entregado. Tiempo total: {fin - inicio:.2f} segundos.")


if __name__ == "__main__":
    main()