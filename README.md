# Customer Analytics: Monthly Revenue Trend (Seaborn)

This repository folder contains a professional Seaborn visualization that shows **monthly revenue trends across customer segments** for executive reporting.

- **Email:** 23f3004267@ds.study.iitm.ac.in
- **Files:** `chart.py` (script), `chart.png` (generated figure, 512×512), `README.md` (this file)

## How to run locally

```bash
# 1) (optional) create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) install deps
pip install seaborn pandas matplotlib numpy pillow

# 3) run the script to generate chart.png
python chart.py
```

## Notes
- Figure size is set to 8×8 inches and saved at **dpi=64**, yielding **512×512** pixels.
- `bbox_inches='tight'` is used for crisp exports; a small post-check ensures the final saved image remains **exactly 512×512** if tight-cropping changes the pixel dimensions.
- The chart uses **`sns.lineplot`** with professional styling.
