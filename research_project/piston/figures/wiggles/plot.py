import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from romtime.conventions import FIG_KWARGS

seaborn.set_theme("paper")

smooth = pd.read_csv("probes_FOM_17.csv", index_col=0)["0.0"].squeeze()
wiggled = pd.read_csv("probes_FOM_18.csv", index_col=0)["0.0"].squeeze()

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(smooth.index, smooth.values, label="smooth", alpha=0.5)
ax.plot(wiggled.index, wiggled.values, label="wiggled")

ax.grid(True)
ax.legend()
ax.set_xlabel("$t$ (s)")
ax.set_ylabel("Outflow velocity (m/s)")

plt.savefig("smooth_vs_wiggled.png", **FIG_KWARGS)
