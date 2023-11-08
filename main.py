import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre las calificaciones de Matematicas y Ciencias')
plt.xlabel('Calificaciones Matematicas')
plt.ylabel('Calificaciones de Ciencias')

plt.show()

materias = ['matematicas', 'ciencias', 'literatura']
materias_promedio = [sum(matematicas)/len(matematicas), sum(ciencias)/len(ciencias), sum(literatura)/len(ciencias)]
errores_materias = [sum(errores_matematicas), sum(errores_ciencias), sum(errores_literatura)]

plt.errorbar(materias, materias_promedio, yerr=errores_materias, fmt='o', capsize=5)
plt.title('Calificaciones Promedio con barras de error')
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')

plt.show()

plt.hist(matematicas, bins=6)
plt.title('Distribución de las Calificaciones de Matematicas')
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Frecuencia')

plt.show()
