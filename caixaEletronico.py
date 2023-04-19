import PySimpleGUI as sg

sg.theme('Reddit')

def janela_inicial():
    layout = [
        [sg.Text('CAIXA ELETRONICO')],
        [sg.Text('Valor do Saque: '), sg.Input(key='valor_saque', size=(8, 1))],
        [sg.Text(key='aviso')],
        [sg.Button('Confirma'), sg.Button('Fechar')]
    ]
    return sg.Window('CAIXA', layout, finalize=True)

def janela_saque():
    layout = [
        [sg.Text('SAQUE')],
        [sg.Text(key='aviso_sacado')],
        [sg.Text('Notas de R$1,00: '), sg.Text(key='notas1')],
        [sg.Text('Notas de R$5,00: '), sg.Text(key='notas5')],
        [sg.Text('Notas de R$10,00: '), sg.Text(key='notas10')],
        [sg.Text('Notas de R$50,00: '), sg.Text(key='notas50')],
        [sg.Text('Notas de R$100,00: '), sg.Text(key='notas100')],
        [sg.Text(key='aviso')],
        [sg.Button('Saque'),sg.Button('Verificar valor de Saque') ,sg.Button('Voltar')]
    ]
    return sg.Window('CAIXA', layout, finalize=True)


janela1, janela2 = janela_inicial(), None

while True:
    janela, eventos, valores = sg.read_all_windows()

    def converter_notas_centenas(valor):
        centenas = valor // 100
        valor %= 100
        return centenas, valor
    def converter_notas_50(valor):
        notas50 = valor // 50
        valor %= 50
        return notas50, valor
    
    def converter_notas_dez(valor):
        dezenas = valor // 10
        valor %= 10
        return dezenas, valor
    
    def converter_notas_5(valor):
        notas5 = valor // 5
        valor %= 5
        return notas5, valor
    
    def converter_notas_unidades(valor):
        unidades = valor // 1
        return unidades
    
    if janela == janela1 and eventos == sg.WIN_CLOSED or eventos == 'Fechar' :
        break

    if janela == janela1 and eventos == 'Confirma' :
        valor_saque = int(valores['valor_saque'])

        if valor_saque < 10 or valor_saque > 600:
            janela1['aviso'].Update('Valor de saque não disponivel.\nApenas valores com no minimo R$10 e no maximo E$600 sao permitidos.')
        else:
            janela1.hide()
            janela2 = janela_saque()

    if janela == janela2 :
       janela2['aviso_sacado'].Update(f'Valor a ser sacado: {valor_saque}')
       
       if eventos == 'Saque' :
            notas100, valor_saque = converter_notas_centenas(valor_saque)
            notas50, valor_saque = converter_notas_50(valor_saque)
            notas10, valor_saque = converter_notas_dez(valor_saque)
            notas5, valor_saque = converter_notas_5(valor_saque)
            notas1 = converter_notas_unidades(valor_saque)

            janela2['notas1'].Update(f'{notas1}')
            janela2['notas5'].Update(f'{notas5}')
            janela2['notas10'].Update(f'{notas10}')
            janela2['notas50'].Update(f'{notas50}')
            janela2['notas100'].Update(f'{notas100}')
            janela2['aviso'].Update('Saque efetuado com sucesso!!')
       
    if janela == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()