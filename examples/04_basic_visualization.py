"""
Basic Data Visualization

Learn how to create simple, effective visualizations to communicate your findings.
Visualization help you and others understand data at a glance.

What you'll learn:
- How to create bar charts
- How to create line plots
- How to create pie charts
- How to customize and save your visualizations

Prerequisites:
- pandas library (install with: pip install pandas)
- matplotlib library (install with: pip install matplotlib)
"""

import pandas as pd
import matplotlib.pyplot as plt

print("=" * 70)
print("Basic Data Visualization Tutorial")
print("=" * 70)
print()

# Load data
print("📂 Loading honey production data...")
data = pd.read_csv("data/honey.csv")
print("✅ Data loaded!\n")

# For better display, we'll use a subset of the data
# Let's focus on a few states in recent years
if "state" in data.columns and "year" in data.columns:
    # Get data for a few states in recent years
    states_to_show = ["CA", "FL", "ND", "SD", "MT"]
    recent_data = data[(data.year >= 2010) & (data.state.isin(states_to_show))]

# VISUALIZATION 1: Bar Chart
print("=" * 70)
print("VISUALIZATION 1: BAR CHART")
print("=" * 70)
print()

if "state" in data.columns and "totalprod" in data.columns:
    # Calculate average production by state (for top 10 states)
    state_avg = data.groupby("state")["totalprod"].mean().sort_values(ascending=False).head(10)
    print("Creating a bar chart of average honey production by state...")
    print()

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))  # width 12 inches, height 6 inches

    # Create the bar chart
    ax.bar(state_avg.index, state_avg.values, color="gold", edgecolor="orange")

    # Add labels and title
    ax.set_xlabel("State", fontsize=12)
    ax.set_ylabel("Average Production (pounds)", fontsize=12)
    ax.set_title("Top 10 States by Average Honey Production", fontsize=14, fontweight="bold")

    # Rotate x-axis labels for better readability
    ax.tick_params(axis="x", rotation=45)

    # Add a grid for easier reading (behind the bars)
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    # Adjust layout to prevent label cutoff
    fig.tight_layout()

    # Save the figure
    plt.savefig("examples/bar_chart_example.png", dpi=300, bbox_inches="tight")
    print("✅ Bar chart saved as 'bar_chart_example.png")
    print()

    # Display all open figures
    plt.show()

# VISUALIZATION 2: Line Plot
print("=" * 70)
print("VISUALIZATION 2: LINE PLOT")
print("=" * 70)
print()

if "year" in data.columns and "totalprod" in data.columns:
    # Calculate total production by year
    yearly_production = data.groupby("year")["totalprod"].sum()

    print("Creating a line plot of honey production over time...")
    print()

    fig, ax = plt.subplots(figsize=(12, 6))

    # Create the line plot
    ax.plot(
        yearly_production.index,
        yearly_production.values,
        marker="o",  # Add circular markers at each data point
        linewidth=2,  # Line thickness
        color="darkorange",  # Line color
        markersize=6,  # Size of markers
        markerfacecolor="gold",  # Fill color of markers
    )

    # Add labels and title
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Total Production (pounds)", fontsize=12)
    ax.set_title("Honey Production over Time", fontsize=14, fontweight="bold")

    # Add a grid
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    fig.tight_layout()

    # Save the figure
    plt.savefig("examples/line_plot_example.png", dpi=300, bbox_inches="tight")
    print("✅ Line plot saved as 'line_plot_example.png")
    print()

    # Display all open figures
    plt.show()

# VISUALIZATION 3: Pie Chart
print("=" * 70)
print("VISUALIZATION 3: PIE CHART")
print("=" * 70)
print()

if "state" in data.columns and "totalprod" in data.columns:
    # Get total production for top 5 states
    top5_states = data.groupby("state")["totalprod"].sum().sort_values(ascending=False).head(5)

    print("Creating a pie chart of production share (top 5 states)...")
    print()

    fig, ax = plt.subplots(figsize=(10, 8))

    # Create the pie chart
    colors = ["gold", "orange", "lightsalmon", "lightcoral", "peachpuff"]
    ax.pie(
        top5_states.values,
        labels=top5_states.index,  # State names
        autopct="%1.1f%%",  # Show percentages
        startangle=90,  # Start from top
        colors=colors,
        explode=(0.1, 0, 0, 0, 0),  # Slightly separate the first slice
    )

    ax.set_title("Top 5 States Share of Total Honey Production", fontsize=14, fontweight="bold", pad=20)

    # Save the bar plot
    plt.savefig("examples/pie_chart_example.png", dpi=300, bbox_inches="tight")
    print("✅ Pie chart saved as 'pie_chart_example.png")
    print()

    # Display all open figures
    plt.show()

# VISUALIZATION 4: Multiple Lines on One Plot
print("=" * 70)
print("VISUALIZATION 4: COMPARING MULTIPLE SERIES")
print("=" * 70)
print()

if "year" in data.columns and "totalprod" in data.columns and "state" in data.columns:
    # Compare production trends for a few states
    states_to_compare = ["CA", "ND", "SD"]

    print(f"Creating a comparison plot for states: {', '.join(states_to_compare)}...")
    print()

    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot a line for each state
    colors_map = {"CA": "blue", "ND": "green", "SD": "red"}

    for state in states_to_compare:
        if state in data["state"].values:
            state_data = data[data["state"] == state].groupby("year")["totalprod"].sum()
            ax.plot(
                state_data.index,  # the years
                state_data.values,  # total production
                marker="o",
                label=state,
                linewidth=2,
                color=colors_map.get(state, "gray"),
            )

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Total Production (pounds)", fontsize=12)
    ax.set_title("Honey Production Comparison by State", fontsize=14, fontweight="bold")
    ax.legend(title="State")
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    fig.tight_layout()

    # Save the graph
    plt.savefig("examples/comparison_plot_example.png", dpi=300, bbox_inches="tight")
    print("✅ Comparison plot saved as 'comparison_plot_example.png")
    print()

    # Display open figures
    plt.show()

# Summary
print("=" * 70)
print("CONGRATULATIONS!")
print("=" * 70)
print("You've learned how to:")
print("  ✓ Create bar charts to compare categories")
print("  ✓ Create line plots to show trends over time")
print("  ✓ Create pie charts to show proportions")
print("  ✓ Plot multiple data series on one chart")
print("  ✓ Customize colors, labels, and titles")
print("  ✓ Save your visualizations as image files")
print()
print("Your visualizations have been saved in the examples/ folder!")
print()
print("Try this yourself:")
print("  • Change the colors of your charts")
print("  • Add more states to the comparison plot")
print("  • Create a horizontal bar chart")
print("  • Experiment with different chart styles")
print()
print("Pro tip: Always choose the right chart type for your data:")
print("  • Bar charts: Compare categories")
print("  • Line plots: Show trends over time")
print("  • Pie charts: Show parts of a whole")
print("  • Scatter plots: Show relationships between variables")
print("=" * 70)
