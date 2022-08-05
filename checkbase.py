# -*- coding: utf-8 -*-
# Для быстрого просмотра таблицы base
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="pharmacy",
    user="kamil",
    password="hduaos82g37x02",
    port=5432) 
cursor = conn.cursor()
cursor.execute("DROP TABLE comms_comms")
conn.commit()