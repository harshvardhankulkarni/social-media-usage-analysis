# Social Media Usage Analysis - Demo Project

Analyzes platform engagement, daily usage patterns, and demographic trends across 7 major social media platforms.

This is a demo project using synthetic data that mirrors real-world social media trends.

## Dataset

500 synthetic user profiles with the following attributes:

- Age group, gender, region
- Primary platform (Instagram, YouTube, WhatsApp, Facebook, Twitter/X, LinkedIn, Snapchat)
- Daily usage in minutes
- Posts per week
- Accounts followed
- Engagement rate percentage
- Years active on social media

## Analysis

1. **Platform Market Share**: Instagram leads at 30%. YouTube at 25%. Snapchat at 5%.
2. **Daily Usage by Platform**: YouTube users spend the most time per session.
3. **Age Group vs Platform**: Youngest users cluster on Instagram and Snapchat. LinkedIn skews older.
4. **Engagement Rate by Platform**: Smaller platforms like LinkedIn and Twitter/X have higher engagement rates despite lower user counts.

## How to Run

```bash
pip install pandas matplotlib numpy
python social_media_analysis.py
```

Output: `social_media_analysis.png` (4-panel chart) and `social_media_data.csv` (full dataset).

## Tech Stack

Python, Pandas, NumPy, Matplotlib

## License

MIT
