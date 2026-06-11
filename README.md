# Integrazione Refiner per dataset robotici

## Descrizione
Questo progetto fornisce una pipeline per importare dataset robotici in formato Parquet, annotarli e rifinirli usando **Refiner**.

## Architettura
- `import_parquet.py`: converte file Parquet in CSV per facilitare l'elaborazione.
- `annotate.py`: aggiunge metadati o etichette al dataset grezzo (es. timestamp, ID sensore).
- `src/process_data.py`: carica il CSV annotato, applica Refiner per il refinement (imputazione valori mancanti, normalizzazione, ecc.) e salva il risultato.
- `data/`: cartella per i dati di input/output (raw_data.csv, annotated_data.csv, refined_data.csv).
- `requirements.txt`: elenco delle dipendenze Python.
- `venv/`: ambiente virtuale opzionale.

## Installazione
```bash
# (opzionale) creare un ambiente virtuale isolato
python3 -m venv venv
source venv/bin/activate

# installare le dipendenze
python3 -m pip install --user --break-system-packages -r requirements.txt
```

## Uso
### 1. Importazione Parquet
```bash
python3 import_parquet.py --input data/raw_data.parquet --output data/raw_data.csv
```

### 2. Annotazione
```bash
python3 annotate.py --input data/raw_data.csv --output data/annotated_data.csv
```

### 3. Refinement (pipeline principale)
```bash
python3 src/process_data.py
```

## Esempi
Dopo aver eseguito la pipeline, troverai:
- `data/raw_data.csv`: dati grezzi importati da Parquet.
- `data/annotated_data.csv`: dati con annotazioni aggiuntive.
- `data/refined_data.csv`: dati raffinati da Refiner, pronti per l'analisi o il training di modelli.

## Note sulle GPU
I test di performance che sfruttano le GPU (ad esempio benchmark di Refiner) **devono essere eseguiti manualmente** solo quando le GPU sono libere. Evita di avviarli in ambienti condivisi o durante l'uso intensivo della GPU da altri processi.

## Variabili d'ambiente
- `DATA_DIR` (default `data/`) indica la cartella dei dati in ingresso.
- `OUTPUT_DIR` (default `data/`) indica la cartella di destinazione per i risultati.

## Stato
✅ COMPLETATO — 2026-06-11
Tutte le fasi sono state realizzate: struttura progetto, dipendenza Refiner, script di importazione Parquet, pipeline di annotazione, documentazione d'uso e note GPU.

## Licenza
Questo progetto è rilasciato sotto licenza MIT.