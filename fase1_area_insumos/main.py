# Projeto de Agricultura Digital - FarmTech Solutions 

# Variaves globais  


culturas = ['Soja','Milho']
insumos_disponiveis = ['Fosfato', 'Potássio']
areas = []
insumos = []
tipos_insumos = []
tipos_culturas = []


# Funções 

def calcular_area_retangulo(largura,comprimento): 
  return largura * comprimento 

def calcular_area_circulo(raio): 
  return 3.14 * raio ** 2 

def calcular_manejo_insumos(cultura, quantidade_por_metro, area):
  if cultura == 'Soja': 
    fator = 1.0

  else:
    fator = 2.0 

  return quantidade_por_metro * fator * area

def inserir_dados(isUpdate, indexUpdate):
  print("\n--- Inserir Dados de Plantio ---")
  print("Escolha a cultura:")

  for i, cultura in enumerate(culturas):
    print(f"{i + 1}. {cultura}")

  cultura_escolhida = int(input("Digite o número da cultura: ")) -1 
  cultura_nome = culturas[cultura_escolhida]
  if isUpdate:
    tipos_culturas[indexUpdate] = cultura_nome
  else:
    tipos_culturas.append(cultura_nome)
  
  if(cultura_nome == 'Soja'):
    forma = 1
  else :
    forma = 2
  
  if forma == 1:
    print("Área retangular")
    largura = float(input("Digite a largura da área (metros): "))
    comprimento = float(input("Digite o comprimento da área (metros): "))
    area = calcular_area_retangulo(largura, comprimento)
  elif forma == 2:
    print("Área circular")
    raio = float(input("Digite o raio da área (metros): "))
    area = calcular_area_circulo(raio)
  else:
    print("Forma inválida. Tente novamente.")
    return

  if isUpdate:
    areas[indexUpdate] = area
  else:
    areas.append(area)

  print("Escolha o tipo de insumo:")
  for i, insumo in enumerate(insumos_disponiveis):
    print(f"{i + 1}. {insumo}")
    
  tipo_insumo = int(input("Digite o número do insumo: ")) - 1

  if isUpdate:
    tipos_insumos[indexUpdate]=insumos_disponiveis[tipo_insumo]
  else:
    tipos_insumos.append(insumos_disponiveis[tipo_insumo])
    
  quantidade_por_metro = float(input("Digite a quantidade de insumo por metro (ml/m): "))
  total_insumo = calcular_manejo_insumos(cultura_nome, quantidade_por_metro, area)

  if isUpdate:
    insumos[indexUpdate] = total_insumo
  else:
    insumos.append(total_insumo)

  print(f"\nÁrea de plantio calculada: {area:.2f} m²")
  print(f"Total de {insumos_disponiveis[tipo_insumo]} necessário para {cultura_nome}: {total_insumo:.2f} mL/m2")

def exibir_dados():
    print("\n--- Exibir Dados ---")
    for i, area in enumerate(areas):
        print(f"{i + 1}. Área de {tipos_culturas[i]}: {area:.2f} m² - {tipos_insumos[i]} necessário: {insumos[i]:.2f} mL/m2")

def deletar_dados():
  print("\n--- Deletar Dados ---")
  size_areas = len(areas)
  if size_areas == 0:
    print("Não há áreas cadastradas.")
    return  
  print("Escolha o número da área que deseja deletar:")
  for i, area in enumerate(areas):
    print(f"{i + 1}. Área de {tipos_culturas[i]}: {area:.2f} m²")
  numero_area = int(input("Digite o número da área: ")) - 1
  if numero_area < 0 or numero_area >= size_areas:
    print("Número de área inválido.")
    return;
  areas.pop(numero_area)
  tipos_culturas.pop(numero_area)
  insumos.pop(numero_area)
  tipos_insumos.pop(numero_area)
  print("Área deletada com sucesso!")


def atualizar_dados():
  print("\n--- Atualizar Dados ---")
  print("Escolha o número da área que deseja atualizar:")
  sizeAreas = len(areas)
  if sizeAreas == 0:
    print("Não há áreas cadastradas.")
    return
  for i, area in enumerate(areas):
    print(f"{i + 1}. Área de {tipos_culturas[i]}: {area:.2f} m² - {tipos_insumos[i]} necessário: {insumos[i]:.2f} mL/m2")
  numero_area = int(input("Digite o número da área: ")) - 1
  if numero_area < 0 or numero_area >= sizeAreas:
    print("Número de área inválido.")
    return
  else:
    inserir_dados(True, numero_area)
  


def menu_principal():
  while True:
    print("\nMenu Principal")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualização de dados")
    print("4. Deleção de dados")
    print("5. Sair do programa")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
      inserir_dados(False, -1)
    elif opcao == '2':
      exibir_dados()
    elif opcao == '3':
      atualizar_dados()
    elif opcao == '4':
      deletar_dados()
    elif opcao == '5':
      print("Saindo do programa. Até logo!")
      break
    else:
      print("Opção inválida. Tente novamente.")

menu_principal()
