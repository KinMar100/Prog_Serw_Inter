from dependency_injector import containers, providers

from repositories.weather_repo_db import WeatherRepo
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
