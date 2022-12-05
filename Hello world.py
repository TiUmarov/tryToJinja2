from jinja2 import Template

name = "Timur"

templ = Template("Hi {{ name }}")
message = templ.render(name = name)

print(message)