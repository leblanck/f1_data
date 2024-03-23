import fastf1 as f1
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from fastf1 import plotting

plotting.setup_mpl()
f1.Cache.enable_cache('cache')
matplotlib.rcParams['font.family'] = ['Berkeley Mono', 'monospace']
plt.style.use('Solarize_Light2')

race = f1.get_session(2021, 'Zandvoort', 'R')
race.load(telemetry=True)