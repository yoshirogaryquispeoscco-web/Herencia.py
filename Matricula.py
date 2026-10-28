
class Matricula:
    
    def calcular_monto(self) -> float:
        pass

class MatriculaBase(Matricula):
    
    def calcular_monto(self) -> float:
        return 60.00

class ModificadorMatricula(Matricula):
   
    def __init__(self, matricula_envuelta: Matricula):
        self.matricula_envuelta = matricula_envuelta
        
    def calcular_monto(self) -> float:
        return self.matricula_envuelta.calcular_monto()

class RecargoExtemporaneo(ModificadorMatricula):
    def calcular_monto(self) -> float:
        return self.matricula_envuelta.calcular_monto() + 15.00

class RecargoDesaprobatorio(ModificadorMatricula):
    def calcular_monto(self) -> float:
        return self.matricula_envuelta.calcular_monto() + 15.00

class DescuentoBeca(ModificadorMatricula):
    def calcular_monto(self) -> float:
        return self.matricula_envuelta.calcular_monto() / 2

# --- Simulación de los casos ---

# 1. Caso del primer estudiante (Beca aplicada al final)
# Base (60) + Extemporáneo (15) + Desaprobatorio (15) = 90 -> Beca (mitad) = 45
estudiante_1 = DescuentoBeca(RecargoDesaprobatorio( RecargoExtemporaneo( MatriculaBase())))
print(f"Monto Estudiante 1 (Beca al final): S/ {estudiante_1.calcular_monto():.2f}")

# 2. Caso del segundo estudiante (Beca aplicada al principio)
# Base (60) -> Beca (mitad) = 30 + Extemporáneo (15) + Desaprobatorio (15) = 60
estudiante_2 = RecargoDesaprobatorio(RecargoExtemporaneo( DescuentoBeca(MatriculaBase())))
print(f"Monto Estudiante 2 (Beca al inicio): S/ {estudiante_2.calcular_monto():.2f}")
