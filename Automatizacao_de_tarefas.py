
import yfinance as yf;
import pyautogui 
import webbrowser
import pyperclip


""" Automatização de Processos """

""" 
Passo 1 : buscar informações das ações de forma automática;
Passo 2 : criar as análises dos dados;
Passo 3 : enviar um e-mail para o meu gestor com as resultados das análises;
"""


""" Passo 1 : buscar informações das ações de forma automática;
periodo 6meses "6mo" """
#PETR4.SA
alandoalmeida@icloud.com    companie = input("Digite o Ticker da Companhia: ")
ticker = yf.Ticker(companie)
history_data = ticker.history("6mo")
closure = history_data.Close;
""" closure.plot() """

print(closure)

""" 
Passo 2: criar as an´lises dos dados 

- cotação maxima;
- cotação minima;
- cotação Atual;

"""

maximum_quote = round(closure.max(), 2)
minimum_quotation = round(closure.min(), 2)
current_quote = round(closure[-1], 2)

""" 
concatenar "f" antes das aspas duplas
Arrendodar "round" e quantidade de decimais ,2 no final

"""

print(f"A cotação máxima é: R$ {maximum_quote}")
print(f"A cotação mímima é: R$ {minimum_quotation}")
print(f"A cotação Atual é: R$ {current_quote}")


""" 
Passo 3: Enviar um E-mail para o meu Gestor com os resutados das analises 

- abrir um nova aba( ctrl+t)
- digitar o endereço do Gmail e dar um enter
- clilcar no botão escrever;


"""
""" pause de 2 segundo """


url = "https://www.gmail.com"
webbrowser.open(url)

#clicar no botão escrever
import time

time.sleep(5)
print("teste")
pyautogui.position()
posicao = pyautogui.position()
print(f"posicao {posicao}" )


pyautogui.click(x=2436, y=198)
pyperclip.copy("alandoalmeida@icloud.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

message = f"""
Prezado Gestor,

segue as analises, conforme solicitado, da ação {companie} referente aos últimos 6 meses:

Cotação máxima: {maximum_quote}
Cotação mímima: {minimum_quotation}
Cotação Atual: {current_quote}

Att
Alando Almeida

"""
