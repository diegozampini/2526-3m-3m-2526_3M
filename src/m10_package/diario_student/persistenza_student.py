# ### Parte 3: Modulo `persistenza.py`
# Implementa le funzioni per salvare e caricare il diario su file JSON:
# - `salva_diario(diario: dict, nome_file: str) -> None`
# - `carica_diario(nome_file: str) -> dict`
import json

def salva_diario(diario: dict, nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(diario, file, indent=4)
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")

def carica_diario(nome_file: str) -> dict:
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            dati = json.load(file)
        return dati  # restituisce direttamente il diario salvato
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return {"entrate": []} 
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Errore nel parsing del file: {e}")
        return {"entrate": []}
