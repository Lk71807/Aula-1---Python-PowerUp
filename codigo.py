# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
  # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pyautogui
import pyautogui 
import time

pyautogui.PAUSE = 0.5

 #-> clicar o mouse
# pyautogui.write -> escrever um    preo  custo obs   exto
   # RESA000287 Samsung   72.8  nan 
  

# abrir o navegador (Chrome)lk-98@hotmail.com   suasenhaaqui   

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.click("enter")

# pode ser que aque ele demora alguns segundos para carregar o site, então 
time.sleep(3)

# 2. fazer login27.5  12.4  Troca de fornecedor 

pyautogui.click(x=859, y=597)
pyautogui.write("lk-98@hotmail.com")

pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("suasenhaaqui") # sua senha aqui


pyautogui.press("tab")   # passou para o botão de login
pyautogui.press("enter")  #  ai ele entra


time.sleep(3)
# 3. Abrir /Importar a base de dados de produtos para cadastrar
# pip install pandas  e o numpy e o openpyxl
import pandas as pd

# tabela e = a base de dados 
tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4. cadastrar um produto
# str = string = texto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"]) 
      # clicar no campo do codigo do produto
    pyautogui.click(x=593, y=452)
      # preencher o codigo
    pyautogui.write(codigo)
      # passar para o proximo campo
    pyautogui.press("tab")
      # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
      # passar para o proximo campo
    pyautogui.press("tab")
      # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
      # passar para o proximo campo
    pyautogui.press("tab")
      # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
      # passaMOLO000251 Logitechr para o proximo campo
    pyautogui.press("tab")

      # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
      # passar para o proximo campo
    pyautogui.press("tab")
      # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
      # passar para o proximo campo
    pyautogui.press("tab")
      # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.write(str(tabela.loc[linha, "obs"]))
      # passar para o proximo campo
    pyautogui.press("tab")
      # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
      # 5. Repetir tudo isso ate acabar a lista
