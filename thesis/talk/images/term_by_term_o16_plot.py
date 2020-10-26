import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import ImageGrid

import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def spread_points(x, y, spread=0.25, num_pts=100):
    step_size = 2 * spread / num_pts
    new_x = []
    new_y = []

    for i, x_val in enumerate(x):
        for n in range(num_pts):
            new_x.append(x_val - spread + step_size / 2 + n * step_size)
            new_y.append(y[i])

    return new_x, new_y


basis = "truncated NAT"
basis_disp = "NAT"

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = r"\usepackage{siunitx}\sisetup{detect-all}\usepackage{amsmath}\usepackage{sansmath}\sansmath"
plt.rcParams["font.size"] = 14

fig_height = 4.5
fig_width = 5

labels_dict = {
    "-1": "IMSRG(2)",
    "1": "IMSRG(3)-A",
    "4": "IMSRG(3)-B",
    "5": "IMSRG(3)-C",
    "6": "IMSRG(3)-D",
}

with open("data/o16/costs.json") as f:
    data = json.load(f)

fig, ax = plt.subplots()

ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
ax.tick_params(bottom=True, top=True, left=True, right=True, which="both")
ax.tick_params(axis="x", which="both", direction="in")
ax.tick_params(axis="y", which="both", direction="in")
ax.tick_params(which='major', length=5)
ax.tick_params(which='minor', length=3)

costs = []
labels = []
energies = []
for i, key in enumerate(labels_dict):
    costs.append(i + 0.5)
    labels.append(labels_dict[key])
    energies.append(data["NN-only"][basis]["20"][key])

new_costs, new_energies = spread_points(costs, energies)

ax.plot(new_costs, new_energies, linestyle="-.", color="gray", zorder=0)

ax.scatter(new_costs, new_energies, s=1.2, marker="s", zorder=10)

ax.set_ylim((-161.07, -160.93))
ax.set_yticks([-161.06 + 0.02 * s for s in range(100) if -161.06 + 0.02 * s < -160.93])
# plt.xlim((14, 30))

ax.set_xticks(costs)
ax.set_xticklabels(labels, rotation=90)

ax.text(
    0.4,
    0.29,
    r"${}^{16}\text{O}$, " + basis_disp,
    transform=ax.transAxes,
)
ax.text(
    0.4,
    0.22,
    r"$\hbar \Omega = 20$ MeV",
    transform=ax.transAxes,
)
ax.text(
    0.4,
    0.15,
    r"EM 1.8",
    transform=ax.transAxes,
)
ax.text(
    0.4,
    0.08,
    r"$e_{\text{max}} = 2$",
    transform=ax.transAxes,
)
ax.text(
    0.4,
    0.9,
    r"$E_{\text{corr,IMSRG(2)}} = 9.566$ MeV",
    transform=ax.transAxes,
)

plt.xlabel("Truncation scheme")
plt.ylabel("$E$ (MeV)")

plt.gcf().subplots_adjust(left=0.20)
plt.gcf().subplots_adjust(right=0.95)
plt.gcf().subplots_adjust(top=0.95)
plt.gcf().subplots_adjust(bottom=0.30)

plt.gcf().set_size_inches(fig_width, fig_height)
path = "term_by_term_o16_plot.pdf"
plt.savefig(path, dpi=300, transparent=True)
plt.close(fig)
