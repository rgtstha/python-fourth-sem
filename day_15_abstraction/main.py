from abc import ABC, abstractmethod

class DataFetcher(ABC):

    @abstractmethod
    def fetch_data(self, url):
        pass

class ServerDataFetcher(DataFetcher):
    def fetch_data(self, url):
        print("Fetching data from server")
        return f"Network data for {url}"
    
class CacheDataFetcher(DataFetcher):
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        self.cache = {}
        
    def fetch_data(self, url):

        if url in self.cache:
            print("Fetching data from cache")
            return self.cache[url]
        
        else:
            data = self.data_fetcher.fetch_data(url)
            self.cache[url] = data
            return data
        
server = ServerDataFetcher()
cache = CacheDataFetcher(server)

print(cache.fetch_data("www.facebook.com/posts"))
print(cache.fetch_data("www.facebook.com/posts"))