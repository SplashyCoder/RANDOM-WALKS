import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

l = 100

# Caminata A: Sin ruido
steps_A = np.random.choice([-1, 1], size=l)
position_A = np.cumsum(steps_A)

# Caminata B: Ruido bajo
steps_B = np.random.choice([-1, 1], size=l) + 0.05 * np.random.randn(l)
position_B = np.cumsum(steps_B)

# Caminata C: Ruido alto
steps_C = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l)
position_C = np.cumsum(steps_C)

# Graficar todas las caminatas
fig = go.Figure()

# Caminata A
fig.add_trace(go.Scatter(
    x=position_A,
    y=0.05 * np.random.randn(l),  # Mantén algo de variabilidad en y
    mode='markers',
    name='Caminata A (Sin Ruido)',
    marker=dict(color='blue', size=7)
))

# Caminata B
fig.add_trace(go.Scatter(
    x=position_B,
    y=0.05 * np.random.randn(l),
    mode='markers',
    name='Caminata B (Ruido Bajo)',
    marker=dict(color='green', size=7)
))

# Caminata C
fig.add_trace(go.Scatter(
    x=position_C,
    y=0.05 * np.random.randn(l),
    mode='markers',
    name='Caminata C (Ruido Alto)',
    marker=dict(color='red', size=7)
))

# Ajuste del gráfico
fig.update_layout(
    title="Comparación de Caminatas Aleatorias con Diferentes Niveles de Ruido",
    xaxis_title="Posición (x)",
    yaxis_title="Dispersión aleatoria (y)",
    yaxis_range=[-1, 1]
)

fig.show()
