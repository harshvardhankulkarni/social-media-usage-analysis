<!-- GSD -->
# Getting Started: Social Media Usage Analysis

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

## Installation

```bash
git clone https://github.com/harshvardhankulkarni/social-media-usage-analysis.git
cd social-media-usage-analysis
pip install pandas numpy matplotlib plotly
```

## First Run

Run the main analysis script:

```bash
python social_media_analysis.py
```

Expected output:

```
Saved: social_media_analysis.png

--- SOCIAL MEDIA USAGE ANALYSIS (DEMO) ---
Total users analyzed: 500

Platform Market Share:
  Instagram: 30.0% (150 users, 78 mins/day)
  YouTube: 24.6% (123 users, 68 mins/day)
  WhatsApp: 15.4% (77 users, 74 mins/day)
  Facebook: 10.6% (53 users, 74 mins/day)
  Twitter/X: 8.0% (40 users, 70 mins/day)
  LinkedIn: 6.6% (33 users, 73 mins/day)
  Snapchat: 4.8% (24 users, 89 mins/day)

Most used platform: Instagram
Most active age group: 25-34
Average daily usage across all users: 73 mins
Average posts per week: 3.0

Key Insights:
  1. Instagram dominates primary platform preference.
  2. 25-34 age group is most active on social media.
  3. Users with highest engagement spend 4.1% more time on platforms.

Exported: social_media_data.csv, platform_analysis.csv
Done.
```

## Interactive Version

```bash
python generate_interactive.py
```

Opens `social_media_interactive.html` in browser. Hover over chart elements for tooltips. Scatter plot shows usage vs engagement relationship with platform hover labels.

## Expected Output Files

| File | Contents |
|------|----------|
| `social_media_analysis.png` | 4-panel static chart (pie, 2 bars, heatmap) |
| `social_media_data.csv` | 500 rows x 10 columns of generated profiles |
| `platform_analysis.csv` | 7 rows of per-platform aggregated statistics |
| `social_media_interactive.html` | Plotly interactive chart (pie, 2 bars, scatter) |
