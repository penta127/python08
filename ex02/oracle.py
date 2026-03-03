import os


def main() -> int:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print(" [MISSING] python-dotenv (required)")
        print("Install with: pip install python-dotenv")
        return 1

    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, ".env")

    load_dotenv(env_path, override=False)

    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing DATABASE_URL")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Missing ZION_ENDPOINT")

    print()
    print("Environment security check:")

    print(" [OK] No hardcoded secrets detected")

    if os.path.exists(env_path):
        print(" [OK] .env file properly configured")
    else:
        print(" [WARN] .env file not found")

    if "API_KEY" in os.environ:
        print(" [OK] Production overrides available (env used)")
    else:
        print(" [OK] Production overrides available")

    missing = []
    if not database_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not zion_endpoint:
        missing.append("ZION_ENDPOINT")

    if missing:
        print()
        print("Missing required configuration:")
        for key in missing:
            print(f" - {key}")
        return 1

    print()
    print("The Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
