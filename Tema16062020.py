#1. Define a function which receives a string as a parameter.
# The function splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').

#Examples:
#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']

def separa(a):
    if a != '':
        if len(a) % 2 == 1:
            a = a + '_'
        res = []
        i = 0
        while i < len(a) - 1:
            res.append(a[i] + a[i+1])
            i += 2

    return res

a = 'abc'
print(separa(a))
a = 'abcdef'
print(separa(a))



#2. Create a function function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"



#3. According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes, then to define the creation function as stated above.