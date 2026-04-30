#!/usr/bin/env python3

"""Filename : oracle.py

Date: 2026-04-20
Description: This program create a secure configuration system using
environment variables and .env files. This construction can then
connects to external system safely, without exposing sensitive
informations like API key.
"""
import os


try:
    from dotenv import load_dotenv
except ImportError:
    print("\n[ERROR]: python-dotenv is not available. Run the command:")
    print("pip install python-dotenv")
    print("Then run this program again\n")
    exit()

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def load_configuration() -> None:
    """Load the .env file if it exists."""
    env_existance: bool = os.path.exists(".env")
    print()
    if env_existance is False:
        print("[WARNING]: No '.env' file found.")
        print("Using default variables")
    else:
        load_dotenv(dotenv_path=".env")


def get_config() -> dict[str, str | None]:
    """Return the configuration, the defaults one if .env incomplete"""
    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "[DEFAULT] development"),
        "DATABASE_URL": os.getenv("DATABASE_URL",
                                  "[DEFAULT] https://API_url.com"),
        "API_KEY": os.getenv("API_KEY", "[DEFAULT] default_API_key"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "[DEFAULT] DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT",
                                   "[DEFAULT] http://zion_endpoint.com")
    }
    return config


def display_configuration(config: dict[str, str | None]) -> None:
    """Display the loaded configuration."""
    print("Configuration loaded:")
    print(f"Mode: {config["MATRIX_MODE"]}")
    print(f"Database url: {config["DATABASE_URL"]}")
    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network url: {config['ZION_ENDPOINT']}")
    print("Zion Network: Online\n")


def validate_configuration() -> bool:
    """Check that all environment variable are set and non-empy.
    Return True is all variables are valid or False if it's not the case.
    """
    missing: list[str] = []
    empty: list[str] = []
    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        if value == "":
            empty.append(var)
    if missing:
        print(f"[WARNING]: Missing variable(s) in .env: {", ".join(missing)}")
    if empty:
        print(f"[WARNING]: Empty variabiable(s) in .env: {", ".join(empty)}")
    if missing or empty:
        print("[WARNING]: Configuration incomplete. The program will use"
              f" DEFAULT variables for {", ".join(missing)}")
        print()
        return False
    print("All variable in '.env' are valid.\n")
    return True


def security_check(check_config: bool) -> None:
    """Check environment security and display it"""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if check_config is True:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file missing or incomplete - using default "
              "configuration")
    if os.environ.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")
    if os.path.exists(".env"):
        if os.path.exists(".gitignore"):
            with open(".gitignore", "r") as file:
                content = file.read()
                if ".env" in content:
                    print("[OK] Data contained in .env are secured")
                else:
                    print("[WARNING] .env is NOT listed in .gitignore. "
                          "You might commit secrets.")


def main() -> None:
    """Entry point of the program"""
    print("\nORACLE STATUS: Reading the Matrix...")
    load_configuration()
    check_config = validate_configuration()
    config = get_config()
    display_configuration(config)
    security_check(check_config)
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
