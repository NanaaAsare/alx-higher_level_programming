#!/usr/bin/python3
'''
select_states module

This script lists all states from the database hbtn_0e_0_usa
where their name starts with `N`.
The script takes in 3 arguments: mysql_username, mysql_password
and mysql_database_name.
'''

import MySQLdb
import sys

if __name__ == '__main__':
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                         passwd=sys.argv[2], db=sys.argv[3])
            cursor = db.cursor()
                cursor.execute('SELECT * FROM `states` WHERE name\
                                                     LIKE "N%" ORDER BY `id` ASC')
                    [print(state) for state in cursor.fetchall()]
