import unittest
import os
import json

class TestMitigationStrategies(unittest.TestCase):

    def setUp(self):
        # Set up a sample appsettings.json for testing
        self.test_file = "test_appsettings.json"
        sample_data = {
            "Kestrel": {
                "Endpoints": {
                    "Https": {
                        "Url": "http://*:5006",
                        "Certificate": {
                            "Path": "/https/aspnetapp.pfx",
                            "Password": "HardCodedPassword"
                        }
                    }
                }
            }
        }
        with open(self.test_file, "w") as file:
            json.dump(sample_data, file)

        os.environ["CERT_PASSWORD"] = "SecurePassword"

    def tearDown(self):
        # Clean up test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_update_appsettings(self):
        # Call the automation function
        from secure_config_deployment import update_appsettings
        update_appsettings(self.test_file, "CERT_PASSWORD")

        # Validate the update
        with open(self.test_file, "r") as file:
            data = json.load(file)
        self.assertEqual(data["Kestrel"]["Endpoints"]["Https"]["Certificate"]["Password"], "$CERT_PASSWORD")

    def test_enforce_https(self):
        # Call the automation function
        from secure_config_deployment import enforce_https
        enforce_https(self.test_file)

        # Validate the HTTPS enforcement
        with open(self.test_file, "r") as file:
            data = json.load(file)
        self.assertTrue(data["Kestrel"]["Endpoints"]["Https"]["Url"].startswith("https"))

if __name__ == "__main__":
    unittest.main()
