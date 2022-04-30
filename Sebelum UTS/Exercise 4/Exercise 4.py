import numpy as np
# Komposisi tim A
skillsA_ = {'save': 81, 'tackle1': 79, 'passing': 78, 'tackle2':60, 'dribble1': 76, 'dribble2': 80, 'intercepts':85, 'shoot': 92}
mentalA_ = {'GK':80, 'DF':79, 'MD':78, 'ATK':77}

# Komposisi tim B
skillsB_ = {'save': 86, 'tackle1': 80, 'passing': 81, 'tackle2':70, 'dribble1': 70, 'dribble2': 81, 'intercepts':86, 'shoot': 90}
mentalB_ = {'GK':77,'DF':78, 'MD':79, 'ATK':80}

# Jumlah Supporter
kb = 100000
ka = 115000
b = 0
a = 0
t = 90
curr = "A"

# Hitung dari komposisi
def hitung_skill(skill, mentallity):
    def alpha(mentallity):
        return np.random.uniform(0,0.025) * (mentallity/100)
    def beta():
        return np.random.uniform(0,0.025) * (ka/(ka+kb))
    return skill*(1-(alpha(mentallity)+beta()))
def md_(x,y):
    return hitung_skill(x,y)

def atk_(x,y):
    return hitung_skill(x,y)

def gk_(x,y):
    return hitung_skill(x,y)

def df_(x,y):
    return hitung_skill(x,y)
# Awal game
def mulai():
    print('Pertandingan dimulai')
    fieldMid()

# Skor sepakbola
def resultCheck():
    global a, b
    return print(f'Skor pertandingan saat ini adalah {a} - {b}')

def stopBreak(x):
    x = 0
    return x
def resultFinal():
    global a,b
    return print(f'Hasil akhir pertandingan adalah {a} - {b}')
    
# Program pemain sayap/operan
def fieldMid():
    global t, curr
    if t >= 0:
        if curr == "A":
            if md_(skillsA_.get('dribble1'), mentalA_.get('MD')) > md_(skillsB_.get('tackle2'), mentalB_.get('MD')):
                t -= 1
                print('Bola dioper ke penyerang tim A')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "A"
            else:
                t -= 2
                print('Bola diambil oleh penyerang tim B')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "B"
        else:
            if md_(skillsB_.get('dribble1'), mentalB_.get('MD')) > md_(skillsA_.get('tackle2'), mentalA_.get('MD')):
                t -= 1
                print('Bola dioper ke penyerang tim B')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "B"
            else:
                t -= 2
                print('Bola diambil oleh penyerang tim A')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "A"
        fieldAtk()
    else:
        stopBreak(t)
            
# Program penyerangan
def fieldAtk():
    global t, curr, a, b
    if t >= 0:
        if curr == "B":
            if atk_(skillsB_.get('dribble2'),mentalB_.get('ATK')) > df_(skillsA_.get('tackle1'),mentalA_.get('DF')):
                print('Penyerang tim B akan melakukan shooting')
                print(f'waktu pertandingan tersisa {t} menit')
                t -= 1
                if atk_(skillsB_.get('shoot'),mentalB_.get('ATK')) > gk_(skillsA_.get('save'),mentalA_.get('GK')):
                    t -= 2
                    print('tendangan berhasil memasukki gawang, gol bestie!')
                    print(f'waktu pertandingan tersisa {t} menit')
                    b += 1
                    resultCheck()
                    fieldMid()
                    curr = "B"
                else:
                    t -= 3
                    print('sayang sekali, tendangan tidak berhasil memasuki gawang')
                    print(f'waktu pertandingan tersisa {t} menit')
                    curr = "A"
            else:
                t -= 2
                print('Bola diambil oleh pemain pertahanan tim A')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "A"
        else:
            if atk_(skillsA_.get('dribble2'),mentalA_.get('ATK')) > df_(skillsB_.get('tackle1'),mentalB_.get('DF')):
                t -= 1
                print('Penyerang tim A akan melakukan shooting')
                print(f'waktu pertandingan tersisa {t} menit')
                if atk_(skillsA_.get('shoot'),mentalA_.get('ATK')) > gk_(skillsB_.get('save'),mentalB_.get('GK')):
                    t -= 2
                    print('tendangan berhasil memasukki gawang, gol bestie!')
                    print(f'waktu pertandingan tersisa {t} menit')
                    a += 1
                    resultCheck()
                    fieldMid()
                    curr = "A"
                else:
                    t -= 3
                    print('sayang sekali, tendangan tidak berhasil memasuki gawang')
                    print(f'waktu pertandingan tersisa {t} menit')
                    curr = "B"
            else:
                t -= 2
                print('Bola diambil oleh pemain pertahanan tim B')
                print(f'waktu pertandingan tersisa {t} menit')
                curr = "B"
        fieldDf()
    else:
        stopBreak(t)

# Program bertahan
def fieldDf():
    global curr, t
    if t >= 0:
        if curr == "B":
            if df_(skillsB_.get('passing'), mentalB_.get('DF')) > atk_(skillsA_.get('intercepts'),  mentalA_.get('ATK')):
                t -= 2
                print('Bola dioper ke pemain tengah B')
                fieldMid()
            else:
                t -= 1
                print('Bola diambil oleh penyerang tim A')
                fieldAtk()
        else:
            if df_(skillsA_.get('passing'), mentalA_.get('DF')) > atk_(skillsB_.get('intercepts'),  mentalB_.get('ATK')):
                t -= 2
                print('Bola dioper ke pemain tengah A')
                fieldMid()
            else:
                t -= 1
                print('Bola diambil oleh penyerang tim B')
                fieldAtk() 
    else:
        stopBreak(t)
mulai()
