import sqlite3
from settings import CREATE_TABLE_SQL, INSERT_USER_SQL, DELETE_USER_SQL, CREATE_MESSAGE_TABLE_SQL, SEND_MESSAGE_SQL, \
    SHOW_MESSAGES_SQL, SELECT_USER_SQL

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


class DataBaseUsers:

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
            return ret
        else:
            cur.close()
            con.close()
            print('Warning')
            return 0

    def del_user(self, ids, name):
        # Checking for DataBase
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)
        # Initial Complete"""
        ####################################################
        cur = con.cursor()
        cur.execute('SELECT rowid, name, age from users where name = (?) and rowid = (?)',
                    (list(name.split(';'))[0], ids))
        fetch = cur.fetchone()
        if fetch:
            lastid = fetch[0]
            age = fetch[2]
            cur.execute(DELETE_USER_SQL, (ids, name))
            con.commit()
            cur.close()
            con.close()
            return UserCl(lastid, name, age)
        else:
            return UserCl(-1, '', 0)

    def take_user_name(self, ids):
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)

        cur = con.cursor()
        cur.execute(SELECT_USER_SQL, ids)
        ret = cur.fetchone()
        if ret:
            ret = ret[0]
        else:
            ret = 0
        cur.close()
        con.close()
        if ret:
            return ret
        else:
            return -1


class DataBaseMessages:
    def __init__(self, basename):
        self.basename = basename

    def init_dialog(self, idhost, idfriend):
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(CREATE_MESSAGE_TABLE_SQL.format(str(idhost)))
            con.execute(CREATE_MESSAGE_TABLE_SQL.format(str(idfriend)))

    def send_message(self, idhost, idfriend, message):
        self.init_dialog(idhost, idfriend)
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(SEND_MESSAGE_SQL.format(str(idhost)), (idfriend, 'receive', message))
            con.execute(SEND_MESSAGE_SQL.format(str(idfriend)), (idhost, 'sent', message))

    def show_messages(self, idhost, idfriend):
        self.init_dialog(idhost, idfriend)
        con = sqlite3.connect(self.basename)
        cur = con.cursor()
        cur.execute(SHOW_MESSAGES_SQL.format(str(idhost), idfriend))
        ret = cur.fetchall()
        cur.close()
        con.close()
        return ret
