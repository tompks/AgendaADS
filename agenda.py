#Agenda Telefonica
import funcoes

menu = ""
menu = funcoes.bemvindo(menu)

while(menu != "0"):
    if menu == "1":
        funcoes.adicionar()
        menu = funcoes.bemvindo(menu)
    elif menu == "2":
        funcoes.remover()
        menu = funcoes.bemvindo(menu)
    elif menu == "3":
        funcoes.buscar()
        menu = funcoes.bemvindo(menu)
    elif menu == "4":
        funcoes.listar()
        menu = funcoes.bemvindo(menu)
    else:
        funcoes.falha()
        input("Pressione Enter para continuar...")
        menu = funcoes.bemvindo(menu)
print("Obrigado por utilizar nosso sistema!")
exit()
