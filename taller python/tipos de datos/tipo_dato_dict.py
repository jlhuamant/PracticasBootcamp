#tipo de dato dict

registro_usuarios = {
	'user':'jose',
	'user2':'henry',
	'user3':'josue',
	'user4':'cristian',
}

print(registro_usuarios)
print(type(registro_usuarios))
user_edad=dict([['henry','25'],['josue','26']])
#print(user_edad)

print(len(registro_usuarios))

print(registro_usuarios['user4'])

#print(dir(registro_usuarios))

print(registro_usuarios.keys())

print(registro_usuarios.get('user55','user not exist'))
print('hello wolrd')

# registro_usuarios.pop('user')
# print(registro_usuarios)

registro_usuarios['user5']='Rick'
print(registro_usuarios)

registro_usuarios.update({'user6':'pepe'})
print(registro_usuarios)