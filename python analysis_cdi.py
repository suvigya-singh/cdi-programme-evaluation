import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ── LOAD DATA ──────────────────────────────────────────
df = pd.read_csv('data.csv')

print("=" * 55)
print(" CDI PROGRAMME EVALUATION — PYTHON ANALYSIS")
print("=" * 55)

# ── DESCRIPTIVE STATISTICS ─────────────────────────────
print("\n📊 DESCRIPTIVE STATISTICS BY GROUP")
print("-" * 40)
group_stats = df.groupby('group')[
    ['pre_score', 'post_score',
     'parent_confidence_pre',
     'parent_confidence_post']
].mean().round(2)
print(group_stats)

# ── IMPROVEMENT SCORES ─────────────────────────────────
df['score_improvement'] = df['post_score'] - df['pre_score']
df['confidence_improvement'] = (df['parent_confidence_post']
                                - df['parent_confidence_pre'])

print("\n📈 AVERAGE IMPROVEMENT BY GROUP")
print("-" * 40)
print(df.groupby('group')[
    ['score_improvement', 'confidence_improvement']
].mean().round(2))

# ── WILCOXON TEST ──────────────────────────────────────
print("\n🔬 WILCOXON SIGNED-RANK TEST (Treatment group)")
print("-" * 40)
treatment = df[df['group'] == 'Treatment']
control   = df[df['group'] == 'Control']

stat, p = stats.wilcoxon(
    treatment['pre_score'],
    treatment['post_score']
)
print(f"Statistic : {stat}")
print(f"P-value   : {p:.4f}")
print(f"Result    : {'✅ Significant (p < 0.05)' if p < 0.05 else '❌ Not significant'}")

# ── MANN-WHITNEY U TEST ────────────────────────────────
print("\n🔬 MANN-WHITNEY U TEST (Treatment vs Control)")
print("-" * 40)
stat, p = stats.mannwhitneyu(
    treatment['post_score'],
    control['post_score'],
    alternative='two-sided'
)
print(f"Statistic : {stat}")
print(f"P-value   : {p:.4f}")
print(f"Result    : {'✅ Significant (p < 0.05)' if p < 0.05 else '❌ Not significant'}")

# ── COMPLETION RATE ────────────────────────────────────
completion_rate = (df['programme_completed'] == 'Yes').mean() * 100
print(f"\n✅ Programme completion rate: {completion_rate:.0f}%")

# ── RESULTS BY AREA ────────────────────────────────────
print("\n📍 IMPROVEMENT BY GEOGRAPHIC AREA")
print("-" * 40)
area_stats = df.groupby('school_area')['score_improvement'].mean().round(2)
print(area_stats.sort_values(ascending=False))

# ── ATTENDANCE CORRELATION ─────────────────────────────
print("\n📅 SESSIONS ATTENDED vs SCORE IMPROVEMENT")
print("-" * 40)
correlation, p_value = stats.spearmanr(
    treatment['sessions_attended'],
    treatment['score_improvement']
)
print(f"Spearman correlation : {correlation:.3f}")
print(f"P-value              : {p_value:.4f}")
print(f"Result: {'✅ Significant relationship' if p_value < 0.05 else '❌ No significant relationship'}")

# ── GENDER BREAKDOWN ───────────────────────────────────
print("\n👥 IMPROVEMENT BY GENDER (Treatment group)")
print("-" * 40)
gender_stats = treatment.groupby('gender')[
    'score_improvement'
].mean().round(2)
print(gender_stats)

# ── VISUALISATIONS ─────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CDI Programme Evaluation Results',
             fontsize=15, fontweight='bold')

# Chart 1 — Pre vs Post scores by group
group_means = df.groupby('group')[
    ['pre_score', 'post_score']
].mean()
group_means.plot(kind='bar', ax=axes[0, 0],
                 color=['#4C72B0', '#55A868'],
                 edgecolor='white', width=0.6)
axes[0, 0].set_title('Avg Pre vs Post Scores by Group')
axes[0, 0].set_xlabel('')
axes[0, 0].set_ylabel('Score')
axes[0, 0].set_xticklabels(['Control', 'Treatment'], rotation=0)
axes[0, 0].legend(['Pre-Score', 'Post-Score'])

# Chart 2 — Parental confidence
conf_means = df.groupby('group')[
    ['parent_confidence_pre', 'parent_confidence_post']
].mean()
conf_means.plot(kind='bar', ax=axes[0, 1],
                color=['#C44E52', '#8172B2'],
                edgecolor='white', width=0.6)
axes[0, 1].set_title('Parental Confidence Pre vs Post')
axes[0, 1].set_xlabel('')
axes[0, 1].set_ylabel('Confidence (1-5)')
axes[0, 1].set_xticklabels(['Control', 'Treatment'], rotation=0)
axes[0, 1].legend(['Pre', 'Post'])

# Chart 3 — Improvement by area
area_means = df.groupby('school_area')['score_improvement'].mean()
area_means.sort_values().plot(kind='barh', ax=axes[1, 0],
                               color='#4C72B0', edgecolor='white')
axes[1, 0].set_title('Score Improvement by Geographic Area')
axes[1, 0].set_xlabel('Avg Improvement (points)')

# Chart 4 — Sessions attended vs improvement (scatter)
axes[1, 1].scatter(
    treatment['sessions_attended'],
    treatment['score_improvement'],
    color='#55A868', edgecolor='white', s=80
)
axes[1, 1].set_title('Sessions Attended vs Score Improvement')
axes[1, 1].set_xlabel('Sessions Attended')
axes[1, 1].set_ylabel('Score Improvement')

plt.tight_layout()
plt.savefig('results.png', dpi=150)
plt.show()

# ── FINAL SUMMARY ──────────────────────────────────────
print("\n" + "=" * 55)
print(" EVALUATION SUMMARY")
print("=" * 55)
print(f"Total participants        : {len(df)}")
print(f"Treatment group           : {len(treatment)}")
print(f"Control group             : {len(control)}")
print(f"Treatment avg improvement : +{treatment['score_improvement'].mean():.1f} points")
print(f"Control avg improvement   : +{control['score_improvement'].mean():.1f} points")
print(f"Completion rate           : {completion_rate:.0f}%")
print(f"Post confidence (treatment): {treatment['parent_confidence_post'].mean():.1f}/5")
print("=" * 55)