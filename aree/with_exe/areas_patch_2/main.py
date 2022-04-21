from modules_eng.clear import clear


def program_eng():  
        cronologia=[]

        from modules_eng.clear import clear
        from modules_eng.areas_eng import area_quadrato, area_rettangolo, area_triangolo, area_cerchio, area_trapezio
        from modules_eng.whait import whait
 

        def calcolatore_area_eng():  
                print('[0] history')
                print('[1] square')
                print('[2] rectangle')
                print('[3] triangle')
                print('[4] circle')
                print('[5] trapezoid')

                forma=input('==> ')
                if forma == '0':
                        print(cronologia)
                        whait()
                        clear()
                        print ('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()

        
                #quadrato
                if forma == '1':
                        area_quadrato()
                        whait()
                        clear()
                        cronologia.append('area square')
                        print('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()

                #rettangolo
                if forma == '2':
                        area_rettangolo()
                        whait()
                        clear()
                        cronologia.append('area rectangle')
                        print('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()
                #triangolo
                if forma == '3':
                        area_triangolo()
                        whait()
                        clear()
                        cronologia.append('area triangle')
                        print('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()
                #cerchio
                if forma == '4':
                        area_cerchio()
                        whait()
                        clear()
                        cronologia.append('area circle')
                        print('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()
                #trapezio
                if forma == '5':
                        area_trapezio()
                        whait()
                        clear()
                        cronologia.append('area trapezoid')
                        print('you want to do other calculations')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area_eng()
        calcolatore_area_eng()
def program_ita():  
        cronologia=[]

        from modules_ita.clear import clear
        from modules_ita.area_ita import area_quadrato, area_rettangolo, area_triangolo, area_cerchio, area_trapezio
        from modules_ita.whait import whait
 

        def calcolatore_area():   
                print('[0] cronologia')
                print('[1] quadrato')
                print('[2] rettangolo')
                print('[3] triangolo')
                print('[4] cerchio')
                print('[5] trapezio')

                forma=input('==> ')
                if forma == '0':
                        print(cronologia)
                        whait()
                        clear()
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()

                #quadrato
                if forma == '1':
                        area_quadrato()
                        whait()
                        clear()
                        cronologia.append('area quadrato')
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()

                #rettangolo
                if forma == '2':
                        area_rettangolo()
                        whait()
                        clear()
                        cronologia.append('area rettangolo')
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()
                #triangolo
                if forma == '3':
                        area_triangolo()
                        whait()
                        clear()
                        cronologia.append('area triangolo')
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()
                #cerchio
                if forma == '4':
                        area_cerchio()
                        whait()
                        clear()
                        cronologia.append('area cerchio')
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()
                #trapezio
                if forma == '5':
                        area_trapezio()
                        whait()
                        clear()
                        cronologia.append('area trapezio')
                        print('vuoi fare altri calcoli')
                        print('y/n')
                        A= input('==>')
                        if A == 'y':
                                clear()
                                calcolatore_area()
        calcolatore_area()
def select_language():
    print('select language')
    print('[1] English')
    print('[2] Italiano')
    lingua=input('==>')
    if lingua == '1':
        clear()
        program_eng()
    if lingua == '2':
        clear()
        program_ita()
select_language()
"""
programma creato TOTALMENTE da 3lue9 
19/04/2022
all'età di 12 anni 
"""
"""
program TOTALLY created by 3lue9
04/19/2022
at the age of 12
"""