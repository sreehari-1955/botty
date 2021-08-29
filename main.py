from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import discord
import random
import os

import requests

client = discord.Client()

syllabus = {
    "maths": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Mathematics_Sr.Sec_2021-22.pdf",
    "phy": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Physics_2021-22.pdf",
    "chem": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Chemistry_2021-22.pdf",
    "cs": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Computer_Science_Sr.Sec_2021-22.pdf",
    "eng": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Eng-Core_2021-22.pdf",
    "bio": "http://cbseacademic.nic.in/web_material/CurriculumMain22/termwise/SrSecondary/Biology_2021-22.pdf",
}

images = [
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/6-1597330368.jpg?crop=0.5xw:1xh;center,top&resize=980:*",
    "https://gumlet.assettype.com/freepressjournal/2021-01/b22d2143-8846-4d14-b819-ae037e44e622/freepressjournal_2020_09_d68629d6_9da1_4911_b206_df52bf01c03a_FB_IMG_1600849212941.jpg?w=720&dpr=1.0",
    "https://i.pinimg.com/originals/fa/85/c2/fa85c27386f8c6e7a42ffe91f32aa807.jpg",
    "https://drivetribe.imgix.net/AABVrGVgQRS4NiikLYtPxQ?w=300&h=297&auto=format,compress&fit=crop&crop=faces",
    "https://i.pinimg.com/originals/6a/d3/43/6ad343b7d3d60c2494e285565418133d.jpg",
    "https://pics.me.me/twouldbegr-woucould-send-hat-link-16137285.png",
    "https://i.chzbgr.com/full/10747653/hEAAD9A69/of-zelda-proud-link-noises-shef-kitchen-pixelated-food-short-story-link-screaming-character-jumping",
    "https://www.memecreator.org/static/images/memes/5286815.jpg"
]


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    msg = message.content
    chsend = message.channel
    if message.author == client.user:
        return
    if message.content.startswith(".hello"):
        embedVar = discord.Embed(
            title="Hello mate",
            description="This is a bot used for study purposes.\n Here are the listed commands you could use for the syllabus and other resources\n",
            color=0xE10600,
        )
        embedVar.add_field(
            name="CBSE curriculum 2021-22",
            value="1.English:- .eng\n 2.Maths:- .maths\n 3.Physics:- .phy\n 4.Chemistry:- .chem\n 5.Computer Science:- .cs\n 6.Biology:- .bio",
            inline=True,
        )
        embedVar.add_field(
            name="For Fun", value="1. .pog\n 2. .sreeharisidot\n 3. .roll", inline=False
        )
        embedVar.set_footer(
            icon_url="https://www.clipartmax.com/png/small/262-2620113_cbse-logo-central-board-of-secondary-education.png",
            text=f"Godspeed",
        )

        await message.channel.send(embed=embedVar)

    if msg.startswith(".maths"):
        await chsend.send(syllabus["maths"])

    if msg.startswith(".phy"):
        await chsend.send(syllabus["phy"])

    if msg.startswith(".chem"):
        await chsend.send(syllabus["chem"])

    if msg.startswith(".cs"):
        await chsend.send(syllabus["cs"])

    if msg.startswith(".eng"):
        await chsend.send(syllabus["eng"])

    if msg.startswith(".bio"):
        await chsend.send(syllabus["bio"])

    if msg.startswith(".sreeharisidot"):
        await chsend.send(
            "*Omaewa mou shindeiru*\n https://tenor.com/view/omae-wa-mou-shindeiru-nani-gif-10484287"
        )

    if msg.startswith(".roll"):
        await chsend.send(
            "creamroll\n rickroll\n https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825"
        )

    if msg.startswith(".pog"):
        await chsend.send("https://i.imgur.com/aV4iP9W.gif")

    if message.content.startswith(".meme"):
        embedVar = discord.Embed()
        random_num = random.randint(1,100) # rand num b.w 1, 100
        random_link = f'https://memegenerator.net/img/images/{random_num}.jpg' # string interpolation
        embedVar.set_image(url=random_link)
        await message.channel.send(embed=embedVar)

client.run(os.getenv("TOKEN"))
