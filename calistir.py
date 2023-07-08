import PySimpleGUI as sg

#WINDOW_SIZE = (1280, 720)


box_list4 = [str(i) for i in range(1,755)]



genel = [	
            [sg.Combo(box_list4, default_value='bir problem seçiniz', size= (80,1), key='numara'),sg.InputText(default_text='Problem numarası giriniz.',size=(36,1),key='numara2')],
         	[sg.Multiline(default_text='buraya problem gelecek',size=(117,15),do_not_clear=True,key = 'sonuclar_genel')],
            [sg.Multiline(default_text='buraya sonuçlar gelecek',size=(117,10),do_not_clear=True,key = 'sonuclar_genel')],
         	[sg.Button('Hesapla',size=(8,1)),sg.Button('Temizle',size=(8,1)),sg.Exit('Çıkış',size=(8,1))]]


window = sg.Window(title='Euler Resolver', layout= genel, size=(1280,720), location =(0,0), grab_anywhere=True )
window.Read()
