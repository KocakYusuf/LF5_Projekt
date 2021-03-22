"""
    Modul zur Auslagerung der Funktionen von "Hardware_Monitoring.py".

    Autor:  Marvin Bänsch, Marc Busse, Philip Decker, Emin Jafarov, Yusuf Kocak
    Datum:  08.03.2021
"""

import mysql.connector

mydb1 = mysql.connector.connect(   
host="localhost",
user="root",
password="",
database="monitoring"
)
mc1 = mydb1.cursor()

def show():
# Maximalauslastung des RAM ausgeben
        sql = "SELECT MAX(RAM) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Maximale RAM Auslastung:", inhalt)

        # Minimalauslastung des RAM ausgeben
        sql = "SELECT MIN(RAM) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Minimale RAM Auslastung:", inhalt)

        # Durchschnittliche RAM Auslastung
        sql = "SELECT AVG(RAM) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Durschnitt RAM Auslastung:", inhalt)

        # Maximalauslastung des CPU ausgeben
        sql = "SELECT MAX(CPU) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Maximale CPU Auslastung:", inhalt)

        # Minimalauslastung des CPU ausgeben
        sql = "SELECT MIN(CPU) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Minimale CPU Auslastung:", inhalt)

        # Durchschnittliche RAM Auslastung
        sql = "SELECT AVG(CPU) FROM `pi1` "
        mc1.execute(sql)
        inhalt = mc1.fetchall()
        print ("Durschnitt CPU Auslastung:", inhalt)
        mc1.close()