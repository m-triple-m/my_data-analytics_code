import plotly.express as px


def scatter3D(data, x_col, y_col, z_col, color_col, size_col):
    return px.scatter_3d(data_frame=data,
                         x=x_col,
                         y=y_col,
                         z=z_col,
                         color=color_col,
                         size=size_col,
                         height=800)

