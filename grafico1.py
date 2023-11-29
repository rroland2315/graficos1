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

# Datos
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)

# Gráfico
plt.scatter(matematicas, ciencias)
plt.xlabel("Calificaciones de Matemáticas")
plt.ylabel("Calificaciones de Ciencias")
plt.title("Relación entre las calificaciones de Matemáticas y Ciencias")
plt.xlim(50, 100)
plt.ylim(50, 90)

# División del eje y
plt.yticks(np.arange(50, 100,10))
plt.xticks(np.arange(50, 110, 10))
# Mostrar el gráfico
plt.show()
