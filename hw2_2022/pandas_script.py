import matplotlib.pyplot as plt
import matplotlib.image as image
import seaborn as sns
import pandas as pd
import numpy as np
import os

#       ***First task***
reads_data = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
reads_data.head(10)
fig, axes = plt.subplots(nrows=2, ncols=2)

fig.set_figwidth(10)
fig.set_figheight(6)
fig.set_dpi(100)
fig.suptitle('Letter distribution', fontsize=16)
letters = ['A', 'T', 'G', 'C']
for ax in axes.flat:
    col = letters.pop()
    sns.histplot(reads_data[col], ax=ax, color='#15656B')
    ax.set_title(col)
    ax.set_xlabel('')
    ax.set_ylabel('Number of positions')
# plt.show()

a_s = np.random.uniform(0, 10, size=int(reads_data['A'].sum() / 10))
t_s = np.random.uniform(0, 10, size=int(reads_data['T'].sum() / 10))
g_s = np.random.uniform(0, 10, size=int(reads_data['G'].sum() / 10))
c_s = np.random.uniform(0, 10, size=int(reads_data['C'].sum() / 10))

fig, ax = plt.subplots()
ax.scatter(np.random.uniform(0, 1, len(a_s)), a_s, c='#FD455D', s=4, label='A')
ax.scatter(np.random.uniform(0, 1, len(t_s)) + 1, t_s, c='#6CBC11', s=4, label='T')
ax.scatter(np.random.uniform(0, 1, len(g_s)) + 2, g_s, c='#AD09A3', s=4, label='G')
ax.scatter(np.random.uniform(0, 1, len(c_s)) + 3, c_s, c='#08C2D0', s=4, label='C')

ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Letter count (Scaled)', size=16)
ax.legend(prop={'size': 16}, frameon=False, markerscale=6)

fig.set_figwidth(14)
fig.set_figheight(10)

# plt.show()

#       ***Second task***
mean_mathces = reads_data['matches'].mean()
subset_mathces = reads_data.query('matches > @mean_mathces')[['pos', 'reads_all', 'mismatches', 'deletions',
                                                              'insertions']]
path_to = './'
subset_mathces.to_csv(os.path.join(path_to, 'train_part.csv'), header=True)

#       ***First task***
# (https://www.kaggle.com/parulpandey/forbes-highest-paid-athletes-19902019)

atheletes = pd.read_csv('./Forbes Richest Atheletes (Forbes Richest Athletes 1990-2020).csv', index_col=0)
atheletes.head()
atheletes.index = atheletes.index - 1
atheletes.describe()
atheletes.info()
# print(atheletes.shape)
atheletes.isnull().sum()
atheletes.isnull().sum()

# Rename some columns for convenience
atheletes.rename(columns={'earnings ($ million)': 'earned', 'Current Rank': 'Cur_rank',
                          'Previous Year Rank': 'Prev_year'}, inplace=True)

# Let's find the athlete who earned the most money in a year
# print(atheletes.iloc[atheletes['earned'].idxmax(), :]['Name'])
# Let's find the athlete who earned the least money in a year
# print(atheletes.iloc[atheletes['earned'].idxmin(),:]['Name'] # Surprisingly it is him)

# Let's find the athletes who earned the most money during this period (1990-2020)
top_10_atheletes = atheletes.groupby('Name').agg({'earned': 'sum'}).sort_values(by='earned', ascending=False) \
    .reset_index().head(10)
# print(top_10_atheletes)

# Btw we can visualize these top10 atheletes:
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(8)
fig.set_dpi(80)
sns.set_theme(style="whitegrid")
sns.barplot(y='Name', x='earned', data=top_10_atheletes, color='gold', edgecolor='black')
ax.set_ylabel('')
ax.set_xlabel('Money earned, millions $', size=14, labelpad=20)
ax.set_title('The reachiest athletes from 1990-2020', size=20, pad=20)

# Changes in total earning cash over the years
cash_changes = atheletes.groupby('Year').agg({'earned': 'sum'}).reset_index()
fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(8)
fig.set_dpi(80)

ax.plot(cash_changes['Year'], cash_changes['earned'], ls='-', lw=6, color='red')
ax.set_title('Changes in money earned over years', size=16, pad=10)
ax.set_ylabel('Cash in US$(millions)', size=14, labelpad=10)
ax.set_xlabel('Year', size=14, labelpad=20)

# Let's see the nationality distribution:
atheletes_without_duplicates = atheletes.drop_duplicates(['Name'])
atheletes_without_duplicates['Nationality'].value_counts()  # As expected:)

fig, ax = plt.subplots()
fig.set_figwidth(16)
fig.set_figheight(10)
fig.set_dpi(80)

sns.set_theme(style="white")
sns.countplot(y='Nationality', data=atheletes_without_duplicates, color='gold', alpha=1,
              order=atheletes_without_duplicates['Nationality'].value_counts().index)
ax.set_title('The prevalence Nationality in the Forbes list', size=18, pad=10)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
ax.set_ylabel(ylabel='Nationality', fontsize=16)
ax.set_xlabel('')

# print(atheletes[atheletes['Nationality'] == 'Russia']) # Here is a single Russian athelet in this list

# How Tyson's cash changed over these years
im = image.imread('./tyson.jpeg')
tyson = atheletes[atheletes['Name'] == 'Mike Tyson']
fig, ax = plt.subplots()
ax.grid()
ax.plot('Year', 'earned', data=tyson)
ax.set_title("Mike Tyson earnings in US$(millions)")
fig.figimage(im, -90, -90, cmap='ocean', alpha=.4)
plt.show()


#        **Fourth task**

def read_gff(path, fields=None):
    """Reads .gff file and returns pandas.Dataframe.
    path_to - path to .gff file can be absolute and relative.
    fields - column names, recieves a list(optional)"""
    if fields is None:
        fields = ['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
    gff = pd.read_csv(path, sep='\t', comment='#', names=fields)
    return gff


def read_bed6(path, fields=None):
    """Read .bed file and returns pandas.Dataframe.
    path_to - path to .bed file can be absolute and relative.
    fields - column names, recieves a list(optional)"""
    if fields is None:
        fields = ['chromosome', 'start', 'end', 'name', 'score', 'strand']
    bed = pd.read_csv(path, sep='\t', comment='#', names=fields)
    return bed


gff = read_gff('./rrna_annotation.gff')
bed6 = read_bed6('./alignment.bed')
# print(gff.head(3))
# print(bed6.head(3))

# Extract rRNA type in a 'attribute' column
gff['attributes'] = gff['attributes'].str.extract(r'(\d+S)')

print(gff.head(3))
print(bed6.shape)

rna_table = pd.DataFrame(gff.groupby(['chromosome'])['attributes'].value_counts()). \
    rename(columns={'attributes': 'count'})
rna_table.head(11)
rna_table = rna_table.unstack(level=(0)).T
rna_table = rna_table.droplevel(level=0, axis=0)

ind = [i.replace('Reference_', '') for i in rna_table.index]
fig = plt.figure()

fig.set_figwidth(18)
fig.set_figheight(12)
ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)

ax_1.bar(x=rna_table.index, height=rna_table['5S'], color='green')
ax_1.set_xticklabels(ind)
ax_1.set_title('5S', size=16)

ax_2.bar(x=rna_table.index, height=rna_table['16S'])
ax_2.set_xticklabels(ind)
ax_2.set_title('16S', size=16)

ax_3.bar(x=rna_table.index, height=rna_table['23S'], color='red')
ax_3.set_xticklabels(ind)
ax_3.set_title('23S', size=16)

bed_combined = gff.merge(bed6, how='right', on='chromosome', suffixes=['_x', '_y'])
bed_combined.head()
bed_intersected = bed_combined[(bed_combined['start_x'] - 1 > bed_combined['start_y'])  # If I am right with indexing
                               & (bed_combined['end_x'] - 1 < bed_combined['end_y'])]
print(bed_intersected.head(10))
