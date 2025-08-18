def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:<20}", end="")
        print()
    print("\n")


def get_movimientos():
    movimientos = [
        ["id_mov", "fecha", "monto", "Tipo_mov", "categoria", "Descripcion", "Cuenta_origen", "Cuenta_destino"],
        [1, "8/16/2025", 3500, "Gasto", "Transporte", "Recarga Sube", "-", "-"],
        [2, "8/17/2025", 12000, "Gasto", "Ocio", "Cena en restaurante", "-", "-"],
        [3, "8/18/2025", 2000, "Gasto", "Salud", "Suplementos GYM", "-", "-"],
        [4, "8/19/2025", 15000, "Transferencia", "-", "Paso de banco hipotecario a BBVA", "Banco hipotecario", "BBVA"],
        [5, "8/20/2025", 8500, "Gasto", "Hogar", "Pago de internet", "-", "-"]
    ]
    return movimientos


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



def main():
    print("=== Movimientos ===")
    print_matrix(get_movimientos())

    print("=== Categorias ===")
    print_matrix(get_categorias())

main()
