import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


def create_report(df, errores, output_path):

    # creamos la carpeta de salida si todavía no existe
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        # agrupamos por proveedor y ordenamos por total facturado
        resumen = (
            df.groupby(["RFC Emisor", "Nombre Emisor"], as_index=False)
            .agg({"Total": "sum", "IVA trasladado": "sum"})
            .sort_values("Total", ascending=False)
        )

        # guardamos el detalle y el resumen en hojas separadas
        with pd.ExcelWriter(output_path / "reporte_cfdi.xlsx") as writer:
            df.to_excel(writer, sheet_name="Detalle", index=False)
            resumen.to_excel(writer, sheet_name="Resumen por proveedor", index=False)

    except Exception as e:
        errores.append(["reporte", "error al crear el excel: " + str(e)])
        logger.exception("No se pudo crear el reporte de Excel")

    # guardamos las incidencias en CSV
    df_errores = pd.DataFrame(errores, columns=["Archivo", "Error"])
    ruta_errores = output_path / "reporte_errores.csv"
    df_errores.to_csv(ruta_errores, index=False, encoding="utf-8-sig")
    logger.info(
        "Reporte de errores guardado en %s (%s incidencias)",
        ruta_errores,
        len(errores),
    )
