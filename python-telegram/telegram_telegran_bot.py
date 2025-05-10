import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Cargar las variables del archivo .env
load_dotenv()

# Reemplaza con tu api_id y api_hash
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

# Nombre del archivo de sesión
client = TelegramClient('my_session', api_id, api_hash)

async def main():
    await client.start()

    # Obtener tus datos
    me = await client.get_me()
    print(me.stringify())

    # Enviar un mensaje a ti mismo como prueba
    group_username = os.getenv('GROUP_USERNAME')
    await client.send_message(group_username, 'English Learning Test')

with client:
    client.loop.run_until_complete(main())