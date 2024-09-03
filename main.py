import sys
import asyncio
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
import aiosqlite
import os
from database import Database

class FlightManagementSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.db = None
        self.setWindowTitle("Flight Management System")
        self.setup_ui()
        asyncio.run(self.init_db())
        asyncio.run(self.load_flight_data())

    def setup_ui(self):
        main_layout = QVBoxLayout()
        heading = QLabel("Flight Management System")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(heading)

        available_flights_label = QLabel("Available Flights")
        available_flights_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        available_flights_label.setStyleSheet("font-size: 18px; margin-top: 20px;")
        main_layout.addWidget(available_flights_label)

        self.flight_table = QTableWidget()
        self.flight_table.setColumnCount(5)
        self.flight_table.setHorizontalHeaderLabels(["Flight Number", "Destination", "Departure", "Time", "Price"])
        self.flight_table.horizontalHeader().setStretchLastSection(True)
        self.flight_table.setStyleSheet("font-size: 14px;")
        main_layout.addWidget(self.flight_table)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        book_now_button = QPushButton("Book Now")
        book_now_button.setStyleSheet("font-size: 14px; padding: 5px 15px;")
        button_layout.addWidget(book_now_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    async def init_db(self):
        try:
            db_path = f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
            self.db = Database(connection=await aiosqlite.connect(db_path))
            async with aiosqlite.connect(db_path) as db:
                with open(f"{os.path.realpath(os.path.dirname(__file__))}/database/schema.sql") as file:
                    await db.executescript(file.read())
                await db.commit()
        except Exception as e:
            print(f"Error initializing database: {e}")

    async def load_flight_data(self):
        try:
            query = """
            SELECT flight_number, arrival_airport, departure_airport, flight_time, price
            FROM flights
            """
            flights = await self.db.run_query(query)
            self.flight_table.setRowCount(len(flights))
            for row_idx, flight in enumerate(flights):
                for col_idx, data in enumerate(flight):
                    self.flight_table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        except Exception as e:
            print(f"Error loading flight data: {e}")

def main():
    app = QApplication(sys.argv)
    window = FlightManagementSystem()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
