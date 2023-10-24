import os
from dependency_injector import containers, providers
from services.weather_service import WeatherService

env_val = os.getenv("WeatherType")

if env_val == '0':
    from repositories.weather_repo_txt import WeatherRepo
elif env_val == '1':
    from repositories.weather_repo_db import WeatherRepo
else:
    # default
    from repositories.weather_repo_txt import WeatherRepo


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )
    service = providers.Factory(
        WeatherService,
        repo=repo,
    )
