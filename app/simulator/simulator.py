import os
import shutil
from simulator.encryptor import toy_encrypt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SANDBOX_DIR = os.path.join(BASE_DIR, "sandbox")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")


class Simulator:

    def __init__(self, log_callback=None):
        self.log_callback = log_callback

    def log(self, message):
        print(message)

        if self.log_callback:
            self.log_callback(message)

    def backup_file(self, filepath):
        filename = os.path.basename(filepath)
        backup_path = os.path.join(BACKUP_DIR, filename)

        shutil.copy2(filepath, backup_path)

        self.log(f"Backup created: {filename}")

    def encrypt_file(self, filepath):
        with open(filepath, "rb") as f:
            data = f.read()

        encrypted = toy_encrypt(data)

        new_path = filepath + ".demo"

        with open(new_path, "wb") as f:
            f.write(encrypted)

        os.remove(filepath)

        self.log(f"Modified: {os.path.basename(new_path)}")

    def create_ransom_note(self):
        note_path = os.path.join(SANDBOX_DIR, "RANSOM_NOTE.txt")

        with open(note_path, "w") as f:
            f.write(
                "SAFE EDUCATIONAL CYBERSECURITY SIMULATION\n"
                "No real damage has occurred.\n"
            )

        self.log("Ransom note created")

    def run(self):
        self.log("Simulation started")

        os.makedirs(BACKUP_DIR, exist_ok=True)

        for filename in os.listdir(SANDBOX_DIR):
            filepath = os.path.join(SANDBOX_DIR, filename)

            if os.path.isfile(filepath) and not filename.endswith(".demo"):
                self.backup_file(filepath)
                self.encrypt_file(filepath)

        self.create_ransom_note()

        self.log("Simulation completed")