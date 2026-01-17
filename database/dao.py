from database.DB_connect import DBConnect
from model.sightings import Sighting
from model.states import State


class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_sightings():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM sighting """

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT YEAR(s_datetime) as year FROM sighting ORDER BY year """

        cursor.execute(query)

        anni = [row["year"] for row in cursor]

        cursor.close()
        conn.close()
        return anni
    @staticmethod
    def read_shapes(year:int):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT shape FROM sighting
                where YEAR(s_datetime) = %s"""

        cursor.execute(query, (year,))

        forma=[row["shape"] for row in cursor]

        cursor.close()
        conn.close()
        return forma

    @staticmethod
    def read_stati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM state """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_neighbors():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM neighbor """

        cursor.execute(query)

        pairs=set()
        for row in cursor:
            a= row["state1"].strip().upper()
            b= row["state2"].strip().upper()
            pairs.add(tuple(sorted((a, b))))

        cursor.close()
        conn.close()
        return list(pairs)

    @staticmethod
    def conta_avvistamenti_per_stato(year: int, shape: str) ->dict[str, int]:
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT upper(trim(s.state)) as st, Count(id) as num_avvistamenti FROM sighting s
        WHERE YEAR(s_datetime) = %s
        and shape = %s 
        group by st"""

        cursor.execute(query, (year, shape,))

        count={row["st"]: row["num_avvistamenti"]for row in cursor}

        cursor.close()
        conn.close()
        return count