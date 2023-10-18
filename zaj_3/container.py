import os

from dependency_injector import containers, providers

from repositories.weather_repo_txt import WeatherRepo
from services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )
    service = providers.Factory(
        WeatherService,
        repo=repo,
    )

    try:
        print("a", os.environ["a"])
    except KeyError:
        print("zmienna nie istnieje")


print(os.environ.items())


