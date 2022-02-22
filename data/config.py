from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMIN_CHAT_ID = env.int('ADMIN_CHAT_ID')

DEVELOPMENT = env.bool('DEVELOPMENT')

SHELVE_STORAGE_PATH = env.str('SHELVE_STORAGE_PATH')
ERRORS_FILE_PATH = env.str('ERRORS_FILE_PATH')
