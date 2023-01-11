from machine import Pin
from time import sleep
ldr=Pin(4,Pin.IN)
l=[]
MORSE_CODE_DICTIONARY = { '  ':' ',
                          'A':'.-',
                          'B':'-...',
                          'C':'-.-.',
                          'D':'-..',
                          'E':'.',
                          'F':'..-.',
                          'G':'--.',
                          'H':'....',
                          'I':'..',
                          'J':'.---',
                          'K':'-.-',
                          'L':'.-..',
                          'M':'--',
                          'N':'-.',
                          'O':'---',
                          'P':'.--.',
                          'Q':'--.-',
                          'R':'.-.',
                          'S':'...',
                          'T':'-',
                          'U':'..-',
                          'V':'...-',
                          'W':'.--',
                          'X':'-..-',
                          'Y':'-.--',
                          'Z':'--..',
                          '1':'.----',
                          '2':'..---',
                          '3':'...--',
                          '4':'....-',
                          '5':'.....',
                          '6':'-....',
                          '7':'--...',
                          '8':'---..',
                          '9':'----.',
                          '0':'-----',
                          ',':'--..--',
                          '.':'.-.-.-',
                          '?':'..--..',
                          '/':'-..-.',
                          '-':'-....-',
                          '(':'-.--.',
                          ')':'-.--.-',
                          '_':'_',
                          }

def Morse_to_Txt(morse):
    text = [k for i in morse.split() for k,v in MORSE_CODE_DICTIONARY.items() if i==v]
    new_text = ''.join(text)
    print(new_text)
    
def loop():
    count=0
    q=0
    global l
    while True:
        m=ldr.value()
        sleep(0.5)
        if m==1:
            while True:
                m=ldr.value()
                print(m)
                if m==1:
                    count+=1
                    q=0
                    sleep(0.1)
                else :
                    l.append(str(count))
                    count=0
                    q+=1
                    if q==15:
                        break
                    sleep(0.2)
        else:
            if q==15:
                break    

def change():
    print(l)
    s=''
    for i in l:
        s=s+i
    print(s)
    w=s.replace('000000',' _ ')
    g=w.replace('00',' ')
    u=g.replace('3','.')
    e=u.replace('4','.')
    k=e.replace('6','-')
    x=k.replace('7','-')
    print(x)
    Morse_to_Txt(x)

loop()
change()