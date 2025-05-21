# Modelo de Banco de Dados para Monitoramento de Culturas

Este documento descreve o modelo de banco de dados utilizado para monitoramento de culturas em uma plantação, utilizando sensores de umidade, pH e nutrientes.

## Entidades

### Sensores
- **id_sensor** (INT,  PRIMARY KEY, AUTO_INCREMENT , NOT NULL)
- **sensor_tipo** (VARCHAR(50), NOT NULL)
- **sensor_local** (VARCHAR(100), NOT NULL)
- **id_planta** (INT, NOT NULL, FOREIGN KEY referencing Plantacao(id_planta))

### Plantacao
- **id_planta** (INT,  PRIMARY KEY, AUTO_INCREMENT , NOT NULL)
- **cultura** (VARCHAR(100), NOT NULL)
- **area_planta** (DECIMAL(10,2), NOT NULL)
- **local_planta** (VARCHAR(100), NOT NULL)

### Dados_do_sensor
- **id_sens_dado** (INT, PRIMARY KEY, AUTO_INCREMENT , NOT NULL)
- **umidade** (INT, NOT NULL)
- **ajuste_data** (DATETIME, NOT NULL)
- **ph_valor** (DECIMAL(4,2), NOT NULL)
- **nutri_qntd** (DECIMAL(5,2), NOT NULL)
- **dado_clima** (VARCHAR(100), NOT NULL)
- **id_sensor** (INT, NOT NULL, FOREIGN KEY referencing Sensores(id_sensor))

## Relacionamentos
- Uma **Plantacao** pode ter vários **Sensores** (1:N)
- Um **Sensor** coleta múltiplas **Leituras de Dados** (1:N)

## Tipos de Dados
| Entidade         | Atributo         | Tipo de Dado                  |
|------------------|------------------|-------------------------------|
| Sensores         | id_sensor        | INT                           |
| Sensores         | sensor_tipo      | VARCHAR(50)                   |
| Sensores         | sensor_local     | VARCHAR(100)                  |
| Sensores         | id_planta        | INT                           |
| Plantacao        | id_planta        | INT                           |
| Plantacao        | cultura          | VARCHAR(100)                  |
| Plantacao        | area_planta      | DECIMAL(10,2)                 |
| Plantacao        | local_planta     | VARCHAR(100)                  |
| Dados_do_sensor   | id_sens_dado    | INT                           |
| Dados_do_sensor   | umidade          | INT                          |
| Dados_do_sensor   | ajuste_data      | DATETIME                     |
| Dados_do_sensor   | ph_valor         | DECIMAL(4,2)                 |
| Dados_do_sensor   | nutri_qntd      | DECIMAL(5,2)                  |
| Dados_do_sensor   | dado_clima       | VARCHAR(100)                 |
| Dados_do_sensor   | id_sensor        | INT                          |

## Diagrama Entidade-Relacionamento
![Diagrama](https://github.com/user-attachments/assets/f95da7e8-6729-4582-aa79-41d3d7c6a706)

