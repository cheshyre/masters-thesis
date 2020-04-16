import json
import os

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import ImageGrid
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import scipy.interpolate

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

fig_height = 1.05

# Set maximum momentum to show
kmax = 4.0

# Define new even grid for data
nodes = np.linspace(0.0, kmax, 200)

# Set lambdas to show
lambdas = [5.0, 4.0, 3.0, 2.0, 1.5]

with open("data/EM500new_data.json") as f:
    data = json.load(f)

# Set up initial figure
figure = plt.figure(1, (len(lambdas) * fig_height, fig_height))

# Set up grid in figure
grid = ImageGrid(
    figure,
    111,
    nrows_ncols=(1, len(lambdas)),
    axes_pad=0.0,
    share_all=False,
    label_mode="L",
    #  cbar_location="right",
    #  cbar_mode="single",
)

# Iterate over lambdas
for i, lam in enumerate(lambdas):
    # Get old nodes for data
    data_nodes = np.array(data[str(lam)]["nodes"])

    # Read in potential
    potential = np.array(data[str(lam)]["matrix_elements"]).reshape(
        (len(data_nodes), len(data_nodes))
    )

    # Interpolate potential
    interp = scipy.interpolate.RectBivariateSpline(data_nodes, data_nodes, potential)
    potential = interp(nodes, nodes)

    # Plot potential matrix on corresponding axis in grid
    ax = grid[i]
    im = ax.matshow(
        potential,
        extent=[0.0, kmax, kmax, 0.0],
        vmin=-1 / 2,
        vmax=1 / 2,
        cmap=plt.cm.RdBu_r,
    )

    # Set ticks for axes for this axis
    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])

    # Set xlabel on 3rd grid
    if i == 2:
        ax.set_xlabel(r"$p'$ (fm$^{-1}$)", labelpad=8)
        ax.xaxis.set_label_position("top")

    # Set ylabel on first grid
    if i == 0:
        ax.set_ylabel(r"$p$ (fm$^{-1}$)")

    # Add label for lambda value
    unit = r" fm${}^{-1}$"
    if lam == 50:
        lam = r"\infty"
        unit = ""
    ax.text(0.2, 3.5, "$\\lambda={}${}".format(lam, unit))

    # Move xticks to top
    ax.tick_params(axis="x", which="both", bottom=True, top=True, labelbottom=False)
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(axis="x", direction="in")
    ax.tick_params(axis="y", direction="in")
    # Disable yticks for grids after the left most
    if i != 0:
        ax.tick_params(axis="y", which="both", left=False)

    if i == len(lambdas) - 1:
        axins = inset_axes(
            ax,
            width="10%",
            height="100%",
            loc="lower left",
            bbox_to_anchor=(1.05, 0, 1, 1),
            bbox_transform=ax.transAxes,
            borderpad=0,
        )

# Set colorbar
#  grid.cbar_axes[0].colorbar(im)
cbar = plt.colorbar(im, cax=axins, ticks=[-0.5, 0, 0.5])
cbar.ax.set_yticklabels(["-0.5", "0 (fm)", "0.5"])
# Set colorbar labels
#  for i, cax in enumerate(grid.cbar_axes):
#      cax.set_yticks([-0.5, 0, 0.5])
#      labels = [item.get_text() for item in cax.get_yticklabels()]
#      labels = ["-0.5", "", "0.5"]
#      labels[1] = r"0 (MeV)"
#      cax.set_yticklabels(labels)

# Set xticks to top
plt.tick_params(axis="x", which="both", bottom=True, top=True, labelbottom=False)

# Adjust margins
plt.gcf().subplots_adjust(left=0.08)
plt.gcf().subplots_adjust(right=0.87)
plt.gcf().subplots_adjust(top=0.86)
plt.gcf().subplots_adjust(bottom=-0.08)

# Set size of plot
#  plt.gcf().set_size_inches(4.17 * fig_height,  1.2 * fig_height)
plt.gcf().set_size_inches(6 * fig_height, 1.6 * fig_height)

# Save as PDF
plt.savefig("vnn_srg_emn500_n3lo.pdf", dpi=300, transparent=True)
