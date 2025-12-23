from database.DB_connect import DBConnect

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
    def get_all_geni():
        try:
            conn = DBConnect.get_connection()
        except Exception as e:
            print(e)

        lista_cromosomi = set()
        map_geni = {}
        cursor = conn.cursor(dictionary=True)

        query = """ SELECT *
                    FROM gene g 
                    WHERE g.cromosoma > 0"""
        cursor.execute(query)
        for row in cursor:
            lista_cromosomi.add(row['cromosoma'])
            map_geni[row['id']] = row['cromosoma']
        print(lista_cromosomi)
        print(map_geni)

        cursor.close()
        conn.close()
        return lista_cromosomi, map_geni

    @staticmethod
    def get_all_interazioni():
        try:
            conn = DBConnect.get_connection()
        except Exception as e:
            print(e)

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
        FROM interazioni """
        cursor.execute(query)
