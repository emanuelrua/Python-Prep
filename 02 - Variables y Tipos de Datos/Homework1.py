a = 32
print (a)

print (type (8.5))

print (type(a))

minombre = "Emanuel Josue Rua Fuenamyor"

numcomp = 3 - 1j

print (type (numcomp))

pi = 3.1416

t1 = 'True'
t2 = True

print ('la variable "True" es tipo ', type(t1), ', y la variable True es tipo', type(t2))


suma = 1 + 3.5

a1 = 3 - 1j
a2 = 4 + 5j

print (a1+a2)

b1 = a1 + 3.5
print (b1)

print (4*3)

print (2**8)

b2 = 27/4
print (b2)

print (27//4)

print (27%4)

print (6*4+3)

ciudad = 'Maracaibo'
pais = 'Venezuela'
print (ciudad +', '+pais)

print (2 == '2')
#es falso ya que 2 es Entero y '2' es texto

print (2 == int('2'))

#a = float ('3,8') da error debido a que el número decimal esta siendo marcado por una coma cuando deberia ser un punto, una solucion correcta seria a = float ('3.8')

c1 = 3
c1 -= 2
print (c1)

print (1 << 2)
#el resultado es debido a que el 1 se ha movido 4 bits


print (2 + '2')
#no esta permitido la suma de dos tipos de variables, en caso de ser ambas int el resultado seria 4 y en caso de ser str el resultado seria 22

d1 = 'hola'
d2 = 2
print (d1 * d2)