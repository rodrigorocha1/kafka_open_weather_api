from kafka import KafkaProducer
import json
from typing import Dict


class KafkaProdutorCliente:
    def __init__(self, bootstrap_servers: str) -> None:
        self.__produtor = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )

    def enviar_mensagem(self, topico: str, mensagem: Dict):
        self.__produtor.send(topic=topico, value=mensagem)
        self.__produtor.flush()
