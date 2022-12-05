# This file is made for learning jinja raw, for, if blocks

import jinja2
from jinja2 import Template

data = ''' This is data that
i don't want to touch and just
print as it exist
and it's named {{ name }} '''

testTemplate = Template(data)
testMsg = testTemplate.render(name = 'WontTouch')

print(testMsg, end="\n\n")

data = '''{% raw %} This is data that
i don't want to touch and just
print as it exist
and it's named {{ name }} {% endraw %}'''

testTemplate2 = Template(data)
testMsg2 = testTemplate2.render(name = 'WontTouch')

print(testMsg2, end="\n\n")

# stop for a minute, i can create a html page
#link = ''' Just a link <a href=#>Yeah that's a link</a>'''
#aPage = Template(link)
#rendPage = aPage.render()
# maybe i can, but i don't know how to open this /\

link = ''' Just a link <a href=#>Yeah that's a link</a>'''
aPage = Template("{{ link | e }}") # flag e mean escape for <> simbols
rendPage = aPage.render(link = link)

print(rendPage, end="\n\n")

humans = [{'id': 1, 'being': 'Timur', 'age': 20},
    {'id': 2, 'being': 'Ruslan', 'age': 21},
    {'id': 3, 'being': 'Ilia', 'age': 19},
    {'id': 4, 'being': 'CEO', 'age': 'over 9000'}]

listHumans = '''<select name = "Humans">
{% for i in humans-%}
{% if i['id'] > 1-%}
    <option value="{{ i['id'] }}">{{ i['being'] }} is {{ i['age'] }} years old</option>
{% else -%}
     <option value="{{ i['id'] }}">{{ i['being'] }} is {{ i['age'] }} years old and on a bit loh</option>
{% endif -%}
{% endfor -%}
</select>'''
listTempl = Template(listHumans)
listMessage = listTempl.render(humans = humans)

print(listMessage, end="\n\n")

#escMsg = escape(link) <-- wont work 
#print(escSmg)
