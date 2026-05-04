import discord
from discord.ext import commands
from discord import app_commands
import os
from flask import Flask
from threading import Thread

# 24時間維持用
app = Flask('')
@app.route('/')
def home(): return "Bot is alive!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # スラッシュコマンドを登録
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="loopvc", description="VCに参加します")
async def loopvc(interaction: discord.Interaction):
    if interaction.user.voice:
        await interaction.user.voice.channel.connect()
        await interaction.response.send_message("接続したよ！")
    else:
        await interaction.response.send_message("先にVCに入ってね。")

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
