from pacientes.domain.models.receta_model import Receta
from pacientes.domain.ports.input.consultar_receta import ConsultarRecetaPort

class ConsultarRecetaUseCase(ConsultarRecetaPort):

    def consultar(self, receta_id: int):
        receta = Receta(
            id=receta_id,
            equipo_base=[
                "Cuchillo",
                "Cazuela",
                "Tabla de cortar"
            ]
        )

        return {
            "mensaje": f"Cosultando receta {receta.id}",
            "equipo_base": receta.equipo_base
        }
