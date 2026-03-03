import os
import sys
import site


def get_site_packages_path() -> str:
    try:
        site_packages = site.getsitepackages()
        if site_packages:
            return site_packages[0]
        else:
            return "Unavailable (no site-packages path found)"
    except Exception as error:
        return f"Unavailable ({error})"


def main() -> None:
    is_env = sys.prefix != sys.base_prefix

    if is_env:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()

        current_site_packages = get_site_packages_path()
        print("Package installation path:")
        print(current_site_packages)
        print()

        global_site_packages = current_site_packages.replace(
            sys.prefix, sys.base_prefix, 1
        )
        print("Global package path (base Python):")
        print(global_site_packages)

    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()

        current_site_packages = get_site_packages_path()
        print("Global package installation path:")
        print(current_site_packages)
        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate   # On Windows")
        print()

        print("Then run this program again.")


if __name__ == "__main__":
    main()
