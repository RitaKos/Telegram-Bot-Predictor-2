from dataclasses import dataclass
from environs import Env


@dataclass
class TelegramBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TelegramBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(tg_bot=TelegramBot(
        token=env.str("BOT_TOKEN"),
        admin_ids=list(map(int, env.list("ADMINS"))))
    )
