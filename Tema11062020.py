# 1. Reverse the order of the items in an array.
# Example: a = [1, 2, 3, 4, 5]
# Result:  a = [5, 4, 3, 2, 1]

#Varianta 1
print(' Exercitiu 1')
a=[i for i in range(1,6)]
print(a)
b=[]
for i in a:
    b.append(a[-i])
print('   Varianta 1 ' + str(b))

#Varianta 2
a.reverse()
print('   Varianta 2 ' + str(a))


# 2. Get the number of occurrences of var b in array a.
# Example: a = [1, 1, 2, 2, 2, 2, 3, 3, 3] b = 2
# Result: 4
print()
print(' Exercitiu 2')
a=[1, 1, 2, 2, 2, 2, 3, 3, 3]
b=2
rezultat=0
for i in a:
    if i==b:
        rezultat += 1
print('   Valoarea ' +str(b) +' apare de ' + str(rezultat) + ' ori in lista ' + str(a))



# 3. Given a sentence as string, count the number of words in it.
# Example: a = 'ana are mere si nu are pere'
# Result: 7
print()
print(' Exercitiu 3')
a = input("Introduceti textul de analizat : ")
if a == '':
    # daca nu s-a introdus nici un text de la consola -  atunci initializare cu textul din cerinta exercitiului
    a = 'ana are mere si nu are pere'

nr_cuvinte = 0
nr_spatii = 0

if a != '':
    for i in a:
        if i == ' ':
            nr_spatii += 1

nr_cuvinte = nr_spatii + 1
print('in textul "' + str(a) + '" avem ' + str(nr_cuvinte) + ' cuvinte')
