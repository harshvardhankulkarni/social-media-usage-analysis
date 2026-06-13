# Social Media Usage Analysis - Demo Project

Analyzes platform engagement, daily usage patterns, and demographic trends across 7 major social media platforms. Uses synthetic data that mirrors real-world social media trends.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Data aggregation and pivot tables
- NumPy 1.24+ - Statistical distributions
- Matplotlib 3.7+ - Multi-panel visualizations
- Seaborn 0.12+ - Statistical plots (optional)

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/social-media-usage-analysis.git
cd social-media-usage-analysis
pip install pandas numpy matplotlib
```

### Running

```bash
python social_media_analysis.py
```

Expected output:

```
--- SOCIAL MEDIA USAGE ANALYSIS (DEMO) ---
Total users analyzed: 500
Platform Market Share:
  Instagram: 29.8% (149 users, 78 mins/day)
  YouTube: 25.0% (125 users, 68 mins/day)
  ...
Exported: social_media_data.csv, platform_analysis.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| social_media_analysis.png | 4-panel visualization chart |
| social_media_data.csv | Full dataset (500 user profiles) |
| platform_analysis.csv | Platform-level aggregated statistics |

## How It Works

### Dataset

500 synthetic user profiles with these attributes:

| Attribute | Values | Distribution |
|-----------|--------|-------------|
| age_group | 13-17, 18-24, 25-34, 35-44, 45-54, 55+ | Weighted toward 18-34 |
| gender | Male, Female, Other | 48/48/4 |
| region | Urban, Suburban, Rural | 45/35/20 |
| primary_platform | Instagram, YouTube, WhatsApp, Facebook, Twitter/X, LinkedIn, Snapchat | Weighted by real market share |
| daily_usage_mins | 5 to 480 minutes | Gamma distribution (mean ~73 min) |
| engagement_rate_pct | 0-15% | Beta distribution |
| years_active | 1-14 years | Uniform |

### Analysis Performed

1. Platform market share distribution.
2. Average daily usage by platform.
3. Age group vs platform heatmap.
4. Engagement rate by platform.
5. Usage category segmentation (Low to Extreme).

## Project Structure

```
social-media-usage-analysis/
  social_media_analysis.py   Main analysis script
  README.md                  This file
  docs/
    architecture.md           Design and methodology
    runbook.md                Operations guide
```

## Configuration

Modify these parameters at the top of the script:

- `n_users` - Sample size (default: 500).
- Platform weights in `np.random.choice(platforms, p=[...])`.
- Age group weights for different demographic distributions.

## License

MIT
