
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="fase6_visao_computacional/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

---

# 🌾 Projeto Fase 7 – Sistema Completo de Gestão Agrícola Inteligente

## 👥 Grupo 11

### 👨‍🎓 Integrantes:
- [Caio Rodrigues Castro](https://www.linkedin.com/in/caiorcastro/)
- [Celeste Leite dos Santos](https://www.linkedin.com/in/celeste-leite-dos-santos-66352a24b/)
- [Felipe Soares Nascimento](https://www.linkedin.com/in/digitalmanagerfelipesoares/)
- [Wellington Nascimento de Brito](https://www.linkedin.com/in/)

### 👩‍🏫 Professores:
- **Tutor:** [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/)
- **Coordenador:** [André Godoi Chiovato](https://www.linkedin.com/in/profandregodoi/)

---

## 📜 Descrição

O projeto Fase 7 consolida as entregas das fases anteriores (1 a 6) em um sistema único e completo de **gestão agrícola inteligente**, com:

- Dashboard interativo em Streamlit;
- Cálculo de área e manejo de insumos (Fase 1);
- Banco de dados relacional com DER/MER e integração (Fase 2);
- Simulação IoT com sensores e automação de irrigação (Fase 3);
- Predição com machine learning e classificação de irrigação (Fase 4);
- Integração com serviços na AWS e envio de alertas com SNS (Fase 5);
- Visão computacional com YOLOv8 para classificação de culturas (Fase 6).

---

## 📁 Arquivos e Demonstrações

- 📹 **Vídeo demonstrativo**: [Assista no YouTube](https://youtu.be/EcCqpf9p_oI)
- 📦 **Dataset**: [Download do dataset](https://drive.google.com/file/d/1Yj9sYI9tum4c2c6ysYFp4-Cw4MS6WZCg/view?usp=drive_link)

---

## 🔧 Como Executar o Sistema

### Pré-requisitos

- Python 3.10+
- MySQL rodando localmente com banco `FarmTech` e tabela `dados_irrigacao`
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- Streamlit
- AWS CLI configurado com permissões SNS (opcional)

### Instalação

```bash
pip install -r requirements.txt
```

### Execução

```bash
streamlit run fase7_dashboard_final/dashboard.py
```

---

## 🎯 Conclusão

Este projeto demonstrou a aplicação integrada de diversas tecnologias para o agronegócio digital:

- 📊 Visualização de dados e predições com Streamlit;
- 🤖 Aprendizado de máquina para decisões inteligentes de irrigação;
- 🛰️ Sensores e automação simulada com ESP32;
- 🧠 Classificação visual com YOLOv8;
- ☁️ Serviços de nuvem e alertas por e-mail usando AWS SNS.

A integração de todas as fases possibilitou uma visão holística da gestão agrícola inteligente, simulando um sistema completo e aplicável no mercado real.

---

## ⚡ Pontos Fortes e Limitações

**Pontos Fortes:**

- Modularidade entre fases;
- Alta integração entre visão computacional, sensores e ML;
- Simulação realista com banco de dados relacional;
- Interface visual clara e objetiva.

**Limitações:**

- Dataset limitado (cenoura/batata);
- Tempo de treino em YOLO no Colab;
- Dependência de permissões AWS para alertas.

---

## 🗃 Histórico de Versões

* 7.0.0 - 23/05/2025 - Integração completa das fases e dashboard final.
* 6.0.0 - Fase de Visão Computacional (YOLO)
* 5.0.0 - Integração AWS SNS e segurança

---

## 📋 Licença

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
  <a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por
  <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a>
  está licenciado sob
  <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer">CC BY 4.0</a>.
</p>
