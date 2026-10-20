




def resolver_duplicados(df,errores):
    # se eliminan los duplicados por UUID, dejando el primero que se encuentra
    df = df.drop_duplicates(subset=["UUID"], keep="first")
    errores.append(["Se eliminaron los duplicados por UUID si hay, dejando el primero que se encuentra"])
    return df, errores
