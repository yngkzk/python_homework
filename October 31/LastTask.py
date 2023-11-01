def user_to_json(name, age, position, salary):
    return '{"name": "%s", "age": %d, "position", "%s", "salary": %.1f}' % (name, age, position, salary)

print(user_to_json('Me', 18, 'jun', 400000.23))
