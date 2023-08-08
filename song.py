import tkinter as tk
import webbrowser as wb
import random
variable_song = ['뎁트 (Dept) - Paris with You','keshi - skeletons','moonlight 92914','Ashley Alisha - No More',
'keshi - beside you','Porto girl','slchld - girls are innocent','Jesse Barrera feat. Jeff Bernat & Johnny Stimson - "Casual"',
'예빛 (YeBit) - 소낙비 (Shower) ','크르르 (krr) - 무슨 관계 _ Between us','일기 박소은','정우물 (jungumul) - home',
'blue jungumul','DOGWHINE - Apologise for the monument','PLASUI PLASUI - SHOES','oceanfromtheblue - 검은머리 (girl) (feat. 블루 BLOO)']
def give_some_relax_song():
    name = str(window_box.get())
    if name != 'Peter':
        return
    random_song = random.choice(variable_song)
    variable_song.remove(random_song)
    if random_song == '뎁트 (Dept) - Paris with You':
        wb.open('https://www.youtube.com/watch?v=xpFHBGQslTE')

    elif random_song == 'keshi - skeletons':
        wb.open('https://www.youtube.com/watch?v=w_6fWYY6pRw')

    elif random_song == 'moonlight 92914':
        wb.open('https://www.youtube.com/watch?v=CBrYbMKGbVw')

    elif random_song == 'Ashley Alisha - No More':
        wb.open('https://www.youtube.com/watch?v=L0sCWCkUklY')

    elif random_song == 'keshi - beside you':
        wb.open('https://www.youtube.com/watch?v=aMyO6GNkfpo')

    elif random_song == 'Porto girl':
        wb.open('https://www.youtube.com/watch?v=XZr31wJfgeY')

    elif random_song == 'slchld - girls are innocent':
        wb.open('https://www.youtube.com/watch?v=I5BR1ulxfrQ')

    elif random_song == 'Jesse Barrera feat. Jeff Bernat & Johnny Stimson - "Casual"':
        wb.open('https://www.youtube.com/watch?v=fACfypWLqXg')

    elif random_song == '예빛 (YeBit) - 소낙비 (Shower) ':
        wb.open('https://www.youtube.com/watch?v=vMxlKQybcCM')

    elif random_song == '크르르 (krr) - 무슨 관계 _ Between us':
        wb.open('https://www.youtube.com/watch?v=Jfx14Lr4wic')

    elif random_song == '일기 박소은':
        wb.open('https://www.youtube.com/watch?v=fWIHNzkqr6k')

    elif random_song == '정우물 (jungumul) - home':
        wb.open('https://www.youtube.com/watch?v=vU19bGeakrs')

    elif random_song == 'blue jungumul':
        wb.open('https://www.youtube.com/watch?v=GASAPJiR-24')

    elif random_song == 'DOGWHINE - Apologise for the monument':
        wb.open('https://www.youtube.com/watch?v=b8wECujNfUM')

    elif random_song == 'PLASUI PLASUI - SHOES':
        wb.open('https://www.youtube.com/watch?v=U4E-KodhGlc')

    elif random_song == 'oceanfromtheblue - 검은머리 (girl) (feat. 블루 BLOO)':
        wb.open('https://www.youtube.com/watch?v=PG6ZAgtbBME')




window = tk.Tk()
window.geometry('1080x780')
window.configure(bg='pink')

window_title = tk.Label(window , text= 'This is relax program',font= (('Times'),15), bg='#87b3ee')
window_title.pack(pady=100)

window_box = tk.Entry(window,width=20 , font= ('Arial 15'),bg='#a903fc')
window_box.pack()

window_button = tk.Button(window,
                          text= 'relax' , font= (('Helvetica'),12)
                          , bg='#8610dd',width=8 , command=give_some_relax_song
                          )
window_button.pack(pady=25)

window.mainloop()
