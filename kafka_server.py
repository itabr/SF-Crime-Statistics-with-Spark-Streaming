import producer_server
import pathlib

TOPIC_NAME = 'com.udacity.service.calls'
SERVER_URL = 'localhost:99'
CLIENT_ID = 'com.udacity.dep.police.broker'

def run_kafka_server():
	# TODO get the json file path
    input_file = pathlib.Path(__file__).parent.joinpath('police-department-calls-for-service.json')

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers=SERVER_URL,
        client_id=CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
