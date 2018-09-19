import sqlite3

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

def adapt_point(point):
    return ("%f;%f" % (point.x, point.y)).encode('ascii')

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)

# Register the adapter
sqlite3.register_adapter(Point, adapt_point)

# Register the converter
sqlite3.register_converter("point", convert_point)

p = Point(4.0, -3.2)
print(p)
#########################
# 1) Using declared types
con = sqlite3.connect("tmp.db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test (pt_col point)")

cur.execute("insert into test(pt_col) values (?)", (p,))
cur.execute("insert into test(pt_col) values (?)", (Point(1.0, -1.0),))
cur.execute("insert into test(pt_col) values (?)", (Point(-5, 1000),))
cur.execute("select pt_col from test")
print("with declared types:")
for x in cur.fetchall():
    print(x[0])


cur.close()
con.close()
