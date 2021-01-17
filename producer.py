from json import dumps
from kafka import KafkaProducer
from data_simulator import data, images

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
producer.send('topic_name', data)
producer.send('topic_name', images)
