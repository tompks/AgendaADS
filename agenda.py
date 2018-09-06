#Agenda Telefonica
import funcoes

menu = funcoes.bemvindo()

while(menu != "0"):
    if menu == "1":
        funcoes.novocontato()
        menu = funcoes.bemvindo()
    elif menu == "2":
        funcoes.remover()
        menu = funcoes.bemvindo()
    elif menu == "3":
        funcoes.buscar()
        menu = funcoes.bemvindo()
    elif menu == "4":
        funcoes.listar()
        menu = funcoes.bemvindo()
    else:
        funcoes.falha()
        menu = funcoes.bemvindo()
        
print("Obrigado por utilizar nosso sistema!")

exit()
