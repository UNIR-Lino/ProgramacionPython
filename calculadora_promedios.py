def ingresar_calificaciones():
    materias = []
    calificaciones = []
    while True:
        materia = input("Ingrese el nombre de la materia: ")
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {materia} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        
        materias.append(materia)
        calificaciones.append(calificacion)
        
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        if continuar != 's':
            break
            
    return materias, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    mejor_idx = calificaciones.index(max(calificaciones))
    peor_idx = calificaciones.index(min(calificaciones))
    return mejor_idx, peor_idx

def main():
    print("--- Calculadora de Promedios ---")
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias:
        print("No se ingresaron materias. Fin del programa.")
        return
        
    promedio = calcular_promedio(calificaciones)
    idx_aprobadas, idx_reprobadas = determinar_estado(calificaciones)
    mejor_idx, peor_idx = encontrar_extremos(calificaciones)
    
    print("\n--- Resumen Final ---")
    print("Materias y Calificaciones:")
    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]}")
        
    print(f"\nPromedio general: {promedio:.2f}")
    
    print("\nMaterias Aprobadas:")
    if idx_aprobadas:
        for i in idx_aprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("- Ninguna")
        
    print("\nMaterias Reprobadas:")
    if idx_reprobadas:
        for i in idx_reprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("- Ninguna")
        
    print(f"\nMejor calificación: {materias[mejor_idx]} ({calificaciones[mejor_idx]})")
    print(f"Peor calificación: {materias[peor_idx]} ({calificaciones[peor_idx]})")
    
    print("\n¡Gracias por utilizar la Calculadora de Promedios! Hasta luego.")

if __name__ == "__main__":
    main()
