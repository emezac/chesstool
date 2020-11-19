from Cheetah.Template import Template
templateDef = open("template.html", encoding="ISO-8859-1").read()
t = Template(templateDef)
t.title = 'Hello World Example!'
t.set_position = "here"
print(t)
