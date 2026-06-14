<!-- GSD -->
# Configuration: Social Media Usage Analysis

All configuration is inline in `social_media_analysis.py` and `generate_interactive.py`. No external config files.

## Primary Parameters (social_media_analysis.py)

### User Count

```
File: social_media_analysis.py, line 12
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `n_users` | `500` | Number of synthetic user profiles to generate |

### Platform Configuration

```
File: social_media_analysis.py, lines 14, 24-25
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `platforms` | `['Instagram', 'YouTube', 'WhatsApp', 'Facebook', 'Twitter/X', 'LinkedIn', 'Snapchat']` | 7 social media platforms |
| Platform weights | `[0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05]` | Primary platform selection probabilities (must sum to 1.0) |

### Demographic Parameters

```
File: social_media_analysis.py, lines 15-17, 21-23
```

| Parameter | Default Probabilities | Values |
|-----------|----------------------|--------|
| `age_groups` | `[0.10, 0.25, 0.30, 0.18, 0.10, 0.07]` | 13-17, 18-24, 25-34, 35-44, 45-54, 55+ |
| `genders` | `[0.48, 0.48, 0.04]` | Male, Female, Other |
| `regions` | `[0.45, 0.35, 0.20]` | Urban, Suburban, Rural |

### Behavioral Parameters

```
File: social_media_analysis.py, lines 26-30
```

| Parameter | Distribution | Parameters | Clipping |
|-----------|-------------|------------|----------|
| `daily_usage_mins` | `np.random.gamma(2.5, 30, n_users)` | shape=2.5, scale=30 | clip(5, 480) |
| `posts_per_week` | `np.random.poisson(3, n_users)` | lambda=3 | clip(0, 50) |
| `accounts_followed` | `np.random.lognormal(4.5, 1.2, n_users)` | mean=4.5, sigma=1.2 | clip(1, 5000) |
| `engagement_rate_pct` | `np.random.beta(2, 8, n_users) * 100` | alpha=2, beta=8 | implicit [0, 100] |
| `years_active` | `np.random.randint(1, 15, n_users)` | low=1, high=15 | — |

### Derived Metric (Usage Category)

```
File: social_media_analysis.py, lines 36-38
```

| Parameter | Value |
|-----------|-------|
| `pd.cut bins` | `[0, 30, 60, 120, 300, 500]` |
| Labels | `Low (<30m)`, `Moderate (30-60m)`, `High (1-2h)`, `Very High (2-5h)`, `Extreme (5h+)` |

### Visualization Parameters

```
File: social_media_analysis.py, lines 59-98
```

| Parameter | Value | Description |
|-----------|-------|-------------|
| `figsize` | `(14, 10)` | Figure dimensions in inches |
| `colors` | `plt.cm.Set2(np.linspace(0, 1, 7))` | 7-color qualitative palette |
| `dpi` | `150` | PNG resolution |
| Bbox inches | `tight` | Crop whitespace around figure |

### CSV Export

```
File: social_media_analysis.py, lines 121-122
```

| File | Contents |
|------|----------|
| `social_media_data.csv` | Full DataFrame `df` (500 rows x 10 columns + derived) |
| `platform_analysis.csv` | Aggregated `platform_stats` (7 rows x 5 columns) |

## Interactive Parameters (generate_interactive.py)

| Parameter | Location | Default |
|-----------|----------|---------|
| `n` | Line 9 | `500` |
| `platforms` | Line 10 | Same 7 as main script |
| `age_groups` | Line 11 | Same 6 as main script |
| `colors` | Line 12 | `px.colors.qualitative.Set2[:7]` |
| Platform weights | Line 17 | `[0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05]` |
| Age weights | Line 16 | `[0.1, 0.25, 0.3, 0.18, 0.1, 0.07]` |
| Usage distribution | Line 18 | `gamma(2.5, 30).clip(5, 480)` |
| Engagement distribution | Line 19 | `beta(2, 8).round(3) * 100` |
| Posts distribution | Line 20 | `poisson(3).clip(0, 50)` |
| Figure height | Line 51 | `700` |
| Title | Line 51 | `'Social Media Usage Analysis - Interactive'` |

## Random Seed

Both scripts use `np.random.seed(42)` (line 11 in main, line 8 in interactive) for deterministic, reproducible output. Change the seed value to generate different synthetic datasets while maintaining the same statistical distributions.

## Shared Constraints

Both scripts must use identical values for these to stay synchronized:
- `np.random.seed` value
- Platform names and weights
- Age group names and weights
- Distribution parameters (gamma, beta, poisson)
