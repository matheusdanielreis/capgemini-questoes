def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


def Analysis(item):
    global anagramArrayAux
    aux = 0
    countItem = anagramArrayAux.count(item)
    if countItem > 1:
        anagramArrayAux.remove(item)
        aux += 1
    return aux

anagram = input()
countAnagram = 0
countItem = ''

anagramArray = Convert(anagram)
anagramArrayAux = anagramArray
print(anagramArray)

for item in anagramArray:
    aux = Analysis(item)
    countAnagram += aux

print(countAnagram)


