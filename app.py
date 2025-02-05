import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Separator Dimensions (meters)
LENGTH = 2  # Separator length
DIAMETER = 0.5  # Separator diameter
WEIR_HEIGHT = 0.3  # Height of weir plate

# Function to create 3D separator with inlets and outlets
def create_separator():
    theta = np.linspace(0, 2 * np.pi, 40)
    z = np.linspace(-LENGTH / 2, LENGTH / 2, 40)
    theta_grid, z_grid = np.meshgrid(theta, z)

    x_grid = (DIAMETER / 2) * np.cos(theta_grid)
    y_grid = (DIAMETER / 2) * np.sin(theta_grid)

    fig = go.Figure()

    # Separator Shell
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="gray", opacity=0.3, name="Separator"))

    # Inlet Pipe (Left Side)
    inlet_x = np.linspace(-LENGTH / 2 - 0.2, -LENGTH / 2, 10)
    fig.add_trace(go.Scatter3d(x=inlet_x, y=np.zeros(10), z=np.zeros(10), mode="lines",
                               line=dict(color="red", width=6), name="Inlet Pipe"))

    # Gas Outlet (Top)
    fig.add_trace(go.Scatter3d(x=[LENGTH / 2], y=[0], z=[DIAMETER / 2], mode="markers",
                               marker=dict(color="yellow", size=8), name="Gas Outlet"))

    # Oil Outlet (Right Side, Middle)
    fig.add_trace(go.Scatter3d(x=[LENGTH / 2], y=[0], z=[0.1], mode="markers",
                               marker=dict(color="orange", size=8), name="Oil Outlet"))

    # Water Outlet (Right Side, Bottom)
    fig.add_trace(go.Scatter3d(x=[LENGTH / 2], y=[0], z=[-0.2], mode="markers",
                               marker=dict(color="blue", size=8), name="Water Outlet"))

    # Weir Plate (Partial Wall for Oil-Water Separation)
    weir_x = np.array([0.2, 0.2, -0.2, -0.2])
    weir_y = np.zeros(4)
    weir_z = np.array([-0.3, WEIR_HEIGHT, WEIR_HEIGHT, -0.3])
    fig.add_trace(go.Mesh3d(x=weir_x, y=weir_y, z=weir_z, color='lightgray', opacity=0.6, name="Weir Plate"))

    return fig

# Function to animate the flow of oil, water, and gas
def animate_flow():
    fig = create_separator()

    num_frames = 30
    frames = []

    for i in range(num_frames):
        shift = i * 0.05  # Flow movement shift

        # Simulated flow paths
        water_flow = go.Scatter3d(
            x=np.linspace(-0.4, 0.4, 15) + np.sin(i * 0.2) * 0.05,
            y=np.zeros(15),
            z=np.linspace(-0.3, -0.1, 15),
            mode="lines",
            line=dict(color="blue", width=5),
            name="Water Flow"
        )
        oil_flow = go.Scatter3d(
            x=np.linspace(-0.3, 0.3, 15) + np.sin(i * 0.3) * 0.05,
            y=np.zeros(15),
            z=np.linspace(-0.1, 0.1, 15),
            mode="lines",
            line=dict(color="orange", width=5),
            name="Oil Flow"
        )
        gas_flow = go.Scatter3d(
            x=np.linspace(-0.2, 0.2, 15) + np.sin(i * 0.4) * 0.05,
            y=np.zeros(15),
            z=np.linspace(0.1, DIAMETER / 2, 15),
            mode="lines",
            line=dict(color="yellow", width=5),
            name="Gas Flow"
        )

        frames.append(go.Frame(data=[water_flow, oil_flow, gas_flow]))

    fig.frames = frames

    fig.update_layout(
        title="Oilfield Three-Phase Separator (3D Interactive Animation)",
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
        ),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Start Animation", method="animate", args=[None, dict(frame=dict(duration=100, redraw=True))])]
        )]
    )

    return fig

# Streamlit UI
st.title("3D Horizontal Three-Phase Separator")
st.write("Visualize the oil, water, and gas separation in a horizontal three-phase separator.")

if st.button("Show Separator"):
    st.plotly_chart(create_separator())

if st.button("Start Animation"):
    st.plotly_chart(animate_flow())
