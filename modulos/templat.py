from dataclasses import dataclass, field

@dataclass
class Templat:
    name: str
    mensagens: list = field(default_factory=list)
    







# class Templat:
#     def __init__(self, name:str, mensagens: list = []) -> None:
#         self.mensagens: list = field(default_factory=list)
#         self.name = name
        # self.mensagens = mensagens

    # def addMensage(self, msg:str):
    #     self.mensagens.append(msg)