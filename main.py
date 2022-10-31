#by lizard#2097

word = list(input("word: "))
nps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]


def factorizar(n):
    ret = []
    for i in range(1,n + 1):
        if n%i == 0:
            ret.append(i)
    #print("ret1:",ret)
    if len(ret)%2 != 0:
        ret.insert((len(ret)//2+1),ret[(len(ret)//2)])
    #print("ret2:",ret)
    return ret[int((len(ret)/2)-1):int((len(ret)/2)+1)]

def ToBF(l,n = 0):
    L = int(ord(l)) - int(n)
    #print("l:",l)
    #print("ord(l):",ord(l))
    #print("L:",L)
    #print("n:",n)
    BFCode = ""
    char = "+"
    if L < 0:
        L *= -1
        char = "-"
    if L**(1/2) == (L**(1/2))//1:
        for i in range(int((L**(1/2))//1)):
            BFCode += "+"
        BFCode += "[>"
        for i in range(int((L**(1/2))//1)):
            BFCode += char
        BFCode += "<-]>.<"
    elif L not in nps:
        fact = factorizar(L)
        for i in range(fact[0]):
            BFCode += "+"
        BFCode += "[>"
        for i in range(fact[1]):
            BFCode += char
        BFCode += "<-]>.<"
    elif L in nps:
        fact = factorizar(L - 1)
        #print("[0]:",fact[0])
        #print("[1]:",fact[1])
        for i in range(fact[0]):
            BFCode += "+"
        BFCode += "[>"
        for i in range(fact[1]):
            BFCode += char
        BFCode += f"<-]>{char}.<"
    return BFCode
f = open("main.bf","w")
lastI = 0
script = ""
for i in word:
    script += ToBF(i,lastI)
    lastI = ord(i)
f.write(script)
f.close()
