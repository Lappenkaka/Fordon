import personbil
import lastbil

looping = True 

opel_gron=personbil.personbil("opel", "gron", 420)
BMW_vit=personbil.personbil("BMW", "vit", 69)

Scania_rosa=lastbil.lastbil("Scainia", "rosa", 10)
Volvo_rost=lastbil.lastbil("Volvo","rost", 90)

personbils_lista=[opel_gron,BMW_vit]
lastbils_lista=[Scania_rosa,Volvo_rost]

def print_fordonslista(fordonlista):
    for ettfordon in fordonlista

while looping:

    go = input("\vill ni lista fordonen igen j/n")

    if(go == "n"):
        break
