from logging import root
import xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd

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

    for i in range(1, 21):
        ruta = Path(carpeta) / f"factura_{i:02d}.xml"

        #saber si el archivo existe, si no existe se agrega a la lista de errores y se continua con el siguiente
        if not ruta.exists():
            errores.append([ruta.name, "no existe el archivo"])
            continue

        try:
            facturas.append(leer_xml(ruta))
        except ET.ParseError as e: #xml parse error
            errores.append([ruta.name, "xml dañado: " + str(e)])
        except Exception as e: # cualquier otro error
            errores.append([ruta.name, "error: " + str(e)])


    df = pd.DataFrame(facturas, columns=columnas) 
    return df, errores
