import pandas as pd
import matplotlib.pyplot as plt

# Load your air quality data into a DataFrame
# Replace 'your_data.csv' with the actual path to your dataset
df = pd.read_csv('C:\Air_Quality_Index_TN.csv')

# Explore your data using df.head() or df.info() to understand its structure

# Calculate average SO2, NO2, and RSPM/PM10 levels across different areas
avg_so2 = df.groupby('City/Town/Village/Area')['SO2'].mean()
avg_no2 = df.groupby('City/Town/Village/Area')['NO2'].mean()
avg_rspm_pm10 = df.groupby('City/Town/Village/Area')['RSPM/PM10'].mean()

# Create a bar chart to visualize the average SO2 levels by area
plt.figure(figsize=(12, 6))
plt.bar(avg_so2.index, avg_so2.values)
plt.xlabel('City/Town/Village/Area')
plt.ylabel('Average SO2 Level')
plt.title('Average SO2 Levels by City/Town/Village/Area')
plt.xticks(rotation=90)
plt.show()

# Create similar bar charts for NO2 and RSPM/PM10
plt.figure(figsize=(12, 6))
plt.bar(avg_no2.index, avg_no2.values)
plt.xlabel('City/Town/Village/Area')
plt.ylabel('Average NO2 Level')
plt.title('Average NO2 Levels by City/Town/Village/Area')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(avg_rspm_pm10.index, avg_rspm_pm10.values)
plt.xlabel('StatCity/Town/Village/Area')
plt.ylabel('Average RSPM/PM10 Level')
plt.title('Average RSPM/PM10 Levels by City/Town/Village/Area')
plt.xticks(rotation=90)
plt.show()

# You can customize these charts and create more visualizations as needed

# plt.savefig('average_so2_levels.png')
 #lt.savefig('average_no2_levels.png')
 #plt.savefig('average_rspm_pm10_levels.png')
