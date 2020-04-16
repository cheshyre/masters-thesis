import json
import os

import matplotlib.pyplot as plt
import matplotlib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = [r"\usepackage{lmodern}"]
plt.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]
plt.rcParams["font.family"] = ["Latin Modern Roman"]

with open("data/pairing_ham_data.json") as f:
    data = json.load(f)

plot_configs = {
    "exact": {"label": "Exact", "line_style": "^-",},
    "imsrg2": {"label": "IM-SRG(2)", "line_style": "o-",},
    "imsrg3": {"label": "IM-SRG(3)", "line_style": "s-",},
}

fig, ax = plt.subplots()

for key in plot_configs:
    print(key)
    label = plot_configs[key]["label"]
    line_style = plot_configs[key]["line_style"]
    g = data[key]["g"]
    E = data[key]["E"]
    E_corr = [E[i] - (2 - g[i]) for i in range(len(E))]

    ax.plot(g, E_corr, line_style, label=label)

ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")

plt.legend()
plt.xlabel(r"$g$ (MeV)")
plt.ylabel(r"$E_{\text{corr}}$ (MeV)")

plt.gcf().set_size_inches(5, 3.75)
plt.savefig("pairing_ham_imsrg3.pdf", dpi=300)

plt.close(fig=fig)
