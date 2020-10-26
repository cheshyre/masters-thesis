import json
import os

import matplotlib.pyplot as plt
import matplotlib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = [r"\usepackage{lmodern}"]
plt.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]
plt.rcParams["font.family"] = ["Latin Modern Roman"]

with open("data/evolve_data.json") as f:
    data = json.load(f)

plot_configs = {
    "E": {"label": r"$E(s)$", "line_style": ".-", "zorder": 10,},
    "MBPT2": {"label": "MBPT2", "line_style": ".-", "zorder": 5,},
    "MBPT3": {"label": "MBPT3", "line_style": ".-", "zorder": 0,},
}

fig, ax = plt.subplots()

max_s = 0.1

s = data["s"]

i = 0
while s[i] < max_s:
    i += 1

for key in plot_configs:
    print(key)
    label = plot_configs[key]["label"]
    zorder = plot_configs[key]["zorder"]
    line_style = plot_configs[key]["line_style"]
    vals = data[key]

    ax.plot(s[:i], vals[:i], line_style, label=label, zorder=zorder)

ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")

plt.legend()
plt.xlabel(r"$s$ (MeV${}^{-1}$)")
plt.ylabel(r"$E$ (MeV)")

plt.subplots_adjust(left=0.20, right=0.98, top=0.95, bottom=0.15)
plt.gcf().set_size_inches(2.5, 2.5)
plt.savefig("he4_imsrg2_flow.pdf", dpi=300)

plt.close(fig=fig)
