import json
import os

import matplotlib.pyplot as plt
import matplotlib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = [r"\usepackage{lmodern}"]
plt.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]
plt.rcParams["font.family"] = ["Latin Modern Roman"]

with open("data/kai_results.json") as f:
    data = json.load(f)

plot_configs = {
    "E_bare": {"label": r"$E(s=0)$", "line_style": "^-", "zorder": 10,},
    "E_full": {"label": r"$E(s \rightarrow \infty)$", "line_style": "o-", "zorder": 5,},
}

hbar_omegas = [16, 20, 24, 28, 32]

fig, ax = plt.subplots()

for key in plot_configs:
    print(key)
    label = plot_configs[key]["label"]
    zorder = plot_configs[key]["zorder"]
    line_style = plot_configs[key]["line_style"]
    vals = [data[key][str(hbar_omega)] for hbar_omega in hbar_omegas]

    ax.plot(hbar_omegas, vals, line_style, label=label, zorder=zorder)

ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")
ax.set_xticks(hbar_omegas)

plt.legend()
plt.xlabel(r"$\hbar \Omega$ (MeV)")
plt.ylabel(r"$E$ (MeV)")

plt.subplots_adjust(left=0.20, right=0.98, top=0.95, bottom=0.15)
plt.gcf().set_size_inches(2.5, 2.5)
plt.savefig("he4_imsrg2_energies.pdf", dpi=300)

plt.close(fig=fig)
