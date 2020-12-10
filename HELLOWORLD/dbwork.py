import sqlite3
from settings import CREATE_TABLE_SQL, INSERT_USER_SQL, DELETE_USER_SQL, CREATE_MESSAGE_TABLE_SQL, SEND_MESSAGE_SQL, \
    SHOW_MESSAGES_SQL, SELECT_USER_SQL, CHECK_USER_SQL, INIT_FRIENDS_TABLE_SQL, ADD_FRIEND_SQL, DELETE_FRIEND_SQL, \
    SELECT_FRIENDS_SQL

BASE_NAME = 'users1.db'


class UserCl:
    def __init__(self, ids, name, password):
        self.id = ids
        self.Name = name
        self.Password = password

    def __repr__(self):
        return "(%i;%s;%i)" % (self.id, self.Name, self.Password)

    def __str__(self):
        return "id:%i, Name %s, Age %i " % (self.id, self.Name, self.Password)


class DataBaseUsers:

    def __init__(self, name):
        self.name = name

    def init_data_base(self):

        # Checking for DataBase
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)

    def init_user(self, name, password):

        # Checking for DataBase
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)
        # Initial Complete"""
        ####################################################
        cur = con.cursor()
        cur.execute(INSERT_USER_SQL, (name, password))
        con.commit()
        return UserCl(cur.lastrowid, name, password)

    @staticmethod
    def take_users(type_of_take='ALL', names=''):

        con = sqlite3.connect(BASE_NAME)
        with con:
            con.execute(CREATE_TABLE_SQL)
        """ Initial Complete"""
        ####################################################

        cur = con.cursor()
        if type_of_take == 'ONE':
            cur.execute('SELECT rowid, name, password from users where name = (?)', (list(names.split(';'))[0],))
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
            cur.execute('SELECT rowid, name, password from users where name in {}'.format(i), list(names.split(';')))
            ret = cur.fetchall()
            cur.close()
            con.close()
            return ret
        elif type_of_take == 'ALL':
            cur.execute('SELECT rowid, name, password from users')
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
        cur.execute('SELECT rowid, name, password from users where name = (?) and rowid = (?)',
                    (list(name.split(';'))[0], ids))
        fetch = cur.fetchone()
        if fetch:
            lastid = fetch[0]
            password = fetch[2]
            cur.execute(DELETE_USER_SQL, (ids, name))
            con.commit()
            cur.close()
            con.close()
            return UserCl(lastid, name, password)
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

    def check_user(self, name, password):
        con = sqlite3.connect(self.name)
        with con:
            con.execute(CREATE_TABLE_SQL)
        cur = con.cursor()
        cur.execute(CHECK_USER_SQL, (name, password))
        user = cur.fetchone()
        if user:
            return UserCl(user[0], user[1], user[2])
        else:
            return False


class DataBaseFriends:
    def __init__(self, basename):
        self.basename = basename

    def init_user(self, idhost):
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(INIT_FRIENDS_TABLE_SQL.format(idhost))

    def add_friend(self, idhost, idfriend):
        self.init_user(idhost)
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(ADD_FRIEND_SQL.format(idhost), (idfriend, DataBaseUsers(BASE_NAME).take_user_name(idfriend)))

    def delete_friend(self, idhost, idfriend):
        self.init_user(idhost)
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(DELETE_FRIEND_SQL.format(idhost), idfriend)

    def show_friends(self, idhost):
        self.init_user(idhost)
        con = sqlite3.connect(self.basename)
        cur = con.cursor()
        cur.execute(SELECT_FRIENDS_SQL.format(idhost))
        ret = cur.fetchall()
        if ret:
            cur.close()
            con.close()
            print(ret)
            return ret
        else:
            return -1


class DataBaseMessages:
    def __init__(self, basename):
        self.basename = basename

    def init_dialog(self, idhost, idfriend):
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(CREATE_MESSAGE_TABLE_SQL.format(idhost))
            con.execute(CREATE_MESSAGE_TABLE_SQL.format(idfriend))

    def send_message(self, idhost, idfriend, message):
        self.init_dialog(idhost, idfriend)
        con = sqlite3.connect(self.basename)
        with con:
            con.execute(SEND_MESSAGE_SQL.format(idhost), (idfriend, 'receive', message))
            con.execute(SEND_MESSAGE_SQL.format(idfriend), (idhost, 'sent', message))

    def show_messages(self, idhost, idfriend):
        self.init_dialog(idhost, idfriend)
        con = sqlite3.connect(self.basename)
        cur = con.cursor()
        cur.execute(SHOW_MESSAGES_SQL.format(idhost), idfriend)
        ret = cur.fetchall()
        cur.close()
        con.close()
        return ret
