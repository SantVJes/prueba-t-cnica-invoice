# Automatización de revisión de CFDI

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Estructura del proyecto

```
cfdis/              # Archivos XML de entrada (CFDI)
src/                # Código fuente de la solución, organizado en módulos
output/             # Resultados generados: Excel y log de incidencias
main.py             # Punto de entrada; ejecuta el flujo completo
requirements.txt    # Dependencias del proyecto
```

## Decisiones técnicas

_Pendiente._

## Uso de herramientas de IA

Usé Claude Code (Anthropic) como apoyo en dos aspectos:

- **Configuración del entorno de trabajo:** creación del entorno virtual, instalación de
  dependencias, `requirements.txt`, `.gitignore` e inicialización del repositorio.
- **Consultoría:** como guía para resolver dudas y consultar documentación (lectura de XML
  con namespaces, pandas, openpyxl, logging).
- **Documentación:** apoyo en la redacción de este README y de la documentación del proyecto.

El código de la solución lo escribí yo, y puedo explicar cada parte.
