from Publisher import Publisher
from Subscriber import Subscriber

if __name__ == '__main__':
    pub = Publisher()
    pub.puslish("No one will receive this message!")
    print()

    sub1 = Subscriber()
    pub.subscribe(sub1)
    pub.puslish("Only first subscriber will receive this message!")
    print()

    sub2 = Subscriber()
    pub.subscribe(sub2)
    pub.puslish("Both subscribers will receive this message!")
    print()

    pub.unsubscribe(sub1)
    pub.puslish("Only second subscriber will receive this message!")
    print()