import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Definir los equipos y sus enfrentamientos recogidos del modelo de arbol de decision y bosques aleatorios
semifinales = ['Real Madrid vs Bayern Munich', 'PSG vs Borussia Dortmund']
finalistas = ['Real Madrid', 'PSG']
campeon = 'Real Madrid'

# Crear la visualización
fig, ax = plt.subplots(figsize=(12, 6))

# Colores y estilos para el gráfico
colors = {'semifinales': '#FFD700', 'finalistas': '#00BFFF', 'campeon': '#32CD32'}
linewidths = {'semifinales': 1.5, 'finalistas': 2, 'campeon': 2.5}

# Dibujar las conexiones (líneas) entre los nodos
ax.plot([1, 2], [3, 2], 'k-', lw=linewidths['finalistas'])  # Semifinal 1 a Campeón
ax.plot([1, 2], [1, 2], 'k-', lw=linewidths['finalistas'])  # Semifinal 2 a Campeón
ax.plot([0, 1], [3, 3], 'k--', lw=linewidths['semifinales'])  # Enfrentamiento 1 a Finalista 1
ax.plot([0, 1], [1, 1], 'k--', lw=linewidths['semifinales'])  # Enfrentamiento 2 a Finalista 2

# Dibujar los nodos (círculos)
ax.scatter([0, 0, 1, 1, 2], [3, 1, 3, 1, 2], s=[100]*5, c=[colors['semifinales']]*2 + [colors['finalistas']]*2 + [colors['campeon']], zorder=5)

# Etiquetas de los nodos
for i, txt in enumerate(semifinales + finalistas + [campeon]):
    ax.text(i//3 + (i%3!=2)*0.05, [3, 1, 3, 1, 2][i] + 0.1, txt, fontsize=11, ha='center', va='center')

# Ajustes finales del gráfico
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(0, 4)
plt.axis('off')  # Ocultar ejes

# Mostrar el gráfico
plt.show()
