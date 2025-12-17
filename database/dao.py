from database.DB_connect import DBConnect
from model.dto.gene import Gene
from model.dto.interazione import Interazione


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
    def read_all_cromosomi():
        try:
            conn = DBConnect.get_connection()
        except Exception as e:
            print(e)

        result = []

        cursor = conn.cursor()
        query = """SELECT distinct cromosoma FROM gene g WHERE g.cromosoma!=0"""

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])
            print(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_geni():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """
                select g.id as id, g.funzione as funzione, g.essenziale as essenziale, g.cromosoma as cromosoma
                from gene g
                """

        cursor.execute(query)

        for row in cursor:
            oggetto_gene = Gene(**row)
            result[row['id']] = row['cromosoma']
            print(oggetto_gene)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_interazioni():
        conn = DBConnect.get_connection()

        result = set()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM interazione i """

        cursor.execute(query)

        for row in cursor:
            oggetto_interazione = Interazione(**row)
            result.add(oggetto_interazione)
            print(oggetto_interazione)

        cursor.close()
        conn.close()
        return result