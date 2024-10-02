# from pyrandwalk import *
# import numpy as np
# states = [0, 1, 2, 3, 4]
# trans = np.array([[1,    0, 0,    0, 0],
#                 [0.25, 0, 0.75, 0, 0],
#                 [0, 0.25, 0, 0.75, 0],
#                 [0, 0, 0.25, 0, 0.75],
#                 [0, 0,    0, 1,    0]])
# rw = RandomWalk(states, trans)
# rw.prob_sec([2, 1, 0])
# states, probs = rw.run()
# print(rw.get_edges())

import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

l = 100
steps = np.random.choice([-1, 1], size=l) + 0.05 * np.random.randn(l) # l steps
position = np.cumsum(steps) # integrate the position by summing steps values
y = 0.05 * np.random.randn(l)

fig = go.Figure(data=go.Scatter(
    x=position,
    y=y,
    mode='markers',
    name='Random Walk in 1D',
    marker=dict(
        color=np.arange(l),
        size=7,
        colorscale='Reds',
        showscale=True,
    )
))

fig.update_layout(yaxis_range=[-1, 1])
fig.show()