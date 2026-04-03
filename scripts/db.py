import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'data_validation',
        user = 'postgres',
        password = 'helloworld'
    )
    return conn


def insert_checks(results):
    conn = get_connection()
    cur = conn.cursor()

    query = """
                INSERT INTO data_quality_check (table_name, check_type, check_result, check_time)
                VALUES(%s,%s,%s,%s)
    """

    for r in results:
        cur.execute(query,(
            r['table_name'],
            r['check_type'],
            r['check_result'],
            r['check_time'],
        ))
    conn.commit()
    cur.close()
    conn.close()

from datetime import datetime

def insert_pipeline_run(status, records, errors):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO data_pipeline_runs (run_time, status, records_processed, errors_detected)
        VALUES (%s, %s, %s, %s)
    """

    cur.execute(query, (
        datetime.now(),
        status,
        records,
        errors
    ))
    
    conn.commit()
    cur.close()
    conn.close()

