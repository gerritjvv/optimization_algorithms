import matplotlib.pyplot as plt
import numpy as np


def plot(fs, lbls=[], x=(-100, 100)):
    if not isinstance(fs, list):
        fs = [fs]

    if not isinstance(lbls, list):
        lbls = [lbls]

    x = np.arange(x[0], x[1])
    for i, f in enumerate(fs):
        if lbls:
            lbl = lbls[i]
        else:
            lbl = f"f_{i}"

        f_v = np.vectorize(f)
        y = f_v(x)
        plt.plot(x, y, label=lbl)

    plt.show()
