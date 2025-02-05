import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_separator():
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(0, 2.2)
    ax.set_ylim(-0.3, 0.3)

    # Separator Vessel
    separator = patches.Rectangle((0, -0.25), 2, 0.5, linewidth=2, edgecolor='black', facecolor='lightgray')
    ax.add_patch(separator)

    # Phase Layers
    water = patches.Rectangle((0, -0.25), 2, 0.15, linewidth=0, facecolor='blue', alpha=0.6, label="Water")
    oil = patches.Rectangle((0, -0.1), 2, 0.15, linewidth=0, facecolor='orange', alpha=0.6, label="Oil")
    gas = patches.Rectangle((0, 0.05), 2, 0.2, linewidth=0, facecolor='yellow', alpha=0.5, label="Gas")

    ax.add_patch(water)
    ax.add_patch(oil)
    ax.add_patch(gas)

    # Weir Plate
    weir = patches.Rectangle((1.5, -0.25), 0.05, 0.3, linewidth=2, edgecolor='black', facecolor='darkgray', label="Weir Plate")
    ax.add_patch(weir)

    # Inlet and Outlets
    ax.plot(-0.1, 0, "ro", markersize=8, label="Inlet")
    ax.plot(2.1, -0.1, "go", markersize=8, label="Water Outlet")
    ax.plot(2.1, 0.1, "bo", markersize=8, label="Oil Outlet")
    ax.plot(2.1, 0.25, "yo", markersize=8, label="Gas Outlet")

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Three-Phase Separator (Oil-Water-Gas)")

    plt.legend()
    st.pyplot(fig)

# Streamlit UI
st.title("Three-Phase Separator Visualization")
st.write("This app visualizes a horizontal three-phase separator with oil, water, and gas layers.")

if st.button("Show Separator"):
    draw_separator()
