from jinja2 import Template

class HumanBieng:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
timur = HumanBieng("Timur", 20)

template = Template("Hi, my name is {{ t.name }} and i'm {{ t.age }} years old")
message = template.render(t = timur)

print(message)

#name = "Timur"
#age = 20

#templ = Template("Hi {{ n }}")
#message = templ.render(n = name)
#templ2 = Template("You are {{ a }} years old, damn you are child")
#ageMessage = templ2.render(a = age)

#message2 = f"Привет {name}"
#print(message2)