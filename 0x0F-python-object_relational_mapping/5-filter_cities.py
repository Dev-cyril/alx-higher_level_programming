#!/usr/bin/python3
"""A module that list all data in `state` table in `hbtn_0e_0_usa` database
    with name starting with 'N'
 """


from sys import argv
import MySQLdb


if __name__ == '__main__':
    dataBaseConnect = MySQLdb.connect(host='localhost',
                                      port=3306, user=argv[1],
                                      passwd=argv[2], db=argv[3],
                                      charset='utf8')
    data = dataBaseConnect.cursor()
    data.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id ASC", (sys.argv[4],))
    rows = data.fetchall()
    print(", ".join(city[0] for city in rows))
    data.close()
    dataBaseConnect.close()
