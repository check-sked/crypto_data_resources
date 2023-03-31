import csv
import requests
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation
import seaborn as sns

# Input chain name
chain = "Arbitrum"

# Make a request to the endpoint
response = requests.get(f"https://api.llama.fi/charts/{chain}")

# Parse the JSON response
data = response.json()

# Parse the data and extract the dates and liquidity values
dates = []
liquidity = []
for entry in data:
    date_time = datetime.datetime.utcfromtimestamp(int(entry['date']))
    dates.append(date_time)
    liquidity.append(float(entry['totalLiquidityUSD']))

# Set up the figure and axis
sns.set_style("darkgrid")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlabel("", fontsize=12)
ax.set_ylabel("Total Liquidity", fontsize=12)
ax.set_title(f"{chain} TVL", fontsize=16)

# Define the Y axis formatter
def y_fmt(x, pos):
    if x >= 1e9:
        return f"${x/1e9:.1f}b"
    elif x >= 1e6:
        return f"${x/1e6:.1f}m"
    else:
        return f"${x:,.0f}"

y_formatter = ticker.FuncFormatter(y_fmt)
ax.yaxis.set_major_formatter(y_formatter)

# Format the X axis dates
date_format = mdates.DateFormatter("%Y-%m-%d")
fig.autofmt_xdate(rotation=60)
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Define the animation function
def animate(i):
    # Plot the data up to the i-th point
    ax.plot(dates[:i+1], liquidity[:i+1], color="blue", linewidth=2)

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(dates), interval=25)

# Add Twitter handle tag
twitter_tag = r"$\bf{@Check\_Sked}$"
fig.text(0.93, 0.93, twitter_tag, fontsize=10, color="gray", ha="right", va="top")

# Show the plot
plt.show()