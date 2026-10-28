import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    pr = np.array(param)
    gr = np.array(grad)
    mt = np.array(m)
    vt = np.array(v)

    mt_new = beta1 * mt + (1-beta1) * gr
    vt_new = beta2 * vt + (1-beta2) * np.power(gr, 2)

    mt_corr = mt_new/(1-np.power(beta1, t))
    vt_corr = vt_new/(1-np.power(beta2, t))

    pr_new = pr - lr * (mt_corr/(np.sqrt(vt_corr) + eps))

    return pr_new, mt_new, vt_new
    pass