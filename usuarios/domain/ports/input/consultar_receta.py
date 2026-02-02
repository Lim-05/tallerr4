from abc import ABC, abstractmethod

class ConsultarRecetaPort(ABC):

    @abstractmethod
    def consultar(self, receta_id: int):
        pass
