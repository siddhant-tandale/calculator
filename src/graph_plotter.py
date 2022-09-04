import plotly.graph_objects as go
import numpy as np
from math import *


def plot_equation(equation: str):

    x_ = np.arange(-50, 50, 0.01)
    y = [eval(equation) for x in x_]

    layout = go.Layout(
        width=1024,
        height=1024,
        plot_bgcolor='#ffffff'
    )

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=x_, y=y, line=dict(color='firebrick', width=3)))

    fig.update_xaxes(range=[min(x_)/10, max(x_)/10], gridcolor='#3e3e3e', zerolinecolor='#3e3e3e')
    fig.update_yaxes(range=[min(x_)/10, max(x_)/10], gridcolor='#3e3e3e', zerolinecolor='#3e3e3e')

    fig.show()