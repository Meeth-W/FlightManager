import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt6.QtCore import Qt

class FlightManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Flight Management System")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        heading = QLabel("Flight Management System", self)
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(heading)

        available_flights_label = QLabel("Available Flights", self)
        available_flights_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        available_flights_label.setStyleSheet("font-size: 18px; margin-top: 20px;")
        main_layout.addWidget(available_flights_label)

        flight_table = QTableWidget(self)
        flight_table.setRowCount(10)  # Set initial row count
        flight_table.setColumnCount(5)  # Set column count
        flight_table.setHorizontalHeaderLabels(["Flight Number", "Destination", "Departure", "Time", "Price"])

        flight_table.horizontalHeader().setStretchLastSection(True)
        flight_table.setStyleSheet("font-size: 14px;")

        main_layout.addWidget(flight_table)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)

        book_now_button = QPushButton("Book Now", self)
        book_now_button.clicked.connect(self.book_now_function)
        book_now_button.setStyleSheet("font-size: 14px; padding: 5px 15px;")
        button_layout.addWidget(book_now_button)

        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

    def book_now_function(self):
        
        pass

def main():
    app = QApplication(sys.argv)
    window = FlightManagementSystem()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
