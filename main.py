import logging
from pathlib import Path

from src.creat_report import create_report
from src.read_xml import leer_carpeta
from src.resolver_duplicados import resolver_duplicados


path_cfdis = Path(__file__).parent / "cfdis"
path_output = Path(__file__).parent / "output"


def main():

    # configuramos el logging para que guarde la información en un archivo de log
    logging.basicConfig(
        filename=path_output / "ejecucion.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
    )

    # leemos los XML y generamos el reporte
    df, errores = leer_carpeta(path_cfdis)
    df, errores = resolver_duplicados(df, errores)
    create_report(df, errores, path_output)

    
    logging.info("Proceso terminado: %s facturas, %s incidencias", len(df), len(errores))


if __name__ == "__main__":
    main()
