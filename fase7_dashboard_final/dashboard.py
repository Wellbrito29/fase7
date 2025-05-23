import streamlit as st
import sys
import os
import subprocess
import xml.etree.ElementTree as ET

# Habilita import de outras fases
sys.path.append(os.path.abspath(".."))

# Importa interface da Fase 1
from fase1_area_insumos.component import interface_fase1
from fase3_iot_irrigacao.component import interface_fase3
from fase4_dashboard_ml.component import interface_fase4
from fase6_visao_computacional.component import interface_fase6


# Configuração da página
st.set_page_config(page_title="Gestão Agrícola Integrado", layout="wide")
st.title("🌱 Sistema de Gestão Agrícola Integrado")

# Navegação lateral
pagina = st.sidebar.radio(
    "📌 Selecione a fase:",
    [
        "Fase 1 – Área e Insumos",
        "Fase 2 – Visualizar DER.XML",
        "Fase 3 – IoT Irrigação",
        "Fase 4 – Dashboard ML",
        "Fase 6 – Visão Computacional",
    ],
)

# Fase 1 – Interface interativa
if pagina == "Fase 1 – Área e Insumos":
    interface_fase1()


# Fase 2 – Visualização do DER.XML
elif pagina == "Fase 2 – Visualizar DER.XML":
    st.subheader("📄 Visualização do DER.XML")
    try:
        tree = ET.parse("../fase2_banco_dados/DER.XML")
        root = tree.getroot()

        st.subheader("📑 Conteúdo do DER.XML")
        xml_string = ET.tostring(root, encoding="unicode")
        st.code(xml_string, language="xml")

        st.subheader("🔍 Estrutura das Tags")
        for child in root:
            st.write(f"🔹 Tag: `{child.tag}` | Atributos: `{child.attrib}`")
    except Exception as e:
        st.error(f"Erro ao carregar DER.XML: {e}")

# Fase 3 – IoT
elif pagina == "Fase 3 – IoT Irrigação":
    interface_fase3()


# Fase 4 – Dashboard com Machine Learning
elif pagina == "Fase 4 – Dashboard ML":
    interface_fase4()

# Fase 6 – Visão Computacional
elif pagina == "Fase 6 – Visão Computacional":
    interface_fase6()
