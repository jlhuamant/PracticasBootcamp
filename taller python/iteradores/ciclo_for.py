""" python ciclo FOR """

nombre = 'jose luis huaman'
lista_empresas_it = ['twitter','netflix','xiaomi','apple']
lista_divisas= ['euro','dolar','yen','libra-esterlina']

# for elemento in nombre:
# 	print(elemento)

# 	print(elemento.upper()*5)

# lo que esta haciendo es aplicar un conversor, convertirlo en lista

for item in lista_empresas_it:
	print(item.upper())	
	if len(lista_empresas_it) >= 4:
		for value in lista_divisas[2:]:
			print(value)

print('#'*20)

for value in enumerate(lista_divisas):
	print(value)

# for index, value in enumerate(lista_divisas):
# 	print(index)
# 	print(value)

for index, value in enumerate(lista_divisas):
	if index == 3:
	print(value)	