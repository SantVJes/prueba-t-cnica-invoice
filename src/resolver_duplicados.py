import logging


logger = logging.getLogger(__name__)


def resolver_duplicados(df, errores):
    # contamos los UUID repetidos, conservando el primero
    cantidad = int(df.duplicated(subset=["UUID"], keep="first").sum())
    errores.extend([["duplicados", "UUID duplicado; se descarta una factura"]] * cantidad)

    # avisamos en el log si encontramos duplicados
    if cantidad:
        logger.warning("Se descartaron %s facturas con UUID duplicado", cantidad)

    return df.drop_duplicates(subset=["UUID"], keep="first"), errores
