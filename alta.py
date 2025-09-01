def add_expense(movimientos, categorias):
    id_mov = len(movimientos)

    fecha = input("Ingrese la fecha (MM/DD/YYYY): ")
    monto = input("Ingrese el monto: ")
    movimientos.append([monto])
    tipo_mov = input("Ingrese el tipo de movimiento (Gasto/Transferencia): ")

    print("\nSeleccione la categoría:")
    for cat in categorias[1:]:
        print(f"{cat[0]} - {cat[1]} ({cat[2]})")

    cat_id = int(input("Ingrese el número de categoría: "))

    categoria = "Desconocido"
    for cat in categorias[1:]:
        if cat[0] == cat_id:
            categoria = cat[1]

    descripcion = input("Ingrese la descripción: ")
    cuenta_origen = input("Ingrese la cuenta origen (o '-' si no aplica): ")
    cuenta_destino = input("Ingrese la cuenta destino (o '-' si no aplica): ")
    movimientos.append([id_mov, fecha, monto, tipo_mov, categoria, descripcion, cuenta_origen, cuenta_destino])

    print("\n Movimiento agregado correctamente!\n")

