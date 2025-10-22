import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage, max_time):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage, ms = 1, linewidth = 0.5, color = '#1f77b4')
    plt.set_xlabel('Time, s')
    plt.set_ylabel('Voltage, V')
    plt.set_xlim(0, max_time*1.1)
    plt.set_ylim(0,max_voltage*1.1)
    plt.show()