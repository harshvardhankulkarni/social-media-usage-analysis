<!-- GSD -->
# Testing: Social Media Usage Analysis

## Automated Tests

This project has no automated test suite. The analysis is deterministic (fixed random seed) so output is identical across runs.

## Manual Validation Checklist

### Run 1: Main Script

```bash
python social_media_analysis.py
```

Check:

- [ ] Script completes without errors
- [ ] Console prints "Saved: social_media_analysis.png"
- [ ] Console prints "Exported: social_media_data.csv, platform_analysis.csv"
- [ ] Console prints "Done."

### Run 2: Output Existence

- [ ] `social_media_analysis.png` exists and is viewable
- [ ] `social_media_data.csv` exists
- [ ] `platform_analysis.csv` exists

### Run 3: Data Integrity

```python
import pandas as pd
df = pd.read_csv('social_media_data.csv')
```

- [ ] `df.shape == (500, 10)` — 500 profiles, 10 columns
- [ ] Column names match: `user_id, age_group, gender, region, primary_platform, daily_usage_mins, posts_per_week, accounts_followed, engagement_rate_pct, years_active, daily_category`
- [ ] `df['user_id'].nunique() == 500` — all unique IDs
- [ ] `df['daily_usage_mins'].min() >= 5` — clip lower bound
- [ ] `df['daily_usage_mins'].max() <= 480` — clip upper bound
- [ ] `df['primary_platform'].value_counts().sum() == 500`
- [ ] 7 unique platforms in `df['primary_platform']`
- [ ] 6 unique age groups in `df['age_group']`
- [ ] 5 unique categories in `df['daily_category']`

### Run 4: Platform Stats

```python
pa = pd.read_csv('platform_analysis.csv')
```

- [ ] `pa.shape == (7, 5)` — 7 platforms, 5 columns
- [ ] Column names: `primary_platform, user_count, avg_usage, avg_posts, avg_engagement, pct_users`
- [ ] `pa['pct_users'].sum() ≈ 100` (may be 99.9-100.1 due to rounding)

### Run 5: Chart Validation

- [ ] PNG shows 4 panels in 2x2 grid
- [ ] Panel [0,0]: Pie chart with 7 labeled segments, percentages shown
- [ ] Panel [0,1]: Vertical bar chart with value labels on top
- [ ] Panel [1,0]: Heatmap with 6 rows (age groups) x 7 columns (platforms), numeric annotations, YlOrRd colormap
- [ ] Panel [1,1]: Horizontal bar chart with value labels
- [ ] Chart uses Set2 color palette (7 distinct colors)

### Run 6: Interactive Version

```bash
python generate_interactive.py
```

- [ ] Script completes, prints "Saved: social_media_interactive.html"
- [ ] HTML file opens in browser
- [ ] 4 panels render: pie, 2 bars, scatter
- [ ] Hover tooltips work on all panels
- [ ] Scatter plot shows daily_usage_mins on x-axis, engagement_rate_pct on y-axis
- [ ] Pie chart shows percentages

### Run 7: Reproducibility

- [ ] Delete CSVs and PNG, rerun `social_media_analysis.py` — output files are byte-identical (same seed)
- [ ] Delete HTML, rerun `generate_interactive.py` — same output
