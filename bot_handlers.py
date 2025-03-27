from aiogram import types, Dispatcher
from avito_booster import promote_ad
import traceback

user_tasks = {}

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def start_cmd(message: types.Message):
        await message.answer("✅ Welcome! Send me your Avito link to start promotion.")

    @dp.message_handler(lambda m: m.text.startswith("http"))
    async def handle_ad_link(message: types.Message):
        user_tasks[message.from_user.id] = {"link": message.text}
        await message.answer("📍 Now, enter the city for promotion:")

    @dp.message_handler(lambda m: message.from_user.id in user_tasks and "city" not in user_tasks[message.from_user.id])
    async def handle_city(message: types.Message):
        user_tasks[message.from_user.id]["city"] = message.text
        await message.answer("🔎 Enter a search query to find your ad:")

    @dp.message_handler(lambda m: message.from_user.id in user_tasks and "query" not in user_tasks[message.from_user.id])
    async def handle_query(message: types.Message):
        try:
            user_tasks[message.from_user.id]["query"] = message.text
            task = user_tasks.pop(message.from_user.id)
            await message.answer("⏳ Promoting your ad... Please wait about 30 seconds.")
            await promote_ad(task["city"], task["query"])
            await message.answer("✅ Promotion completed successfully!")
        except Exception as e:
            print(traceback.format_exc())
            await message.answer(f"❌ Promotion failed.\n\nError:\n{e}")
