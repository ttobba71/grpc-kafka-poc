import logging

from avant.messaging import consumer
from examples.confluent_kafka_example_producer import CleanedData


# This is an example consumer message handler method.  Every message consumed from the
# Topic or Queue will filter through this method for processing.
async def handler(value: CleanedData):
    print(f'Handled: {value}')


if __name__ == '__main__':
    import asyncio
    import sys

    logging.basicConfig(level=logging.INFO)

    config_path = sys.argv[1]

    asyncio.run(consumer.main(config_path, 'confluent_test'))
