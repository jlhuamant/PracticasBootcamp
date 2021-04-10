# #tipo de datos lista o array

lista_companies=['facebook', 'google','google','airbnb','netflix','twitter']
# print(len(lista_companies))
# print(type(lista_companies))
# companie='facebook'
# list_companies2 = list(companie)
# print(list_companies2)
# print(len(lista_companies))

# print(lista_companies[0])
# print(lista_companies[-1])
# print(lista_companies[-2])
# print(lista_companies[1:3])
# print(lista_companies[-2:])
# print(lista_companies[len(lista_companies)-2:])

# print(dir(lista_companies))

lista_companies.append('wathsapp')
lista_companies.append('messenger')
print(lista_companies)

# lista_companies.clear()
print(lista_companies)
googles_vals = lista_companies.count('google')
lista_companies.extend(['etoro','uber'])

print(lista_companies)

print(lista_companies.index('uber'))
print(lista_companies)

# lista_companies.insert(0,'instagram')
print(lista_companies)

lista_companies.insert(len(lista_companies),'instagram')
print(lista_companies)

lista_companies.remove('twitter')
lista_companies.remove('netflix')

# print(lista_companies)

# lista_companies.pop()
# print(lista_companies)
# #elimina el ultimo elemento

# #delete_company = lista_companies.pop(0)
# print(lista_companies)
# # print(delete_company)
# #elimina elemnto indicado

# lista_companies.reverse()
# print(lista_companies)

# lista_companies.sort()
# print(lista_companies)

print(lista_companies)
lista_companies_new=lista_companies.copy()
lista_companies_new.append('dojopy')
print(lista_companies_new)
print(lista_companies)