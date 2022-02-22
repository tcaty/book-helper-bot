from data.config import ERRORS_FILE_PATH


def write_error(username: str, first_name: str, last_name: str, chat_id: str, message_text: str, exception):
    with open(ERRORS_FILE_PATH, 'a') as file:
        file.write(
            f'\n\nUsername: {username} \n'
            f'First name: {first_name} \n'
            f'Last name: {last_name} \n'
            f'Chat id: {chat_id} \n\n'
            f'Message text: {message_text} \n\n'
            f'Exception: {exception} \n\n'
            f'{"=" * 40}'
        )
