import discord
from discord.ext import commands, tasks
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageOps, ImageColor
from io import BytesIO
import io
import os

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@tasks.loop(minutes=1)
async def banner():
    id = 693835534694350888
    members = sum([len(ch.members) for ch in bot.get_guild(id).voice_channels])
    with Image.open("Framee.png") as img:
        draw = ImageDraw.Draw(img)
        fnt_1 = ImageFont.truetype("DrukCyr-Super.ttf", size=90)
        id = 693835534694350888
        draw.text((740, 380), f"{str(members)}", font=fnt_1)
        fnt_2 = ImageFont.truetype("DrukCyr-Super.ttf", size=90)
        draw.text((615, 270), str(bot.get_guild(id).member_count), font=fnt_2)
        fnt_3 = ImageFont.truetype("DrukCyr-Super.ttf", size=160)
        draw.text((1000, 1000), str(bot.get_guild(id).premium_subscription_count), font=fnt_3)
        return await bot.get_guild(id).edit(banner=get_bio_from_image(img))


def get_bio_from_image(img):
    bio = io.BytesIO()
    bio.name = 'image.png'
    img.save(bio, 'png')
    return bio.getvalue()


@bot.event
async def on_ready():
    banner.start()


bot.run('NzMzOTgxMzA4MDE5MDE1NzEw.XxLDXA.TSFC-M3w2s32pSG9EB2ImxBTqc0')