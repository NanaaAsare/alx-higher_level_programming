#!/usr/bin/python3
'''
select_states module

This script lists all states from the database hbtn_0e_0_usa
where name matches argument.
The script takes in 4 arguments: mysql_username, mysql_password,
mysql_database_name and state_name_searched.
'''

import MySQLdb
import sys

if __name__ == '__main__':
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                         passwd=sys.argv[2], db=sys.argv[3])
            cursor = db.cursor()
                cursor.execute('SELECT * FROM `states` WHERE name = "{name}"\
                                    ORDER BY `id` ASC'.format(name=sys.argv[4]))
                    [print(state) for state in cursor.fetchall()]
