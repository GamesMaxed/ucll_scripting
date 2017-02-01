import random
import os
import zipfile
import re


template = """Name: {fname} {lname} ({qid})
Assignment: Examen
Date Submitted: Sunday, February 5, 2017 {hours:02}:{minutes:02}:{seconds:02} AM CET
Current Grade: Needs Grading

Submission Field:
There is no student submission text data for this assignment.

Comments:
There are no student comments for this assignment.

Files:
	Original filename: {filename}.zip
	Filename: Examen_{qid}_attempt_2017-02-05-{hours:02}-{minutes:02}-{seconds:02}_{filename}.zip
"""


with open('first-names.txt', 'r') as file:    
    first_names = [ line.strip() for line in file if re.fullmatch(r'[a-zA-Z]+', line.strip()) ]

with open('last-names.txt', 'r') as file:
    last_names = [ line.strip() for line in file ]

qids = [ "q0{:06}".format(n) for n in range(100000, 999999) ]


def random_string(length):
    return "".join( [ random.choice('abcdefghijklmnopqrstvuwxyz') for _ in range(0, length) ] )


def generate_submission():
    bindings = {}
    bindings['hours'] = random.randrange(0, 12)
    bindings['minutes'] = random.randrange(0, 60)
    bindings['seconds'] = random.randrange(0, 60)
    bindings['fname'] = random.choice(first_names)
    bindings['lname'] = random.choice(last_names)
    bindings['qid'] = random.choice(qids)
    bindings['filename'] = random_string(8)

    first_names.remove(bindings['fname'])
    last_names.remove(bindings['lname'])
    qids.remove(bindings['qid'])

    filename = "submissions/Examen_{qid}_attempt_2017-02-05-{hours:02}-{minutes:02}-{seconds:02}.txt".format(**bindings)

    with open(filename, 'w') as file:
        file.write(template.format(**bindings))

    with zipfile.ZipFile('submissions/Examen_{qid}_attempt_2017-02-05-{hours:02}-{minutes:02}-{seconds:02}_{filename}.zip'.format(**bindings), 'w') as zip:
        for i in range(0, random.randrange(1,10)):
            data = random_string(1000)
            zip.writestr('src/file{}'.format(i), data)


def generate_submissions(n):
    if not os.path.isdir('submissions'):
        os.makedirs('submissions')
    
    for _ in range(0, n):
        generate_submission()
    
if __name__ == '__main__':
    random.seed(76456)
    generate_submissions(10)
