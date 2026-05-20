import sys
from PyQt5.QtWidgets import QApplication

from ui.dashboard import Dashboard
from database.db import init_db


def main():

    init_db()

    app = QApplication(sys.argv)

    window = Dashboard()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()