from jinja2 import Template

name = "Timur"
age = 20

templ = Template("Hi {{ n }}")
message = templ.render(n = name)
templ2 = Template("You are {{ a }} years old, damn you are child")
ageMessage = templ2.render(a = age)

print(message, ageMessage, sep="\n")



#message2 = f"Привет {name}"

#print(message2)