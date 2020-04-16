import json
import os

import matplotlib.pyplot as plt
import matplotlib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# matplotlib font configurations
matplotlib.rcParams["text.latex.preamble"] = [
    # i need upright \micro symbols, but you need...
    r"\usepackage{siunitx}",
    # ...this to force siunitx to actually use your fonts
    r"\sisetup{detect-all}",
    #  # set the normal font here
    #  r"\usepackage{helvet}",
    #  # load up the sansmath so that math -> helvet
    r"\usepackage{sansmath}",
    #  # <- tricky! -- gotta actually tell tex to use!
    r"\sansmath",
]

# Use tex for matplotlib
plt.rc("text", usetex=True)

with open("data/pairing_ham_data.json") as f:
    data = json.load(f)

plot_configs = {
    #  "exact": {
    #      "label": "Exact",
    #      "line_style": "^-",
    #  },
    "ccsd": {"label": "CCSD", "line_style": "D-",},
    "imsrg2": {"label": "IM-SRG(2)", "line_style": "o-",},
    "imsrg3": {"label": "IM-SRG(3)", "line_style": "s-",},
}

fig, ax = plt.subplots()

E_exact = data["exact"]["E"]
g_exact = data["exact"]["g"]
E_exact_corr = [E_exact[i] - (2 - g_exact[i]) for i in range(len(E_exact))]

for key in plot_configs:
    print(key)
    label = plot_configs[key]["label"]
    line_style = plot_configs[key]["line_style"]
    g = data[key]["g"]
    E = data[key]["E"]
    E_corr = [E[i] - (2 - g[i]) for i in range(len(E))]

    E_corr_rel = [
        E_corr[i] / E_exact_corr[i] if g[i] != 0.0 else 1 for i in range(len(E))
    ]

    ax.plot(g, E_corr_rel, line_style, label=label)

ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")

plt.legend()
plt.xlabel(r"$g$ (MeV)")
plt.ylabel(r"$E_{\text{corr}}/E_{\text{corr,exact}}$ (MeV)")

plt.gcf().set_size_inches(5, 3.75)
plt.savefig("pairing_ham_imsrg3_relative.pdf", dpi=300, transparent=True)

plt.close(fig=fig)
