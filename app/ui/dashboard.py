from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QMessageBox,
    QHBoxLayout
)

from ui.styles import DARK_STYLE
from ui.widgets import StatusCard

from simulator.simulator import Simulator
from defender.monitor import DefenderMonitor
from defender.recovery import Recovery

from database.db import insert_log


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.monitor = None
        self.alert_count = 0

        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Ransomware Simulator + Defender")
        self.resize(900, 600)

        self.setStyleSheet(DARK_STYLE)

        layout = QVBoxLayout()

        self.status_label = QLabel("Status: SAFE")
        layout.addWidget(self.status_label)

        cards_layout = QHBoxLayout()

        self.score_card = StatusCard("Threat Score", "0")
        self.files_card = StatusCard("Files Monitored", "3")
        self.alert_card = StatusCard("Alerts", "0")

        cards_layout.addWidget(self.score_card)
        cards_layout.addWidget(self.files_card)
        cards_layout.addWidget(self.alert_card)

        layout.addLayout(cards_layout)

        button_layout = QHBoxLayout()

        self.start_defender_btn = QPushButton("Start Defender")
        self.start_sim_btn = QPushButton("Start Simulation")
        self.restore_btn = QPushButton("Restore Files")
        self.clear_logs_btn = QPushButton("Clear Logs")

        button_layout.addWidget(self.start_defender_btn)
        button_layout.addWidget(self.start_sim_btn)
        button_layout.addWidget(self.restore_btn)
        button_layout.addWidget(self.clear_logs_btn)

        layout.addLayout(button_layout)

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)

        layout.addWidget(self.logs)

        self.setLayout(layout)

        self.start_defender_btn.clicked.connect(self.start_defender)
        self.start_sim_btn.clicked.connect(self.start_simulation)
        self.restore_btn.clicked.connect(self.restore_files)
        self.clear_logs_btn.clicked.connect(self.clear_logs)

    def add_log(self, message):

        self.logs.append(message)

        insert_log(message)

    def update_score(self, score):

        self.score_card.update_value(str(score))

        if score >= 8:

            self.status_label.setText("Status: THREAT DETECTED")

            self.alert_count += 1
            self.alert_card.update_value(str(self.alert_count))

        else:
            self.status_label.setText("Status: SAFE")

    def show_alert(self):

        msg = QMessageBox()

        msg.setWindowTitle("Threat Detected")

        msg.setText(
            "Suspicious ransomware-like activity detected"
        )

        msg.exec_()

        self.add_log("Threat detected")

    def start_defender(self):

        if not self.monitor:

            self.monitor = DefenderMonitor(self)

            self.monitor.start()

    def start_simulation(self):

        simulator = Simulator(
            log_callback=self.add_log
        )

        simulator.run()

    def restore_files(self):

        recovery = Recovery(
            log_callback=self.add_log
        )

        recovery.restore()

    def clear_logs(self):

        self.logs.clear()