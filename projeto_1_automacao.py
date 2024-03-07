#  Passo a Passo do projeto:

#  Passo 1: entrar no sistema da empresa:
    #  https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # instalar a biblioteca pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#  entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.typewrite(link)
pyautogui.press("enter")

#  dar uma pausa, um pouco maior (4 segundos):
time.sleep(4)

#  Passo 2: Fazer login:
#  clicar no formulário de e-mail:
pyautogui.click(x=622, y=410)
#  preenche o campo do email:
pyautogui.write("gustavolvjardim@gotmail.com")
pyautogui.press("tab")
#  preenche o campo de senha
pyautogui.write("007vtcfpg")
pyautogui.press("tab")
#  aperta a tecla enter para logar:
pyautogui.press("enter")

time.sleep(4)

# Passo 3: Importar a base de dados para cadastramento:
#  pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar primeiro produto:
# para cada linha da minha tabela:
for linha in tabela.index:
    # clicar no primeiro campo
    pyautogui.click(x=541, y=293)

    # digitar código do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # digitar marca do marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # digitar tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # digitar categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # digitar preço do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # digitar custo unitario do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # digitar obs do produto
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    #  apertar botao de enviar:
    pyautogui.press("enter")
    pyautogui.scroll(10000)

#  Passo 5: Repetir o processo de cadastro até acabar - loop for: