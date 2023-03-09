from requests import get, post, delete

print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/2').json())
print(get('http://localhost:5000/api/users/99').json())
#print(get('http://localhost:5000/api/users/q').json())
print(post('http://localhost:5000/api/users').json())

print(post('http://localhost:5000/api/users',
           json={'name': '123'}).json())

print(post('http://localhost:5000/api/users',
           json={'name': 'xzc',
                 'about': 'zxcvbnm,./',
                 'email': 'zxc@qw.com',}).json())


print(delete('http://localhost:5000/api/users/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/users/1').json())
