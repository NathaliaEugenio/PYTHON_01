# print('Olá, mundo')

import os

restaurantes=['PythonBurguer','Madalousso','Notubo']

def exibir_nome_do_programa():
    print('𝑆𝑎𝑏𝑜𝑟 𝑒𝑥𝑝𝑟𝑒𝑠𝑠\n')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')
    
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja cadastrar')
    restaurantes.append(nome_do_restaurante)

    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    for restaurante in restaurantes:
        print(restaurante)
        
    voltar_menu_principal
        
def finalizar_app():
    exibir_subtitulo('Finalizar app')
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def escolher_opcao():
    try:
        opcao_escolhida=int(input('Escolha uma opção'))
        
        if opcao_escolhida==1:
            print('Você escolheu cadastrar um restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            print('Você escolheulistar os restaurante')
            listar_restaurantes()
        elif opcao_escolhida==3:
            print('ativar restaurante')
        else:
            opcao_invalida()
    except:
        opcao_invalida
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()