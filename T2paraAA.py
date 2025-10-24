import random

def generar_palabra():
    return ''.join(chr(random.randint(97, 122)) for _ in range(4))

def generar_matriz(filas, columnas):
    return [[generar_palabra() for _ in range(columnas)] for _ in range(filas)]

def tiene_vocal(palabra):
    for vocal in "aeiou":
        if vocal in palabra:
            return True
    return False

def contar_vocales_divide_y_venceras(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas == 1 and columnas == 1:
        return 1 if tiene_vocal(matriz[0][0]) else 0

    if filas == 1:
        mitad = columnas // 2
        izquierda = [matriz[0][:mitad]]
        derecha = [matriz[0][mitad:]]
        return (contar_vocales_divide_y_venceras(izquierda) +
                contar_vocales_divide_y_venceras(derecha))

    if columnas == 1:
        mitad = filas // 2
        arriba = matriz[:mitad]
        abajo = matriz[mitad:]
        return (contar_vocales_divide_y_venceras(arriba) +
                contar_vocales_divide_y_venceras(abajo))

    mitad_f = filas // 2
    mitad_c = columnas // 2

    sub1 = [fila[:mitad_c] for fila in matriz[:mitad_f]]   
    sub2 = [fila[mitad_c:] for fila in matriz[:mitad_f]]   
    sub3 = [fila[:mitad_c] for fila in matriz[mitad_f:]]   
    sub4 = [fila[mitad_c:] for fila in matriz[mitad_f:]]   

    return (contar_vocales_divide_y_venceras(sub1) +
            contar_vocales_divide_y_venceras(sub2) +
            contar_vocales_divide_y_venceras(sub3) +
            contar_vocales_divide_y_venceras(sub4))

def main():
    try:
        filas = int(input("Ingrese la cantidad de filas: "))
        columnas = int(input("Ingrese la cantidad de columnas: "))

        if filas <= 0 or columnas <= 0:
            print("Las dimensiones deben ser mayores que cero.")
            return

        matriz = generar_matriz(filas, columnas)

        print("\nMatriz generada:")
        print("")
        for fila in matriz:
            print(' '.join(fila))

        total = contar_vocales_divide_y_venceras(matriz)
        print(f"\nCantidad de palabras con al menos una vocal: {total}")

    except ValueError:
        print("Ingrese solo numeros enteros validos...")

if __name__ == "__main__":
    main()
