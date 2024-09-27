from consumidor.kafka_consumidor import KafkaConsumidorCliente


def main():
    kafka_consumer = KafkaConsumidorCliente(
        bootstrap_servers='localhost:9092',
        group_id='weather_grupo',
        topico='topico_tempo'
    )

    kafka_consumer.consumidor_mensagens()


if __name__ == '__main__':
    main()
