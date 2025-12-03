import discord
import os
from keep_alive import keep_alive 

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    print("HIBA: A 'TOKEN' környezeti változó nincs beállítva. A bot nem indul el.")
    exit()

TARGET_USER_ID = 381205842378096642 

FIX_NICKNAME = "Átnevezés Blokkálva" 

intents = discord.Intents.default()
intents.members = True 

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Bot bejelentkezve, mint: {client.user}!")
    print(f"👀 Figyelt Felhasználó ID: {TARGET_USER_ID}")
    print("---")

@client.event
async def on_member_update(before, after):

    if after.id != TARGET_USER_ID:
        return
    
    if before.nick != after.nick:
        
        if after.nick != FIX_NICKNAME:
            try:
                await after.edit(nick=FIX_NICKNAME)
                print(f"🔥 BLOKKOLVA: Visszaállítva {after.name} nevéről. Cél ID: {after.id}")
            except discord.Forbidden:
                print(f"⚠️ HIBA: Nincs jogom átnevezni a CÉL felhasználót: {after.name}. ID: {after.id}")
            except Exception as e:
                print(f"❌ Általános hiba történt a célfelhasználó átnevezése során: {e}")


keep_alive() 

client.run(TOKEN)
