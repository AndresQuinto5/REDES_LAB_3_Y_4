from dvr import main1
from flooding import main2
from lsr import main3



apagar = True 

while apagar == True:
    print(
    """

    Bienvenidos a lab 3 y 4

    1. DVR
    2. Flooding
    3. LSR
    4. Salir 

    """
    )
    entrada = int(input("Ingrese el numero de la opcion deseada: "))
    if entrada == 1:
        main1.main1()
        pass
    if entrada == 2:
        main2.main2()
    if entrada == 3:
        main3.main3()
        pass
    if entrada == 4:
        apagar = False
    else:
        print("Opcion seleccionada no existe")
