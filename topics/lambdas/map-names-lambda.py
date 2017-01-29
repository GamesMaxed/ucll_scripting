def get_name(`\pgfmark{get_name:p:start}`p`\pgfmark{get_name:p:end}`):
    `\pgfmark{get_name:body:start}`return p.name`\pgfmark{get_name:body:end}`

map(persons, get_name)

# kan geschreven worden als

map(persons, lambda `\pgfmark{lambda:p:start}`p`\pgfmark{lambda:p:end}`: `\pgfmark{lambda:body:start}`p.name`\pgfmark{lambda:body:end}`)
