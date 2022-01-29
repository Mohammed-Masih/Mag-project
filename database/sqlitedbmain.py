import sqlite3
import pandas as pd

class Qry:
    def __init__(self, db):
        self.db = db
        self.res = None
        self.conn = None

    def run(self, qry):
        self.conn = sqlite3.connect(self.db)
        self.res = self.conn.execute(qry)
        return self


    def getList(self):
        data = [row for row in self.res]
        self.conn.close()
        return data

    def getConn(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn

    def getDict(self):
        cols = [x[0] for x in self.res.description]
        r = []
        for x in self.res:
            temp = {}
            for y in cols:temp[y] = x[cols.index(y)]
            r.append(temp)
        self.conn.close()
        return r

    def commit(self):
        self.conn.commit()
        self.conn.close()
        return self

    def getCols(self):
        return [x[0] for x in self.res.description]

    def getDf(self):
        return pd.DataFrame(self.res, columns=[x[0] for x in self.res.description])

qry = Qry('main.db')