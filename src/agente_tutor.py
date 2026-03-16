"""
SkillAgent - Agente Tutor de AI para PyMEs
"""
from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """Eres SkillAgent, el tutor de inteligencia artificial para empleados de PyMEs mexicanas.

Tu misión: hacer que cualquier empleado, sin importar su nivel técnico, pueda usar herramientas de AI en su trabajo diario.

Principios:
- Explica siempre con ejemplos del contexto mexicano y de PyMEs
- Usa lenguaje sencillo, sin anglicismos innecesarios
- Da ejercicios prácticos que se puedan hacer hoy mismo
- Celebra los logros del aprendiz
- Adapta tu ritmo al nivel del estudiante

Cuando el usuario complete un módulo, genera un resumen de lo aprendido y sugiere el siguiente paso."""

class AgenteSkill:
    def __init__(self, nombre_empleado: str, empresa: str, rol: str):
        self.nombre = nombre_empleado
        self.empresa = empresa
        self.rol = rol
        self.historial = []
        
    def enseñar(self, mensaje_usuario: str) -> str:
        self.historial.append({"role": "user", "content": mensaje_usuario})
        
        contexto = f"Estás enseñando a {self.nombre}, que trabaja como {self.rol} en {self.empresa}."
        
        respuesta = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=SYSTEM_PROMPT + f"\n\nContexto del estudiante: {contexto}",
            messages=self.historial
        )
        
        respuesta_texto = respuesta.content[0].text
        self.historial.append({"role": "assistant", "content": respuesta_texto})
        return respuesta_texto

if __name__ == "__main__":
    agente = AgenteSkill("María García", "Distribuidora León SA", "Administradora")
    print(agente.enseñar("Hola, quiero aprender a usar inteligencia artificial en mi trabajo"))
