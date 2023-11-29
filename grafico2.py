mport numpy as np
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



# Importar los datos
calificaciones_promedio = [75, 65, 80]
errores = np.random.normal(0, 10, (3,))

# Crea el gráfico de barras de error
plt.errorbar(["Matemáticas", "Ciencias", "Literatura"], calificaciones_promedio, yerr=errores, fmt='o')

# Agrega etiquetas a los ejes
plt.xlabel("Materia")
plt.ylabel("Calificación promedio")

# Agrega un título al gráfico
plt.title("Calificaciones promedio por materia")

# Agrega una leyenda
plt.legend(["Promedio"], loc="best")

# Muestra el gráfico
plt.show()
