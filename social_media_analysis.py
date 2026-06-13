"""
Social Media Usage Analysis - Demo Project
Analyzes platform engagement, daily usage, and demographic patterns.
Uses synthetic data mirroring real-world social media trends.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n_users = 500

platforms = ['Instagram', 'YouTube', 'WhatsApp', 'Facebook', 'Twitter/X', 'LinkedIn', 'Snapchat']
age_groups = ['13-17', '18-24', '25-34', '35-44', '45-54', '55+']
genders = ['Male', 'Female', 'Other']
regions = ['Urban', 'Suburban', 'Rural']

data = {
    'user_id': [f'U{i:04d}' for i in range(1, n_users + 1)],
    'age_group': np.random.choice(age_groups, n_users, p=[0.1, 0.25, 0.3, 0.18, 0.1, 0.07]),
    'gender': np.random.choice(genders, n_users, p=[0.48, 0.48, 0.04]),
    'region': np.random.choice(regions, n_users, p=[0.45, 0.35, 0.2]),
    'primary_platform': np.random.choice(platforms, n_users,
        p=[0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05]),
    'daily_usage_mins': np.random.gamma(2.5, 30, n_users).clip(5, 480).round(1),
    'posts_per_week': np.random.poisson(3, n_users).clip(0, 50),
    'accounts_followed': np.random.lognormal(4.5, 1.2, n_users).round(0).clip(1, 5000),
    'engagement_rate_pct': np.random.beta(2, 8, n_users).round(3) * 100,
    'years_active': np.random.randint(1, 15, n_users),
}

df = pd.DataFrame(data)

# Derived metrics
df['daily_category'] = pd.cut(df['daily_usage_mins'],
    bins=[0, 30, 60, 120, 300, 500],
    labels=['Low (<30m)', 'Moderate (30-60m)', 'High (1-2h)', 'Very High (2-5h)', 'Extreme (5h+)'])

# Analysis 1: Platform popularity
platform_stats = df.groupby('primary_platform').agg(
    user_count=('user_id', 'count'),
    avg_usage=('daily_usage_mins', 'mean'),
    avg_posts=('posts_per_week', 'mean'),
    avg_engagement=('engagement_rate_pct', 'mean')
).sort_values('user_count', ascending=False)

platform_stats['pct_users'] = (platform_stats['user_count'] / n_users * 100).round(1)

# Analysis 2: Age group by platform
age_platform = df.pivot_table(index='age_group', columns='primary_platform',
    aggfunc='size', fill_value=0)

# Analysis 3: Usage by region and platform
region_platform = df.pivot_table(index='region', columns='primary_platform',
    values='daily_usage_mins', aggfunc='mean').round(1)

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
colors = plt.cm.Set2(np.linspace(0, 1, 7))

# Plot 1: Platform market share
axes[0, 0].pie(platform_stats['user_count'], labels=platform_stats.index,
    autopct='%1.0f%%', colors=colors, startangle=90)
axes[0, 0].set_title('Primary Platform Distribution')

# Plot 2: Daily usage by platform
usage_order = platform_stats.sort_values('avg_usage', ascending=False)
bars = axes[0, 1].bar(usage_order.index, usage_order['avg_usage'], color=colors)
axes[0, 1].set_title('Average Daily Usage by Platform (mins)')
axes[0, 1].set_ylabel('Minutes per day')
for bar, val in zip(bars, usage_order['avg_usage']):
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
        f'{val:.0f}m', ha='center', fontsize=9)

# Plot 3: Age group platform heatmap
im = axes[1, 0].imshow(age_platform.values, cmap='YlOrRd', aspect='auto')
axes[1, 0].set_xticks(range(len(age_platform.columns)))
axes[1, 0].set_xticklabels(age_platform.columns, rotation=45, ha='right')
axes[1, 0].set_yticks(range(len(age_platform.index)))
axes[1, 0].set_yticklabels(age_platform.index)
axes[1, 0].set_title('Age Group vs Platform')
for i in range(len(age_platform.index)):
    for j in range(len(age_platform.columns)):
        axes[1, 0].text(j, i, int(age_platform.values[i, j]),
            ha='center', va='center', fontsize=8,
            color='white' if age_platform.values[i, j] > age_platform.values.max()/2 else 'black')

# Plot 4: Engagement rate by platform
eng_order = platform_stats.sort_values('avg_engagement', ascending=False)
axes[1, 1].barh(eng_order.index, eng_order['avg_engagement'], color=colors)
axes[1, 1].set_title('Average Engagement Rate by Platform (%)')
axes[1, 1].set_xlabel('Engagement Rate (%)')
for i, val in enumerate(eng_order['avg_engagement']):
    axes[1, 1].text(val + 0.1, i, f'{val:.1f}%', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('social_media_analysis.png', dpi=150, bbox_inches='tight')
print('Saved: social_media_analysis.png')

# Print insights
print('\n--- SOCIAL MEDIA USAGE ANALYSIS (DEMO) ---')
print(f'Total users analyzed: {len(df)}')
print(f'\nPlatform Market Share:')
for _, row in platform_stats.iterrows():
    print(f'  {_}: {row["pct_users"]}% ({row["user_count"]} users, {row["avg_usage"]:.0f} mins/day)')

top_platform = platform_stats.index[0]
top_age = age_platform.sum(axis=1).idxmax()
print(f'\nMost used platform: {top_platform}')
print(f'Most active age group: {top_age}')
print(f'Average daily usage across all users: {df["daily_usage_mins"].mean():.0f} mins')
print(f'Average posts per week: {df["posts_per_week"].mean():.1f}')

print('\nKey Insights:')
print(f'  1. {top_platform} dominates primary platform preference.')
print(f'  2. {age_platform.sum(axis=1).idxmax()} age group is most active on social media.')
print(f'  3. Users with highest engagement spend {df.groupby("daily_category")["engagement_rate_pct"].mean().max():.1f}% more time on platforms.')

export_paths = [platform_stats, age_platform, region_platform]
df.to_csv('social_media_data.csv', index=False)
platform_stats.to_csv('platform_analysis.csv')
print('\nExported: social_media_data.csv, platform_analysis.csv')
print('Done.')
