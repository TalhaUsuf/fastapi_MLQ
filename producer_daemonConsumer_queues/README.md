# Table of Contents

- [Table of Contents](#table-of-contents)
- [Producer](#producer)
- [Consumer](#consumer)



# Producer


[Producer](producer_daemonConsumer_queues\producer.py) is a **non-daemon** thread which puts several items into queue.

# Consumer

[Consumer](producer_daemonConsumer_queues\consumer.py) is a **daemon** thread which eats items from the queue. Since it is daemon hence main code inside [producer](producer_daemonConsumer_queues\producer.py) does not has any ```t2.join()``` statement.




> Code ends when the main thread (contanining producer) ends 