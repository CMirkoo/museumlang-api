import os
from fastapi.responses import JSONResponse

from fastapi import FastAPI
from pydantic import BaseModel
import logging
import json
import uvicorn

import pickle

log_dir = '/app/logs'
os.makedirs(log_dir, exist_ok=True)

# Configurazione del logger per registrare le richieste e risposte
logging.basicConfig(filename=os.path.join(log_dir, 'api_requests.log'),
                    format='[%(levelname)s]%(name)s - %(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Carica il modello di linguaggio pre-addestrato
filename = 'language_detection_pipeline.pkl'
load_pipeline = pickle.load(open(filename, 'rb'))

# Creazione della classe Pydantic per validare l'input
class TextInput(BaseModel):
    text: str # Campo che contiene il testo da analizzare

# Creazione dell'app FastAPI
app = FastAPI()


@app.post("/identify_language")
async def identify_language(data: TextInput):
    """
    Endpoint per identificare la lingua del testo fornito
    - Input: JSON con campo "text"
    - Output: JSON con "language_code" e "confidence"
    """

    # Verifica se il testo è vuoto
    if not data.text or not data.text.strip():
        return JSONResponse(status_code=400, content={"detail": "Il testo non può essere vuoto"})

    try:
        # Predizione della lingua e probabilità dal modello
        prediction = load_pipeline.predict([data.text]) # La previsione è un array di lingue
        confidence = load_pipeline.predict_proba([data.text]) # Probabilità associata

        # Il modello restituisce la lingua e la probabilità per ciascun testo
        language_code = prediction[0]
        language_confidence = max(confidence[0])

        # Creazione della risposta
        response = {
            "language_code": language_code.upper(),
            "confidence": language_confidence
        }

        # Log della richiesta e della risposta
        log_entry = {
            "input_text": data.text,
            "output": response
        }
        logging.info(json.dumps(log_entry, ensure_ascii=False)) # Log in formato JSON per chiarezza

        return response

    except Exception as e:
        logging.error(f"Errore imprevisto: {e}")
        # Se non è possibile determinare la lingua, restituire un errore
        return JSONResponse(status_code=500, content={"detail": "Impossibile indentificare la lingua del testo."})
