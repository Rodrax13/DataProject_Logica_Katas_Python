def diferencia_listas(lista1, lista2):
    # Usamos map() para restar elemento a elemento
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo de uso
lista_a = [10, 20, 30, 40]
lista_b = [1, 5, 10, 15]

resultado = diferencia_listas(lista_a, lista_b)
print(resultado)