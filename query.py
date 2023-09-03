import sqlite3

QUERY_NUMBER = 2

def execute_query(num: int) -> list:
    num = str(num)
    query = f'query_{num}.sql'
    with open(query, 'r') as f:
        sql = f.read()
        
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == "__main__":
    print(execute_query(QUERY_NUMBER))