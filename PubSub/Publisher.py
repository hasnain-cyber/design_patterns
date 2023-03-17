from Subscriber import Subscriber

class Publisher:
    def __init__(self) -> None:
        self.subscribers = set()

    def subscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.discard(subscriber)

    def puslish(self, message) -> None:
        for subscriber in self.subscribers:
            subscriber.receive_message(message)
