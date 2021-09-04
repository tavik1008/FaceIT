import discord
from discord.ext import commands
from discord.ext import tasks
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageOps, ImageColor
from io import BytesIO
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@tasks.loop(minutes=1)
async def banner():
    id = 693835534694350888
    members = sum([len(ch.members) for ch in bot.get_guild(id).voice_channels])
    with Image.open("baner.png") as im:
        draw = ImageDraw.Draw(im)
        fnt_1 = ImageFont.truetype("Arial.ttf", size=160)
        id = 693835534694350888
        draw.text((1000, 860), f"{str(members)}", font=fnt_1)
        fnt_2 = ImageFont.truetype("Arial.ttf", size=160)
        draw.text((990, 640), str(bot.get_guild(id).member_count), font=fnt_2)
        fnt_3 = ImageFont.truetype("Arial.ttf", size=160)
        draw.text((990, 1100), str(bot.get_guild(id).premium_subscription_count), font=fnt_3)
        return await bot.get_guild(id).edit(banner=get_bio_from_image(im))


def get_bio_from_image(img):
    bio = io.BytesIO()
    bio.name = 'image.png'
    img.save(bio, 'png')
    return bio.getvalue()

@bot.event
async def on_ready():
    banner.start()


bot.run(settings['token'])