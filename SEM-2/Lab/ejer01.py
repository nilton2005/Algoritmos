def bitStrings(n):
    """
    Genera todas las posibles cadenas de bits de longitud n utilizando backtracking.
    
    :param n: Longitud de las cadenas de bits
    :return: Lista de todas las posibles cadenas de bits de longitud n
    """
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1']
    
    # Generar cadenas más cortas una vez para evitar llamadas redundantes
    cadenas_mas_cortas = bitStrings(n - 1)
    # Construir las cadenas de bits de longitud n
    return [digito + cadena for digito in ['0', '1'] for cadena in cadenas_mas_cortas]

#Este es el usuario Nilton taco con cuenta professional:

if __name__ == "__main__":
    # Ejecutar y mostrar el resultado para cadenas de bits de longitud 3
    print(bitStrings(3))
