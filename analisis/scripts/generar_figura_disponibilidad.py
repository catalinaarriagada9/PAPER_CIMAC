from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

rows = [
    r"TR$_{total}$",
    r"TR$_{packaging}$",
    r"IC$_{REP,est}$",
    "eC",
    "IRP",
    "MCI",
    "Minimum national MFA",
]
cols = [
    "Availability",
    "Public access",
    "Temporal\ncontinuity",
    "Granularity",
    "Boundary\ncompatibility",
    "Destination\ntraceability",
    "Definitions and\nmetadata",
    "Interoperability",
    "Quality and\nuncertainty",
    "Direct\ncomputability",
]

# 2 = Available, 1 = Partial, 0 = Insufficient.
matrix = np.array([
    [2, 2, 2, 2, 2, 1, 2, 2, 1, 2],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 2, 0, 1, 1],
    [1, 2, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
])

colors = ["#B64B3C", "#D9A928", "#287271"]
cmap = ListedColormap(colors)

fig, ax = plt.subplots(figsize=(13.2, 6.2))
ax.imshow(matrix, cmap=cmap, vmin=-0.5, vmax=2.5, aspect="auto")
ax.set_xticks(np.arange(len(cols)), labels=cols)
ax.set_yticks(np.arange(len(rows)), labels=rows)
ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False, length=0)
plt.setp(ax.get_xticklabels(), rotation=32, ha="left", rotation_mode="anchor", fontsize=9)
plt.setp(ax.get_yticklabels(), fontsize=10)

labels = {0: "I", 1: "P", 2: "A"}
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(j, i, labels[matrix[i, j]], ha="center", va="center",
                color="white" if matrix[i, j] != 1 else "#202020",
                fontsize=10, fontweight="bold")

ax.set_xticks(np.arange(-0.5, len(cols), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=1.4)
ax.tick_params(which="minor", bottom=False, left=False)
for spine in ax.spines.values():
    spine.set_visible(False)

legend = [
    Patch(facecolor=colors[2], label="Available (A)"),
    Patch(facecolor=colors[1], label="Partial (P)"),
    Patch(facecolor=colors[0], label="Insufficient (I)"),
]
ax.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.5, -0.13),
          ncol=3, frameon=False, fontsize=10)
fig.text(0.5, 0.015,
         "Categories are diagnostic and are not aggregated into a composite readiness score.",
         ha="center", va="bottom", fontsize=9, color="#404040")

fig.subplots_adjust(left=0.20, right=0.985, top=0.71, bottom=0.20)
out = Path(__file__).resolve().parents[2] / "figuras"
out.mkdir(exist_ok=True)
fig.savefig(out / "matriz_disponibilidad.pdf", bbox_inches="tight")
fig.savefig(out / "matriz_disponibilidad.png", dpi=300, bbox_inches="tight")
plt.close(fig)
