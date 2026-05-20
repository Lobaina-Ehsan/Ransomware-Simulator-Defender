import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SANDBOX_DIR = os.path.join(BASE_DIR, "sandbox")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")


class Recovery:

    def __init__(self, log_callback=None):
        self.log_callback = log_callback

    def log(self, message):
        print(message)

        if self.log_callback:
            self.log_callback(message)

    def restore(self):

        for filename in os.listdir(SANDBOX_DIR):
            filepath = os.path.join(SANDBOX_DIR, filename)

            if filename.endswith(".demo") or filename == "RANSOM_NOTE.txt":
                os.remove(filepath)
                self.log(f"Removed: {filename}")

        for filename in os.listdir(BACKUP_DIR):
            backup_path = os.path.join(BACKUP_DIR, filename)
            restore_path = os.path.join(SANDBOX_DIR, filename)

            shutil.copy2(backup_path, restore_path)

            self.log(f"Restored: {filename}")

        self.log("Recovery completed")