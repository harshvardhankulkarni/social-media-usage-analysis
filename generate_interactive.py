
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

np.random.seed(42)
n = 500
platforms = ['Instagram', 'YouTube', 'WhatsApp', 'Facebook', 'Twitter/X', 'LinkedIn', 'Snapchat']
age_groups = ['13-17', '18-24', '25-34', '35-44', '45-54', '55+']
colors = px.colors.qualitative.Set2[:7]

df = pd.DataFrame({
    'user_id': [f'U{i:04d}' for i in range(1, n+1)],
    'age_group': np.random.choice(age_groups, n, p=[0.1, 0.25, 0.3, 0.18, 0.1, 0.07]),
    'primary_platform': np.random.choice(platforms, n, p=[0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05]),
    'daily_usage_mins': np.random.gamma(2.5, 30, n).clip(5, 480).round(1),
    'engagement_rate_pct': np.random.beta(2, 8, n).round(3) * 100,
    'posts_per_week': np.random.poisson(3, n).clip(0, 50),
})

fig = make_subplots(rows=2, cols=2,
    subplot_titles=('Platform Distribution', 'Daily Usage by Platform',
                    'Engagement Rate by Platform', 'Usage vs Engagement'),
    specs=[[{'type': 'pie'}, {'type': 'bar'}],
           [{'type': 'bar'}, {'type': 'scatter'}]])

plat_counts = df['primary_platform'].value_counts()
fig.add_trace(go.Pie(labels=plat_counts.index, values=plat_counts.values,
                     marker=dict(colors=px.colors.qualitative.Set2), textinfo='label+percent'), row=1, col=1)

plat_usage = df.groupby('primary_platform')['daily_usage_mins'].mean().sort_values(ascending=False)
fig.add_trace(go.Bar(x=plat_usage.index, y=plat_usage.values,
                     marker_color=px.colors.qualitative.Set2[:7],
                     text=[f'{v:.0f}m' for v in plat_usage.values],
                     textposition='outside', showlegend=False), row=1, col=2)

plat_eng = df.groupby('primary_platform')['engagement_rate_pct'].mean().sort_values(ascending=False)
fig.add_trace(go.Bar(x=plat_eng.index, y=plat_eng.values,
                     marker_color=px.colors.qualitative.Set2[:7],
                     text=[f'{v:.1f}%' for v in plat_eng.values],
                     textposition='outside', showlegend=False), row=2, col=1)

fig.add_trace(go.Scatter(x=df['daily_usage_mins'], y=df['engagement_rate_pct'],
                         mode='markers', marker=dict(color='#3498db', size=4, opacity=0.4),
                         text=[f'{p}: {a}yr' for p, a in zip(df['primary_platform'], df['posts_per_week'])],
                         hovertemplate='Usage: %{x:.0f}m<br>Engagement: %{y:.2f}%<br>%{text}<extra></extra>',
                         showlegend=False), row=2, col=2)

fig.update_layout(height=700, title_text='Social Media Usage Analysis - Interactive')
fig.write_html('social_media_interactive.html')
print('Saved: social_media_interactive.html')
