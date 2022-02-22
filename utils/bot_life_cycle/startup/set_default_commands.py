from aiogram import Dispatcher
from aiogram.types import BotCommand

from data.commands import commands


async def set_default_commands(dp: Dispatcher):
    default_commands = [BotCommand(command.name, command.description) for command in commands.get_commands() if command.default]
    await dp.bot.set_my_commands(default_commands)
