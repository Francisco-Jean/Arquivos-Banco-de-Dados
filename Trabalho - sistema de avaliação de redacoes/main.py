from Usuario import Usuario
from tkinter import *
from tkinter import messagebox
import funcoesBD
from tkinter import ttk
from datetime import date, datetime

class App:
    def __init__(self, master = None):
        self.cor = '#00a39e'
        self.master = master
        self.master.geometry('400x700+30+30')
        self.master['bg'] = self.cor
        self.frame0 = Frame()
        self.frame0.pack()
        self.masternote = ttk.Notebook(self.frame0, height = '100000', width = '100000')
        self.masternote.pack()
        self.fonte = 'Cooper Black'
        self.config = (self.fonte, '15')
        self.config2 = (self.fonte, '25')
        self.corfg = 'white'

        # JANELA DE ACESSO AO USUARIO
        self.frame1 = Frame(self.masternote, bg = self.cor)
        self.frame1.pack()
        self.masternote.add(self.frame1, text = 'Entrar')

        Label(self.frame1, text = 'FREE REDAÇÕES', bg = self.cor, font = (self.fonte, '25', 'bold'), fg = self.corfg).pack(pady = (100,20))
        Label(self.frame1, text = 'Digite seu nome:', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = (10,5))
        self.enterName = Entry(self.frame1)
        self.enterName.pack(pady = (0,20))
        Label(self.frame1, text = 'Digite sua senha:', bg = self.cor, font = self.config, fg = self.corfg).pack()
        self.enterPass = Entry(self.frame1, show = '*')
        self.enterPass.pack(pady = (0,5))
        self.enterButton = Button(self.frame1, font = self.config, text = 'Entrar', command = self.acessarUsuario)
        self.enterButton.pack(pady = 20)

        # JANELA DE CADASTRO DE USUARIO
        self.frame2 = Frame(self.masternote, bg = self.cor, width = '1200')
        self.frame2.pack()
        self.masternote.add(self.frame2, text = 'Cadastrar-se')

        Label(self.frame2, text = 'FREE REDAÇÕES', bg = self.cor, font = (self.fonte, '25', 'bold'), fg = self.corfg).pack(pady = (100,20))
        Label(self.frame2, text = 'Digite seu nome:', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = (10,5))
        self.subName = Entry(self.frame2)
        self.subName.pack()
        Label(self.frame2, text = 'Digite sua senha:', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = (20,0))
        self.subPass = Entry(self.frame2, show = '*')
        self.subPass.pack()
        Label(self.frame2, text = 'Repita sua senha:', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = (20,0))
        self.subPass2 = Entry(self.frame2, show = '*')
        self.subPass2.pack()
        self.subButton = Button(self.frame2, font = self.config, text = 'Cadastrar', command = self.criarUsuario)
        self.subButton.pack(pady = 25)
    
    # FUNÇÃO PARA VALIDAR O ACESSO
    def acessarUsuario(self):
        if not (self.enterName.get() and self.enterPass.get()):
            messagebox.showerror('Dados imcompletos', 'Você não inseriu todos os dados requeridos. Insira-os e tente novamente')
        else:
            dados = funcoesBD.retornarUsuario(self.enterName.get())
            if dados:
                if dados[2] != self.enterPass.get():
                    messagebox.showerror('Senha incorreta', 'A senha inserida não está correta. Por favor, corrija e tente novamente.')
                else:
                    self.homePage(dados)
            else:
                messagebox.showinfo('Usuário inválido', f'O usuário {self.enterName.get()} não foi encontrado em nosso sistema. Entre com o usuário corretamente ou acesse a área de cadastro.')


    # FUNÇÃO PARA VALIDAR O CADASTRO
    def criarUsuario(self):
        if not (self.subName.get() and self.subPass.get() and self.subPass2.get()):
            messagebox.showerror('Dados imcompletos', 'Você não inseriu todos os dados requeridos. Insira-os e tente novamente')
        elif self.subPass.get() != self.subPass2.get():
            messagebox.showerror('Senha não confere', 'As entradas de senha não conferem. Insira-as corretamente e tente novamente!')
        elif len(self.subPass.get()) < 4:
            messagebox.showerror('Senha curta', 'Sua senha deve ter no mínimo 4 caracteres. Corrija e tente novamente!')
        elif ' ' in self.subPass.get():
            messagebox.showerror('Espaços são proibidos', 'Sua senha não pode conter espaços em branco. Corrija e tente novamente!')
        else:
            try:
                funcoesBD.inserirUsuario(self.subName.get(), self.subPass.get())
                messagebox.showinfo('Cadastro concluido', 'Oba! Seu cadastro foi concluído com sucesso. Entre na área de login e acesse a sua Homepage')
            except:
                messagebox.showinfo('Usuario já cadastrado', f'O usuário {self.subName.get()} já existe no nosso sistema. Por favor, digite outro nome e tente novamente!')
    
    # FUÇÃO DE ACESSO À PÁGINA INICIAL
    def homePage(self,dados):
        self.master.geometry('1300x700+10+10')
        self.user = Usuario(dados[0], dados[1], dados[2])

        self.frame0.forget()
        self.frameHome = Frame(self.master, bg = self.cor)
        self.frameHome.pack()

        opcoes = ttk.Notebook(self.frameHome, height = '100000', width = '100000')
        opcoes.pack()

        frameUser = Frame(opcoes, bg = self.cor)
        frameUser.pack()
        frameEscrever = Frame(opcoes, bg = self.cor)
        frameEscrever.pack()
        self.frameVizualizar = Frame(opcoes, bg = self.cor)
        self.frameVizualizar.pack()
        self.frameComentar = Frame(opcoes, bg = self.cor)
        self.frameComentar.pack()

        opcoes.add(frameUser, text = 'Conta do Usuário')
        opcoes.add(frameEscrever, text = 'Escrever redação')
        opcoes.add(self.frameVizualizar, text = 'Redações')
        opcoes.add(self.frameComentar, text = 'Área de Comentários')
        
        # ABA INICIAL
        Label(frameUser, fg = self.corfg, text = 'Usuário:', bg = self.cor, font = self.config).pack(pady = 20)
        Label(frameUser, text = f'{self.user.getName()}', bg = self.cor, font = (self.fonte, '20')).pack(pady = (0,20))

        Label(frameUser, text = '+―――――――――――――――――――――――――――――――――――――――――――――――――――――――+', bg = self.cor).pack(pady = 10)

        Label(frameUser, text = 'Atualizar Senha', bg = self.cor, font = self.config2).pack(pady = (0,20))
        Label(frameUser, text = 'Digite a senha antiga:', bg = self.cor, font = self.config).pack(pady = (0,5))
        self.updatePass = Entry(frameUser, show = '*')
        self.updatePass.pack()
        Label(frameUser, text = 'Digite a senha nova:', bg = self.cor, font = self.config).pack(pady = (15,5))
        self.updatePass1 = Entry(frameUser, show = '*')
        self.updatePass1.pack()
        Label(frameUser, text = 'Repita a senha nova:', bg = self.cor, font = self.config).pack(pady = (15,5))
        self.updatePass2 = Entry(frameUser, show = '*')
        self.updatePass2.pack()
        self.updateButton = Button(frameUser, text = 'Atualizar', command = self.atualizarSenha, font = self.config)
        self.updateButton.pack(pady = 20)

        # ABA DE ESCRITA DAS REDAÇÕES
        Label(frameEscrever, text = 'Escreva sua redação!', bg = self.cor, font = self.config2, fg = self.corfg).pack(pady = 20)
        Label(frameEscrever, text = 'Tema da redação:', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = (0,5))
        self.redacaoTema = Entry(frameEscrever, width = 100)
        self.redacaoTema.pack()
        self.redacaoTexto = Text(frameEscrever, width = 100)
        self.redacaoTexto.pack(pady = (10,20))
        self.redacaoSalvar = Button(frameEscrever, text = 'Salvar', command = self.enviarRedacao, font = self.config)
        self.redacaoSalvar.pack()

        # ABA DE VIZUALIZAÇÃO DAS REDAÇÕES
        modos = ['DATA', 'TEMA']
        Label(self.frameVizualizar, text = 'Minhas redações', bg = self.cor, font = self.config2, fg = self.corfg).pack(pady = 20)
        frameSelect = Frame(self.frameVizualizar, bg = self.cor)
        frameSelect.pack(padx = (0,300))
        Label(frameSelect, text = 'Ordenar por:   ', bg = self.cor).pack(side = LEFT)
        self.modo_vizualizar = ttk.Combobox(frameSelect, values = modos, background = self.cor)
        self.modo_vizualizar.pack(side = LEFT)
        self.modo_vizualizar.set('DATA')
        self.modo_vizualizar.bind('<<ComboboxSelected>>', self.mostrarRedacoesEComents)
        

        # FRAME DE LISTAGEM DAS REDAÇÕES
        self.listRedacoes = Frame(self.frameVizualizar, bg = self.cor)
        self.listRedacoes.pack(fill = BOTH, expand = 1)

        self.frameVizualizarCanv = Canvas(self.listRedacoes, bg = self.cor)
        self.frameVizualizarCanv.pack(side = LEFT, fill = BOTH, expand = 1, padx = 100)

        scrollRedacoes = ttk.Scrollbar(self.listRedacoes, orient = 'vertical', command = self.frameVizualizarCanv.yview)
        scrollRedacoes.pack(side = RIGHT, fill = 'y')

        self.frameVizualizarCanv.configure(yscrollcommand = scrollRedacoes.set)
        self.frameVizualizarCanv.bind('<Configure>', lambda e: self.frameVizualizarCanv.configure(scrollregion = self.frameVizualizarCanv.bbox('all'))) 

        self.mostrarRedFrame = Frame(self.frameVizualizarCanv, bg = self.cor)
        self.frameVizualizarCanv.create_window((0,0), window = self.mostrarRedFrame, anchor = 'nw')

        self.mostrarRedacoesEComents('<<ComboboxSelected>>')

        # ABA PARA ESCREVER COMENTÁRIOS
        modos = ['DATA', 'TEMA']
        Label(self.frameComentar, text = 'Comentar redações', bg = self.cor, font = self.config2, fg = self.corfg).pack(pady = 20)
        frameSelectC = Frame(self.frameComentar, bg = self.cor)
        frameSelectC.pack(padx = (0,300))
        Label(self.frameComentar, text = 'Para comentar uma redação, clique nela.', bg = self.cor, font = self.config, fg = self.corfg).pack(pady = 10)
        updateReds = Button(self.frameComentar, text = 'Atualizar redações', command = self.mostrarRedacoes, font = self.config)
        updateReds.pack(pady = 20)

        # FRAME DE LISTAGEM DAS REDAÇÕES PARA COMENTAR
        self.listRedacoesC = Frame(self.frameComentar, bg = self.cor)
        self.listRedacoesC.pack(fill = BOTH, expand = 1)

        self.frameComentarCanvC = Canvas(self.listRedacoesC, bg = self.cor)
        self.frameComentarCanvC.pack(side = LEFT, fill = BOTH, expand = 1, padx = 100)

        scrollRedacoesC = ttk.Scrollbar(self.listRedacoesC, orient = 'vertical', command = self.frameComentarCanvC.yview)
        scrollRedacoesC.pack(side = RIGHT, fill = 'y')

        self.frameComentarCanvC.configure(yscrollcommand = scrollRedacoesC.set)
        self.frameComentarCanvC.bind('<Configure>', lambda e: self.frameComentarCanvC.configure(scrollregion = self.frameComentarCanvC.bbox('all'))) 

        self.mostrarRedFrameC = Frame(self.frameComentarCanvC, bg = self.cor)
        self.frameComentarCanvC.create_window((0,0), window = self.mostrarRedFrameC, anchor = 'nw')

        self.mostrarRedacoes()

    def enviarRedacao(self):
        
        if not(self.redacaoTema.get() and self.redacaoTexto.get('1.0',END)):
            messagebox.showerror('Dados imcompletos', 'Você deve inserir o tema e o texto da sua redação. Por favor, preencha ambos e tente novamente.')
        else:
            result = funcoesBD.inserirRedacao(self.user.getId(), date.today(), self.redacaoTema.get(), self.redacaoTexto.get('1.0', END))
            if result:
                messagebox.showinfo('Sua redação foi salva', 'Oba! Sua redação foi salva com sucesso. Você pode acessar suas redações na aba \'Redações\'')

    def atualizarSenha(self):
        if not (self.updatePass.get() and self.updatePass1.get() and self.updatePass2.get()):
            messagebox.showerror('Dados imcompletos', 'Você não inseriu todos os dados requeridos. Insira-os e tente novamente')
        elif self.updatePass1.get() != self.updatePass2.get():
            messagebox.showerror('Senha não confere', 'Os cambos de nova senha não conferem.  Insira-os corretamente e tente novamente!')
        elif self.updatePass.get() != self.user.getPassword():
            messagebox.showerror('Senha antiga incorreta', 'Você digitou sua senha antiga incorretamente. Por favor, corrija-a e tente novamente.')
        else:
            result = funcoesBD.atualizarSenha(self.user.getName(), self.updatePass1.get())
            if result:
                messagebox.showinfo('Senha atualizada', 'Sua senha foi atualizada com sucesso. Lembre que seu próximo acesso deverá ser com a nova senha, OK?')
            else:
                messagebox.showerror('Senha não atualizada', 'Sua senha não pôde ser atualizada. Por favor, tente novamente mais tarde.')

    def mostrarRedacoes(self):
        janelas2 = self.mostrarRedFrameC.pack_slaves()

        for r in janelas2:
            r.destroy()

        redacoes = funcoesBD.retornarRedacoes(self.user.getId())

        for x in redacoes:
            texto = Text(self.mostrarRedFrameC, width = 100)
            texto.pack(padx = (180,300), pady = (20,5))
            texto.insert(END, f'Tema: {x[1]}\n\n{x[3]}\n\nAutor: {x[2]}')
            comentar = Button(self.mostrarRedFrameC, text = 'Comentar')
            comentar.pack(padx = (0,120), pady = 20)
            comentar.configure(command = lambda i = x[0]: self.enviarComentario(i))

    def mostrarRedacoesEComents(self, event):
        janelas = self.mostrarRedFrame.pack_slaves()

        for r in janelas:
            r.destroy()

        redacoes, comentarios = funcoesBD.retornarRedacoesEComents(self.user.getId(), self.modo_vizualizar.get())

        for x in redacoes:
            texto = Text(self.mostrarRedFrame, width = 100)
            texto.pack(padx = (180,300), pady = 10)
            data = str(x[3]).split('-')
            texto.insert(END, 'Tema: {}\n\n{}\n\n{:<}'.format(x[1], x[2], f'Data: {data[2]}/{data[1]}/{data[0]}\n\n\n\n'))
            texto.insert(END, '{:^100s}'.format('+――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――+'))
            texto.insert(END, '{:^100s}'.format('Comentários:'))
            for y in comentarios:
                if x[0] == y[0]:
                    data = str(y[3]).split('-')
                    texto.insert(END, f'\n\n\nAssunto: {y[1]} \n\n{y[2]} \n\nData: {data[2]}/{data[1]}/{data[0]} {y[3]}  {y[4]}\n\n')
                    texto.insert(END, '{:^100s}'.format('----------------------------------------------------------------------------------------'))

    def enviarComentario(self, idRedacao):
        self.coment = Tk()
        self.coment.title('Enviar comentário')
        self.coment.geometry('400x600')
        Label(self.coment, text = 'Assunto:', font = self.config).pack(pady = 5)
        self.assunto = Entry(self.coment)
        self.assunto.pack()
        Label(self.coment, text = 'Texto:', font = self.config).pack(pady = (10,5))
        self.comentText = Text(self.coment, width = 30, height = 18)
        self.comentText.pack()
        Button(self.coment, text = 'Enviar', command = lambda: enviar(idRedacao), font = self.config).pack()
        def enviar(idRed):
            result = funcoesBD.enviarComentario(idRedacao, self.user.getId(), self.assunto.get(), self.comentText.get('1.0', END), date.today(), datetime.now().strftime('%H:%M'))
            if result:
                messagebox.showinfo('Comentário enviado', 'Seu comentário foi enviado com sucesso! Apenas o remetente poderá vizualiza-lo.')
                self.coment.destroy()
            else:
                messagebox.showerror('Comentário não enviado', 'Seu comentário não pôde ser enviado. Por favor, tente novamente mais tarde.')

if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()
