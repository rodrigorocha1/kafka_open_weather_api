from produtor.kafka_produtor_cliente import KafkaProdutorCliente
from servico.tempo_service import TempoService
import time


def main():
    kafka_produtor = KafkaProdutorCliente(bootstrap_servers='localhost:9092')
    servico_tempo = TempoService()

    cidades = ['Ribeirão Preto', 'Sertãozinho']
    while True:
        for cidade in cidades:
            dados_tempo = servico_tempo.obter_tempo_atual(cidade=cidade)
            kafka_produtor.enviar_mensagem(
                topico='topico_tempo', mensagem=dados_tempo)
        time.sleep(60)


if __name__ == '__main__':
    main()
