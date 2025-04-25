# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# PROJETO FASE 6 – O COMEÇO DA REDE NEURAL

## Nome do grupo

## Grupo 11

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/caiorcastro/">Caio Rodrigues Castro</a> 
- <a href="https://www.linkedin.com/in/celeste-leite-dos-santos-66352a24b/">Celeste Leite dos Santos</a> 
- <a href="https://www.linkedin.com/in/digitalmanagerfelipesoares/">Felipe Soares Nascimento</a>
- <a href="https://www.linkedin.com/in//">Wellington Nascimento de Brito</a>



## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

Este projeto tem como objetivo aplicar e comparar diferentes abordagens de Visão Computacional na identificação de alimentos (cenoura e batata), com foco em tarefas como classificação e detecção de objetos. As soluções exploradas incluem:

- YOLOv8 Customizado (detecção e localização)
- YOLOv8 Pré-treinado (sem fine-tuning)
- CNN do zero (classificação)

Foram avaliadas acurácia, tempo de treinamento, facilidade de implementação e desempenho na inferência, considerando cenários reais como automação agrícola.


## 📁 Arquivos e Vídeo

- 🔬 **Notebook com a implementação completa**: [Clique aqui para acessar o notebook no Colab](./src/FelipeSoares_Nascimento_RM560151_pbl_fase6_2.ipynb)
- 🎥 **Vídeo demonstrativo**: [Assista aqui](LINK_DO_VÍDEO) 
- 📁 **Dataset utilizado**: [Link para download do dataset](https://drive.google.com/file/d/1Yj9sYI9tum4c2c6ysYFp4-Cw4MS6WZCg/view?usp=drive_link)


## 🔧 Como executar o código

### Pré-requisitos:
- Google Colab ou ambiente Jupyter
- GPU recomendada para treinamento (T4 no Colab)
- Bibliotecas:
  - `ultralytics`
  - `torch`
  - `opencv-python`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

(Instalação automática via `pip install` dentro do notebook)

### Passo a passo:
1. Acesse o [notebook](https://colab.research.google.com/drive/1a4WzYzeUrFlogsQUIHSOoyc4NrMn-Juk?usp=sharing)
2. Monte o Google Drive com o dataset (instrução incluída no notebook).
3. [Link para download do dataset](https://drive.google.com/file/d/1Yj9sYI9tum4c2c6ysYFp4-Cw4MS6WZCg/view?usp=drive_link)

  - faça o download do arquivo zip "dataset-cenoura-batata.zip" e sua no seu drive o arquivo "dataset"
4. Execute as células em sequência:
   - Preparação dos dados
   - Treinamento dos modelos
   - Inferência e avaliação
5. Visualize os resultados diretamente nas saídas do notebook com métricas e imagens inferidas.

## 📊 Resultados comparativo das Abordagens


| Abordagem        | Facilidade | Precisão | Tempo Treinamento | Tempo Inferência |
|------------------|------------|----------|-------------------|------------------|
| YOLO Customizado | Média      | 0,84     | 3h (60 épocas)    | 4,3s/imagem      |
| YOLO Padrão      | Alta       | 0,10     | 0s                | 12,7s/imagem      |
| CNN do Zero      | Média      | 0,94     | 2min             | 25,25s/

## 🎯 Conclusão
Nos nossos testes, vimos diferenças claras entre as abordagens que usamos para identificar alimentos, especialmente batatas e cenouras.

O YOLO customizado O YOLO customizado foi o que apresentou o melhor desempenho geral, uma precisão de 83,84%, indicando ótima capacidade de identificar e localizar os objetos com precisão. Como ele desenha caixas ao redor dos alimentos, é ideal para aplicações em que é necessário saber exatamente onde o alimento está, como em robôs de colheita ou sistemas de triagem automatizada. Por outro lado, exigiu um esforço considerável: foram 3 horas de treinamento no Google Colab e mais o tempo de anotação manual de 200 imagens, o que demandou bastante dedicação.

Já a CNN feita do zero A CNN feita do zero foi eficiente para tarefas de classificação simples (sem localização), com uma precisão estimada de 94%. Ela teve tempo de treinamento curto (cerca de 2 minutos) e exigiu apenas o nome da classe em cada imagem, não foi necessário anotar com caixas. No entanto, sua inferência foi muito lenta (25,2 segundos por imagem), o que limita seu uso em sistemas em tempo real.

Por fim, o YOLO padrão, mesmo sem treinamento com nossos dados, foi capaz de reconhecer alguns objetos do nosso conjunto de teste, como cenouras, mas de forma inconsistente. Em vários casos, confundiu cenoura com laranja e batata com maçã, o que mostra que não estava adaptado ao nosso domínio específico sua precisão estimado foi de aproximadamente 10%, o que é considerado baixo.

## ⚡ Pontos Fortes e Limitações

YOLO Customizado
  - ✅ Detecta e localiza objetos com alta precisão
  - ✅ Acurácia alta (~84%) para cenoura e batata
  - ✅ Consegue identificar vários objetos na mesma imagem
  - ❌ Precisa de rotulagem manual demorada (2 a 3 horas)
  - ❌ Treinamento longo (~1 horas no Colab)
  - ❌ Mais complexo de ajustar e configurar

CNN do Zero
  - ✅ Mais simples de programar e treinar
  - ✅ Só precisa saber a classe da imagem (sem caixas de anotação)
  - ✅ Treinamento mais rápido (estimado em 1-2 min)
  - ❌ Não mostra onde o objeto está na imagem
  - ❌ Tivemos problemas técnicos para rodar no Colab
  - ❌ Não é ideal para imagens com mais de um objeto

YOLO Padrão
  - ✅ Fácil de usar e pronto para testar
  - ✅ Bom para testes e protótipos rápidos
  - ❌ Fraco em precisão para nossas classes específicas
  - ❌ Confunde facilmente objetos parecidos
  - ❌ Não serve para aplicações mais específicas sem ajuste


## 🗃 Histórico de lançamentos

* 2.5.0 - 16/04//2025
    * 
* 1.4.0 - 15/04/2024


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


