<!-- GSD -->
# Social Media Usage Analysis

Demo project analyzing platform engagement and demographic patterns across 7 social media platforms using 500 synthetic user profiles.

## Features

- **Platform Market Share** — Pie chart showing Instagram (30%), YouTube (25%), WhatsApp (15%), Facebook, Twitter/X, LinkedIn, Snapchat distribution
- **Daily Usage Analysis** — Bar chart of average minutes per day by platform, sorted highest to lowest
- **Age Group vs Platform Heatmap** — Cross-tabulation heatmap (6 age groups x 7 platforms) with numeric annotations
- **Engagement Rate Ranking** — Horizontal bar chart comparing average engagement rates by platform
- **Usage Category Segmentation** — Categorical breakdown: Low (<30m), Moderate (30-60m), High (1-2h), Very High (2-5h), Extreme (5h+)
- **Interactive Chart** — Plotly HTML with hover tooltips, pie chart, bar charts, and scatter plot (usage vs engagement)
- **CSV Export** — Full profile dataset (500 rows) and per-platform aggregated stats

## Tech Stack

| Component | Library | Version |
|-----------|---------|---------|
| Data processing | pandas | 2.0+ |
| Statistical distributions | numpy | 1.24+ |
| Static charts | matplotlib | 3.7+ |
| Interactive charts | plotly | 5.x |
| Color palette | Set2 (matplotlib / plotly.qualitative) | — |

## Quick Start

```bash
git clone https://github.com/harshvardhankulkarni/social-media-usage-analysis.git
cd social-media-usage-analysis
pip install pandas numpy matplotlib plotly
python social_media_analysis.py
python generate_interactive.py
```

## Project Structure

```
social-media-usage-analysis/
├── social_media_analysis.py       Main analysis script (static charts + CSV export)
├── generate_interactive.py        Plotly interactive HTML generation
├── social_media_usage_analysis.ipynb  Jupyter notebook
├── index.html                     GitHub Pages landing page
├── social_media_data.csv          Generated dataset (500 user profiles, 10 columns)
├── platform_analysis.csv          Per-platform aggregated stats
├── social_media_analysis.png      Static 4-panel visualization
├── social_media_interactive.html  Interactive Plotly chart
├── docs/
│   ├── ARCHITECTURE.md            Data flow and design decisions
│   ├── GETTING-STARTED.md         Prerequisites and first run
│   ├── DEVELOPMENT.md             Extension and modification guide
│   ├── TESTING.md                 Manual validation procedures
│   └── CONFIGURATION.md           Inline parameters reference
└── README.md                      This file
```

## Demo

This is a portfolio demo project using fully synthetic data. No real user data is collected or processed. Live at [harshvardhankulkarni.github.io/social-media-usage-analysis](https://harshvardhankulkarni.github.io/social-media-usage-analysis/).
