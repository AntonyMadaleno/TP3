import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_quality = "../result/csv/quality_evaluation/"
folder_time = "../result/csv/time_evaluation/"
basename = "statistics_"

def readList(file_path):
    
    l = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line by a comma and remove leading/trailing whitespace
                names = [name.strip() for name in line.strip().split(',')]

                # Check if there are two names
                l.append(names[0])

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        # Handle the file not found error here

    return l

filepath = "../Images_TP3/ListTest1.txt"
names = readList(filepath)

array = np.zeros((5,2,len(names)))

Methods = ["None", "Gray World", "White Patch", "White Patch w Threshold", "MHP"]
Eval = ["MSE", "delta_E_Lab"]

i = 0
for name in names:
    df = pd.read_csv(folder_quality + basename + name + ".csv")
    array[:,:,i] = df.values[:,1:]
    i = i + 1

mean = np.mean(array, axis=2)
median = np.median(array, axis=2)

# Create two subplots for the two bar charts
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first bar chart for the first evaluation method
axs[0].bar(Methods, mean[:, 0], color='b', alpha=0.6, label='MSE')
axs[0].set_xlabel('Results')
axs[0].set_ylabel('score (lower is better)')
axs[0].set_title('Bar Chart Mean MSE')
axs[0].legend()

# Plot the second bar chart for the second evaluation method
axs[1].bar(Methods, mean[:, 1], color='r', alpha=0.6, label='delta_E_Lab')
axs[1].set_xlabel('Results')
axs[1].set_ylabel('score (lower is better)')
axs[1].set_title('Bar Chart Mean delta_E_Lab')
axs[1].legend()

# Adjust layout to prevent overlapping labels
plt.tight_layout()
# Save the plots
plt.savefig("../result/csv/graphs/graphs_quality_mean.png")

# Create two subplots for the two bar charts
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first bar chart for the first evaluation method
axs[0].bar(Methods, median[:, 0], color='b', alpha=0.6, label='MSE')
axs[0].set_xlabel('Results')
axs[0].set_ylabel('score (lower is better)')
axs[0].set_title('Bar Chart Mean MSE')
axs[0].legend()

# Plot the second bar chart for the second evaluation method
axs[1].bar(Methods, median[:, 1], color='r', alpha=0.6, label='delta_E_Lab')
axs[1].set_xlabel('Results')
axs[1].set_ylabel('score (lower is better)')
axs[1].set_title('Bar Chart Mean delta_E_Lab')
axs[1].legend()

# Adjust layout to prevent overlapping labels
plt.tight_layout()
# Save the plots
plt.savefig("../result/csv/graphs/graphs_quality_median.png")

df_mean = pd.DataFrame(mean, columns= Eval, index= Methods)
df_median = pd.DataFrame(median, columns= Eval, index= Methods)

df_mean.to_csv(folder_quality + basename + "mean.csv", index=True)
df_median.to_csv(folder_quality + basename + "median.csv", index=True)

array = np.zeros((4,1,len(names)))

Methods = ["Gray World", "White Patch", "White Patch w Threshold", "MHP"]
Eval = ["time_ms"]

i = 0
for name in names:
    df = pd.read_csv(folder_time + basename + name + ".csv")
    array[:,:,i] = df.values[:,1:]
    i = i + 1

mean = np.mean(array, axis=2)
median = np.median(array, axis=2)

df_mean = pd.DataFrame(mean, columns= Eval, index= Methods)
df_median = pd.DataFrame(median, columns= Eval, index= Methods)

df_mean.to_csv(folder_time + basename + "mean.csv", index=True)
df_median.to_csv(folder_time + basename + "median.csv", index=True)

# Create two subplots for the two bar charts
fig, axs = plt.subplots(1, 1, figsize=(12, 5))

# Plot the first bar chart for the first evaluation method
axs.bar(Methods, mean[:, 0], color='b', alpha=0.6, label='Time in ms')
axs.set_xlabel('Results')
axs.set_ylabel('score (lower is better)')
axs.set_title('Bar Chart Mean time_ms')
axs.legend()

# Adjust layout to prevent overlapping labels
plt.tight_layout()
# Save the plots
plt.savefig("../result/csv/graphs/graphs_time_mean.png")

# Create two subplots for the two bar charts
fig, axs = plt.subplots(1, 1, figsize=(12, 5))

# Plot the first bar chart for the first evaluation method
axs.bar(Methods, median[:, 0], color='b', alpha=0.6, label='Time in ms')
axs.set_xlabel('Results')
axs.set_ylabel('score (lower is better)')
axs.set_title('Bar Chart Median time_ms')
axs.legend()

# Adjust layout to prevent overlapping labels
plt.tight_layout()
# Save the plots
plt.savefig("../result/csv/graphs/graphs_time_median.png")