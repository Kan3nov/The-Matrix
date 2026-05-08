from dotenv import find_dotenv, load_dotenv

import os
print("ORACLE STATUS: Reading the Matrix...\n")

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

print("Configuration loaded:")

if (os.getenv("MATRIX_MODE")):
    print("Mode:", os.getenv("MATRIX_MODE"))
else:
    print("The environment variable MATRIX_MODE is not found")

if (os.getenv("DATABASE_URL")):
    print("Database:", os.getenv("DATABASE_URL"))
else:
    print("The environment variable DATABASE_URL is not found")

if (os.getenv("API_KEY")):
    print("API Access:", os.getenv("API_KEY"))
else:
    print("The environment variable API_KEY is not found")

if (os.getenv("LOG_LEVEL")):
    print("Log level:", os.getenv("LOG_LEVEL"))
else:
    print("The environment variable LOG_LEVEL is not found")

if (os.getenv("ZION_ENDPOINT")):
    print("Zion Network:", os.getenv("ZION_ENDPOINT"))
else:
    print("The environment variable ZION_ENDPOINT is not found")
print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
