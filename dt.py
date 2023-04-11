import numpy as np
from prettytable import PrettyTable
x = PrettyTable()
y = PrettyTable()
from colorama import init, Fore, Back, Style

fs = 0
def init():
    fs = float(input(Fore.BLUE+"INGRESE EL FACTOR DE SERVICIO (entre 1 y 3): "))
    if(fs >= 1 and fs <= 3):
        cal(fs)        
    else:
        print(Fore.RED+"EL FACTOR DE SERVICIO ES INCORRECTO")
        init()

def cal(para):
    caudal = float(input(Fore.BLUE+"INGRESE EL CAUDAL: "))
    te = float(input(Fore.BLUE+"INGRESE LA TEMPERATURA DE ENTRADA: "))
    ts = float(input(Fore.BLUE+"INGRESE LA TEMPERATURA DE SALIDA: "))
    c1 = 1000
    c2 = 0.0003069

    tDT = round(caudal*(te - ts)*para*c1*c2)

    print(Fore.RED+"\n EL DISTRITO MIDE: ", tDT , '\n')
    chillers(tDT)

def chillers(tdt):
    print(Fore.RED+"\n TAMAÑOS DE CHILLERS CETRÍFUGOS Y DE ABSORCIÓN 500TR, 750TR, 1000TR \n")
    print(Fore.RED+"POR FAVOR INDICAR CANTIDAD Y LEA CON DETENIMIENTO \n")
    print(Fore.GREEN+"__________________________________________________________ \n")
   
    c500 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 500TR CENTRÍFUGOS: "))
    c750 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 750TR CENTRÍFUGOS: "))
    c1000 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 1000TR CENTRÍFUGOS: "))

    aa500 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 500TR ABSORCIÓN: "))
    a750 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 750TR ABSORCIÓN: "))
    a1000 = int(input(Fore.BLUE+"INGRESE LA CANTIDAD PARA 1000TR ABSORCIÓN: "))

    #Operación centrífugos
    totalc= (500*c500)+(750*c750)+(1000*c1000)
    totala= (500*aa500)+(750*a750)+(1000*a1000)
    totales = totala + totalc

    tmax = tdt + (tdt*0.5) #Se comprueba el tamaño maximo de TR
    if totales<=tdt:
        print(Fore.RED+"\n LAS TECNOLOGÍAS SELECCIONADAS NO SUMINISTRAN EL TAMAÑO DEL DT \n")
        print(Fore.GREEN+"__________________________________________________________ \n")
        chillers(tdt)
    elif totales >= tmax:
        print(Fore.RED+"\n LAS TECNOLOGÍAS SELECCIONADAS SUPERAN EL TOPE DEL DT")
        print(Fore.GREEN+"__________________________________________________________ \n")
        chillers(tdt)
    else:
        centrifugos(totalc)
        absorcion(totala)

def centrifugos(parametro1):
    
    rp=parametro1*0.3190995427365	
    g=(parametro1*511.13199046407)/1000	
    c=(parametro1*0.0035174111853)*(1925000/0.88)	
    o=c*0.03	
    	
    capex=parametro1*0.0035174111853	
    ft=capex*1000000	
    e=capex*1700000	
    b=capex*2000000
    
    x.field_names=["Energia","Emisiones co2(TCo2 mes)","Capex(USD Megavatios)","Opex(Do-año)"]
    x.add_row(["Red_Publica",e,g,ft])
    x.add_row(["Microturbina a gas",rp,o,rp])           
    x.add_row(["Solar fotovoltaica",b,b,e])
    x.add_row(["Energia eolica",ft,ft,c])
    x.add_row(["Energia biomasa",c,capex,g])
    x.add_row(["TR de los chillers de adsorcion es:",parametro1,"",""])           


    print (x)

def absorcion(parametro2):

    g=(parametro2*511.13199046407)/1000		
    c=((parametro2 * 0.0035174111853)*(1925000/0.88))		
    o=c*0.03		
  		
    capex=parametro2*0.0035174111853		
    ft=(capex*1000000)*1.015		
    b=capex*2000000 

    y.field_names=["Energia","Emisiones co2(TCo2 mes)","Capex(USD Megavatios)","Opex(Do-año)"]
    y.add_row(["Microturbina a gas",g,g,g])
    y.add_row(["Solar termica",capex,capex,capex])           
    y.add_row(["Energia biomasa",b,b,b])
    y.add_row(["TR de los chillers de absorcion es",parametro2,"",""])

    print (y)

init()

    