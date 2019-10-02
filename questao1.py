def raizes (a,b,c):
    delta = (b*b)-(4*a*c)
    if delta >= 0:
        raiz1 = (-b+(delta**0.5))/(2*a)
        raiz2 = (-b-(delta**0.5))/(2*a)
        print ('Raíz 1: ', raiz1)
        print ('Raíz 2: ', raiz2)
        retorno = 0
    else:
        re_raiz = (-b)/(2*a)
        im_raiz=((-delta)**0.5)/(2*a)
        print('Raíz 1: ',re_raiz,' + ',im_raiz,'i')
        print('Raíz 2: ',re_raiz,' - ',im_raiz,'i')
        retorno = 1
    return retorno

def main():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    retorno = raizes(a,b,c)
    print(retorno)

main()
