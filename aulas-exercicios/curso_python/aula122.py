# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# from os import system

from os import system

tarefas = []
elementos = []
historico_desfazer = []

while True:
    
    user = input("Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ")

    if user == "listar":
        print()
        print("TAREFAS:")
        for tarefa in tarefas:
            print(f"{tarefa}")
        print()
    elif user == "desfazer":
        if tarefas:
            print()
            elemento_apagado = tarefas.pop()
            elementos.append(elemento_apagado)
            historico_desfazer.append(elemento_apagado)
            print("TAREFAS:")
            for tarefa in tarefas:
                print(f"{tarefa}")
            print()
        if not tarefas:
            print()
            print("NADA A DESFAZER")
            print()
    elif user == "refazer":
        if historico_desfazer:
            tarefa_refazer = historico_desfazer.pop()
            tarefas.append(tarefa_refazer)
            print()
            print("TAREFAS:")
            for tarefa in tarefas:
                print(f"{tarefa}")
            print()
    elif user == "clear":
        system('cls')
    else:
        print()
        tarefas.append(user)
        print("TAREFAS:")
        for tarefa in tarefas:
            print(f"{tarefa}")
        print()
