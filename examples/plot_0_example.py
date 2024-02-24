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

cpos = [(0.07817110755919496, 0.13558926405422117, 0.5210700195677971),
 (-0.01684039831161499, 0.11015420686453581, -0.0015369504690170288),
 (-0.26589633341798463, 0.9640005779198042, 0.0014232516134205578)]

bunny.plot(cpos=cpos)


# %% [markdown]
# Animation
# ---------
#

# %%

colors = ["red", "green", "blue"]

plotter = pv.Plotter()
plotter.open_gif("file.gif", fps=1)
for i in range(len(colors)):
    plotter.clear_actors()
    plotter.add_mesh(
        bunny,
        color=colors[i]
    )
    plotter.camera_position = cpos
    plotter.write_frame()

plotter.show()

