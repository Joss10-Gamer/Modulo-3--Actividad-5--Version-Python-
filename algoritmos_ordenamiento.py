import os

# 🎨 Colores ANSI
class Colors:
    RESET = "\033[0m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    WHITE = "\033[97m"

def bubble_sort_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:  # Orden descendente
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].lower() < derecha[j].lower():  
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].lower() > clave.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_centered(text, color=Colors.WHITE, width=80):
    print(color + text.center(width) + Colors.RESET)


def menu():
    while True:
        clear_screen()
        print(Colors.CYAN + "="*80 + Colors.RESET)
        print_centered("MENÚ DE ORDENAMIENTO", Colors.CYAN)
        print(Colors.CYAN + "="*80 + Colors.RESET)
        print_centered("1. Ordenar lista de números (Bubble Sort - Descendente)", Colors.YELLOW)
        print_centered("2. Ordenar lista de palabras (Merge Sort - Alfabético)", Colors.YELLOW)
        print_centered("3. Ordenar lista de nombres (Insertion Sort - Alfabético)", Colors.YELLOW)
        print_centered("4. Salir", Colors.YELLOW)
        print(Colors.CYAN + "="*80 + Colors.RESET)

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            datos = input("\nIngresa números separados por espacio: ")
            try:
                lista = [int(x) for x in datos.split()]
                print("\n")
                print_centered(f"Lista original: {lista}", Colors.WHITE)
                ordenada = bubble_sort_desc(lista.copy())
                print_centered(f"✅ Lista ordenada (descendente): {ordenada}", Colors.GREEN)
            except ValueError:
                print_centered("❌ Error: Debes ingresar solo números.", Colors.RED)

        elif opcion == "2":
            datos = input("\nIngresa palabras separadas por espacio: ")
            lista = datos.split()
            if lista:
                print("\n")
                print_centered(f"Lista original: {lista}", Colors.WHITE)
                ordenada = merge_sort(lista.copy())
                print_centered(f"✅ Lista ordenada (alfabético): {ordenada}", Colors.GREEN)
            else:
                print_centered("❌ Error: Debes ingresar al menos una palabra.", Colors.RED)

        elif opcion == "3":
            datos = input("\nIngresa nombres separados por coma: ")
            lista = [x.strip() for x in datos.split(",") if x.strip()]
            if lista:
                print("\n")
                print_centered(f"Lista original: {lista}", Colors.WHITE)
                ordenada = insertion_sort(lista.copy())
                print_centered(f"✅ Lista ordenada (alfabético): {ordenada}", Colors.GREEN)
            else:
                print_centered("❌ Error: Debes ingresar al menos un nombre.", Colors.RED)

        elif opcion == "4":
            print("\n")
            print_centered("👋 Saliendo del programa. ¡Hasta luego!", Colors.CYAN)
            break
        else:
            print("\n")
            print_centered("❌ Opción no válida. Intenta de nuevo.", Colors.RED)

        input("\nPresiona ENTER para continuar...")


# Ejecutar menú principal
menu()
