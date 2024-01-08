from avant.messaging import Driver
from avant.messaging import consumer


async def handler(value: bytes):
    print(f'received message {value}')
    return False


async def run_producer(config_path, name):
    driver: Driver = Driver.driver_from_config(config_path)

    async with driver.producer('avant-msg-test') as producer:
        count = 0
        while True:
            count += 1
            msg = f'{name}: Number {count}'.encode()
            await producer.send(key=f"something {name}".encode(), msg=msg)
            print(f'sent message {msg}')
            await asyncio.sleep(1)


async def start():
    await asyncio.gather(
        run_producer('/Users/jabbot18/Documents/source/messaging-client/avant-msg-test/consumer.ini', 'avant-msg-test1'),
        run_producer('/Users/jabbot18/Documents/source/messaging-client/avant-msg-test/consumer.ini', 'avant-msg-test2'),
        # consumer.main('/Users/jabbot18/Documents/source/messaging-client/avant-msg-test/consumer.ini', 'avant-msg-test')
    )


if __name__ == '__main__':
    import asyncio
    asyncio.run(start())
 