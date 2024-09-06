#1
def milli_to_centi():
    millimeter=float(input("Enter value of millimeter:"))
    centimeter=millimeter/10
    print("Millimeter :",millimeter)
    print("Centimeter :",centimeter)
    length()
#2
def centi_to_milli():
    centimeter=float(input("Enter value of centimeter:"))
    millimeter=centimeter*10
    print("Centimeter :",centimeter)
    print("Millimeter :",millimeter)
    length()
#3
def centi_meter():
    centimeter=float(input("Enter value of centimeter:"))
    meter=centimeter*0.01
    print("Centimeter :",centimeter)
    print("Meter :",meter)
    length()
#4
def meter_centi():
    meter=float(input("Enter value of meter:"))
    centimeter=meter*100
    print("Meter :",meter)
    print("Centimeter :",centimeter)
    length()
#5
def meter_kilometer():
    meter=float(input("Enter value of meter:"))
    kilometer=meter*0.001
    print("Meter :",meter)
    print("Kilometer :",kilometer)
    length()
#6
def kilometer_meter():
    kilometer=float(input("Enter value of kilometer:"))
    meter=kilometer*1000
    print("Kilometer :",kilometer)
    print("Meter :",meter)
    length()
#7
def kilometer_mile():
    kilometer=float(input("Enter value of kilometer:"))
    mile=kilometer*0.6214
    print("Kilometer :",kilometer)
    print("Mile :",mile)
    length()
#8
def mile_kilometer():
    mile=float(input("Enter value of mile:"))
    kilometer=mile*1.609
    print("Mile :",mile)
    print("Kilometer :",kilometer)
    length()
#9
def meter_inch():
    meter=float(input("Enter value of meter:"))
    inch=meter*39.37
    print("Meter :",meter)
    print("Inch :",inch)
    length()
#10
def inch_meter():
    inch=float(input("Enter value of inch:"))
    meter=inch*0.025
    print("Inch :",inch)
    print("Meter :",meter)
    length()
#11
def meter_feet():
    meter=float(input("Enter value of meter:"))
    feet=meter*3.28
    print("Meter :",meter)
    print("Feet :",feet)
    length()
#12
def feet_meter():
    feet=float(input("Enter value of feet:"))
    meter=feet*0.304
    print("Feet :",feet)
    print("Meter :",meter)
    length()

#Length Function
def length():
    print("\n\n-------------Length Conversion-------------")
    print()
    print("\n01: Milllimeter To Centimeter")
    print("02: Centimeter To Milllimeter")
    print("03: Centimeter To Meter")
    print("04: Meter To Centimeter")
    print("05: Meter To Kilometer")
    print("06: Kilometer To Meter")
    print("07: Kilometer To Mile")
    print("08: Mile To Kilometer")
    print("09: Meter To Inch")
    print("10: Inch To Meter")
    print("11: Meter To Feet")
    print("12: Feet To Meter")
    print("13: Back")
    print("14: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        milli_to_centi()
    elif(choice==2):
        centi_to_milli()
    elif(choice==3):
        centi_meter()
    elif(choice==4):
        meter_centi()
    elif(choice==5):
        meter_kilometer()
    elif(choice==6):
        kilometer_meter()
    elif(choice==7):
        kilometer_mile()
    elif(choice==8):
        mile_kilometer()
    elif(choice==9):
        meter_inch()
    elif(choice==10):
        inch_meter()
    elif(choice==11):
        meter_feet()
    elif(choice==12):
        feet_meter()
    elif(choice==13):
        main()
    elif(choice==14):
        print("Good Bye!")
    else:
        print("Wrong Input!!!")
        length()
    
#___________________________________________________________________________________

#1
def cel_f():
    celsius=float(input("Enter value of celsius:"))
    fehrenheit=celsius*(9/5)+32
    print("Celsius :",celsius)
    print("Fehrenheit :",fehrenheit)
    temperature()
#2
def f_cel():
    fehrenheit=float(input("Enter value of fehrenheit:"))
    celsius=(fehrenheit-32)*(5/9)
    print("Fehrenheit :",fehrenheit)
    print("Celsius :",celsius)
    temperature()
#3
def cel_kel():
    celsius=float(input("Enter value of celsius:"))
    kelvin=celsius+273.15
    print("Celsius :",celsius)
    print("Kelvin :",kelvin)
    temperature()
#4
def kel_cel():
    kelvin=float(input("Enter value of kelvin:"))
    celsius=kelvin-273.15
    print("Kelvin :",kelvin)
    print("Celsius :",celsius)
    temperature()

#Temperature Function
def temperature():
    print("\n\n-------------Temperature Conversion-------------")
    print()
    print("\n01: Celsius To Fahrenheit")
    print("02: Fahrenheit To Celsius")
    print("03: Celsius To Kelvin")
    print("04: Kelvin To Celsius")
    print("05: Back")
    print("06: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        cel_f()
    elif(choice==2):
        f_cel()
    elif(choice==3):
        cel_kel()
    elif(choice==4):
        kel_cel()
    elif(choice==5):
        main()
    elif(choice==6):
        print("Good Bye!")
    else:
        print("Wrong Input!!!")
        temperature()
    
#___________________________________________________________________________________

#1
def milligram_gm():
    milligram=float(input("Enter value of milligram:"))
    gram=milligram*0.001
    print("Milligram :",milligram)
    print("Gram :",gram)
    weight()
#2
def gm_milligram():
    gram=float(input("Enter value of gram:"))
    milligram=gram*1000
    print("Gram :",gram)
    print("Milligram :",milligram)
    weight()
#3
def gm_kg():
    gram=float(input("Enter value of gram:"))
    kilogram=gram*0.001
    print("Gram :",gram)
    print("Kilogram :",kilogram)
    weight()
#4
def kg_gm():
    kilogram=float(input("Enter value of kilogram:"))
    gram=kilogram*1000
    print("Kilogram :",kilogram)
    print("Gram :",gram)
    weight()
#5
def milligran_kg():
    milligram=float(input("Enter value of milligram:"))
    kilogram=milligram*0.000001
    print("Milligram :",milligram)
    print("Kilogram :",kilogram)
    weight()
#6
def kg_milligram():
    kilogram=float(input("Enter value of kilogram:"))
    milligram=kilogram*1000000
    print("Kilogram :",kilogram)
    print("Milligram :",milligram)
    weight()
    
#Weight Function
def weight():
    print("\n\n-------------Weight Conversion-------------")
    print()
    print("\n01: Milligran To Gram")
    print("02: Gram To Milligram")
    print("03: Gram To Kilogram")
    print("04: Kilogram To Gram")
    print("05: Milligram To Kilogram")
    print("06: Kilogram To Milligram")
    print("07: Back")
    print("08: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        milligram_gm()
    elif(choice==2):
        gm_milligram()
    elif(choice==3):
        gm_kg()
    elif(choice==4):
        kg_gm()
    elif(choice==5):
        milligran_kg()
    elif(choice==6):
        kg_milligram()
    elif(choice==7):
        main()
    elif(choice==8):
        print("Good Bye!")
    else:
        print("Wrong Input!!!")
        weight()
#___________________________________________________________________________________

#1
def usd_inr():
    usd=float(input("Enter value of United States Dollars:"))
    inr=usd*76.9531
    print("United States Dollars :",usd)
    print("Indian Rupee :",inr)
    currency()
#2
def inr_usd():
    inr=float(input("Enter value of Indian Rupee:"))
    usd=inr*0.0129949281
    print("Indian Rupee :",inr)
    print("United States Dollars :",usd)
    currency()
#3
def eur_inr():
    eur=float(input("Enter value of Euro:"))
    inr=eur*81.108533497
    print("Euro :",eur)
    print("Indian Rupee :",inr)
    currency()
#4
def inr_eur():
    inr=float(input("Enter value of Indian Rupee:"))
    eur=inr*0.0123291589
    print("Indian Rupee :",inr)
    print("Euro :",eur)
    currency()
#5
def cad_inr():
    cad=float(input("Enter value of Canadian Dollar:"))
    inr=cad*59.754082449
    print("Canadian Dollar :",cad)
    print("Indian Rupee :",inr)
    currency()
#6
def inr_cad():
    inr=float(input("Enter value of Indian Rupee:"))
    cad=inr*0.0167352582
    print("Indian Rupee :",inr)
    print("Canadian Dollar :",cad)
    currency()
#7
def btc_inr():
    btc=float(input("Enter value of Bitcoin:"))
    inr=btc*2660842.762
    print("Bitcoin :",btc)
    print("Indian Rupee :",inr)
    currency()
#8
def inr_btc():
    inr=float(input("Enter value of Indian Rupee:"))
    btc=inr/2660842.762
    print("Indian Rupee :",inr)
    print("Bitcoin :",btc)
    currency()
#9
def jpy_inr():
    jpy=float(input("Enter value of Japanese Yen:"))
    inr=jpy*0.5893402928
    print("Japanese Yen :",jpy)
    print("Indian Rupee :",inr)
    currency()
#10
def inr_jpy():
    inr=float(input("Enter value of Indian Rupee:"))
    jpy=inr*1.6968125414
    print("Indian Rupee :",inr)
    print("Japanese Yen :",jpy)
    currency()
    
#Currency Function
def currency():
    print("\n\n-------------Currency Conversion-------------")
    print()
    print("\n01: United States Dollars To Indian Rupee")
    print("02: Indian Rupee To United States Dollars")
    print("03: Euro To Indian Rupee")
    print("04: Indian Rupee To Euro")
    print("05: Canadian Dollar To Canadian Dollar")
    print("06: Indian Rupee To Canadian Dollar")
    print("07: Bitcoin To Indian upee")
    print("08: Indian Rupee To Bitcoin")
    print("09: Japanese Yen To Indian Rupee")
    print("10: Indian Rupee To Japanese Yen")
    print("11: Back")
    print("12: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        usd_inr()
    elif(choice==2):
        inr_usd()
    elif(choice==3):
        eur_inr()
    elif(choice==4):
        inr_eur()
    elif(choice==5):
        cad_inr()
    elif(choice==6):
        inr_cad()
    elif(choice==7):
        btc_inr()
    elif(choice==8):
        inr_btc()
    elif(choice==9):
        jpy_inr()
    elif(choice==10):
        inr_jpy()
    elif(choice==11):
        main()
    elif(choice==12):
        print("Good Bye!")
    else:
        print("Wrong Input!!!")
        currency()
#___________________________________________________________________________________
#Main Function
def main():
    print("\n\n-------------Welcome To All In One Converter-------------")
    print("Developed by: \nPawar Aniket Satish")
    print()
    print("\n1: Length")
    print("2: Temperature")
    print("3: Weight")
    print("4: Currency")
    print("5: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        length()
    elif(choice==2):
        temperature()
    elif(choice==3):
        weight()
    elif(choice==4):
        currency()
    elif(choice==5):
        print("Good Bye! Have a great Day...")
    else:
        print("Wrong Input!!!")
        main()
main()
