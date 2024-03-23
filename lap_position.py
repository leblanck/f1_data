import fastf1 as f1
import matplotlib
import matplotlib.pyplot as plt
import fastf1.plotting

f1.Cache.enable_cache('cache')
matplotlib.rcParams['font.family'] = ['Berkeley Mono', 'monospace']
plt.style.use('Solarize_Light2')

session = f1.get_session(2024, 2, 'R')
session.load(telemetry=False, weather=False)

fig, ax = plt.subplots(figsize=(8.0, 5.0))


for driver in session.drivers:
    driver_laps = session.laps.pick_driver(driver)
    abbreviation = driver_laps['Driver'].iloc[0]
    color = fastf1.plotting.driver_color(abbreviation)
    ax.plot(driver_laps['LapNumber'], driver_laps['Position'], label=abbreviation, color=color)

ax.set_ylim([20.5, 0.5])
ax.set_yticks([1, 5, 15, 20])
ax.set_xlabel('Lap')
ax.set_ylabel('Posiiton')
ax.legend(bbox_to_anchor=(1.0, 1.02))
plt.suptitle(f"{session.event['EventName']} {session.event.year}\n"
             f"Lap Position Changes")
plt.tight_layout()
plt.show()