import numpy as np
import matplotlib.pyplot as plt

def feigenbaum_diagram(r_min=2.5, r_max=4.0, n=1000, iterations=1000, last=100, zoom=False):
    """
    Generate and plot the Feigenbaum diagram for the logistic map.
    
    Parameters:
        r_min: Minimum r value (bifurcation parameter).
        r_max: Maximum r value.
        n: Number of r values to sample.
        iterations: Total iterations for each r.
        last: Number of points to display after transients.
        zoom: If True, display a zoomed-in version of the diagram.
    """
    # Generate r values
    r = np.linspace(r_min, r_max, n)
    x = 1e-5 * np.ones(n)  # Initial condition (small positive value)

    # Prepare results for the last iterations
    results_r = []
    results_x = []

    # Iterate through logistic map
    for i in range(iterations):
        x = r * x * (1 - x)  # Logistic equation
        if i >= iterations - last:  # Save last iterations
            results_r.extend(r)
            results_x.extend(x)

    # Plot Feigenbaum diagram
    plt.figure(figsize=(12, 6))
    plt.plot(results_r, results_x, ',k', alpha=0.25)  # ',' creates pixel-level points
    plt.xlim(r_min, r_max)
    plt.ylim(0, 1)
    plt.title("Feigenbaum Diagram (Logistic Map)")
    plt.xlabel("r (bifurcation parameter)")
    plt.ylabel("x (population)")

    if zoom:
        plt.title("Zoomed Feigenbaum Diagram")
        plt.xlim(r_min, r_min + (r_max - r_min) / 5)
        plt.ylim(0.3, 0.7)

    plt.show()

# Generate the Feigenbaum diagram
feigenbaum_diagram()
