import sqlite3

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
        # Register the adapter
        sqlite3.register_adapter(UserCl, adapt_user)

        # Register the converter
        sqlite3.register_converter("user", convert_user)

        # Checking for DataBase
        con = sqlite3.connect(self.name, detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (p user)""")
        cur.close()
        con.close()

    def init_user(self, user):
        # Register the adapter
        sqlite3.register_adapter(UserCl, adapt_user)

        # Register the converter
        sqlite3.register_converter("user", convert_user)

        # Checking for DataBase
        con = sqlite3.connect(self.name, detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()
        """ Initial Complete"""
        ####################################################

        cur.execute('INSERT INTO users (p) values (?)', (user,))
        con.commit()
        cur.close()
        con.close()

    def take_users(self, type_of_take='ALL', names=''):
        # Register the adapter
        sqlite3.register_adapter(UserCl, adapt_user)

        # Register the converter
        sqlite3.register_converter("user", convert_user)

        con = sqlite3.connect(BASE_NAME, detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()
        cur.execute('SELECT * FROM users')
        user_base = [i[0] for i in cur.fetchall()]
        if type_of_take == 'ONE':
            for i in user_base:
                if i.Name == names:
                    cur.close()
                    con.close()
                    return i
            else:
                cur.close()
                con.close()
                return 0
        elif type_of_take == 'MANY':
            print('Buy')
        elif type_of_take == 'ALL':
            cur.close()
            con.close()
            return user_base
        else:
            print('Warning')
            return 0
