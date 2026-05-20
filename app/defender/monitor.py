import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from defender.detector import ThreatDetector
from defender.recovery import Recovery

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SANDBOX_DIR = os.path.join(BASE_DIR, "sandbox")


class MonitorHandler(FileSystemEventHandler):

    def __init__(self, dashboard):
        super().__init__()

        self.dashboard = dashboard
        self.detector = ThreatDetector()
        self.recovery = Recovery(log_callback=dashboard.add_log)

    def on_modified(self, event):

        if not event.is_directory:
            self.dashboard.add_log(f"Modified: {event.src_path}")
            self.detector.add_event("modify")
            self.dashboard.update_score(self.detector.score)
            self.check_threat()

    def on_moved(self, event):

        if not event.is_directory:
            self.dashboard.add_log(f"Renamed: {event.dest_path}")
            self.detector.add_event("rename")
            self.dashboard.update_score(self.detector.score)
            self.check_threat()

    def on_created(self, event):

        if not event.is_directory:

            self.dashboard.add_log(f"Created: {event.src_path}")

            if "RANSOM_NOTE" in event.src_path:
                self.detector.add_event("ransom_note")

            self.dashboard.update_score(self.detector.score)
            self.check_threat()

    def check_threat(self):

        if self.detector.is_threat():
            self.dashboard.show_alert()
            self.recovery.restore()
            self.detector.reset()


class DefenderMonitor:

    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.observer = Observer()

    def start(self):

        event_handler = MonitorHandler(self.dashboard)

        self.observer.schedule(
            event_handler,
            SANDBOX_DIR,
            recursive=True
        )

        self.observer.start()

        self.dashboard.add_log("Defender monitoring started")

    def stop(self):
        self.observer.stop()
        self.observer.join()