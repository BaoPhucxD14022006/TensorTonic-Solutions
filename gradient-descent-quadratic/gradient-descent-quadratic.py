def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    for _ in range(steps):
        f = 2 * x0 * a + b
        x0 = x0 - f * lr
    return x0