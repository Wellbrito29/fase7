import pandas as pd
import numpy as np
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st


def interface_fase4():
    st.title("🧠 Fase 4 – Sistema de Irrigação Inteligente com Machine Learning")
    st.subheader("Modelagem preditiva usando Random Forest")

    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="03071993Edu",  # ✅ sua senha
            database="FarmTech",
        )

        # Carregar dados do banco
        df = pd.read_sql(
            "SELECT nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao FROM dados_irrigacao",
            conexao,
        )

        # Separação de features e target
        X = df.drop("irrigacao", axis=1)
        y = df["irrigacao"]

        # Treinamento
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        modelo = RandomForestClassifier(random_state=42)
        modelo.fit(X_train, y_train)

        # Avaliação
        predicoes = modelo.predict(X_test)
        acuracia = accuracy_score(y_test, predicoes)

        # Interface do usuário
        st.sidebar.header("📊 Entrada de dados simulada:")
        nutriente_P = st.sidebar.selectbox(
            "Nutriente P (1 = Presente, 0 = Ausente)", [1, 0]
        )
        nutriente_K = st.sidebar.selectbox(
            "Nutriente K (1 = Presente, 0 = Ausente)", [1, 0]
        )
        nivel_ph = st.sidebar.slider("Nível de pH", 0.0, 14.0, 7.0)
        umidade_solo = st.sidebar.slider("Umidade do Solo (%)", 0.0, 100.0, 50.0)
        temperatura = st.sidebar.slider("Temperatura (°C)", 15.0, 40.0, 25.0)

        dados_usuario = np.array(
            [[nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura]]
        )
        resultado = modelo.predict(dados_usuario)[0]
        estado_irrigacao = "💧 Ativada" if resultado else "⛔ Desativada"

        st.write(f"### Acurácia do Modelo: `{acuracia * 100:.2f}%`")
        st.write("### 🔍 Previsão de Irrigação com seus dados:")
        st.success(f"Irrigação: **{estado_irrigacao}**")

        st.write("### 📄 Relatório de Classificação:")
        st.code(classification_report(y_test, predicoes), language="text")

    except Exception as e:
        st.error(f"Erro na Fase 4: {e}")
    finally:
        if "conexao" in locals():
            conexao.close()
