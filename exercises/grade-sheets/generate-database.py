from contextlib import contextmanager
import sqlite3
import random
import re
import sqlite3
import os
import sys


@contextmanager
def connection(file):
    db = sqlite3.connect(file)
    yield db
    db.close()



dbfile = 'grades.db'

if os.path.isfile(dbfile):
    print("Database grades.db already exists")
    print("Delete it first if you want to regenerate it")
    sys.exit(-1)


rnd = random.seed('seed')

    
with connection(dbfile) as db:
    db.execute("CREATE TABLE students (sid INTEGER PRIMARY KEY ASC, fname TEXT, lname TEXT)")
    db.execute("CREATE TABLE courses (cid INTEGER PRIMARY KEY ASC, cname TEXT, weight INTEGER)")
    db.execute("CREATE TABLE grades (sid INTEGER, cid INTEGER, grade INTEGER, PRIMARY KEY(sid, cid), FOREIGN KEY (sid) REFERENCES students(id), FOREIGN KEY (cid) REFERENCES courses(id))")

    firstNames = None
    with open('first-names.txt', 'r') as file:
        firstNames = [ line.strip() for line in file ]

    lastNames = None
    with open('last-names.txt', 'r') as file:
        lastNames = [ line.strip() for line in file ]

    nStudents = 1000
    students = [ (random.choice( firstNames ), random.choice( lastNames )) for _ in range(1, nStudents) ]
        
    for firstName, lastName in students:
        sql = "INSERT INTO students(fname, lname) VALUES ('{}', '{}')".format(firstName, lastName)
        db.execute(sql)

    nCourses = 0
    with open('courses.txt', 'r') as file:
        for line in file:
            match = re.fullmatch(r'(.*), (\d)', line.strip())
            nCourses += 1

            if not match:
                sys.exit('Could not parse ' + line)

            courseName = match.group(1)
            courseWeight = int(match.group(2))

            sql = "INSERT INTO courses(cname, weight) VALUES ('{}', '{}')".format(courseName, courseWeight)
            db.execute(sql)

    
    for cid in range(1, nCourses + 1):
        gaussMu = random.randint(8, 14)
        gaussSigma = random.random() * 5 + 2
        
        for sid in range(1, nStudents + 1):
            if random.random() < 0.75:
                grade = round(random.gauss(gaussMu, gaussSigma))
                grade = max(0, grade)
                grade = min(20, grade)

                sql = "INSERT INTO grades(sid, cid, grade) VALUES({}, {}, {})".format(sid, cid, grade)
                db.execute(sql)

    db.commit()
