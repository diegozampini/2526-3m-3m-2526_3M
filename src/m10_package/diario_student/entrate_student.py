# #### Parte 2: Modulo `entrate.py`
# Implementa funzioni per lavorare con le entrate del diario:
# - `crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict`
#   - `data` è una stringa nel formato `YYYY-MM-DD`
#   - `durata` è il tempo trascorso in minuti
# - `info_entrata(entrata: dict) -> str`
#   - Restituisce una stringa leggibile con data, categoria, durata e testo
# - `crea_diario() -> dict`
#   - Restituisce un dizionario con chiave `entrate` e lista vuota
# - `aggiungi_entrata(diario: dict, entrata: dict) -> None`
# - `rimuovi_entrata(diario: dict, indice: int) -> None`
# - `tempo_totale(diario: dict) -> int`
#   - Somma tutte le durate in minuti
# - `tempo_per_categoria(diario: dict) -> dict[str, int]`
#   - Restituisce il tempo totale speso per categoria
# - `trova_entrate_per_data(diario: dict, data: str) -> list[dict]`

def crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict:
    return {"data": data, "testo": testo, "categoria": categoria, "durata": durata}

def info_entrata(entrata: dict) -> str:
    return f"{entrata['data']} - {entrata['categoria']} ({entrata['durata']} min): {entrata['testo']}"

def  crea_diario() -> dict:
    return {"entrate": 0}

def aggiungi_entrata(diario: dict, entrata: dict) -> None:      \
    diario["entrate"].append(entrata)
    
def rimuovi_entrata(diario: dict, indice: int) -> None:
      if 0 <= indice < len(diario["entrate"]):
        diario["entrate"].pop(indice)
      else:
        print(f"Errore: indice {indice} non valido")
        
def tempo_totale(diario: dict) -> int:
    minuti = diario["durata"] // 60
    return f"{diario['data']} - {diario['testo']} - {diario['categoria']} - {diario['durata']} {minuti} min"

def tempo_per_categoria(diario: dict) -> dict[str, int]:
    categorie = {}
    for entrata in diario["entrate"]:
        categoria = entrata["categoria"]
        durata = entrata["durata"]
        if categoria in categorie:
            categorie[categoria] += durata
        else:
            categorie[categoria] = durata
    return categorie

def trova_entrate_per_data(diario: dict, data: str) -> list [dict]:
    risultato = []
    for entrata in diario["entrate"]:
        if entrata["data"] == data:
            risultato.append(entrata)
    return risultato


