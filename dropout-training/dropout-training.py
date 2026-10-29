import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    x_arr = np.array(x)
    if rng is None:
        rands = np.random.random(x_arr.shape)
    else:
        rands = rng.random(x_arr.shape)

    mask = rands > p

    pattern = np.where(mask, 1/(1-p), 0)

    
    
    return (x_arr * pattern), pattern
    pass