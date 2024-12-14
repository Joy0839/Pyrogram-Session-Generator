import nest_asyncio
import asyncio
from pyrogram import Client
from pyrogram.errors import RPCError

# Apply nest_asyncio to handle event loop conflicts
nest_asyncio.apply()

async def generate_session_string(api_id, api_hash, phone_number):
    try:
        async with Client("my_account", api_id, api_hash, phone_number=phone_number) as app:
            session_string = await app.export_session_string()
            print("Your Pyrogram Session String is:")
            print(session_string)
    except RPCError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Collect user inputs
    api_id = int(input("Enter your API ID: "))
    api_hash = input("Enter your API Hash: ")
    phone_number = input("Enter your phone number (with country code, no '+' or '00'): ")

    # Run the async function
    asyncio.run(generate_session_string(api_id, api_hash, phone_number))
