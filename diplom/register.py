from aiogram.types.bot_command import BotCommand


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(dpbot):
    commands = [
        BotCommand(command="/help", description="ПОМОЩЬ"),
        BotCommand(command="/start", description="СТАРТ"),
        BotCommand(command="/cancel", description="ОТМЕНА")
    ]
    await dpbot.set_my_commands(commands)