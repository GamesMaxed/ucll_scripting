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

    first_names = None
    with open('first-names.txt', 'r') as file:
        first_names = [ line.strip() for line in file ]

    last_names = None
    with open('last-names.txt', 'r') as file:
        last_names = [ line.strip() for line in file ]

    n_students = 1000
    students = [ (random.choice( first_names ), random.choice( last_names )) for _ in range(1, n_students) ]
        
    for first_name, last_name in students:
        sql = "INSERT INTO students(fname, lname) VALUES ('{}', '{}')".format(first_name, last_name)
        db.execute(sql)

    n_courses = 0
    with open('courses.txt', 'r') as file:
        for line in file:
            match = re.fullmatch(r'(.*), (\d)', line.strip())
            n_courses += 1

            if not match:
                sys.exit('Could not parse ' + line)

            course_name = match.group(1)
            course_weight = int(match.group(2))

            sql = "INSERT INTO courses(cname, weight) VALUES ('{}', '{}')".format(course_name, course_weight)
            db.execute(sql)

    
    for cid in range(1, n_courses + 1):
        gauss_mu = random.randint(8, 14)
        gauss_sigma = random.random() * 5 + 2
        
        for sid in range(1, n_students + 1):
            if random.random() < 0.75:
                grade = round(random.gauss(gauss_mu, gauss_sigma))
                grade = max(0, grade)
                grade = min(20, grade)

                sql = "INSERT INTO grades(sid, cid, grade) VALUES({}, {}, {})".format(sid, cid, grade)
                db.execute(sql)

    db.commit()
