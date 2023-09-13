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
        
# CÓDIGO VERSÃO DA AULA

'''import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue'''
