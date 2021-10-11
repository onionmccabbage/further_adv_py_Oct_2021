# here we will have a news publisher and a few subscribers who need to know when news is broadcast
class NewsPublisher: # this is our observable
    def __init__(self):
        self.__subscribers = [] # no subscribers to begin with!
        self.__latestNews = None
    def attach(self, new_sub): # attach a new subscriber
        self.__subscribers.append(new_sub)
    def detach(self): # remove a subscriber
        self.__subscribers.pop() # remove the last one in our collection
    def subscribers(self):
        # iterate over all the subscribers we have
        return [type(x).__name__ for x in self.__subscribers]
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update() # call the update method on the subscriber
    def addNews(self, news):
        self.__latestNews = news
    def getNews(self):
        return 'News: {}'.format(self.__latestNews)

# some subscribers (these are the observers)
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class PrintSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class MediaSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    # iterate over a collection of subscribers, notify each
    for Subscriber in [MediaSubscriber, PrintSubscriber, EmailSubscriber]:
        Subscriber(news_publisher) # we now have three subscribers to our news service
        news_publisher.addNews('something newsworthy just happened')
        news_publisher.notifySubscribers()