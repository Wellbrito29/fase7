import streamlit as st


def interface_fase1():
    culturas = ["Soja", "Milho"]
    insumos_disponiveis = ["Fosfato", "Potássio"]
    tipos_culturas = []
    tipos_insumos = []
    areas = []
    insumos = []

    st.header("🌾 Fase 1 – Cálculo de Área e Insumos")

    cultura = st.selectbox("Escolha a cultura:", culturas)
    forma = st.radio("Formato da área:", ["Retangular", "Circular"])

    if forma == "Retangular":
        largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
        comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)
        area = largura * comprimento
    else:
        raio = st.number_input("Raio (m)", min_value=0.0, step=0.1)
        area = 3.14 * raio**2

    insumo = st.selectbox("Tipo de insumo:", insumos_disponiveis)
    quantidade_por_metro = st.number_input(
        "Quantidade de insumo por m² (ml)", min_value=0.0, step=0.1
    )

    if st.button("➕ Adicionar área"):
        fator = 1.0 if cultura == "Soja" else 2.0
        total = quantidade_por_metro * fator * area
        tipos_culturas.append(cultura)
        tipos_insumos.append(insumo)
        areas.append(area)
        insumos.append(total)
        st.success(f"✅ Área: {area:.2f} m² | {insumo}: {total:.2f} mL")

        st.write("### 💾 Resumo da área cadastrada:")
        st.write(f"Cultura: {cultura}")
        st.write(f"Área: {area:.2f} m²")
        st.write(f"Insumo: {insumo}")
        st.write(f"Total de insumo: {total:.2f} mL")
