import streamlit as st
from pathlib import Path
import importlib.util

# ==============================
# CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Application Financière – Planification Stratégique",
    page_icon="",
    layout="wide"
)

# ==============================
# SESSION STATE
# ==============================
if "scenario" not in st.session_state:
    st.session_state.scenario = "Central"

# ==============================
# TITRE
# ==============================
st.title("Application Financière de Planification Stratégique et Comptable")
st.caption("Auteur : Mohamed Falilou Fall")

# ==============================
# NAVIGATION
# ==============================
pages = {
    "Hypothèses d’activité": "01_Hypotheses_Activite.py",
    "Compte de résultat": "02_Compte_Resultat_Previsionnel.py",
    "Seuil de rentabilité": "03_Seuil_Rentabilite.py",
    "BFR": "04_BFR.py",
    "Plan de financement": "05_Plan_Financement.py",
    "Plan de trésorerie": "06_Plan_Tresorerie.py",
    "Données financières clés": "07_Donnees_Financieres_Cles.py",
    "Scénarios": "08_Scenarios.py",
    "Export & reporting": "09_Export.py",
}

selection = st.sidebar.radio("Choisir un module", list(pages.keys()))

# ==============================
# CHARGEMENT SÉCURISÉ DES PAGES
# ==============================
BASE_DIR = Path.cwd()
PAGE_DIR = BASE_DIR / "app" / "pages"
page_path = PAGE_DIR / pages[selection]

if page_path.exists():
    spec = importlib.util.spec_from_file_location("page_module", page_path)
    page_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page_module)

    if hasattr(page_module, "run"):
        page_module.run()
    else:
        st.error("La page ne contient pas de fonction run()")
else:
    st.error(f"Fichier introuvable : {page_path}")
