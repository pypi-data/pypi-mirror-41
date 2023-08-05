Messaging queue library for the LHCb continuous integration system
==================================================================

Description
-----------

This python module contains an implementation of the interface to rabbitmq for the LHCb Nightly builds.

It relies on RabbitMQ priority queues to handle commands sent in the right order.

The files are the following:
* Common.py: Common tools to interface with the queue...
* CvmsfsDevExchange.py: methods to send and receive messages


Usage
-----

To send a command to the queue, you need to create a connection to RabbitMQ using the get_connection
utility and create a *
```python

from lbmessaging.CvmfsDevExchange import CvmfsDevExchange
from lbmessaging.Common import get_connection

with get_connection() as connection:
    broker = CvmfsDevExchange(connection)
    broker.send_command("mycommand", [ "args1", "args2"] )

```

The *priority* (integer between 0 and 255) and *retry_count* arguments dictate the policies for handling and retrying 
the command.

To receive
```python

from lbmessaging.CvmfsDevExchange import CvmfsDevExchange
from lbmessaging.Common import get_connection

with get_connection() as connection:
    broker = CvmfsDevExchange(connection)
    message = broker.receive_command()
    (command, args, command_date) = message.body 

```


Handling errors
---------------

In case of error, the method *handle_processing_error* should be used.
It either retries the command  by putting it back into the queue, or sends to an error queue if the number of max retry 
been reached.

c.f. TestCommand.py for an example.


Notes
---------------

Provision a new instance of RabbitMQ can be done using LHCbProvisionRabbitMQ.sh

TODO: Document configuration for the RabbitMQ connection 




