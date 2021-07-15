class Usuario():
    def __init__(self, id, name, password):
        self._id = id
        self._name = name
        self._password = password
        self._redacoes = []

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getPassword(self):
        return self._password

    def setId(self, newId):
        self._id = newId

    def setName(self, newName):
        self._name = newName

    def setPassword(self, newPassword):
        self._password = newPassword

    def InserirRedacao(self, redacao):
        self._redacoes.append(redacao)


