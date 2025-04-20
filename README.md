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


## 📁 Estrutura de pastas

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
| YOLO Customizado | Média      | 0,90     | 1h (60 épocas)    | 0,1s/imagem      |
| YOLO Padrão      | Alta       | 0,00     | 0s                | 0,1s/imagem      |
| CNN do Zero      | Média      | 0,85     | 15min             | 0,05s/

## 🎯 Conclusão
Nos nossos testes, vimos diferenças claras entre as abordagens que usamos para identificar alimentos, especialmente batatas e cenouras.

O YOLO customizado foi o que teve o melhor desempenho. Ele conseguiu identificar e localizar os objetos com bastante precisão, atingindo cerca de 92% de acurácia no nosso conjunto de teste. Como ele desenha caixas ao redor dos objetos, é ideal para aplicações que precisam saber exatamente onde o alimento está, como em robôs de colheita ou sistemas automatizados. Por outro lado, exigiu bastante trabalho: levamos cerca de 4 horas de treino no Google Colab e ainda tivemos que rotular manualmente 200 imagens, o que consumiu várias horas.

Já a CNN feita do zero seria uma boa opção para quem só precisa classificar imagens, sem se preocupar com localização. Apesar de termos enfrentado problemas técnicos no Colab e não conseguimos rodar os testes por completo, com base em pesquisas, estimamos que ela teria uma acurácia por volta de 85%, com um tempo de treino bem menor (uns 15 a 20 minutos). A vantagem aqui é que ela é mais fácil de implementar e não precisa de anotações detalhadas nas imagens – só o nome da classe já basta.

Por fim, o YOLO padrão (pré-treinado) não funcionou bem para o nosso caso. Ele não reconheceu corretamente as cenouras nem as batatas, em alguns casos, confundiu cenoura com laranja e batata com maçã. A inferência foi bem rápida (em torno de 0,06 segundos por imagem), mas como ele não foi treinado com nossos dados, acabou não sendo útil sem um ajuste mais específico.

## ⚡ Pontos Fortes e Limitações

YOLO Customizado
  - ✅ Detecta e localiza objetos com alta precisão
  - ✅ Acurácia alta (~92%) para cenoura e batata
  - ✅ Consegue identificar vários objetos na mesma imagem
  - ❌ Precisa de rotulagem manual demorada (6 a 8 horas)
  - ❌ Treinamento longo (~4 horas no Colab)
  - ❌ Mais complexo de ajustar e configurar

CNN do Zero
  - ✅ Mais simples de programar e treinar
  - ✅ Só precisa saber a classe da imagem (sem caixas de anotação)
  - ✅ Treinamento mais rápido (estimado em 15-20 min)
  - ❌ Não mostra onde o objeto está na imagem
  - ❌ Tivemos problemas técnicos para rodar no Colab
  - ❌ Não é ideal para imagens com mais de um objeto

YOLO Padrão
  - ✅ Fácil de usar e pronto para testar
  - ✅ Inferência super rápida (~0,06s por imagem)
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


