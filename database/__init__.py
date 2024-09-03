import aiosqlite

class Database:
    def __init__(self, *, connection: aiosqlite.Connection) -> None:
        self.conn = connection

    async def run_query(self, query: str, params: tuple = ()) -> list:
        async with self.conn.execute(query, params) as cursor:
            return await cursor.fetchall()

    async def insert_dummy_data(self):
        dummy_data = [
            (1, 'AA123', 'Flight A', 'American', 'JFK', 'LAX', '2024-09-15', 1200, 300, 'on_time', 50, 200),
            (2, 'BB456', 'Flight B', 'British', 'LHR', 'DXB', '2024-09-16', 1800, 360, 'delayed', 30, 500),
            (3, 'CC789', 'Flight C', 'Canadian', 'YYZ', 'SFO', '2024-09-17', 1500, 240, 'on_time', 75, 350)
        ]

        query = """
        INSERT INTO flights (
            id, flight_number, flight_name, airline, departure_airport, arrival_airport, flight_date, 
            flight_time, flight_duration, flight_status, available_seats, price
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        async with self.conn.cursor() as cursor:
            await cursor.executemany(query, dummy_data)
            await self.conn.commit()
