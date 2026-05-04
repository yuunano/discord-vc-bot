import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# 24時間動かすためのダミーサーバー
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ボットの処理
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 起動完了")

@bot.command()
async def loopvc(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("VCに接続したよ！")
    else:
        await ctx.send("先にVCに入ってね。")

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
