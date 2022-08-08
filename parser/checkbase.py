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
cursor.execute("CREATE TABLE comms_commms()")
conn.commit()