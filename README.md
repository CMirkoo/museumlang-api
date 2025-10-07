# 🏛️ MuseumLangAPI – Sistema di Riconoscimento della Lingua per Testi Museali

**MuseumLangAPI** è un progetto di messa in produzione di un sistema di riconoscimento automatico della lingua per testi museali, sviluppato in **Python**, con un’architettura **FastAPI + Nginx + Docker**.  
Il progetto fornisce un servizio **REST API** per identificare automaticamente la lingua di un testo, permettendo l’integrazione nei sistemi informativi del museo.

---

## 🎯 Obiettivo

La gestione multilingue delle descrizioni museali è spesso un processo manuale e soggetto a errori.  
L’obiettivo di *MuseumLangAPI* è automatizzare il riconoscimento della lingua, rendendo il processo:

- **Accessibile** da remoto tramite API REST;  
- **Scalabile**, grazie all’uso di container Docker;  
- **Affidabile**, tramite un modello di machine learning pre-addestrato.  

---

## 🧩 Funzionalità principali

- 🔍 **Riconoscimento automatico** della lingua di un testo.  
- ⚡ **API REST** pronte all’uso (basate su FastAPI).  
- 🐳 **Containerizzazione completa** con Docker e Nginx come reverse proxy.  
- 🚀 **Deploy semplificato** con lo script `deploy.py`.  

---

## 🧠 Modello di Machine Learning

Il modello è stato addestrato su testi multilingue (italiano, inglese, tedesco) e salvato in formato `.pkl`.  
Puoi scaricarlo direttamente da questo link:

🔗 **[Download language_detection_pipeline.pkl](https://github.com/Profession-AI/progetti-python/raw/refs/heads/main/Messa%20in%20produzione%20di%20un%20sistema%20per%20il%20riconoscimento%20della%20lingua%20di%20testi%20per%20un%20museo/language_detection_pipeline.pkl)**

> Dopo il download, posiziona il file nella cartella principale del progetto (`/museumlang-api`).

---
