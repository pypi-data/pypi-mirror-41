asynqp
======

[![Build Status](https://travis-ci.org/benjamin-hodgson/asynqp.svg?branch=master)](https://travis-ci.org/benjamin-hodgson/asynqp)
[![Documentation Status](https://readthedocs.org/projects/asynqp/badge/?version=v0.4)](https://readthedocs.org/projects/asynqp/?badge=v0.4)
[![Coverage Status](https://coveralls.io/repos/benjamin-hodgson/asynqp/badge.svg?branch=master&service=github)](https://coveralls.io/github/benjamin-hodgson/asynqp?branch=master)
[![Requirements Status](https://requires.io/github/benjamin-hodgson/asynqp/requirements.svg?branch=master)](https://requires.io/github/benjamin-hodgson/asynqp/requirements/?branch=master)

`asynqp` is an AMQP (aka [RabbitMQ](rabbitmq.com)) client library for
Python 3.4's new [`asyncio`](https://docs.python.org/3.4/library/asyncio.html) module.

Check out the [official documentation](http://asynqp.readthedocs.org/).


Example
-------

```python
import asyncio
import asynqp


@asyncio.coroutine
def hello_world():
    """
    Sends a 'hello world' message and then reads it from the queue.
    """
    # connect to the RabbitMQ broker
    connection = yield from asynqp.connect('localhost', 5672, username='guest', password='guest')

    # Open a communications channel
    channel = yield from connection.open_channel()

    # Create a queue and an exchange on the broker
    exchange = yield from channel.declare_exchange('test.exchange', 'direct')
    queue = yield from channel.declare_queue('test.queue')

    # Bind the queue to the exchange, so the queue will get messages published to the exchange
    yield from queue.bind(exchange, 'routing.key')

    # If you pass in a dict it will be automatically converted to JSON
    msg = asynqp.Message({'hello': 'world'})
    exchange.publish(msg, 'routing.key')

    # Synchronously get a message from the queue
    received_message = yield from queue.get()
    print(received_message.json())  # get JSON from incoming messages easily

    # Acknowledge a delivered message
    received_message.ack()

    yield from channel.close()
    yield from connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())
```


Installation
------------

`asynqp` is [on the Cheese Shop](https://pypi.python.org/pypi/asynqp), so you can install it using Pip:
```
pip install asynqp
```

If you want the latest development version, you can install it from source:
```
git clone https://github.com/benjamin-hodgson/asynqp.git
cd asynqp
python setup.py install
```
