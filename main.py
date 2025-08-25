def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:<20}", end="")
        print()
    print("\n")

def get_categorias():
    categorias = [
        ["id_cat", "categoria", "subcategoria", "Descripcion"],
        [1, "Interbanking", "Transferencias a bancos", "Paso de banco hipotecario a BBVA"],
        [2, "Hogar", "Servicios", "Pago de internet"],
        [3, "Ocio", "Restaurantes", "Cena en restaurante"],
        [4, "Salud", "Gimnasio", "Suplementos GYM"],
        [5, "Transporte", "Pases", "Recarga Sube"],
        [6, "Otros", "Adicciones", "Gramo de Flores"]
    ]
    return categorias

def create_movimientos():
    return [["id_mov", "fecha", "monto", "Tipo_mov", "categoria", "Descripcion", "Cuenta_origen", "Cuenta_destino"]]

def add_expense(movimientos, categorias):
    id_mov = len(movimientos)

    fecha = input("Ingrese la fecha (MM/DD/YYYY): ")
    monto = input("Ingrese el monto: ")
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

"""def main():
    categorias = get_categorias()
    movimientos = create_movimientos()
    add_expense(movimientos, categorias)
    add_expense(movimientos, categorias)
    print("\n=== Movimientos registrados ===")
    print_matrix(movimientos)

main()"""
def main():
    categorias = get_categorias()
    movimientos = create_movimientos()
    
    corriendo = True
    while corriendo:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo gasto")
        print("2. Ver movimientos registrados")
        print("3. Modificar un movimiento")
        print("4. Eliminar un movimiento")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            add_expense(movimientos, categorias)
        
        elif opcion == '2':
            print("\n=== Movimientos registrados ===")
            print_matrix(movimientos)
            
        elif opcion == '3':
            id_modificar = int(input("Ingrese el ID del movimiento a modificar: "))
            encontrado = False
            i = 0
            while i < len(movimientos) and not encontrado:
                if i > 0 and movimientos[i][0] == id_modificar:
                    nuevo_monto = float(input(f"Nuevo monto (actual: {movimientos[i][2]}): "))
                    movimientos[i][2] = nuevo_monto
                    print("El movimiento fue actualizado correctamente.")
                    encontrado = True
                i += 1
            if not encontrado:
                print("El movimiento no fue encontrado.")
                
        elif opcion == '4':
            id_eliminar = int(input("Ingrese el ID del movimiento a eliminar: "))
            encontrado = False
            i = 0
            while i < len(movimientos) and not encontrado:
                if i > 0 and movimientos[i][0] == id_eliminar:
                    del movimientos[i]
                    print("El movimiento fue eliminado correctamente.")
                    encontrado = True
                i += 1
            if not encontrado:
                print("El movimiento ingresado no fue encontrado.")
        
        elif opcion == '5':
            corriendo = False
            print("Finalizando el programa...")
            
        else:
            print("La opción ingresada no es válida. Por favor, intente de nuevo.")

main()
