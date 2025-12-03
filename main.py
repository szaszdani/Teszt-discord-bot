import discord
import os
from keep_alive import keep_alive 

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    exit()

TARGET_USER_IDS = [
    217390116728078336,
    520266857442312194
]

FIX_NICKNAME = "Trashstappen (Fos Bull)" 

intents = discord.Intents.default()
intents.members = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot bejelentkezve, mint: {client.user}!")
    print(f"Figyelt ID-k: {TARGET_USER_IDS}")
    print("---")

@client.event
async def on_member_update(before, after):
   
    if after.id not in TARGET_USER_IDS:
        return
    
    if before.nick != after.nick:
        if after.nick != FIX_NICKNAME:
            try:
                await after.edit(nick=FIX_NICKNAME)
                
                print(f"BLOKKOLVA: Visszaállítva {after.name} nevéről. Cél ID: {after.id}")
                
            except discord.Forbidden:
                print(f"HIBA: Nincs jogom átnevezni a célfelhasználót: {after.name}. ID: {after.id}")
            except Exception as e:
                print(f"Általános hiba történt az átnevezés során: {e}")


keep_alive() 

client.run(TOKEN)
