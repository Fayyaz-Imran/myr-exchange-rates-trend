import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('exchangerates.csv')

# Filter data for years 2022, 2023, and 2024
df_2022 = data[data['date'].str.startswith('2022')].drop(columns=['date'])
df_2023 = data[data['date'].str.startswith('2023')].drop(columns=['date'])
df_2024 = data[data['date'].str.startswith('2024')].drop(columns=['date'])

# Function to calculate percent change
def calculate_percent_change(df):
    return (df.iloc[-1] - df.iloc[0]) / df.iloc[0] * 100

# Calculate percent change for each year
percent_change_2022 = calculate_percent_change(df_2022)
percent_change_2023 = calculate_percent_change(df_2023)
percent_change_2024 = calculate_percent_change(df_2024)

# Plotting all in one visualization using subplots
fig, axes = plt.subplots(4, 1, figsize=(8, 24))

# Plot percent change for each year
bars_2022 = axes[0].bar(percent_change_2022.index, percent_change_2022.values, color='skyblue')
axes[0].set_title('Percent Change in 2022')
axes[0].set_xlabel('Currency')
axes[0].set_ylabel('Percent Change')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis='y')
for bar in bars_2022:
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', 
                 ha='center', va='bottom')

bars_2023 = axes[1].bar(percent_change_2023.index, percent_change_2023.values, color='lightgreen')
axes[1].set_title('Percent Change in 2023')
axes[1].set_xlabel('Currency')
axes[1].set_ylabel('Percent Change')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y')
for bar in bars_2023:
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', 
                 ha='center', va='bottom')

bars_2024 = axes[2].bar(percent_change_2024.index, percent_change_2024.values, color='salmon')
axes[2].set_title('Percent Change in 2024')
axes[2].set_xlabel('Currency')
axes[2].set_ylabel('Percent Change')
axes[2].tick_params(axis='x', rotation=45)
axes[2].grid(axis='y')
for bar in bars_2024:
    axes[2].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', 
                 ha='center', va='bottom')

# Subplot 3: Trend of Percent Change Over 3 Years
axes[3].plot(percent_change_2022.index, percent_change_2022.values, marker='o', color='skyblue', label='2022')
axes[3].plot(percent_change_2023.index, percent_change_2023.values, marker='o', color='lightgreen', label='2023')
axes[3].plot(percent_change_2024.index, percent_change_2024.values, marker='o', color='salmon', label='2024')
axes[3].set_title('Trend of Percent Change Over 3 Years')
axes[3].set_xlabel('Currency')
axes[3].set_ylabel('Percent Change')
axes[3].tick_params(axis='x', rotation=45)
axes[3].legend()
axes[3].grid(True)

plt.tight_layout()
plt.show()
