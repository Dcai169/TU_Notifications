from jinja2 import Environment, PackageLoader, select_autoescape

e = Environment(loader=PackageLoader('TU_Notifications', 'templates'),
                autoescape=select_autoescape(['html','xml']))

def render(in_):
    index = e.get_template('index.html')
    return index.render(updates=in_)