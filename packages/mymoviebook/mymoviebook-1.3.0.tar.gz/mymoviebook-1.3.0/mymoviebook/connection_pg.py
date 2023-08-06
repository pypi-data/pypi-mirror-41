## @brief Package to manage postgresql connection functionss
## THIS IS FROM XULPYMONEY PACKAGE IF YOU NEED THIS MODULE PLEASE SYNC IT FROM THERE, FOR EXAMPLE
## THIS FILE HAS BEEN DOWNLOADED AT 2019-01-09 05:07:22.447650 FROM https://github.com/Turulomio/xulpymoney/xulpymoney/connection_pg.py.
## @code
##       print ("Copying libmanagers.py from Xulpymoney project")
##        os.chdir("your directory)
##        os.remove("connection_pg.py")
##        os.system("wget https://raw.githubusercontent.com/Turulomio/xulpymoney/master/xulpymoney/connection_pg.py  --no-clobber")
##        os.system("sed -i -e '3i ## THIS FILE HAS BEEN DOWNLOADED AT {} FROM https://github.com/Turulomio/xulpymoney/xulpymoney/connection_pg.py.' connection_pg.py".format(datetime.datetime.now()))
## @encode

import datetime
import psycopg2
import psycopg2.extras

class Connection:
    def __init__(self):
        self.user=None
        self.password=None
        self.server=None
        self.port=None
        self.db=None
        self._con=None
        self._active=False
        self.init=None

    def init__create(self, user, password, server, port, db):
        self.user=user
        self.password=password
        self.server=server
        self.port=port
        self.db=db
        return self

    def cursor(self):
        return self._con.cursor()

    def mogrify(self, sql, arr):
        cur=self._con.cursor()
        s=cur.mogrify(sql, arr)
        cur.close()
        return  s

    def setAutocommit(self, b):
        self._con.autocommit = b


    def cursor_one_row(self, sql, arr=[]):
        cur=self._con.cursor()
        cur.execute(sql, arr)
        row=cur.fetchone()
        cur.close()
        return row

    def load_script(self, file):
        cur= self._con.cursor()
        procedures  = open(file,'r').read() 
        cur.execute(procedures)
        cur.close()       

    def cursor_one_column(self, sql, arr=[]):
        """Returns un array with the results of the column"""
        cur=self._con.cursor()
        cur.execute(sql, arr)
        for row in cur:
            arr.append(row[0])
        cur.close()
        return arr

    def cursor_one_field(self, sql, arr=[]):
        """Returns only one field"""
        cur=self._con.cursor()
        cur.execute(sql, arr)
        row=cur.fetchone()[0]
        cur.close()
        return row

    def commit(self):
        self._con.commit()

    def rollback(self):
        self._con.rollback()

    def connection_string(self):
        return "dbname='{}' port='{}' user='{}' host='{}' password='{}'".format(self.db, self.port, self.user, self.server, self.password)

    ## Returns an url of the type psql://
    def url_string(self):
        return "psql://{}@{}:{}/{}".format(self.user, self.server, self.port, self.db)

    def connect(self, connection_string=None):
        """Used in code to connect using last self.strcon"""
        if connection_string==None:
            s=self.connection_string()
        else:
            s=connection_string
        try:
            self._con=psycopg2.extras.DictConnection(s)
        except psycopg2.Error as e:
            print (e.pgcode, e.pgerror)
            return
        self.init=datetime.datetime.now()
        self._active=True

    def disconnect(self):
        self._active=False
        self._con.close()

    def is_active(self):
        return self._active

    def is_superuser(self):
        """Checks if the user has superuser role"""
        res=False
        cur=self.cursor()
        cur.execute("SELECT rolsuper FROM pg_roles where rolname=%s;", (self.user, ))
        if cur.rowcount==1:
            if cur.fetchone()[0]==True:
                res=True
        cur.close()
        return res
