# Entregável 1  
# 📌 Predição do Rendimento da Safra 🌾  

## 📖 Descrição do Projeto  
Este projeto faz parte da **Fase 5 - Modelagem de Dados com Regressão Supervisionada** e tem como objetivo prever o rendimento da safra a partir de variáveis climáticas e condições do solo.  

Utilizamos técnicas de **Análise Exploratória de Dados (EDA)**, **Clusterização** e **Modelagem Preditiva** para entender os padrões nos dados e construir modelos de Machine Learning.

## 🚀 Como Acessar o Notebook no Google Colab  
Clique no link abaixo para abrir o notebook diretamente no Google Colab:  

🔗 **[Abrir no Colab](https://colab.research.google.com/drive/1SS8zWIDoqEoF_d_DnROrxCq0Kj2wsN4u#scrollTo=514cb14e)**  
  **[Link video](https://www.loom.com/share/fc7cc47a851a49838e0ce55b8678849e?sid=68c48e4e-e38c-4db5-8adc-0eebc094dc93)**

## 📂 Estrutura do Projeto  
```
📦 projeto-safra  
 ┣ 📜 crop_yield.csv          # Base de dados utilizada no projeto  
 ┣ 📜 Wellington_pbl_fase4.ipynb  # Notebook Jupyter com análise e modelos  
 ┣ 📜 README.md               # Arquivo de descrição do projeto  
```

## 🛠 Tecnologias Utilizadas  
- Python 🐍  
- Pandas e NumPy para manipulação de dados  
- Matplotlib e Seaborn para visualização  
- Scikit-Learn para Machine Learning  
- Jupyter Notebook e Google Colab para análise interativa  

## 📌 Como Executar Localmente  
Caso queira rodar o notebook no seu próprio ambiente:  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/projeto-safra.git
   ```  
2. Instale as dependências necessárias:  
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```  
3. Execute o notebook Jupyter:  
   ```bash
   jupyter notebook Wellington_pbl_fase4.ipynb
   ```  

---  

# Entregável 2  
# ☁️ Estimativa de Custos AWS para Hospedagem da API  

## 📌 Requisitos  
A estimativa de custos foi realizada utilizando a **Calculadora da AWS**, considerando a seguinte configuração para a hospedagem da API:  

- **2 vCPUs**  
- **1 GiB de memória**  
- **Até 5 Gigabit de rede**  
- **50 GB de armazenamento (HD)**  

## 📊 Comparação de Custos (On-Demand – 100%)  

| Região           | Custo da Instância (730h/mês) | Armazenamento (50GB) | Custo Total Mensal |
|----------------|----------------------------|----------------------|------------------|
| **Virgínia do Norte (us-east-1)** | $33,87 | $5,00 | **$38,87** |
| **São Paulo (sa-east-1)** | $39,06 | $6,00 | **$45,06** |

- **A opção mais econômica** é a **região da Virgínia do Norte**, com um custo total de **$38,87/mês**, enquanto a região de **São Paulo** custa **$45,06/mês**.  

## 🔍 Considerações sobre Restrições Legais e Acesso aos Dados  
- **Se houver necessidade de armazenar os dados no Brasil** por **restrições legais**, a opção de São Paulo é a mais adequada.  
- **Se o objetivo for reduzir custos e a latência não for um problema**, a **Virgínia do Norte é a melhor escolha**.  

## 📌 Conclusão  
Se não houver exigências legais para armazenar os dados no Brasil, **hospedar a instância na Virgínia do Norte é mais econômico**.  
Porém, caso seja necessário um acesso rápido aos dados coletados no Brasil, **a opção de São Paulo pode ser justificada** mesmo com um custo maior.  

🔗 **Referência:** [AWS Pricing Calculator](https://calculator.aws/#/)  

---  
📅 **Entrega Fase 4 - Modelagem de Dados com Regressão Supervisionada**  
