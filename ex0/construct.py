import sys
import site

if (sys.base_prefix == sys.prefix):
    print("MATRIX STATUS: You're still plugged in\n")
    print("Current Python:", sys.executable)
    print("Virtual environment: None detected\n")
    print("WARNING: Your're in the global environment!\n" +
          "The machines can see everything you install\n")
    print("To enter the construct, run: python -m venv matrix_env source " +
          "matrix_env/bin/activate # On Unix\nmatrix_env\\Scripts\\" +
          "activate # On Windows \nThen run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct")
    print("\nCurrent Python: ", sys.executable)
    print("Virtual Environment:", str(sys.prefix).split("/")[-1])
    print("Environment Path:", str(sys.prefix))
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print(site.getsitepackages()[0])
