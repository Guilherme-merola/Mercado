from conversor_moeda import conversor_float_str


class Produto():
    contador = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__contador = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def codigo_produto(self: object) -> int:
        return self.__contador
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def preco(self: object) -> float:
        return self.__preco
    
    def __str__(self) -> str:
        descricao = f"""
---------------------------------------
Código: {self.codigo_produto}
Nome: {self.nome}
Preço: {conversor_float_str(self.preco)}
---------------------------------------
        """
        return descricao
    
    def somar_valor(self: object, quantidade: int) -> float:
        return self.preco * quantidade
    