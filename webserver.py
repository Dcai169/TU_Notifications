from jinja2 import Environment, PackageLoader, select_autoescape

e = Environment(loader=PackageLoader('TU_Notifications', 'templates'),
                autoescape=select_autoescape(['html','xml']))
index = e.get_template('index.html')

print(index.render(updates=['Team Update 01', 'Team Update 02']))