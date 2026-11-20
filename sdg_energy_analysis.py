"""
Solar & Wind Energy Transition vs. Grid Carbon Emissions (2020–2026)
DPS Bangalore North | Class X AI (417) Capstone Project

Run:
    pip install -r requirements.txt
    python src/sdg_energy_analysis.py

The input dataset is transcribed from the project report. It represents an
institutional and urban smart-grid cluster in Bengaluru as described in that
report; it should not be interpreted as an independently audited national dataset.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "energy_emissions_2020_2026.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["Total_Renewable_MWh"] = df["Solar_MWh"] + df["Wind_MWh"]
df["Total_Energy_MWh"] = df["Total_Renewable_MWh"] + df["Coal_Grid_MWh"]
df["Renewable_Share_Pct"] = (
    df["Total_Renewable_MWh"] / df["Total_Energy_MWh"] * 100
).round(2)

solar_growth = (df["Solar_MWh"].iloc[-1] / df["Solar_MWh"].iloc[0] - 1) * 100
co2_reduction = (1 - df["CO2_Tons"].iloc[-1] / df["CO2_Tons"].iloc[0]) * 100
correlation = np.corrcoef(df["Total_Renewable_MWh"], df["CO2_Tons"])[0, 1]
solar_cagr = ((df["Solar_MWh"].iloc[-1] / df["Solar_MWh"].iloc[0]) ** (1 / 6) - 1) * 100
wind_cagr = ((df["Wind_MWh"].iloc[-1] / df["Wind_MWh"].iloc[0]) ** (1 / 6) - 1) * 100
crossover = df.loc[
    df["Total_Renewable_MWh"] > df["Coal_Grid_MWh"], "Year"
]
crossover_year = int(crossover.iloc[0]) if not crossover.empty else None

print("\n=== SDG 7 & 13 ENERGY TRANSITION SUMMARY (2020–2026) ===")
print(df[[
    "Year", "Total_Renewable_MWh", "Coal_Grid_MWh",
    "Renewable_Share_Pct", "CO2_Tons"
]].to_string(index=False))
print(f"\nSolar generation growth: +{solar_growth:.1f}%")
print(f"CO2 emissions reduction: -{co2_reduction:.1f}%")
print(f"Pearson correlation (renewables vs CO2): r = {correlation:.4f}")
print(f"Solar CAGR: {solar_cagr:.2f}% | Wind CAGR: {wind_cagr:.2f}%")
print(f"First year renewables exceed coal: {crossover_year or 'Not observed'}")

# Chart 1: grouped bar chart
x = np.arange(len(df))
width = 0.26
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.bar(x - width, df["Solar_MWh"], width, label="Solar", color="#f59e0b")
ax.bar(x, df["Wind_MWh"], width, label="Wind", color="#0ea5e9")
ax.bar(x + width, df["Coal_Grid_MWh"], width, label="Thermal coal grid", color="#475569")
ax.set_title("Annual Energy Generation by Source (2020–2026)", weight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Energy (MWh)")
ax.set_xticks(x, df["Year"])
ax.grid(axis="y", linestyle="--", alpha=0.35)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "chart1_energy_mix_bars.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Chart 2: separate scales avoid implying that unlike units are directly comparable
fig, ax1 = plt.subplots(figsize=(10, 5.5))
ax2 = ax1.twinx()
line1 = ax1.plot(
    df["Year"], df["Total_Renewable_MWh"], marker="o", linewidth=2.6,
    color="#16a34a", label="Total renewable energy (MWh)"
)
line2 = ax2.plot(
    df["Year"], df["CO2_Tons"], marker="s", linewidth=2.6,
    linestyle="--", color="#dc2626", label="CO2 emissions (metric tons)"
)
ax1.set_title("Renewable Energy Growth vs. CO2 Emissions (2020–2026)", weight="bold")
ax1.set_xlabel("Year")
ax1.set_ylabel("Renewable energy (MWh)", color="#15803d")
ax2.set_ylabel("CO2 emissions (metric tons)", color="#b91c1c")
ax1.grid(True, linestyle=":", alpha=0.35)
lines = line1 + line2
ax1.legend(lines, [line.get_label() for line in lines], loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "chart2_renewables_vs_co2.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Export the derived table for inspection
df.to_csv(OUTPUT_DIR / "processed_energy_data.csv", index=False)
print(f"\nCharts and processed data saved in: {OUTPUT_DIR}")
