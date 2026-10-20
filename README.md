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
output/             # Resultados generados: Excel, incidencias CSV y log de ejecución
main.py             # Punto de entrada; ejecuta el flujo completo
requirements.txt    # Dependencias del proyecto
```

## Archivos generados

Al ejecutar `python main.py`, los resultados se guardan automáticamente en `output/`:

- `reporte_cfdi.xlsx`: detalle de CFDI procesados y resumen por proveedor.
- `reporte_errores.csv`: incidencias encontradas (por ejemplo, XML dañados, archivos faltantes o UUID duplicados). Se genera incluso si no hay incidencias.
- `ejecucion.log`: registro de cada ejecución; incluye el inicio, las incidencias y el resultado final. Se conserva y añade al final en ejecuciones posteriores.

Para consultarlos, abre la carpeta `output/` en el explorador de archivos o abre el CSV y el log con un editor de texto o una hoja de cálculo.

## Uso de herramientas de IA

Usé Claude Code (Anthropic) como apoyo en dos aspectos:

- **Configuración del entorno de trabajo:** creación del entorno virtual, instalación de
  dependencias, `requirements.txt`, `.gitignore` e inicialización del repositorio.
- **Consultoría:** como guía para resolver dudas y consultar documentación (lectura de XML
  con namespaces, pandas, openpyxl, logging).
- **Documentación:** apoyo en la redacción de este README y de la documentación del proyecto.

El código de la solución lo escribí yo, y puedo explicar cada parte.
