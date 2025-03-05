import discord
from discord.ext import commands, tasks
import asyncio
import datetime
import ssl
import certifi
import re

ssl_context = ssl.create_default_context(cafile=certifi.where())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

reminders = {}

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    checkReminders.start()

@tasks.loop(seconds=1)
async def checkReminders():
    current_time = datetime.datetime.now()
    to_remove = []
    for user_id, reminder_list in reminders.items():
        for reminder in reminder_list:
            if reminder['time'] <= current_time:
                user = await bot.fetch_user(user_id)
                await user.send(f"Reminder: {reminder['message']}")
                to_remove.append((user_id, reminder))
    
    for user_id, reminder in to_remove:
        reminders[user_id].remove(reminder)
        if not reminders[user_id]:
            del reminders[user_id]

@bot.command(name='setReminder')
async def setReminder(ctx, date: str, time: str, *, message: str):
    try:
        reminder_time = datetime.datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
        if ctx.author.id not in reminders:
            reminders[ctx.author.id] = []
        reminders[ctx.author.id].append({'time': reminder_time, 'message': message})
        await ctx.send(f'Reminder set for {date} {time}')
    except ValueError:
        await ctx.send('Invalid date/time format. Use YYYY-MM-DD HH:MM')

@bot.command(name='setReminderIn')
async def setReminderIn(ctx, time_str: str, *, message: str):
    time_pattern = re.compile(r'(\d+)([smh])')
    matches = time_pattern.findall(time_str)
    
    if not matches:
        await ctx.send('Invalid time format. Use the format like "10s", "5m", "2h".')
        return
    
    total_seconds = 0
    for amount, unit in matches:
        if unit == 's':
            total_seconds += int(amount)
        elif unit == 'm':
            total_seconds += int(amount) * 60
        elif unit == 'h':
            total_seconds += int(amount) * 3600
    
    reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=total_seconds)
    if ctx.author.id not in reminders:
        reminders[ctx.author.id] = []
    reminders[ctx.author.id].append({'time': reminder_time, 'message': message})
    await ctx.send(f'Reminder set for {time_str} from now')

@bot.command(name='deleteReminder')
async def deleteReminder(ctx, index: int):
    if ctx.author.id in reminders and 0 <= index < len(reminders[ctx.author.id]):
        removed = reminders[ctx.author.id].pop(index)
        await ctx.send(f'Reminder "{removed["message"]}" deleted.')
        if not reminders[ctx.author.id]:
            del reminders[ctx.author.id]
    else:
        await ctx.send('Invalid reminder index.')

@bot.command(name='modifyReminder')
async def modifyReminder(ctx, index: int, date: str, time: str, *, message: str):
    try:
        reminder_time = datetime.datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
        if ctx.author.id in reminders and 0 <= index < len(reminders[ctx.author.id]):
            reminders[ctx.author.id][index] = {'time': reminder_time, 'message': message}
            await ctx.send(f'Reminder modified to {date} {time}')
        else:
            await ctx.send('Invalid reminder index.')
    except ValueError:
        await ctx.send('Invalid date/time format. Use YYYY-MM-DD HH:MM')

@bot.command(name='createPoll')
async def createPoll(ctx, question: str, *options: str):
    if len(options) > 10:
        await ctx.send('You can only provide a maximum of 10 options.')
        return
    if len(options) < 2:
        await ctx.send('You need to provide at least 2 options.')
        return

    embed = discord.Embed(title=question, description="\n".join([f"{i+1}. {option}" for i, option in enumerate(options)]))
    message = await ctx.send(embed=embed)

    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    for i in range(len(options)):
        await message.add_reaction(reactions[i])

bot.run('MTM0NjgwMTYwMDUyNTUwNDU1Mg.G1QMG6.A8PFwApketDegNQlaQ_8srCTnmXITC0r99alJI')