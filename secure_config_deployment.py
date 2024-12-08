import os
import json


def update_appsettings(file_path, env_var_name):
    """
    Updates the appsettings.json to replace hardcoded credentials with environment variables.
    """
    try:
        with open(file_path, "r") as file:
            settings = json.load(file)

        # Replace hardcoded password with environment variable
        settings["Kestrel"]["Endpoints"]["Https"]["Certificate"]["Password"] = f"${env_var_name}"

        with open(file_path, "w") as file:
            json.dump(settings, file, indent=4)

        print(f"Updated {file_path} to use environment variable for sensitive data.")
    except Exception as e:
        print(f"Failed to update appsettings.json: {e}")


def enforce_https(file_path):
    """
    Ensures HTTPS is enforced in the appsettings.json.
    """
    try:
        with open(file_path, "r") as file:
            settings = json.load(file)

        # Update endpoints to enforce HTTPS
        settings["Kestrel"]["Endpoints"]["Https"]["Url"] = "https://*:5006"

        with open(file_path, "w") as file:
            json.dump(settings, file, indent=4)

        print(f"HTTPS enforced in {file_path}.")
    except Exception as e:
        print(f"Failed to enforce HTTPS: {e}")


if __name__ == "__main__":
    # Path to appsettings.json
    appsettings_path = "./appsettings.json"

    # Define environment variable for password
    env_var_name = "CERT_PASSWORD"
    os.environ[env_var_name] = "YourSecurePasswordHere"

    # Automate mitigation
    update_appsettings(appsettings_path, env_var_name)
    enforce_https(appsettings_path)
