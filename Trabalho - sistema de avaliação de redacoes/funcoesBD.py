import mysql.connector

def inserirUsuario(nome,senha):
    con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
    comando = '''INSERT INTO usuario 
    (NOME, SENHA) 
    VALUES 
    ('{}', '{}')'''.format(nome,senha)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    cursor.close()
    con.close()   

def retornarUsuario(nome):
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
        comando = "SELECT * FROM db_redacoes.usuario WHERE NOME = '{}'".format(nome)
        cursor = con.cursor()
        cursor.execute(comando)
        return cursor.fetchone()
    except:
        return 0

def atualizarSenha(userName, newSenha):
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
        comando = "UPDATE usuario SET SENHA = '{}' WHERE NOME = '{}'".format(newSenha, userName)
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        return 1
    except:
        return 0

def inserirRedacao(idUser, data, tema, texto):
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
        comando = '''INSERT INTO redacao 
        (idUSUARIO, DATA, TEMA, TEXTO) 
        VALUES 
        ('{}', '{}', '{}', '{}')'''.format(idUser, data, tema, texto)
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        return 1
    except:
        return 0


def retornarRedacoesEComents(userId, modo):
    if modo == 'TEMA':
        ordem = ''
    else:
        ordem = 'DESC'
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
        comando = f'''SELECT idREDACAO, TEMA, TEXTO, DATA FROM db_redacoes.redacao, db_redacoes.usuario 
                      WHERE redacao.idUSUARIO = usuario.idUSUARIO and usuario.idUSUARIO = '{userId}' ORDER BY {modo} {ordem};'''
        cursor = con.cursor()
        cursor.execute(comando)
        redacoes = cursor.fetchall()
        comando = f'''SELECT redacao.idREDACAO, ASSUNTO, comentario.TEXTO, comentario.DATA, comentario.HORA FROM db_redacoes.comentario, db_redacoes.redacao, db_redacoes.usuario 
                      WHERE redacao.idREDACAO = comentario.idREDACAO AND redacao.idUSUARIO = usuario.idUSUARIO 
                      AND redacao.idUSUARIO = '{userId}' ORDER BY redacao.idREDACAO AND comentario.DATA AND comentario.HORA;'''
        cursor.execute(comando)
        comentarios = cursor.fetchall()
        return redacoes, comentarios
    except:
        return 0

def retornarRedacoes(userId):

    con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
    comando = f'''SELECT idREDACAO, TEMA, NOME, TEXTO FROM db_redacoes.redacao, db_redacoes.usuario 
                  WHERE redacao.idUSUARIO = usuario.idUSUARIO AND NOT(usuario.idUSUARIO = '{userId}') 
                  ORDER BY DATA;'''
    cursor = con.cursor()
    cursor.execute(comando)
    return cursor.fetchall()

def enviarComentario(redId, userId, assunto, texto, data, hora):
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_redacoes', user = 'root', password = 'jean6032')
        comando = f'''INSERT INTO comentario (idREDACAO, idUSUARIO, ASSUNTO, TEXTO, DATA, HORA)
                    VALUES ('{redId}', '{userId}', '{assunto}', '{texto}', '{data}', '{hora}');'''
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        cursor.close()
        con.close()
        return 1
    except:
        return 0

if __name__ == '__main__':
    # id = inserirUsuario('jonas', 'csk98u9')
    # print(retornarUsuario('jean'))
    # print(atualizarSenha('jean','senhajean1'))
    # text = '''Oi
    # Bom dia, queria lhe dizer o meu seguinte texto: (...).'''
    # print(inserirRedacao('1', '2020-01-01', 'Globalização',text))
    '''for x in retornarRedacoes('2'):
        print(x)

    for x in retornaRedacoesNoComents('2'):
        print(x)'''
    
    print(enviarComentario('3', '1', 'Bom dia!', 'Bom dia. Gostei da sua redação!', '2021-10-30', '22:16'))