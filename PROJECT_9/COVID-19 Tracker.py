import requests
import matplotlib.pyplot as plt

url = "https://disease.sh/v3/covid-19/all"  # Global data

response = requests.get(url)
data = response.json()

# Display stats
print(f"🌍 Global COVID-19 Stats:")
print(f"🦠 Cases: {data['cases']}")
print(f"✅ Recovered: {data['recovered']}")
print(f"💀 Deaths: {data['deaths']}")

# Pie chart
labels = ['Active', 'Recovered', 'Deaths']
sizes = [
    data['cases'] - data['recovered'] - data['deaths'],
    data['recovered'],
    data['deaths']
]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Global COVID-19 Distribution")
plt.axis('equal')
plt.show()