import random
import logging
from .. import loader, utils
from random import randint, choice
logger = logging.getLogger(__name__)

class ArtsSkadMod(loader.Module):
    """Юникод арты"""
    strings = {'name': 'ArtsSkadMod'}

    async def neponalcmd(self, message):
        """Используй .neponal <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>ТЕКСТ ПОСЛЕ КОМАНДЫ ВВЕДИ СУК!</b>')
            return
        else:
            neponal = ("<code>{~x~}\n"
                    "[><]\n"
                    "^  ^\n"
                    "А вот тут я не понял ты что... </code>" + f"<code>{text}</code>")
            await message.edit(neponal)

        if text == "podpiskad":
            await message.edit("<code>{~x~}\n"
                                      "[><]\n"
                                      "^  ^\n"
                               "Я не понял ты ещё не подписался на меня в Инстаграме -></code> @pro100sans")


    async def cowsayscmd(self, message):
        """Используй .cowsays <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нет текста после команды :c</b>')
            return
        else:
            cowsays = ("<code> "
                      f"< {text} >\n"
                      "\n"
                      "     \   ^__^\n"
                      "	     \  (00)\_______\n"
                      "         (__)\  FUCK  )\/\n"
                      "             ||----w||\n"
                      "	            ||     ||</code>")
            await message.edit(cowsays)


    async def padayuqscmd(self, message):
        """Используй .padayus <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ПАДАЮ")
            padayus = ("┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      f"┛┗┛┗┛┃ <b>{text}</b>!\n"
                      "┓┏┓┏┓┃ ＼○／\n"
                      "┛┗┛┗┛┃ /\n"
                      "┓┏┓┏┓┃ノ)\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n")
            await message.edit(padayus)
        else:
            padayus = ("┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      f"┛┗┛┗┛┃ <b>{text}</b>!\n"
                      "┓┏┓┏┓┃ ＼○／\n"
                      "┛┗┛┗┛┃ /\n"
                      "┓┏┓┏┓┃ノ)\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n")
            await message.edit(padayus)


    async def priletelscmd(self, message):
        """Используй .prilitesq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Я ЕБУ СОБАК! ВСЕГДА ГОТОВ! ТРАХНУТЬ НЕСКОЛЬКО КОООТОООВ!")
            prilitels = ("▬▬▬.◙.▬▬▬\n"
                        "  ═▂▄▄▓▄▄▂\n"
                        "◢◤ █▀▀████▄▄▄▄◢◤\n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                        "◥█████◤ прилетел сказать что-то важное...\n"
                        "══╩══╩═\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬☻/ - <b>{text}</b>\n"
                        "╬═╬/▌\n"
                        "╬═╬/ \ ")
            await message.edit(prilitels)
        else:
            prilitels = ("▬▬▬.◙.▬▬▬\n"
                        "  ═▂▄▄▓▄▄▂\n"
                        "◢◤ █▀▀████▄▄▄▄◢◤\n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                        "◥█████◤ прилетел сказать что-то важное...\n"
                        "══╩══╩═\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        f"╬═╬☻/ - <b>{text}</b>\n"
                        "╬═╬/▌\n"
                        "╬═╬/ \ ")
            await message.edit(prilitels)


    async def huytebescmd(self, message):
        """Используй .huytebes <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("МАЯК ТЕБЕ В РОТ!")
            huytebes = ("...............▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       "................▐▄▀▀▀▀▀▄▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "................▐▒▒▒▒▒▒▒▌\n"
                       "..................▀▌▒▀▒▐▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebes)
        else:
            huytebes = ("...............▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       "................▐▄▀▀▀▀▀▄▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "................▐▒▒▒▒▒▒▒▌\n"
                       "..................▀▌▒▀▒▐▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebes)


    async def lolscmd(self, message):
        """Используй .lols."""
        lols = ("┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
               "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
               "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
               "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
               "┗━━━┛╰━━━━╯┗━━━┛\n")
        await message.edit(lols)


    async def fuckyouscmd(self, message):
        """Используй .fuckyous."""
        fuckyous = ("┏━┳┳┳━┳┳┓\n"
                   "┃━┫┃┃┏┫━┫┏┓\n"
                   "┃┏┫┃┃┗┫┃┃┃┃\n"
                   "┗┛┗━┻━┻┻┛┃┃\n"
                   "┏┳┳━┳┳┳┓┏┫┣┳┓\n"
                   "┣┓┃┃┃┃┣┫┃┏┻┻┫\n"
                   "┃┃┃┃┃┃┃┃┣┻┫┃┃\n"
                   "┗━┻━┻━┻┛┗━━━┛\n")
        await message.edit(fuckyous)


    async def housescmd(self, message):
        """Используй .houses."""
        houses = ("╯▅╰╱▔▔▔▔▔▔▔╲╯╯\n"
                 "▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭\n"
                 "▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭\n"
                 "╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲\n"
                 "▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔\n"
                 "▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏\n"
                 "▕┓▔┗┓▔┏▏▕┗▏ ┓▔┏\n")
        await message.edit(houses)


    async def helloscmd(self, message):
        """Используй .hellos."""
        hellos = ("┈┏┓┏┳━┳┓┏┓┏━━┓┈\n"
                 "┈┃┃┃┃┏┛┃┃┃┃┏┓┃┈\n"
                 "┈┃┗┛┃┗┓┃┃┃┃┃┃┃┈\n"
                 "┈┃┏┓┃┏┛┃┃┃┃┃┃┃┈\n"
                 "┈┃┃┃┃┗┓┗┫┗┫╰╯┃┈\n"
                 "┈┗┛┗┻━┻━┻━┻━━┛┈\n")
        await message.edit(hellos)


    async def coffeescmd(self, message):
        """Используй .coffees <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Попей Говна!")
            coffees = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffees)
        else:
            coffees = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffees)


    async def tvscmd(self, message):
        """Используй .tvs <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ТЕЛЕВИЗОР ГОВОРИТ ЧТО ТЫ НЕ ПОДПИСАН НА VitecP")
            tvs = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tvs)
        else:
            tvs = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tvs)


    async def grenscmd(self, message):
        """Используй .grens <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("L♥VE IN A HOLE!")
            grens = ("─▄▀▀███═◯\n"
                    "▐▌▄▀▀█▀▀▄\n"
                    "█▐▌─────▐▌\n"
                    "█▐█▄───▄█▌\n"
                    "▀─▀██▄██▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(grens)
        else:
            grens = ("─▄▀▀███═◯\n"
                    "▐▌▄▀▀█▀▀▄\n"
                    "█▐▌─────▐▌\n"
                    "█▐█▄───▄█▌\n"
                    "▀─▀██▄██▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(grens)


    async def bruhscmd(self, message):
        """Используй .bruhs."""
        bruhs = ("╭━━╮╱╱╱╱╱╭╮\n"
                "┃╭╮┃╱╱╱╱╱┃┃\n"
                "┃╰╯╰┳━┳╮╭┫╰━╮\n"
                "┃╭━╮┃╭┫┃┃┃╭╮┃\n"
                "┃╰━╯┃┃┃╰╯┃┃┃┃\n"
                "╰━━━┻╯╰━━┻╯╰╯\n")
        await message.edit(bruhs)


    async def unoscmd(self, message):
        """Используй .unos."""
        unos = ("⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇")
        await message.edit(unos)


async def pandacmd(self, message):
        """Используй .panda. <emoji>; ничего."""
        emoji = utils.get_args_raw(message)
                                panda = ("<code>Мурррррррр..../n"
                                        "_______________$$$$__$$$$/n"
                                        "____$$$$ $$____$$$$$$$$_$$/n"
                                        "____$$__$$$$$$$$$$$$$___$/n"
                                        "____$_________ $$$$$_$$$$$$/n"
                                        "____$$_________$$$$$$$$$$$/n"
                                        "___$$_____________ __$$$$$/n"
                                        "___$_____________________$/n"
                                        "___$___________________ __$$$$$/n"
                                        "______$$$$$________$$$$$$/n"
                                        "_____$___♥♥♥♥♥___♥♥♥♥♥___$/n"
                                        "____$$__♥♥♥♥♥♥♥_♥♥♥♥♥♥♥__$$/n"
                                        "____$__♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥___$/n"
                                        "_____$$_♥♥♥♥♥♥♥♥♥♥♥♥♥♥___$/n"
                                        "______$$_♥♥♥♥♥♥♥♥♥♥♥♥__$$/n"
                                        "_____ __$__♥♥♥♥♥♥♥♥♥♥__$/n"
                                        "____$$$$$__♥♥♥♥♥♥♥♥__$$$$$/n"
                                        "___$$____$__ ♥♥♥♥♥♥__$____$$/n"
                                        "___$$$$$$$$__♥♥♥♥__$$$$$$$$/n"
                                        "___________$__ ♥♥__$/n"
                                        "____________$__♥_$/n</code>")
        if emoji:
            panda = megapanda.replace('♥️', emoji)
        await message.edit(panda)


    async def impscmd(self, message):
        """Используй .impss <@ или реплай>."""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        if not args and not reply:
            user = await message.client.get_me()
        if reply:
            user = await utils.get_user(await message.get_reply_message())
        if args:
            user = await message.client.get_entity(args)
        impss = ['wasn`t the impostor', 'was the impostor']
        imps = ("<code>.      　。　　　　•　    　ﾟ　　.      .     。\n"
               "　　.　　　.　　　  .　　　.　　　　　。　　   。　   .\n"
               "　.　　      。        ඞ   。　    .     　.　      •      .\n"
               f"•     {user.first_name} {choice(imps)} 。　   .\n"
               f"　 。     {randint(1, 5)} impostor(s) remains.　　　.　 　.\n"
               ",　　　　.　 .　　       .        •   •    。.\n"
               "。  •　   .   　ﾟ 　  •  　ﾟ .        .    　.</code>")
        await message.edit(imps)


    async def catcmd(self, message):
        """Используй .cat"""
        r = random.randint(0, 8)
        logger.debug(r)
        if r == 0:
            await utils.answer(message, "ଲ(ⓛ ω ⓛ)ଲ")
        elif r == 1:
            await utils.answer(message, "(=ＴェＴ=)")
        elif r == 2:
            await utils.answer(message,"̫͍(ฅ'ω'ฅ)")
        elif r == 3:
            await utils.answer(message, "ฅ(• ɪ •)ฅ")
        elif r == 4:
            await utils.answer(message, "ヾ(=`ω´=)ノ")
        elif r == 5:
            await utils.answer(message, "(=ↀωↀ=)")
        elif r == 6:
            await utils.answer(message, "( • )( • )ԅ(≖‿≖ԅ)")
        elif r == 7:
            await utils.answer(message, "(=ω=)..nyaa")                      
        else:
            await utils.answer(message, "Здесь был VetalKot XD")
