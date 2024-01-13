import pyautogui
import time
import pyperclip

'''
                  ,---------------------------,                                ############ 
                  |  /---------------------\  |                              ########++########
                  | |                       | |                            ####            ###### 
                  | |     Projetos          | |                          ####                  ####  
                  | |      Pessoais         | |                        ####                    #### 
                  | |       -Arthur         | |                        ####   Pesquisando        ##               
                  | |                       | |                        ####         e            #### 
                  |  \_____________________/  |                        ##++   aprendendo         ####  
                  |___________________________|                        ####                      ##  
                ,---\_____     []     _______/------,                  ####                    ####
              /         /______________\           /|                    ####                  #### 
            /___________________________________ /  | ___                ####                #### 
            |                                   |   |    )                 ######        ############ 
            |  _ _ _                 [-------]  |   |   (                    ################  ########  
            |  o o o                 [-------]  |  /    _)_                        ####        ########## 
            |__________________________________ |/     /  /                                      ########## 
        /-------------------------------------/|      ( )/                                         ########## 
      /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /                                                      ##########   
    /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /                                                          ##########   
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                              ########
                                                                                                          ###### 
'''
# Pressiona a tecla Win
pyautogui.press("win")
time.sleep(2)

# Abre o Microsoft Edge
pyautogui.write("microsoft edge")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)

# Realiza uma busca pelo valor do dólar
pyautogui.click(x=343, y=72)# este clique seria um atalho para ir ao  google dentro do navegador (por ser microft edge, inicia com o bing)
time.sleep(3)
pyautogui.write("valor do dolar")# aqui, ja estaria aberta a barra de pesquisa
pyautogui.press("enter")
time.sleep(3)

# Copia o valor do dólar da página da web
pyautogui.click(x=249, y=441, clicks=2, interval=0.25)
pyautogui.hotkey("ctrl", "c")

# Recupera o valor copiado
dolar_str = pyperclip.paste()

# Converte o valor recuperado para float, ja que inicialmente era um valor string
dolar = float(dolar_str.replace(',', '.'))

# É feito a multiplicação com o valor do dolar 
resu1 = dolar * 2
resu2 = dolar * 3
resu3 = dolar * 4

# Imprime os resultados
print("Valor do dólar:", dolar)
print("Resultado 1:", resu1)
print("Resultado 2:", resu2)
print("Resultado 3:", resu3)


