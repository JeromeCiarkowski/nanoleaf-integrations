# standard library
import os
import random

# third-party
from discord.ext import commands
from dotenv import load_dotenv
from nanoleafapi import discovery
from nanoleafapi import Nanoleaf

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
NANOLEAF_IP_ADDRESS = os.getenv("NANOLEAF_IP_ADDRESS")
NANOLEAF_AUTH_TOKEN = os.getenv("NANOLEAF_AUTH_TOKEN")

MALFORMED_MESSAGE_ERROR_MESSAGE = "Malformed message received. Nothing happened!"

nanoleaf = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

bot = commands.Bot(command_prefix="!nanoleaf ")


@bot.command(name="debugger", help='Type "!nanoleaf debugger" to debug.')
async def debugger(ctx, arg=None, *args):
    breakpoint()


@bot.command(name="connect", help="Performs functionality related to connection")
async def connect(ctx, ip_address):
    # TODO everything
    pass


@bot.command(name="identify", help="Performs functionality related to identification")
async def identify(ctx):
    # TODO everything
    pass


@bot.command(name="power", help="Performs functionality related to power")
async def power(ctx, arg):
    if arg == "on":
        nanoleaf.power_on()
    elif arg == "off":
        nanoleaf.power_off()
    elif arg == "toggle":
        nanoleaf.toggle_power()
    else:
        await ctx.send(MALFORMED_MESSAGE_ERROR_MESSAGE)

    status = (
        f"Nanoleaf is powered on."
        if nanoleaf.get_power()
        else f"Nanoleaf is powered off."
    )
    await ctx.send(status)


@bot.command(name="color", help="Performs functionality related to color")
async def color(ctx, *args):
    if len(args) == 1:
        if args[0].isalpha():
            if args[0] == "white":
                color = (255, 255, 255)
            if args[0] == "red":
                color = (255, 0, 0)
            elif args[0] == "orange":
                color = (255, 127, 0)
            elif args[0] == "yellow":
                color = (255, 255, 0)
            elif args[0] == "green":
                color = (0, 255, 0)
            elif args[0] == "blue":
                color = (0, 0, 255)
            elif args[0] == "indigo":
                color = (46, 43, 95)
            elif args[0] == "violet":
                color = (139, 0, 255)
            else:
                await ctx.send(MALFORMED_MESSAGE_ERROR_MESSAGE)
            nanoleaf.set_color(color)
        elif args[0].isnumeric():
            color = (int(args[0]), int(args[0]), int(args[0]))
            nanoleaf.set_color(color)
        else:
            await ctx.send(MALFORMED_MESSAGE_ERROR_MESSAGE)
            return
    elif len(args) == 3:
        if all([arg.lstrip("-").isnumeric() for arg in args]):
            color = (int(args[0]), int(args[1]), int(args[2]))
            nanoleaf.set_color(color)
        else:
            await ctx.send(MALFORMED_MESSAGE_ERROR_MESSAGE)
            return
    else:
        await ctx.send(MALFORMED_MESSAGE_ERROR_MESSAGE)
        return

    status = f"Nanoleaf color is {color}."
    await ctx.send(status)


@bot.command(name="brightness", help="Performs functionality related to brightness")
async def brightness(ctx, arg=None):
    if arg:
        if arg.isnumeric():
            nanoleaf.set_brightness(int(arg))

    status = f"Nanoleaf brightness is {nanoleaf.get_brightness()}"
    await ctx.send(status)


@bot.command(name="hue", help="Performs functionality related to hue")
async def hue(ctx, arg=None):
    if arg == None:
        nanoleaf.get_hue()
    else:
        try:
            nanoleaf.set_hue(int(arg))
        except Exception as e:
            temp = "orary"
            # TODO error handling

    status = f"Nanoleaf hue is {nanoleaf.get_hue()}."
    await ctx.send(status)


@bot.command(name="saturation", help="Performs functionality related to saturation")
async def saturation(ctx, arg=None):
    if arg == None:
        nanoleaf.get_saturation()
    else:
        try:
            nanoleaf.set_saturation(int(arg))
        except Exception as e:
            temp = "orary"
            # TODO error handling

    status = f"Nanoleaf saturation is {nanoleaf.get_saturation()}."
    await ctx.send(status)


@bot.command(
    name="color_temperature", help="Performs functionality related to color temperature"
)
async def color_temperature(ctx, arg=None):
    if arg == None:
        nanoleaf.get_color_temp()
    else:
        try:
            nanoleaf.set_color_temp(int(arg))
        except Exception as e:
            temp = "orary"
            # TODO error handling

    status = f"Nanoleaf color temperature is {nanoleaf.get_color_temp()}."
    await ctx.send(status)


@bot.command(name="effects", help="Performs functionality related to effects")
async def effects(ctx, arg=None):
    if arg:
        try:
            nanoleaf.set_effect(arg)
        except Exception as e:
            temp = "orary"
            # TODO error handling

    status = (
        f"Nanoleaf current effect:\n{nanoleaf.get_current_effect()}\n\nNanoleaf available effects:\n"
        + "\n".join(effect for effect in nanoleaf.list_effects())
    )
    await ctx.send(status)


bot.run(TOKEN)
