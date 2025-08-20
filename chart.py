import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter

# ------------------------------
# Professional Seaborn styling
# ------------------------------
sns.set_theme(style="whitegrid", context="talk", font_scale=1.1)

# ------------------------------
# Generate realistic synthetic data
# Business scenario: monthly revenue by segment with seasonality + growth
# ------------------------------
rng = np.random.default_rng(42)

# 24 months to show trend clearly
months = pd.period_range("2024-01", "2025-12", freq="M").to_timestamp()

segments = [
    {"name": "Enterprise", "base": 650, "trend": 11.0, "season_amp": 140, "noise": 40},
    {"name": "SMB",        "base": 420, "trend":  8.0, "season_amp": 120, "noise": 35},
    {"name": "Consumer",   "base": 310, "trend":  6.5, "season_amp": 160, "noise": 50},
]

rows = []
for t, date in enumerate(months):
    m = date.month  # 1..12
    # Seasonal pattern: stronger in festival/holiday months (Nov-Dec) with a mid-year bump
    seasonal_base = (
        np.sin(2 * np.pi * (m - 1) / 12 + np.pi / 6)          # main annual cycle
        + 0.35 * np.sin(4 * np.pi * (m - 1) / 12)             # secondary harmonic
    )
    for seg in segments:
        seasonal = seasonal_base * (seg["season_amp"] / 2.0)
        value = seg["base"] + seg["trend"] * t + seasonal + rng.normal(0, seg["noise"])
        rows.append({"month": date, "segment": seg["name"], "revenue_kusd": max(0, value)})

df = pd.DataFrame(rows)

# ------------------------------
# Build the line plot
# ------------------------------
plt.figure(figsize=(8, 8))  # ensures 512x512 at dpi=64

ax = sns.lineplot(
    data=df,
    x="month",
    y="revenue_kusd",
    hue="segment",
    marker="o",
    linewidth=2.2,
    palette="Set2",
)

# Labels and title
ax.set_title("Monthly Revenue Trend by Customer Segment", pad=14)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (USD, thousands)")

# Format y-axis with thousands and $
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"${int(y):,}k"))

# Improve legend and grid aesthetics
ax.legend(title="Segment", loc="upper left", frameon=True)
sns.despine()

# Tighten layout a bit for presentation
plt.tight_layout()

# ------------------------------
# Export exactly 512x512
# ------------------------------
# Guideline-required call:
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

# If tight bbox alters pixel dims, correct to exactly 512x512.
try:
    from PIL import Image
    im = Image.open("chart.png")
    if im.size != (512, 512):
        im = im.resize((512, 512), Image.LANCZOS)
        im.save("chart.png")
except Exception:
    # If Pillow not available, we leave the image as saved.
    pass
