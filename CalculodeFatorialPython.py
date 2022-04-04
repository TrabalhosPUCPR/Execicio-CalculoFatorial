esc = int(input('Digite qual calculo de fatorial para testar (1=estruturada, 2=recursiva, 3=vetorial) '))

#ESTRUTURADA
if(esc == 1):
    import time
    fat = int(input('Digite o fatorial '))
    start_time = time.time()
    f = 1

    for x in range(1, fat):
        f *= fat
        fat -= 1
        
    print(f)
    print('O tempo para executar o codigo foi: ', time.time() - start_time)



#RECURSIVA
if(esc == 2):
    import time
    fat = int(input('Digite o fatorial '))
    start_time = time.time()
    f = 1

    def fatorial(fat, f):
        f *= fat
        fat -= 1
        if fat >= 1:
            return fatorial(fat, f)
        else:
            return f 

    print(fatorial(fat, f))
    print('O tempo para executar o codigo foi: ', time.time() - start_time)



#VETORIAL
if(esc ==3):
    print('VALOR ACIMA DE 33 NAO FUNCIONA')
    import numpy as np
    import time
    fat = int(input('Digite o fatorial '))
    start_time = time.time()
    f = 1

    fat = np.arange(1, fat+1)
    fat = np.cumprod(fat)

    print(fat)
    print('O fatorial e: ',fat[-1])
    print('O tempo para executar o codigo foi: ', time.time() - start_time)


