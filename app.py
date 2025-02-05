import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

def create_3d_separator():
    # Cylinder dimensions
    length = 2
    radius = 0.25
    
    # Create cylinder surface
    theta = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(0, length, 50)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Create plot
    fig = go.Figure()

    # Separator shell
    fig.add_trace(go.Surface(x=x, y=y, z=z, opacity=0.2, colorscale='gray', showscale=False))

    # Fluid layers (simplified)
    fluid_z = np.linspace(0, length, 50)
    for layer, color, label in zip([0.1, 0.2, 0.3], ['blue', 'orange', 'yellow'], ['Water', 'Oil', 'Gas']):
        fig.add_trace(go.Surface(
            x=x, y=y, z=fluid_z - (length/2) + layer,
            colorscale=[[0, color], [1, color]],
            showscale=False, opacity=0.6,
            name=label
        ))

    # Layout
    fig.update_layout(
        title="3D Three-Phase Separator",
        scene=dict(
            xaxis=dict(title='Width (m)'),
            yaxis=dict(title='Height (m)'),
            zaxis=dict(title='Length (m)', range=[-length/2, length/2])
        ),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    return fig

def animate_flow():
    # Animation settings
    steps = 20
    delay = 0.1  # seconds

    for step in range(steps):
        # Update the fluid levels to simulate flow
        fig = create_3d_separator()
        shift = 0.05 * np.sin(2 * np.pi * step / steps)
        fig.update_traces(selector=dict(name='Water'), zshift=shift)
        fig.update_traces(selector=dict(name='Oil'), zshift=-shift)
        fig.update_traces(selector=dict(name='Gas'), zshift=shift)

        st.plotly_chart(fig)
        time.sleep(delay)

# Streamlit UI
st.title("Interactive 3D Three-Phase Separator")
st.write("Visualize and animate the flow of oil, water, and gas in a horizontal three-phase separator.")

if st.button("Start Animation"):
    animate_flow()
else:
    fig = create_3d_separator()
    st.plotly_chart(fig)
