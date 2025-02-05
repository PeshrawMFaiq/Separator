import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Define separator dimensions
LENGTH = 2  # meters
DIAMETER = 0.5  # meters

# Function to create 3D separator
def create_separator():
    theta = np.linspace(0, 2 * np.pi, 40)
    z = np.linspace(-LENGTH / 2, LENGTH / 2, 40)
    theta_grid, z_grid = np.meshgrid(theta, z)

    x_grid = (DIAMETER / 2) * np.cos(theta_grid)
    y_grid = (DIAMETER / 2) * np.sin(theta_grid)

    fig = go.Figure()

    # Separator shell
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="gray", opacity=0.3, name="Separator"))

    return fig

# Function to animate flow
def animate_flow():
    fig = create_separator()

    num_frames = 30
    frames = []

    for i in range(num_frames):
        shift = i * 0.05  # Flow shift per frame

        # Simulated fluid flows
        water_flow = go.Scatter3d(
            x=np.linspace(-0.4, 0.4, 15) + np.sin(i * 0.2) * 0.05,
            y=np.zeros(15),
            z=np.linspace(-0.5, 0, 15),
            mode="lines",
            line=dict(color="blue", width=5),
            name="Water"
        )
        oil_flow = go.Scatter3d(
            x=np.linspace(-0.3, 0.3, 15) + np.sin(i * 0.3) * 0.05,
            y=np.zeros(15),
            z=np.linspace(0, 0.3, 15),
            mode="lines",
            line=dict(color="orange", width=5),
            name="Oil"
        )
        gas_flow = go.Scatter3d(
            x=np.linspace(-0.2, 0.2, 15) + np.sin(i * 0.4) * 0.05,
            y=np.zeros(15),
            z=np.linspace(0.3, 0.6, 15),
            mode="lines",
            line=dict(color="yellow", width=5),
            name="Gas"
        )

        frames.append(go.Frame(data=[water_flow, oil_flow, gas_flow]))

    fig.frames = frames

    fig.update_layout(
        title="Three-Phase Separator (Interactive 3D Flow)",
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
st.title("3D Three-Phase Separator Visualization")
st.write("Visualize the flow of oil, water, and gas in a horizontal three-phase separator.")

if st.button("Show Separator"):
    st.plotly_chart(create_separator())

if st.button("Start Animation"):
    st.plotly_chart(animate_flow())
