import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    arr = np.zeros((seq_len, d_model))
    pos = np.arange(0, seq_len)[:, np.newaxis]
    i = np.arange(0, d_model, 2)
    
    arr[:, 0::2] = np.sin(pos/(np.power(base, (i/d_model))))
    if d_model%2 == 0:
        arr[:, 1::2] = np.cos(pos/(np.power(base, (i/d_model))))
    else:
        arr[:, 1::2] = np.cos(pos/(np.power(base, (i[:-1]/d_model))))
    return arr
    pass