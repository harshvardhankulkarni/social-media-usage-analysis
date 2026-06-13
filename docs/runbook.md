# Runbook: Social Media Usage Analysis

## When to Use This Runbook

- Running the analysis for the first time.
- Modifying platform weights or demographic distributions.
- Exporting results for a marketing report.

## Prerequisites

- Python 3.8+ installed.
- pip installed.

## Procedure

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Step 2: Run the Analysis

```bash
cd path/to/social-media-usage-analysis
python social_media_analysis.py
```

### Step 3: Verify Output

Check for these files:

- `social_media_analysis.png` - 4-panel chart (pie, bars, heatmap, horizontal bars).
- `social_media_data.csv` - 500 rows with all user attributes.
- `platform_analysis.csv` - Aggregated platform statistics.

### Step 4: Interpret the Results

Key insights from the console output:

- Which platform has the largest market share.
- Which age group is most active.
- Average daily usage across all users.
- Which platform has the highest engagement rate.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| No chart displayed | Backend not set | Add `matplotlib.use('Agg')` before import |
| Platform weights wrong | Modified probabilities | Reset to original or ensure they sum to 1.0 |
| Heatmap labels overlap | Too many platforms | Reduce to top 5 platforms |
| CSV has 0 rows | Script failed mid-execution | Check for error before the CSV export line |
| All users same platform | Seed issue or wrong probability | Check `p` argument in `np.random.choice` |

## Customization

### Change Sample Size

```python
n_users = 1000  # Default is 500
```

### Adjust Platform Weights

```python
platforms = ['Instagram', 'YouTube', 'WhatsApp', 'Facebook', 'Twitter/X', 'LinkedIn', 'Snapchat']
weights = [0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05]  # Must sum to 1.0
```

### Add a New Platform

1. Add the platform name to the `platforms` list.
2. Add a weight in the `p` parameter.
3. Ensure all weights still sum to 1.0.
4. Add the platform to the color palette if desired.

## Escalation

Open a GitHub issue with:

- Modified script or parameters.
- Error output if any.
- Expected vs actual results.
- Python version.
