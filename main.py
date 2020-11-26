import discord
from colorama import Fore
token = open('token.txt', 'r').read()

if token == '':
    print(f'{Fore.RED}ERROR: TOKEN_NOT_FOUND')
    print(f'DM WRLD#1266 FOR SUPPORT')
else:
    print(f'{Fore.RED}███╗░░░███╗███████╗░██████╗░██████╗░█████╗░░██████╗░███████╗  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░{Fore.RESET}')
    print(f'{Fore.RED}████╗░████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝░██╔════╝  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗{Fore.RESET}')
    print(f'{Fore.RED}██╔████╔██║█████╗░░╚█████╗░╚█████╗░███████║██║░░██╗░█████╗░░  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝{Fore.RESET}')
    print(f'{Fore.RED}██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██║██║░░╚██╗██╔══╝░░  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗{Fore.RESET}')
    print(f'{Fore.RED}██║░╚═╝░██║███████╗██████╔╝██████╔╝██║░░██║╚██████╔╝███████╗  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║{Fore.RESET}')
    print(f'{Fore.RED}╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝{Fore.RESET}')
    print('\n\n')
    print('[1] Message Logger\n[2] Message Logger With Author\n[3] Message Logger with Author and Server\n[4] Message Logger With Author and Server And Channel')
    choice = input('\n\n>>>> ')

    client = discord.Client()
    if choice == '1':
        @client.event
        async def on_message_delete(message):
            print(f'{Fore.LIGHTCYAN_EX}Message Deleted: {message.content}')
        client.run(token, bot=False)
    elif choice == '2':
        @client.event
        async def on_message_delete(message):
            print(f'{Fore.LIGHTCYAN_EX}Message Deleted: {message.content} Author: {message.author}')
        client.run(token, bot=False)
    elif choice == '3':
        @client.event
        async def on_message_delete(message):
            print(f'{Fore.LIGHTCYAN_EX}Message Deleted: {message.content} Author: {message.author} Server: {message.server}')
        client.run(token, bot=False)
    elif choice == '4':
        @client.event
        async def on_message_delete(message):
            print(f'{Fore.LIGHTCYAN_EX}Message Deleted: {message.content} Author: {message.author} Server: {message.guild} Channel: {message.channel}')
        client.run(token, bot=False)

