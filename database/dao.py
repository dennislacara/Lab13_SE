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
                    WHERE g.cromosoma != 0"""
        cursor.execute(query)
        for row in cursor:
            lista_cromosomi.add(row['cromosoma'])
            map_geni[row['id']] = row['cromosoma']

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
        query = """ WITH Tabella AS (
                    SELECT distinct gx.cromosoma as Cromosoma1, gy.cromosoma as Cromosoma2, i.correlazione
                    FROM interazione i, gene gx, gene gy
                    WHERE i.id_gene1 = gx.id and i.id_gene2 = gy.id
                        and gx.cromosoma != 0  and gy.cromosoma != 0
                        and gx.cromosoma != gy.cromosoma 
                    GROUP  BY gx.cromosoma, gy.cromosoma, i.correlazione
                    )
                    SELECT t.Cromosoma1, t.Cromosoma2, sum(t.correlazione ) as peso
                    FROM Tabella t
                    GROUP BY t.Cromosoma1 , t.Cromosoma2 
                """

        cursor.execute(query)
        result = []
        for row in cursor:
            arco = (row['Cromosoma1'], row['Cromosoma2'], float(row['peso']))
            result.append(arco)
        cursor.close()
        conn.close()

        return result
