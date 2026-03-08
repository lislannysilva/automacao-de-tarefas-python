# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

# pausa entre comandos
pyautogui.PAUSE = 0.5

# tempo para você se preparar antes da automação começar
time.sleep(3)

# abrir o navegador (chrome)
pyautogui.press("win")
time.sleep(1)

pyautogui.write("chrome")
time.sleep(1)

pyautogui.press("enter")

# esperar o navegador abrir
time.sleep(5)

# entrar no link
pyautogui.hotkey("ctrl", "l")  # seleciona barra de endereço
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Fazer login

# selecionar o campo de email
pyautogui.click(x=851, y=382)

# escrever o email
pyautogui.write("lislanny.tech@gmail.com")

# ir para senha
pyautogui.press("tab")

# escrever senha
pyautogui.write("sua senha")

# entrar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

# Passo 3: Importar base de produtos
tabela = pd.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# Passo 4: Cadastrar produtos
for linha in tabela.index:

    # clicar no campo código
    pyautogui.click(x=732, y=249)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    # voltar para o topo
    pyautogui.scroll(5000)

    time.sleep(1)