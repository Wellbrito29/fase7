import streamlit as st
import os
import glob
from PIL import Image
from ultralytics import YOLO


def extrair_metricas(result):
    return {
        "precision": float(result.box.mp),
        "recall": float(result.box.mr),
        "map50": float(result.box.map50),
        "map5095": float(result.box.map),
        "inference_time": round(float(result.speed["inference"]), 2),
    }


def interface_fase6():
    st.title("📷 Fase 6 – Visão Computacional com YOLOv8")
    st.subheader("Classificação de Cenoura e Batata com visão computacional")

    # Caminho absoluto do arquivo data.yaml
    dataset_yaml = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "dataset/data.yaml")
    )

    dataset_teste = os.path.join(os.path.dirname(__file__), "dataset/teste")
    nome_30 = "experimento_30epocas"
    nome_60 = "experimento_60epocas"

    peso_30 = f"runs/detect/{nome_30}/weights/best.pt"
    peso_60 = f"runs/detect/{nome_60}/weights/best.pt"

    pasta_pred_30 = "runs/detect/deteccao_30epocas"
    pasta_pred_60 = "runs/detect/deteccao_60epocas"

    if not os.path.exists(dataset_yaml):
        st.error(f"❌ Arquivo data.yaml não encontrado em: {dataset_yaml}")
        return

    # Treinar modelo com 30 épocas
    if st.button("🚀 Treinar modelo com 30 épocas"):
        model = YOLO("yolov8n.pt")
        model.train(data=dataset_yaml, epochs=30, imgsz=640, batch=16, name=nome_30)
        st.success("✅ Modelo de 30 épocas treinado!")

    # Treinar modelo com 60 épocas
    if st.button("🚀 Treinar modelo com 60 épocas"):
        model = YOLO("yolov8n.pt")
        model.train(data=dataset_yaml, epochs=60, imgsz=640, batch=16, name=nome_60)
        st.success("✅ Modelo de 60 épocas treinado!")

    # Predição com 30 épocas
    if st.button("🔍 Predição com modelo de 30 épocas"):
        if not os.path.exists(peso_30):
            st.error("❌ Modelo de 30 épocas não treinado ainda.")
            return
        model = YOLO(peso_30)
        model.predict(
            source=dataset_teste, conf=0.25, save=True, name="deteccao_30epocas"
        )
        st.success("✅ Predição realizada com sucesso!")

    # Predição com 60 épocas
    if st.button("🔍 Predição com modelo de 60 épocas"):
        if not os.path.exists(peso_60):
            st.error("❌ Modelo de 60 épocas não treinado ainda.")
            return
        model = YOLO(peso_60)
        model.predict(
            source=dataset_teste, conf=0.25, save=True, name="deteccao_60epocas"
        )
        st.success("✅ Predição realizada com sucesso!")

    # Comparação automática
    if st.button("📊 Comparar desempenho 30 x 60 épocas"):
        if not (os.path.exists(peso_30) and os.path.exists(peso_60)):
            st.warning("Treine ambos os modelos antes de comparar.")
            return

        modelo_30 = YOLO(peso_30)
        modelo_60 = YOLO(peso_60)

        metrics_30 = extrair_metricas(modelo_30.val())
        metrics_60 = extrair_metricas(modelo_60.val())

        st.markdown("### 📈 Comparação entre modelos")
        st.table(
            {
                "Métrica": [
                    "Precisão",
                    "Recall",
                    "mAP@0.5",
                    "mAP@0.5:0.95",
                    "Tempo de Inferência (ms/img)",
                ],
                "30 épocas": [
                    f"{metrics_30['precision']:.4f}",
                    f"{metrics_30['recall']:.4f}",
                    f"{metrics_30['map50']:.4f}",
                    f"{metrics_30['map5095']:.4f}",
                    f"{metrics_30['inference_time']} ms",
                ],
                "60 épocas": [
                    f"{metrics_60['precision']:.4f}",
                    f"{metrics_60['recall']:.4f}",
                    f"{metrics_60['map50']:.4f}",
                    f"{metrics_60['map5095']:.4f}",
                    f"{metrics_60['inference_time']} ms",
                ],
            }
        )

    # Exibir imagens com predições
    st.markdown("### 📸 Resultados das Predições:")
    col1, col2 = st.columns(2)

    def mostrar_imagens(pasta, col):
        if os.path.exists(pasta):
            imagens = sorted(glob.glob(f"{pasta}/*.jpg"))[:4]
            for img_path in imagens:
                col.image(
                    Image.open(img_path),
                    caption=os.path.basename(img_path),
                    use_column_width=True,
                )

    with col1:
        st.markdown("🔹 Detecção – 30 épocas")
        mostrar_imagens(pasta_pred_30, col1)

    with col2:
        st.markdown("🔹 Detecção – 60 épocas")
        mostrar_imagens(pasta_pred_60, col2)
