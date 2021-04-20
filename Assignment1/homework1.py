import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.patches import Rectangle

data = pd.read_csv('sunshine.csv')
data['season'] = 'Season'
data['nb_day'] = 31
data.loc[data['month'].isin(['Apr', 'Jun', 'Sep', 'Nov']), 'nb_day'] = 30
data.loc[data['month'].isin(['Feb']), 'nb_day'] = (7 * 29 + 23 * 28) / 30
data['ratio'] = data['sunshine'] / (24 * data['nb_day'])
data.loc[data['month'].isin(['Dec', 'Jan', 'Feb']), 'season'] = 'Winter'
data.loc[data['month'].isin(['Mar', 'Apr', 'May']), 'season'] = 'Spring'
data.loc[data['month'].isin(['Jun', 'Jul', 'Aug']), 'season'] = 'Summer'
data.loc[data['month'].isin(['Sep', 'Oct', 'Nov']), 'season'] = 'Autumn'
table = data.groupby(['city', 'season']).mean().reset_index()

cities = data.city.unique()
seasons = data.season.unique()

plt.figure(1, figsize=(24, 16))

for i, city in enumerate(cities):
    for j, season in enumerate(seasons):
        ratio = table.loc[(table['city'] == city) & (table['season'] == season)].reset_index()['ratio'].loc[0]
        plt.subplot2grid((len(cities) + 1, len(seasons) + 1), (i, j + 1))
        plt.pie([ratio, 1 - ratio], colors=['gold', 'slategrey'])

for i, city in enumerate(cities):
    plt.subplot2grid((len(cities) + 1, len(seasons) + 1), (i, 0))
    plt.text(0, 0, city, fontsize=32)
    plt.axis('off')
    plt.xlim((0, 1))
    plt.ylim((-0.5, 0.5))

for j, season in enumerate(seasons):
    plt.subplot2grid((len(cities) + 1, len(seasons) + 1), (len(cities), j + 1))
    plt.text(0, 0, season, fontsize=32, ha='center')
    plt.axis('off')
    plt.xlim((-0.5, 0.5))
    plt.ylim((0, 1))

ax = plt.subplot2grid((len(cities) + 1, len(seasons) + 1), (len(cities), 0))
ax.add_patch(Rectangle((0, 0.1), 0.3, 0.2, facecolor = 'slategrey', fill=True))
ax.add_patch(Rectangle((0, 0.8), 0.3, 0.2, facecolor = 'gold', fill=True))
plt.text(0.4, 0.8, 'Sunshine', fontsize=24)
plt.text(0.4, 0.3, 'Nighttime /', fontsize=24)
plt.text(0.4, 0, 'Cloudy sky', fontsize=24)
plt.axis('off')
plt.xlim((0, 1))
plt.ylim((0, 1))

plt.suptitle('Where and when to enjoy sunshine?', fontsize=40)
plt.savefig('ducela_a1.png', format='png')