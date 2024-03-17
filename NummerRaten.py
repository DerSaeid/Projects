from random import randint

shoro = int(input('az che adadi mitonam entekhab konam? '))
payan = int(input('ta che adadi mitonam entekhab konam? '))
adad_shansi = randint(shoro, payan)

for i in range(1, 6):
    hads_karbar = int(input('adadi ra ke entekhab kardam hads bezan: '))
    # yek adad random entekhab shode va karbar an ra hads mizanad
    if hads_karbar < adad_shansi:
        if i == 5:
            print(f'adadi ke entekhab karde boodam {adad_shansi} bood\n')
        else:
            print(f'{5 - i} ta joon dige dari')
            print('yekam boro bala\n')

    elif hads_karbar > adad_shansi:
        if i == 5:
            print(f'adadi ke entekhab karde boodam {adad_shansi} bood\n')
        else:
            print(f'{5 - i} ta joon dige dari')
            print('yekam bia paiin\n')

    else:
        print('dorost hads zadi hoooooora!!!!')
        break
