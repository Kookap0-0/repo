import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage, max_time):
    plt.figure(figsize=(10,6))
    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.xlim(0, max_time*1.1)
    plt.ylim(0,max_voltage*1.1)
    plt.grid(which='major',linestyle='-')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle='--', linewidth = 0.5)

    plt.plot(time,voltage, ms = 1, linewidth = 0.5, color = '#1f77b4')

    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = [0]
    for i in range(len(time)-1):
        sampling_periods.append(time[i+1]-time[i])

    plt.figure(figsize=(10,6))    
    plt.title('Распределение периодов дискредитации измерений по времени на одно измерение')
    plt.xlabel('Период измерения, с')
    plt.ylabel('Количество измерений')
    plt.xlim(0, 0.6)
    plt.grid(which='major',linestyle='-')
    plt.minorticks_on()
    plt.grid(which='minor',linestyle='--', linewidth = 0.5)

    plt.hist(sampling_periods)

    plt.show()