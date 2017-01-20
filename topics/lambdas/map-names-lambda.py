def getName(`\pgfmark{getName:p:start}`p`\pgfmark{getName:p:end}`):
    `\pgfmark{getName:body:start}`return p.name`\pgfmark{getName:body:end}`

map(persons, getName)

# kan geschreven worden als

map(persons, lambda `\pgfmark{lambda:p:start}`p`\pgfmark{lambda:p:end}`: `\pgfmark{lambda:body:start}`p.name`\pgfmark{lambda:body:end}`)
