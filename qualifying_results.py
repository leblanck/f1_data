import fastf1 as f1
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from timple.timedelta import strftimedelta
from fastf1 import plotting
from fastf1.core import Laps

f1.Cache.enable_cache('cache')
matplotlib.rcParams['font.family'] = ['Berkeley Mono', 'monospace']
plt.style.use('Solarize_Light2')


f1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme=None, misc_mpl_mods=False)
session = f1.get_session(2024, 3, 'Q')
session.load()

#Getting Driver abbreviations
drivers = pd.unique(session.laps['Driver'])

list_fastest_laps = list()
for drv in drivers:
    drvs_fastest_lap = session.laps.pick_driver(drv).pick_fastest()
    list_fastest_laps.append(drvs_fastest_lap)

fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)

#Getting fastest overall lap
pole_lap = fastest_laps.pick_fastest()

#Setting Lap Delta
fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']

#Getting team colors
team_colors = list()
for index, lap in fastest_laps.iterlaps():
    color = f1.plotting.team_color(lap['Team'])
    team_colors.append(color)

fig, ax = plt.subplots()
ax.barh(fastest_laps.index, fastest_laps['LapTimeDelta'], color=team_colors, edgecolor='grey')
ax.set_yticks(fastest_laps.index)
ax.set_yticklabels(fastest_laps['Driver'])

# show fastest at the top
ax.invert_yaxis()

# draw vertical lines behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(True, which='major', linestyle='--', color='black', zorder=-1000)

#convert pole lap time to string for title
lap_time_string = strftimedelta(pole_lap['LapTime'], '%m:%s.%ms')

#create chart title
plt.suptitle(f"{session.event['EventName']} {session.event.year} Qualifying\n"
             f"Fastest Lap: {lap_time_string} ({pole_lap['Driver']})")

#show chart
plt.show()