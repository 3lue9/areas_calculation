def program():  
        cronologia=[]

        from modules.clear import clear
        from modules.area import area_quadrato, area_rettangolo, area_triangolo, area_cerchio, area_trapezio
        from modules.whait import whait
 

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
program()
