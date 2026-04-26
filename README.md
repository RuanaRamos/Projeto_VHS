# 🤖 Projekt VHaS: Vielseitige Handhabungslösung
> **Kognitive Übersetzung und digitale Inklusion in der deutschen Industrie**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projetovhs-26042026.streamlit.app/)

## 📌 Übersicht
Dieses Projekt nutzt **Human-Centered AI**, um Industriearbeitern den Zugang zu komplexen technischen Handbüchern zu erleichtern. Durch den Einsatz von **RAG (Retrieval-Augmented Generation)** wandelt das System komplizierte Dokumentationen in einfache, handlungsorientierte Anweisungen um.

### 🚩 Die Herausforderung: Der digitale Graben
Die deutsche Industrie steht vor einer kritischen Produktivitätslücke:
* **Funktionaler Analphabetismus:** Rund 12,1 % der Bevölkerung haben Schwierigkeiten mit komplexen Texten.
* **Operativer Sektor:** 60 % der Mitarbeiter im operativen Bereich kämpfen mit komplizierter Software.
* **Risiko:** Bedienfehler, Maschinenstillstände und Sicherheitsrisiken durch zu komplexe Benutzeroberflächen.

---

## 💡 Die Lösung: Menschzentrierte KI
VHaS fungiert als intelligente Ebene, die technische Dokumentationen abfängt und sie in **leicht verständliche Anweisungen** (Niveau eines 10-jährigen Kindes) übersetzt – direkt am Point of Need.

### Kernfunktionen
| Funktion | Beschreibung |
| :--- | :--- |
| **Vereinfachte Sprache** | Komplexe Begriffe werden in einfache Handlungsanweisungen umgewandelt. |
| **Mehrsprachigkeit** | Unterstützung für die internationale Belegschaft (Deutsch, Englisch, Polnisch, Türkisch, etc.). |
| **Echtzeit-Assistenz** | Sofortige Antworten basierend auf den Original-PDF-Handbüchern. |
| **Adaptive Intelligenz** | Dynamische Anpassung der Sprache an das Profil des Mitarbeiters. |

---

## 🛠️ Technische Architektur
Das System ist auf Effizienz und deutschen Datenschutz (DSGVO-Konformität) optimiert:

* **Orchestrierung:** [LangChain](https://www.langchain.com/) für den RAG-Workflow.
* **Embeddings & Datenschutz:** Open-Source Modelle von **Hugging Face** stellen sicher, dass sensible Daten lokal verarbeitet werden können.
* **Hochleistungs-Processing:** Nutzung der **Groq Cloud (LPUs)** für Antwortzeiten in Millisekunden, ideal für den Fabrikalltag.
* **Vektor-Datenbank:** **FAISS** für hocheffiziente semantische Suche.
* **Klassifizierung:** Scikit-learn (Logistische Regression) zur Analyse des Schwierigkeitsgrades.

---

## ⚙️ Installation & Setup

Befolgen Sie diese Schritte, um das Projekt lokal auszuführen:

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/projeto-vhs.git](https://github.com/SEU-USUARIO/projeto-vhs.git)
   cd projeto-vhs
