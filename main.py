import random

import discord
from discord.ext import commands, tasks
import aiohttp


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents,
    help_command=None
)




@tasks.loop(seconds=1)
async def dexscreener_loop():
    channel = bot.get_channel(1310044096194416711)
    if not channel:
        print("Could not find dexscreener channel")
        return

    url = "https://api.dexscreener.com/latest/dex/tokens/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    return
                
                data = await response.json()
                
                if not data.get('pairs') or len(data['pairs']) == 0:
                    return
                
                pair = data['pairs'][0]
                
                embed = discord.Embed(
                    title=f"🔍 ${pair['baseToken']['name']} ({pair['baseToken']['symbol']})",
                    url=pair['url'],
                    color=0x00ff00,
                    timestamp=discord.utils.utcnow()
                )
                
                embed.add_field(
                    name="💰 Price USD",
                    value=f"${pair.get('priceUsd', 'N/A')}",
                    inline=True
                )
                
                if pair.get('fdv'):
                    embed.add_field(
                        name="📊 Market Cap",
                        value=f"${'{:,.2f}'.format(pair['fdv'])}",
                        inline=True
                    )
                
                if pair.get('liquidity', {}).get('usd'):
                    embed.add_field(
                        name="💧 Liquidity",
                        value=f"${'{:,.2f}'.format(pair['liquidity']['usd'])}",
                        inline=True
                    )
                
                async for message in channel.history(limit=1):
                    last_message = message
                    if last_message.author == bot.user:
                        await last_message.edit(embed=embed)
                        return
                
                await channel.send(embed=embed)
                
        except Exception as e:
            print(f"Error in dexscreener loop: {e}")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    dexscreener_loop.start()
    print("------")

bot.run("YOUR TOKEN")
