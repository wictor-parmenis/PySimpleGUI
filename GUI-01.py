import PySimpleGUI as sg

def home():
    sg.theme('Black')
    flayout = [
        [sg.Text('Selecione um colégio e entenda mais sobre ele ')],
        [sg.Button('Colégio Lions Parnamirim'), sg.Button('Colégio Porto Digital')],
        [sg.Text('')],
        [sg.Button('Sair')]
    ]

    janela1 = sg.Window('Situação digital dos Colégios Lions e Porto Digital', flayout, size=(400,200), element_justification='center')
    button, values = janela1.read()

    if button == 'Colégio Lions Parnamirim':
        janela1.close()
        layout = [
            [sg.Text(
                'O colégio Lions, é um colégio localizado em: xxx, e de acordo com os dados do xxx, possui um nota de xxx\n'
                'no IDEB. Atualmente, devido a esse momento de pandemia, o colégio vem prestando o seu serviço de educação \n'
                'por meio de aulas online, via internet ou Televisão no canal xxx. Entretanto, apesar disso, nota-se que:\n'
                'A presença online da escola não é muito forte em suas redes sociais.\n O que é algo preocupante, afinal,'
                'Hoje em dia, as redes sociais são as maiores fontes de divulgação que existem hoje em dia.\n'
                'Consequentemente, devido a essa postura digital do colégio supôe-se que, muitos alunos, sentem-se perdidos\n'
                'em relação as suas aulas ou o seu cronograma de estudos.\n'
                'Para resolver isso, é importante que o colégio, contrate algum profissional para gerenciar as suas redes sociais\n'
                'Ou, se for mais cômodo, fornecer uma bolsa para algum aluno do 3º ano do ensino médio, fazer essas atividades.')],
            [sg.Button('Redes Sociais', key='redes1'), sg.Button('Home', key='home')]
        ]

        janela2 = sg.Window('Situação digital do colégio Lions', layout, size=(400, 400),
                            element_justification='center')
        button, values = janela2.read()

        while True:
            if button == 'home':
                janela2.close()
                home()
            if button == 'redes1':
                janela2.close()
                layout2 = [
                    [sg.Text('Instagram: @escola_lions\nFacebook: Escola Estadual Lions De Parnamirim\nE-mail: escolalionsdeparnamirim@gmail.com \n')],
                    [sg.Button('Home', key='home1'), sg.Button('Back')]
                ]

                janela3 = sg.Window('Redes Sociais do colégio Lions', layout2, size= (400,300), element_justification='center')
                button, values = janela3.read()

                if button == 'home1':
                    janela3.close()
                    home()
                if button == 'Back':
                    exit()
    if button == 'Colégio Porto Digital':
        janela1.close()
        layout = [
            [sg.Text(
                'O colégio Porto Digital, é um colégio localizado em: xxx, e de acordo com os dados do xxx, possui um nota de xxx\n'
                'no IDEB. Atualmente, devido a esse momento de pandemia, o colégio vem prestando o seu serviço de educação \n'
                'por meio de aulas online, via internet ou Televisão no canal xxx. Entretanto, apesar disso, nota-se que:\n'
                'A presença online da escola não é muito forte em suas redes sociais.\n O que é algo preocupante, afinal,'
                'Hoje em dia, as redes sociais são as maiores fontes de divulgação que existem hoje em dia.\n'
                'Consequentemente, devido a essa postura digital do colégio supôe-se que, muitos alunos, sentem-se perdidos\n'
                'em relação as suas aulas ou o seu cronograma de estudos.\n'
                'Para resolver isso, é importante que o colégio, contrate algum profissional para gerenciar as suas redes sociais\n'
                'Ou, se for mais cômodo, fornecer uma bolsa para algum aluno do 3º ano do ensino médio, fazer essas atividades.')],
            [sg.Button('Redes Sociais', key='redes2'), sg.Button('Home', key='home')]
        ]

        janela2 = sg.Window('Situação digital do colégio Porto Digital', layout, size=(400, 400),
                            element_justification='center')
        button, values = janela2.read()
        while True:
            if button == 'home':
                janela2.close()
                home()
            if button == 'redes2':
                janela2.close()
                layout3 = [
                    [sg.Text('Instagram: @eteportodigital\nYoutube: ETE PORTO DIGITAL\nFacebook: ETE Porto Digital\nE-mail: eteportodigital@gmail.com\n')],
                    [sg.Button('Home', key='home2'), sg.Button('Back')]
                ]

                janela3 = sg.Window('Redes Sociais do colégio Porto Digital', layout3, size=(400, 300),
                                    element_justification='center')
                button, values = janela3.read()

                if button == 'home2':
                    janela3.close()
                    home()
                if button == 'Back':
                    exit()

    if button == 'Sair':
        exit()

home()
