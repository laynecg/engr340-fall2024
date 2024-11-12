import numpy as np
import matplotlib.pyplot as plt

# Motor specifications (example values)
no_load_speed = 4300  # rpm
stall_torque = 2400  # N-cm
rated_voltage = 12  # V
no_load_current = 0.07  # A
stall_current = 1  # A

# Generate speed points
speeds = np.linspace(0, no_load_speed, 100)

# Calculate torque points
torques = stall_torque * (1 - speeds / no_load_speed)

# Calculate current points
currents = no_load_current + (stall_current - no_load_current) * (torques / stall_torque)

# Calculate power points
powers = torques * speeds * 2 * np.pi / 60  # Convert rpm to rad/s

# Calculate efficiency points
input_power = rated_voltage * currents
efficiencies = (powers / input_power) * 100

# Create the merged graph
fig, ax1 = plt.subplots(figsize=(12, 8))

# Torque curve (left y-axis)
color = 'tab:red'
ax1.set_xlabel('Speed (rpm)')
ax1.set_ylabel('Torque (Ncm)', color=color)
ax1.plot(speeds, torques, color=color, label='Torque')
ax1.tick_params(axis='y', labelcolor=color)

# Power curve (right y-axis)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Power (W)', color=color)
ax2.plot(speeds, powers, color=color, label='Power')
ax2.tick_params(axis='y', labelcolor=color)

# Efficiency curve (far right y-axis)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
color = 'tab:green'
ax3.set_ylabel('Efficiency (%)', color=color)
ax3.plot(speeds, efficiencies, color=color, label='Efficiency')
ax3.tick_params(axis='y', labelcolor=color)

# Title and legend
plt.title('Motor Performance Curves')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, loc='upper center')

plt.grid(True)
plt.tight_layout()
plt.show()