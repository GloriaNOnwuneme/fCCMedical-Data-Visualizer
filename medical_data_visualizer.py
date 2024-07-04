import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['weight']/((df['height']/100)**2) > 25
df.loc[:,'overweight'] = np.array([1 if n else 0 for n in df['overweight']])

# 3
df.loc[:,'cholesterol'] = np.array([0 if n<=1 else 1 for n in df['cholesterol']])
df.loc[:,'gluc'] = np.array([0 if n<=1 else 1 for n in df['gluc']])


# 4
def draw_cat_plot():
    # 5
    df_cat = df[['cholesterol','gluc','smoke','alco','active','cardio']]


    # 6
    
    df_long = df_cat.melt(id_vars='cardio')
    
    # 7
    #fCC instructions - Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #However, catplot has a 'col' parameter which I've used instead


    # 8
    fig = sns.catplot(data=df_long, x='variable', row=None, col='cardio', hue='value', kind='count', color=None, palette=None, legend='auto', legend_out=True,)


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
        & (df['height'] >= df['height'].quantile(0.025)) 
        & (df['height'] <= df['height'].quantile(0.975)) 
        & (df['weight'] >= df['weight'].quantile(0.025)) 
        & (df['weight'] <= df['weight'].quantile(0.975)) ]


    # 12
    corr = df.corr().loc['age':, :'cardio']

    #Changed from corr = df.loc[:, 'age':].corr().loc['sex':, :'cardio'] to pass freeCodeCamp requirements
    #filtered to exclude like-like correlations (and their associated axis ticks)

    # 13
    mask = np.reshape([False if j<=i else True for i in range(len(corr)) for j in range(len(corr))], (len(corr), len(corr)) )

    # 14
    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(corr, cmap='Blues', mask=mask, annot=True, fmt=".1f")

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
