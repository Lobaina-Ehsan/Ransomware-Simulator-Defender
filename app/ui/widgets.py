from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatusCard(QFrame):

    def __init__(self, title, value):
        super().__init__()

        self.setStyleSheet("""
            QFrame {
                border: 2px solid #00ff99;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        layout = QVBoxLayout()

        self.title = QLabel(title)
        self.value = QLabel(value)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def update_value(self, new_value):
        self.value.setText(new_value)