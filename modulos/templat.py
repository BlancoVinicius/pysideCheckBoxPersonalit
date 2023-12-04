
class Templat():
    def __init__(self, name:str, mensagens: list = []) -> None:
        self.name = name
        self.mensagens = mensagens

    def addMensage(self, msg:str):
        self.mensagens.append(msg)