class Subscriber:
    subscriber_count = 0

    def __init__(self) -> None:
        Subscriber.subscriber_count += 1
        self.subscriber_id = Subscriber.subscriber_count

    def receive_message(self, message) -> None:
        print(
            f"Subscriber {self.subscriber_id}: received message: {message}")
