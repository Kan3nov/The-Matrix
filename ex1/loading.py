import importlib.util
import sys

print(importlib.__file__)
print("LOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
error = False

if importlib.util.find_spec("pandas"):
    import pandas as pd  # type: ignore
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
else:
    error = True
    print("[Error] pandas - Data manipulation is not found")

if importlib.util.find_spec("numpy"):
    import numpy as np  # type: ignore
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
else:
    error = True
    print("[Error] numpy - Numerical computation is not found")

if importlib.util.find_spec("matplotlib"):
    import matplotlib as mat  # type: ignore
    print(f"[OK] matplotlib ({mat.__version__}) - Visualization ready")
else:
    print("[Error] matplotlib - Visualization is not found")
    error = True

if (error):
    print("\nSome dependencies are missing - exiting program")
    sys.exit()

print("\nAnalyzing Matrix data...")
print("Processing 100 data points...")
x = np.random.randint(1000, size=(100))
y = np.random.randint(1000, size=(100))
df = pd.DataFrame({'x': x, 'y': y})
print("Generating visualization...")
df.plot(kind="scatter", x="x", y='y')
mat.pyplot.savefig("matrix_analysis.png")

print("\nAnalysis complete!")
print("Results saved to: matrix_analysis.png")
