import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Write code here
    arr_W = np.array(w)
    arr_g = np.array(g)
    arr_s = np.array(s)

    st = beta * arr_s + (1-beta) * np.power(arr_g, 2)
    wt = arr_W - lr/(np.sqrt(st + eps)) * arr_g

    return wt, st
    pass