#!/usr/bin/python3
"""A module that list all data in `state` table in `hbtn_0e_0_usa` database with name starting with 'N'"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    dataBaseConnect = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset='utf-8')
    data = dataBaseConnect.cursor()
    data.execute("SELECT * FROM states WHERE name = 'N%' ORDER BY id ASC")
    for eachRow in data:
        print(eachRow)
    data.close()
    dataBaseConnect.close()
