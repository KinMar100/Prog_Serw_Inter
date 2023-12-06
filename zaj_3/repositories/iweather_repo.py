from abc import ABC


# interface

class IWeatherRepo(ABC):
    def get_data(self) -> str:
        pass
