<!-- GSD -->
# Development: Social Media Usage Analysis

## Project Structure

```
social-media-usage-analysis/
├── social_media_analysis.py       — Main: 124 lines. Generate → Analyze → Visualize → Export
├── generate_interactive.py        — Interactive: 53 lines. Plotly HTML output
├── social_media_usage_analysis.ipynb  — Jupyter equivalent of main script
├── index.html                     — GitHub Pages landing (HTML/CSS, no frameworks)
├── social_media_data.csv          — Generated dataset (git-ignored or tracked)
├── platform_analysis.csv          — Aggregated stats (git-ignored or tracked)
├── social_media_analysis.png      — Static chart (git-ignored or tracked)
├── social_media_interactive.html  — Interactive chart (git-ignored or tracked)
└── docs/                          — GSD-standard documentation
```

## How to Add a Platform

1. Add the name to `platforms` list in `social_media_analysis.py` (line 14) and `generate_interactive.py` (line 10)
2. Add a weight in the `p` parameter of `np.random.choice` — all weights must sum to 1.0
3. If adding beyond 7 items, extend the color palette: `colors = plt.cm.Set2(np.linspace(0, 1, len(platforms)))`
4. In `generate_interactive.py`, update `marker_color` to use `px.colors.qualitative.Set2[:len(platforms)]`

Example — add TikTok:

```python
platforms = ['Instagram', 'YouTube', 'WhatsApp', 'Facebook', 'Twitter/X', 'LinkedIn', 'Snapchat', 'TikTok']
# Original weights sum to 1.0; redistribute:
weights = [0.25, 0.22, 0.14, 0.09, 0.08, 0.06, 0.04, 0.12]  # sum = 1.0
```

## How to Modify Demographics

**Age groups** — Change `age_groups` list and corresponding probabilities in `p` parameter:

```python
age_groups = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']  # add 65+
# Update probabilities, must sum to 1.0:
np.random.choice(age_groups, n_users, p=[0.08, 0.22, 0.28, 0.17, 0.10, 0.08, 0.07])
```

Note: Heatmap dimensions auto-adjust via `pivot_table`; no axis code changes needed.

**Gender/Region** — Same pattern. Update the list and probability vector.

## How to Add a New Chart

1. Add a new subplot index: update `plt.subplots(2, 2)` to `(2, 3)` or `(3, 2)` etc.
2. Compute the data (e.g., new pivot table or aggregation).
3. Plot on the new axis. Example — add posts-per-week by age:

```python
# Add after line 95 in social_media_analysis.py:
age_posts = df.groupby('age_group')['posts_per_week'].mean()
axes[1, 2].bar(age_posts.index, age_posts.values, color='#3498db')
axes[1, 2].set_title('Avg Posts per Week by Age')
axes[1, 2].tick_params(axis='x', rotation=45)
```

4. In `generate_interactive.py`, update `specs` array and add corresponding Plotly trace.

## How to Regenerate Data with Different Seed

Change `np.random.seed(42)` in both scripts. Different seeds produce different distributions while maintaining the same statistical shape.

## Synchronization Rules

- `social_media_analysis.py` and `generate_interactive.py` must share the same seed, platform list, age groups, and probability vectors to produce consistent outputs
- If you add columns to the main script's DataFrame, add matching columns to `generate_interactive.py` if they appear in the interactive chart
- Update `docs/CONFIGURATION.md` when changing default parameters
