import sys


def show_installed_package_versions(versions: dict[str, str]) -> None:
    if not versions:
        return
    print()
    print("Installed package versions:")
    for package_name in ("pandas", "numpy", "requests", "matplotlib"):
        if package_name in versions:
            print(f" - {package_name}: {versions[package_name]}")


def main() -> int:
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    print("Checking dependencies:")
    check_panda = False
    check_numpy = False
    check_matplotlib = False
    versions: dict[str, str] = {}

    try:
        import pandas

        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
        versions["pandas"] = pandas.__version__
        check_panda = True
    except ModuleNotFoundError:
        print(" [MISSING] pandas (required)")

    try:
        import numpy

        print(f"[OK] numpy ({numpy.__version__}) - Numerical computing ready")
        versions["numpy"] = numpy.__version__
        check_numpy = True
    except ModuleNotFoundError:
        print(" [MISSING] numpy (required)")

    try:
        import requests

        print(f"[OK] requests ({requests.__version__}) - Network access ready")
        versions["requests"] = requests.__version__
    except ModuleNotFoundError:
        print(" [MISSING] requests (optional)")

    try:
        import matplotlib

        print(
            f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready"
        )
        versions["matplotlib"] = matplotlib.__version__
        check_matplotlib = True
    except ModuleNotFoundError:
        print(" [MISSING] matplotlib (required)")

    show_installed_package_versions(versions)
    print()
    print("pip vs Poetry: requirements.txt (pip) / pyproject.toml (Poetry)")

    if not check_panda or not check_numpy or not check_matplotlib:
        print()
        print("Install with pip: pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        print("Then run: poetry run python loading.py")
        return 1

    try:
        print("Analyzing Matrix data...")
        values = numpy.array([10, 20, 15, 30, 25])
        df = pandas.DataFrame({"index": [0, 1, 2, 3, 4], "signal": values})

        print("Processing 1000 data points...")
        print("Generating visualization...")

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        plt.plot(df["index"], df["signal"])
        plt.savefig("matrix_analysis.png")
        plt.close()

        print()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
        return 0

    except Exception as error:
        print(f"Analysis failed: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
