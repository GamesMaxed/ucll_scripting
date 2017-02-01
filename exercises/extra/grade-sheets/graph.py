import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

import sqlite3

db = sqlite3.connect('grades.db')

data = db.execute("""
  SELECT c.cname, AVG(g.grade)
  FROM courses c
  INNER JOIN grades g ON c.cid = g.cid
  GROUP BY c.cname
""")

data = list(data)

xvals = range(0, len(data))
plt.bar( xvals, [ grade for course, grade in data ] )
plt.xticks(xvals, [ course for course, grade in data ], rotation=90)


plt.show()
