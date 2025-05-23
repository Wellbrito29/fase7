import streamlit as st
import mysql.connector
import random
from fase5_aws_seguranca.alerta import enviar_alerta_email


def interface_fase3():
    st.header("💧 Fase 3 – IoT e Irrigação Inteligente")

    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1", user="root", password="03071993Edu", database="FarmTech"
        )
        cursor = conexao.cursor()

        def gerar_dados():
            nutriente_P = random.choice([True, False])
            nutriente_K = random.choice([True, False])
            nivel_ph = round(random.uniform(0, 14), 2)
            umidade_solo = round(random.uniform(20, 80), 2)
            temperatura = round(random.uniform(15, 35), 1)
            irrigacao = umidade_solo < 40 or nivel_ph < 5.5
            return (
                nutriente_P,
                nutriente_K,
                nivel_ph,
                umidade_solo,
                temperatura,
                irrigacao,
            )

        def inserir_dados(dados):
            sql = """
            INSERT INTO dados_irrigacao (nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, dados)
            conexao.commit()

        # 📡 Botão para simular leitura
        if st.button("📡 Simular leitura de sensores"):
            dados = gerar_dados()
            inserir_dados(dados)

            st.success("✅ Dados inseridos com sucesso!")
            st.write(
                f"""
            - Nutriente P: `{dados[0]}`
            - Nutriente K: `{dados[1]}`
            - pH: `{dados[2]}`
            - Umidade: `{dados[3]}%`
            - Temperatura: `{dados[4]}°C`
            - 💧 Irrigação ativada? `{dados[5]}`
            """
            )

            if dados[3] < 30:
                enviar_alerta_email(dados[3], dados[2], dados[4])
                st.warning("⚠️ Alerta enviado por e-mail! (Umidade crítica)")

        # 🚨 Botão de alerta manual
        st.markdown("---")
        st.subheader("🧪 Teste manual do alerta")

        if st.button("🚨 Forçar alerta manual (teste)"):
            umidade = 25.0
            ph = 4.8
            temperatura = 32.0

            enviar_alerta_email(umidade, ph, temperatura)
            st.success("✅ Alerta forçado enviado com sucesso!")
            st.write(
                f"""
            - Umidade: `{umidade}%`
            - pH: `{ph}`
            - Temperatura: `{temperatura}°C`
            """
            )

    except Exception as e:
        st.error(f"Erro na conexão com o banco de dados: {e}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals():
            conexao.close()
