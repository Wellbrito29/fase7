library(httr)
library(jsonlite)

# Definir coordenadas para São Paulo
latitude <- -23.5505
longitude <- -46.6333

# URL da API Open Meteo para dados atuais
url <- paste0("https://api.open-meteo.com/v1/forecast?latitude=", latitude,
              "&longitude=", longitude, "&hourly=temperature_2m,precipitation")

# Fazer a requisição
response <- GET(url)

# Verificar se a requisição foi bem-sucedida
if (status_code(response) == 200) {
  # Converter a resposta JSON em um data frame
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))
  
  
  temperatures <- data$hourly$temperature_2m
  media <- mean(temperatures)
  desvio_padrao <- sd(temperatures)
  # Exibir os dados
  
  print("--------Dados----------")
  print(paste("Média de temperatura",media))
  print(paste("Desvio padrão temperatura",desvio_padrao))
} else {
  print(paste("Erro ao conectar-se à API. Status code:", status_code(response)))
  print(content(response, "text", encoding = "UTF-8"))

# -------------------------------------------------------------------------

  
}
