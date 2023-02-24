import pyautogui as pg
import time

destino = str(input('cole o endereco do arquivo a ser aberto '))
pg.alert('não mexa')
pg.PAUSE = 0.5
pg.press('winleft')
time.sleep(2)
pg.write(destino)
time.sleep(2)
pg.press('enter')