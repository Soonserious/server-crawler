import enum


class Singleton:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

class Address(Singleton):
    address_list =[]
    current_page = 0;
    search_engine = None

    def set_search_engine(self, search_engine):
        self.search_engine = SearchEngine(search_engine)

    def set_address_list(self, address_list):
        self.address_list = address_list

    def get_address_list(self):
        address = self.address_list[self.current_page]
        self.current_page += 1
        return address

class SearchEngineManager(Singleton):

    def get_search_engine(self, search_engine):
        result = None
        if search_engine == "naver":
            result = SearchEngine.NAVER
        return result

class SearchEngine(bytes, enum.Enum):

    def __new__(cls, value, tag, wrong_tag, search_engine_url, keyword_encoding):
        obj = bytes.__new__(cls, [value])
        obj._value = value
        obj.tag = tag
        obj.wrong_tag = wrong_tag

    NAVER = ('naver', 'sp_nws', 'not_found','https://search.naver.com/search.naver?where=news&sm=tab_jum&query=', None)

if __name__ == "__main__":
    address = Address.instance()
    address.set_search_engine("naver")
