import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import ImageGrid

import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

basis = "HF"
basis_disp = "HF"

truncation_disp_lookup = {
    "imsrg2": "IMSRG(2)",
    "imsrg3": r"IMSRG(3)-$N^7$",
}

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = r"\usepackage{lmodern}\usepackage{amsmath}"
plt.rcParams["font.family"] = ["Latin Modern Roman"]
plt.rcParams["font.size"] = 12

fig_height = 5
fig_width = 5

# Set up initial figure
fig, axs = plt.subplots(
    2, 2, sharex="col", sharey="row", gridspec_kw={"hspace": 0, "wspace": 0}
)

(ax1, ax2), (ax3, ax4) = axs

for ax in [ax1, ax2, ax3, ax4]:
    ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
    ax.tick_params(bottom=True, top=True, left=True, right=True, which="both")
    ax.tick_params(axis="x", which="both", direction="in")
    ax.tick_params(axis="y", which="both", direction="in")
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', length=3)

# Top left
ham = "NN-only"
for truncation in ["imsrg2", "imsrg3"]:
    with open(f"data/he4/{truncation}/data.json") as f:
        data = json.load(f)
    hws = []
    energies = []
    for key in data[ham][basis]:
        entry = data[ham][basis][key]
        if entry["converged"]:
            hws.append(int(key))
            energies.append(entry["E"])
    ax1.plot(hws, energies, "o-", label=truncation_disp_lookup[truncation])

# Top right
ham = "NN+3N"
for truncation in ["imsrg2", "imsrg3"]:
    with open(f"data/he4/{truncation}/data.json") as f:
        data = json.load(f)
    hws = []
    energies = []
    for key in data[ham][basis]:
        entry = data[ham][basis][key]
        if entry["converged"]:
            hws.append(int(key))
            energies.append(entry["E"])
    ax2.plot(hws, energies, "o-", label=truncation_disp_lookup[truncation])

# Bottom left
ham = "NN-only"
for truncation in ["imsrg2", "imsrg3"]:
    with open(f"data/he4/{truncation}/data.json") as f:
        data = json.load(f)
    hws = []
    radii = []
    for key in data[ham][basis]:
        entry = data[ham][basis][key]
        if entry["converged"]:
            hws.append(int(key))
            radii.append(entry["R"])
    ax3.plot(hws, radii, "o-", label=truncation_disp_lookup[truncation])

# Bottom right
ham = "NN+3N"
for truncation in ["imsrg2", "imsrg3"]:
    with open(f"data/he4/{truncation}/data.json") as f:
        data = json.load(f)
    hws = []
    radii = []
    for key in data[ham][basis]:
        entry = data[ham][basis][key]
        if entry["converged"]:
            hws.append(int(key))
            radii.append(entry["R"])
    ax4.plot(hws, radii, "o-", label=truncation_disp_lookup[truncation])


ax3.set_xlabel(r"$\hbar \Omega$ (MeV)")
ax4.set_xlabel(r"$\hbar \Omega$ (MeV)")
ax3.set_xlim((18, 34))
ax4.set_xlim((18, 34))
ax3.set_xticks([20, 24, 28, 32])
ax4.set_xticks([20, 24, 28, 32])
ax1.set_ylabel(r"$E$ (MeV)")
ax3.set_ylabel(r"$R_{\text{ch}}$ (fm)")
ax1.set_ylim((-29.5, -25.5))
ax1.set_yticks([-29, -28, -27, -26])
ax3.set_ylim((1.75, 2.25))
ax3.set_yticks([1.8, 1.9, 2.0, 2.1, 2.2])
ax1.legend(loc="lower left")

plt.text(
    0.5,
    1.05,
    "EM 1.8",
    ha="center",
    transform=ax1.transAxes,
)
plt.text(
    0.5,
    1.05,
    "EM 1.8/2.0",
    ha="center",
    transform=ax2.transAxes,
)
plt.text(
    0.1,
    0.85,
    r"${}^{4}\text{He}$, " + basis_disp,
    ha="left",
    transform=ax2.transAxes,
)
plt.text(
    0.1,
    0.75,
    r"$e_{\text{max}} = 2$",
    ha="left",
    transform=ax2.transAxes,
)

plt.gcf().subplots_adjust(left=0.15)
plt.gcf().subplots_adjust(right=0.95)
plt.gcf().subplots_adjust(top=0.90)
plt.gcf().subplots_adjust(bottom=0.10)

plt.gcf().set_size_inches(fig_width, fig_height)
path = "he4_HF_results.pdf"
plt.savefig(path, dpi=300)
plt.close(fig)
