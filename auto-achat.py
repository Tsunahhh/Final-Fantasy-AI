"""
    ***AUTO-ACHAT***
    Auteur: Tsuna
    Date: 09/03
    Desc: Pour spam l'achat d'une maison afin de tenter
            de l'avoir avant les autres joueurs . x)
"""
import pyautogui
import time
import random

# Randomisation des actions*/
def randtemps():
    """
        Permet de randomiser les action afin d'être 'invisible' aux autres et 
        de ressembler un maximum à un humain.
    """
    temps = random.randint(250, 1500)
    temps = temps*0.001
    
    return temps

# Timer avant de spam
for i in range(10):
    print("{0} avant de spam !0".format(10-i))
    time.sleep(1)

# Boucle de spam d'achats
while True:
    for i in range(3):
        pyautogui.press('num0')
        time.sleep(randtemps())
    pyautogui.press('num2')
    time.sleep(randtemps())
    pyautogui.press('num0')
    time.sleep(randtemps())
    pyautogui.press('num4')
    time.sleep(randtemps())
    pyautogui.press('num0')
    time.sleep(randtemps())