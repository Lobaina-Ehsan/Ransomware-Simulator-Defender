class ThreatDetector:

    def __init__(self):
        self.score = 0

    def add_event(self, event_type):

        if event_type == "modify":
            self.score += 1

        elif event_type == "rename":
            self.score += 2

        elif event_type == "ransom_note":
            self.score += 5

    def is_threat(self):
        return self.score >= 8

    def reset(self):
        self.score = 0