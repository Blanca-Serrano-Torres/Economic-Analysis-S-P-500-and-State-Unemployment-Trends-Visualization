# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
import time
import plotly.io as pio




# %%
from fredapi import Fred



# %%
fred_key = 'API_KEY'
fred = Fred(api_key=fred_key)

# %% [markdown]
# Search for economic data

# %%
sp_search = fred.search('S&P', order_by='popularity')

# %%
sp_search.head()

# %% [markdown]
# Pull Raw Data & Plot

# %%
sp500 = fred.get_series(series_id='SP500')
sp500.plot(figsize=(10,5), title='S&P 500', lw=2)
plt.show()

# %% [markdown]
# Pull and Join Multiple Data Series

# %%
unemp_df = fred.search('unemployment rate state', filter=('frequency','Monthly'))
unemp_df = unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
unemp_df = unemp_df.loc[unemp_df['title'].str.contains('Unemployment Rate')]

# %%
all_results = []

for myid in unemp_df.index:
    results = fred.get_series(myid)
    results = results.to_frame(name=myid)
    all_results.append(results)
    time.sleep(0.1) # Don't request to fast and get blocked
uemp_results = pd.concat(all_results, axis=1)

# %%
cols_to_drop = []
for i in uemp_results:
    if len(i) > 4:
        cols_to_drop.append(i)
uemp_results = uemp_results.drop(columns = cols_to_drop, axis=1)

# %%
uemp_states = uemp_results.copy()  #.drop('UNRATE', axis=1)
uemp_states = uemp_states.dropna()
id_to_state = unemp_df['title'].str.replace('Unemployment Rate in ','').to_dict()
uemp_states.columns = [id_to_state[c] for c in uemp_states.columns]

# %% [markdown]
# Pull April 2024 Unemployment Rate Per States

# %%
ax = uemp_states.loc[uemp_states.index == '2024-05-01'].T \
    .sort_values('2024-05-01') \
    .plot(kind='barh', figsize=(8, 12), width=0.7, edgecolor='black',
          title='Unemployment Rate by State, May 2024')
ax.legend().remove()
ax.set_xlabel('% Unemployed')
plt.show()

# %% [markdown]
# Pull Participation Rate

# %%
part_df = fred.search('participation rate state', filter=('frequency','Monthly'))
part_df = part_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')

# %%
part_id_to_state = part_df['title'].str.replace('Labor Force Participation Rate for ','').to_dict()

all_results = []

for myid in part_df.index:
    results = fred.get_series(myid)
    results = results.to_frame(name=myid)
    all_results.append(results)
    time.sleep(0.1) # Don't request to fast and get blocked
part_states = pd.concat(all_results, axis=1)
part_states.columns = [part_id_to_state[c] for c in part_states.columns]

# %%
# Fix DC
uemp_states = uemp_states.rename(columns={'the District of Columbia':'District Of Columbia'})

# %%
fig, axs = plt.subplots(10, 5, figsize=(30, 30), sharex=True)
axs = axs.flatten()

i = 0
for state in uemp_states.columns:
    if state in ["District Of Columbia", "Puerto Rico"]:
        continue
    ax2 = axs[i].twinx()
    uemp_states.query('index >= 2020 and index < 2024')[state] \
        .plot(ax=axs[i], label='Unemployment')
    part_states.query('index >= 2020 and index < 2024')[state] \
        .plot(ax=ax2, label='Participation', color='orange')  # Changed color to avoid seaborn
    ax2.grid(False)
    axs[i].set_title(state)
    i += 1

plt.tight_layout()
plt.show()


# %%
state = 'California'
fig, ax = plt.subplots(figsize=(10, 5), sharex=True)
ax2 = ax.twinx()

# Plotting unemployment data for California
uemp_states2 = uemp_states.asfreq('MS')
l1 = uemp_states2.query('index >= 2020 and index < 2024')[state].plot(ax=ax, label='Unemployment')

# Plotting participation data for California
l2 = part_states.dropna().query('index >= 2020 and index < 2024')[state].plot(ax=ax2, label='Participation', color='orange')

# Customizing the plot
ax2.grid(False)
ax.set_title(state)
fig.legend(labels=['Unemployment', 'Participation'])

plt.show()



