my_file = open('url.txt', encoding='utf-8')
text = my_file.read()
my_file.close()


def parse(site_name):
    domain = site_name.split('?')
    domain = domain[0].split('/')
    domain.remove('')
    var = domain[0][:-1]
    domain.pop(0)
    domain.insert(0, var)
    domain_path = site_name.split('?')
    domain.append(domain_path[1])
    return domain


def get_parameters(full_path):
    parameters = {}
    index = full_path[3]
    settings = index.split('&')
    for x in settings:
        data = x.split('=')
        parameters[data[0]] = data[1]
    return parameters


parsed = parse(text)
path = get_parameters(parsed)

message = f'''
- протокол: %s
- домен: %s
- путь: /%s
- параметры запроса: {path}
''' % (parsed[0], parsed[1], parsed[2])
print(message)