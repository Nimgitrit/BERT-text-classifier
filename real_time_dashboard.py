import streamlit as st
import matplotlib.pyplot as plt
import time

# Initialize an empty list to store loss values
loss_values = []

# Set the title of the app
st.title("Real-Time Training Loss Visualization")

# Start the loop that simulates real-time graph updates
for epoch in range(10):  # Simulating 10 epochs
    loss = 1 / (epoch + 1)  # Simulated loss value
    loss_values.append(loss)

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(loss_values, label="Loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_title("Training Loss Over Time")
    ax.legend()
    ax.grid()

    # Display the plot in Streamlit
    st.pyplot(fig)

    time.sleep(1)  # Simulate training time delay