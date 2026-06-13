# Architecture: Social Media Usage Analysis

## Context

Social media platforms compete for user attention. Understanding usage patterns across platforms, age groups, and regions helps businesses choose where to invest their marketing budget.

## Goals

- Determine platform market share distribution.
- Identify usage patterns by demographic group.
- Compare engagement rates across platforms.
- Produce a visual report combining multiple analyses.

## Design

### Data Flow

```
Synthetic User Generator
  - 500 profiles with realistic distributions
  - 7 platforms with weighted market share
  - Demographic attributes (age, gender, region)
  - Behavioral attributes (usage, posts, engagement)
        |
        v
Raw DataFrame (500 rows x 10 columns)
        |
        +---> Platform aggregation (market share, avg usage)
        +---> Age-platform pivot table
        +---> Region-platform usage matrix
        +---> Engagement rate ranking
        |
        v
Visualization (2x2 grid) + CSV Exports
```

### Statistical Distributions Used

```python
# Daily usage (gamma distribution - matches real usage patterns)
daily_usage_mins = np.random.gamma(2.5, 30, n_users)

# Posts per week (Poisson distribution)
posts_per_week = np.random.poisson(3, n_users)

# Engagement rate (beta distribution - bounded between 0-100%)
engagement_rate_pct = np.random.beta(2, 8, n_users)

# Accounts followed (log-normal distribution)
accounts_followed = np.random.lognormal(4.5, 1.2, n_users)
```

### Visualization Layout

```
Panel 1: Pie chart - Platform market share
Panel 2: Bar chart - Daily usage by platform
Panel 3: Heatmap - Age group vs platform
Panel 4: Horizontal bar - Engagement rate by platform
```

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Gamma distribution for usage | Real usage data is right-skewed. Gamma models this well. |
| 7 platforms only | Covers 95%+ of social media activity. Excludes niche platforms. |
| Primary platform only | Simplifies analysis. Users typically have one main platform. |
| Synthetic data | No API keys needed. No rate limits. Fully reproducible. |

## Trade-offs

- **Primary platform vs multi-platform**: Users typically use 3-4 platforms. The analysis simplifies to primary platform only. A multi-platform analysis would need more complex data generation.
- **Self-reported vs measured data**: Synthetic data assumes users can identify their primary platform. Real behavioral data (from platform APIs) would be more accurate but harder to obtain.
- **Static snapshot**: The analysis is a single time point. Real usage patterns shift over time (seasonal, trend-driven).

## Integration Points

- **Input**: Self-generates data. Replace with survey CSV or API data.
- **Output**: `platform_analysis.csv` can feed into marketing strategy docs or BI dashboards.
- **Extending**: Add platform switching analysis, time-of-day patterns, or content type preferences.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib
