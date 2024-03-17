from random import randint

start = int(input('Ab welche Nummer kann ich auswählen? '))
end = int(input('bis welche Nummer kann ich auswählen? '))
adad_shansi = randint(start, end)

for i in range(1, 6):
    hads_karbar = int(input('Schätz mal die Nummer, die ich ausgewählt habe : '))
    # yek adad random entekhab shode va karbar an ra hads mizanad
    if hads_karbar < adad_shansi:
        if i == 5:
            print(f'die richtige Nummer war {adad_shansi} \n')
        else:
            print(f'Du hast noch {5 - i} Chancen')
            print('Wähle eine größere Zahl\n')

    elif hads_karbar > adad_shansi:
        if i == 5:
            print(f'die richtige Nummer war {adad_shansi} bood\n')
        else:
            print(f'Du hast noch {5 - i} Chancen')
            print('Wähle eine kleinere Zahl\n')

    else:
        print('ES WAR RICHTICH HOOOOOORRRAAAAA!!!!')
        break
