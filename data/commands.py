from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    name: str
    description: str
    default: bool


@dataclass(frozen=True)
class Commands:
    start: Command = Command('start', 'Запустить бота 🤖', True)
    help: Command = Command('help', 'Помощь ❔', True)
    menu: Command = Command('menu', 'Меню 📋', True)
    settings: Command = Command('settings', 'Настройки ⚙️', True)

    def get_commands(self):
        return self.__dict__.values()


commands = Commands()
