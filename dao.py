from models import Usuario

USUARIO_POR_ID = 'SELECT id, nome, senha from usuarios where id = %s and senha = %s'


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def busca_por_id(self, id, senha):
        cursor = self.__db.connection.cursor()
        cursor.execute(USUARIO_POR_ID, (id, senha))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
