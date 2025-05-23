import boto3


def enviar_alerta_email(umidade, ph, temperatura):
    sns = boto3.client("sns", region_name="us-east-2")

    mensagem = (
        f"⚠️ ALERTA CRÍTICO – IRRIGAÇÃO\n\n"
        f"Umidade: {umidade}%\n"
        f"pH: {ph}\n"
        f"Temperatura: {temperatura}°C\n\n"
        f"Ação recomendada: ativar irrigação manual ou verificar sensores."
    )

    response = sns.publish(
        TopicArn="arn:aws:sns:us-east-2:586139607549:alerta-irrigacao",
        Subject="🚨 Alerta de Irrigação – Sistema Agrícola",
        Message=mensagem,
    )

    return response
