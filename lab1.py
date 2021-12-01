fold = open('WarAndWorld.txt', 'r')
a = fold.read()
alphabet = ['смещение',' ','а','б','в','г','д','е',
'ж','з','и','й','к','л','м','н','о','п','р','с','т',
'у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
'А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М',
'Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ',
'Ъ','Ы','Ь','Э','Ю','Я','a','b','c','d','e','f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','A','B','C','D','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
def encrypt(msg, shift):
    ret = ""
    for x in msg:
        if x in alphabet:
            indMsg = alphabet.index(x)
            for z in shift:
                if z in alphabet:
                    indShift = alphabet.index(z)
                    ret += alphabet[(indMsg+indShift)%128]

    return ret
a = a.lower()
newText =(encrypt(a, "а")) 
print(a)

def decrypt(msg, shift=2):
    ret = ""
    for x in msg:
        if x in alphabet:
            ind = alphabet.index(x)
            ret += alphabet[ind-shift]
        else:
            ret += x
    return ret
print()
print()
print()
print((decrypt(newText)))
 