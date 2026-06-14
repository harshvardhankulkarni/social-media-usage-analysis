<!-- GSD -->

# Social Media Usage Analysis — Architecture

## Context and Goals

Analyzes platform engagement and demographic patterns across 7 social media platforms using 500 synthetic user profiles. Portfolio demo showcasing multi-dimensional data analysis with categorical and numerical data.

## Data Flow

```
Synthetic Profile Generation (500 users, seed=42)
  → 7 platforms assigned by weighted probabilities
  → Daily usage simulation (gamma/beta distributions)
  → Engagement rate calculation
  → Platform market share analysis
  → Age group vs platform cross-tabulation
  → Usage category segmentation (Low to Extreme)
  → 4-panel static visualization
  → Interactive Plotly HTML chart
  → CSV export (per-user and per-platform)
```

## Components

| File | Role |
|------|------|
| `social_media_analysis.py` | Main analysis: data generation, cross-tabulation, segmentation, static chart, CSV export |
| `generate_interactive.py` | Generates interactive Plotly HTML version |
| `social_media_usage_analysis.ipynb` | Jupyter notebook for exploratory development |
| `social_media_data.csv` | 500 user profiles with usage data |
| `platform_analysis.csv` | Per-platform aggregated statistics |
| `social_media_analysis.png` | Static 4-panel visualization |
| `social_media_interactive.html` | Interactive Plotly chart |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| 500 synthetic users | Statistically meaningful sample size without large data |
| 7 platforms | Covers major social networks for realistic analysis |
| Weighted platform assignment | Mirrors real-world market share distribution (Instagram 30% lead) |
| Heatmap for age-platform | Visual density pattern for demographic segmentation |
| Gamma/distribution-based usage | Simulates realistic heavy-tail usage patterns |

## Trade-offs

- Synthetic data lacks real behavioral complexity
- Platform weights are static approximations
- No time-series dimension (snapshot, not trends)
- Self-reported usage patterns would differ from actual analytics data

## File Organization

```
social-media-usage-analysis/
├── social_media_analysis.py
├── generate_interactive.py
├── social_media_usage_analysis.ipynb
├── social_media_analysis.png
├── social_media_interactive.html
├── social_media_data.csv
├── platform_analysis.csv
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
