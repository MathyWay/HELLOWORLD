import sqlite3
from settings import CREATE_TABLE_SQL, INSERT_USER_SQL

BASE_NAME = 'users1.db'


class UserCl:
    def __init__(self, ids, name, age):
        self.id = ids
        self.Name = name
        self.Age = age

    def __repr__(self):
        return "(%i;%s;%i)" % (self.id, self.Name, self.Age)

    def __str__(self):
        return "id:%i, Name %s, Age %i " % (self.id, self.Name, self.Age)


def adapt_user(user):
    return ("%i;%s;%i" % (user.id, user.Name, user.Age)).encode('ascii')


def convert_user(s):
    ids, name, age = list(s.split(b";"))
    ids = int(ids.decode("utf-8"))
    name = name.decode("utf-8")
    age = int(age.decode("utf-8"))
    return UserCl(ids, name, age)


class DataBase:

    def __init__(self, name):
        self.name = name

    def init_data_base(self):

        # Checking for DataBase
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)

    def init_user(self, name, age):

        # Checking for DataBase
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)
        # Initial Complete"""
        ####################################################
        cur = con.cursor()
        cur.execute(INSERT_USER_SQL, (name, age))
        con.commit()
        return UserCl(cur.lastrowid, name, age)

    @staticmethod
    def take_users(type_of_take='ALL', names=''):

        con = sqlite3.connect(BASE_NAME)
        with con:
            con.execute(CREATE_TABLE_SQL)
        """ Initial Complete"""
        ####################################################

        cur = con.cursor()
        if type_of_take == 'ONE':
            cur.execute('SELECT rowid, name, age from users where name = (?)', (list(names.split(';'))[0],))
            ret = cur.fetchall()
            cur.close()
            con.close()
            return ret
        elif type_of_take == 'MANY':
            print(list(names.split(';')))
            i = '(?'
            a = 1
            while a < len((list(names.split(';')))):
                i += ',?'
                a += 1
            i += ')'
            cur.execute('SELECT rowid, name, age from users where name in {}'.format(i), list(names.split(';')))
            ret = cur.fetchall()
            cur.close()
            con.close()
            return ret
        elif type_of_take == 'ALL':
            cur.execute('SELECT rowid, name, age from users')
            ret = cur.fetchall()
            cur.close()
            con.close()
            print(ret)
            return ret
        else:
            cur.close()
            con.close()
            print('Warning')
            return 0
