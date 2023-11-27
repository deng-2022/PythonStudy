import plotly.graph_objs as go
from plotly.subplots import make_subplots

trace1 = go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 4, 6, 8, 10], mode='lines+markers', name='折线图')

fig = make_subplots(rows=1, cols=1)
fig.add_trace(trace1, row=1, col=1)
fig.update_layout(title_text='Plotly折线图示例', xaxis_title='X轴', yaxis_title='Y轴')
fig.show()


# import plotly.graph_objs as go
# from plotly.subplots import make_subplots
#
# trace1 = go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 4, 6, 8, 10], mode='lines+markers', name='折线图')
# trace2 = go.Bar(x=[1, 2, 3, 4, 5], y=[3, 6, 9, 12, 15], name='柱状图')
#
# fig = make_subplots(rows=1, cols=2)
# fig.add_trace(trace1, row=1, col=1)
# fig.add_trace(trace2, row=1, col=2)
# fig.update_layout(title_text='Plotly折线图与柱状图示例', xaxis_title='X轴', yaxis_title='Y轴')
# fig.show()
