import logging
import xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

# namespaces que vienen en el xml
ns = {
    "cfdi": "http://www.sat.gob.mx/cfd/4",
    "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital",
}

columnas = ["Archivo", "UUID", "RFC Emisor", "Nombre Emisor", "Fecha", "Subtotal", "IVA trasladado", "Total"]


def leer_xml(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    # si el tag no es el del comprobante no es un cfdi
    if root.tag != "{http://www.sat.gob.mx/cfd/4}Comprobante":
        raise ValueError("no es cfdi, tag: " + root.tag)

    emisor = root.find("cfdi:Emisor", ns)
    impuestos = root.find("cfdi:Impuestos", ns)
    timbre = root.find("cfdi:Complemento/tfd:TimbreFiscalDigital", ns)

    # guardamos todos en un diccionario para despues pasarlo a un dataframe 
    datos = {
        "Archivo": ruta.name,
        "UUID": timbre.get("UUID"),
        "RFC Emisor": emisor.get("Rfc"),
        "Nombre Emisor": emisor.get("Nombre"),
        "Fecha": root.get("Fecha"),
        "Subtotal": float(root.get("SubTotal")),
        "IVA trasladado": float(impuestos.get("TotalImpuestosTrasladados")),
        "Total": float(root.get("Total")),
    }
    return datos


def leer_carpeta(carpeta):
    facturas = []
    errores = []

    # revisamos los 20 archivos esperados
    for i in range(1, 21):
        ruta = Path(carpeta) / f"factura_{i:02d}.xml"

        if not ruta.exists():

            mensaje = "no existe el archivo"
            errores.append([ruta.name, mensaje])

            # registramos en el log los archivos que no se encontraron
            logger.warning("%s: %s", ruta.name, mensaje)
            continue

        try:

            facturas.append(leer_xml(ruta))

        except ET.ParseError as e:

            mensaje = "xml dañado: " + str(e)
            errores.append([ruta.name, mensaje])
            # registramos en el log los errores de lectura del XML
            logger.warning("%s: %s", ruta.name, mensaje)

        except Exception as e:
            mensaje = "error: " + str(e)

            errores.append([ruta.name, mensaje])
            
            # registramos otros errores sin detener la lectura
            logger.warning("%s: %s", ruta.name, mensaje)


    # reunimos las facturas válidas en una tabla
    df = pd.DataFrame(facturas, columns=columnas)
    return df, errores
