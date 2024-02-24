"""
Example gallery
===============

This examples demonstrates how to show static/interactive and animated pyvista scenes
"""


# %% [markdown]
# Load data and plot
# ------------------
#

# %%
import pyvista as pv
from pyvista import examples

bunny = examples.download_bunny()
bunny.plot()


# %% [markdown]
# Animation
# ---------
#

# %%
target_reductions = [0, 0.5, 0.9, 0.95]
bunnies = [bunny.decimate(tr) for tr in target_reductions]

plotter = pv.Plotter()
plotter.open_gif("file.gif", fps=3)
for i in range(len(bunnies)):
    plotter.clear_actors()
    plotter.add_mesh(
        bunnies
    )
    plotter.write_frame()

plotter.show()

