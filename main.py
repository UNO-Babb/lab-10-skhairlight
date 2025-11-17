#MapPlot.py
#Name: Salsabiel Khair Allah
#Date: Nov.16
#Assignment: Lab 10

import pandas as pd
import matplotlib.pyplot as plt
import airlines

data = airlines.get_reports()

years = []
delays = []

# ----- Step 2: Explore/Extract Data -----
for row in data:
    years.append(row["Time"]["Year"])
    delays.append(row["Statistics"]["Delays"]["Total"])

# ----- Step 3: Make DataFrame -----
df = pd.DataFrame({
    "Year": years,
    "Delays": delays
})

# ----- Step 4: Clean Data -----
df = df[df["Delays"] > 0]
df = df[df["Delays"] < 200000]

# ----- Step 3: Plot -----
plt.plot(df["Year"], df["Delays"])
plt.xlabel("Year")
plt.ylabel("Total Delays")
plt.title("Airline Delays Over Time")
plt.show()

# ----- Step 5: Explanation -----
print("This graph shows how airline delays changed over time. The plot makes it easy to see peaks and overall trends.")


