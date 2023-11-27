from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

p = figure(title="Bokeh折线图示例", x_axis_label='X轴', y_axis_label='Y轴')
p.line(x, y, legend_label="折线图", line_width=2)
show(p)

