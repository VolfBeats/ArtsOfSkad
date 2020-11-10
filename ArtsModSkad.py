import random
import logging
from .. import loader, utils
from random import randint, choice
logger = logging.getLogger(__name__)


def register(cb):
    cb(ArtsModSkad())

class ArtsModSkad(loader.Module):
    """Юникод арты"""
    strings = {'name': 'ArtsModSkad'}

    async def neponcmd(self, message):
        """Используй .nepon <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нет текста после команды :c</b>')
            return
        else:
            nepon = ("<code>{~x~}\n"
                    "[><]\n"
                    "^  ^\n"
                    "А вот тут я не понял ты что... </code>" + f"<code>{text}</code>")
            await message.edit(nepon)

        if text == "podpiskaq":
            await message.edit("<code>{~x~}\n"
                                      "[><]\n"
                                      "^  ^\n"
                               "Я не понял ты ещё не подписался на меня в Инстаграме -></code> @pro100sans")


    async def cowsayqcmd(self, message):
        """Используй .cowsayq <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нет текста после команды :c</b>')
            return
        else:
            cowsayq = ("<code> "
                      f"< {text} >\n"
                      "\n"
                      "     \   ^__^\n"
                      "	     \  (00)\_______\n"
                      "         (__)\  FUCK  )\/\n"
                      "             ||----w||\n"
                      "	            ||     ||</code>")
            await message.edit(cowsayq)


    async def padayuqcmd(self, message):
        """Используй .padayuq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ПАДАЮ")
            padayuq = ("┓┏┓┏┓┃\n"
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
            await message.edit(padayuq)
        else:
            padayuq = ("┓┏┓┏┓┃\n"
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
            await message.edit(padayuq)


    async def priletelqcmd(self, message):
        """Используй .prilitelq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Я ЛЮБЛЮ СОСАТЬ ХУИ, А ТЫ?!")
            prilitelq = ("▬▬▬.◙.▬▬▬\n"
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
            await message.edit(prilitelq)
        else:
            prilitelq = ("▬▬▬.◙.▬▬▬\n"
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
            await message.edit(prilitelq)


    async def huytebeqcmd(self, message):
        """Используй .huytebeq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("МАЯК ТЕБЕ В РОТ!")
            huytebeq = ("...............▄▄▄▄▄\n"
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
            await message.edit(huytebeq)
        else:
            huytebeq = ("...............▄▄▄▄▄\n"
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
            await message.edit(huytebeq)


    async def lolqcmd(self, message):
        """Используй .lolq."""
        lolq = ("┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
               "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
               "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
               "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
               "┗━━━┛╰━━━━╯┗━━━┛\n")
        await message.edit(lolq)


    async def fuckyouqcmd(self, message):
        """Используй .fuckyouq."""
        fuckyouq = ("┏━┳┳┳━┳┳┓\n"
                   "┃━┫┃┃┏┫━┫┏┓\n"
                   "┃┏┫┃┃┗┫┃┃┃┃\n"
                   "┗┛┗━┻━┻┻┛┃┃\n"
                   "┏┳┳━┳┳┳┓┏┫┣┳┓\n"
                   "┣┓┃┃┃┃┣┫┃┏┻┻┫\n"
                   "┃┃┃┃┃┃┃┃┣┻┫┃┃\n"
                   "┗━┻━┻━┻┛┗━━━┛\n")
        await message.edit(fuckyouq)


    async def houseqcmd(self, message):
        """Используй .houseq."""
        houseq = ("╯▅╰╱▔▔▔▔▔▔▔╲╯╯\n"
                 "▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭\n"
                 "▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭\n"
                 "╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲\n"
                 "▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔\n"
                 "▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏\n"
                 "▕┓▔┗┓▔┏▏▕┗▏ ┓▔┏\n")
        await message.edit(houseq)


    async def helloqcmd(self, message):
        """Используй .helloq."""
        helloq = ("┈┏┓┏┳━┳┓┏┓┏━━┓┈\n"
                 "┈┃┃┃┃┏┛┃┃┃┃┏┓┃┈\n"
                 "┈┃┗┛┃┗┓┃┃┃┃┃┃┃┈\n"
                 "┈┃┏┓┃┏┛┃┃┃┃┃┃┃┈\n"
                 "┈┃┃┃┃┗┓┗┫┗┫╰╯┃┈\n"
                 "┈┗┛┗┻━┻━┻━┻━━┛┈\n")
        await message.edit(helloq)


    async def coffeeqcmd(self, message):
        """Используй .coffeeq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Это тебе :з")
            coffeeq = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffeeq)
        else:
            coffeeq = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffeeq)


    async def tvqcmd(self, message):
        """Используй .tvq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ТЕЛЕВИЗОР ГОВОРИТ ЧТО ТЫ НЕ ПОДПИСАН НА VitecP")
            tvq = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tvq)
        else:
            tvq = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tvq)


    async def grenqcmd(self, message):
        """Используй .grenq <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ГРАНАТУ ТЕБЕ В РОТ! МАРМОК©")
            grenq = ("─▄▀▀███═◯\n"
                    "▐▌▄▀▀█▀▀▄\n"
                    "█▐▌─────▐▌\n"
                    "█▐█▄───▄█▌\n"
                    "▀─▀██▄██▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(grenq)
        else:
            grenq = ("─▄▀▀███═◯\n"
                    "▐▌▄▀▀█▀▀▄\n"
                    "█▐▌─────▐▌\n"
                    "█▐█▄───▄█▌\n"
                    "▀─▀██▄██▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(grenq)


    async def bruhqcmd(self, message):
        """Используй .bruhq."""
        bruhq = ("╭━━╮╱╱╱╱╱╭╮\n"
                "┃╭╮┃╱╱╱╱╱┃┃\n"
                "┃╰╯╰┳━┳╮╭┫╰━╮\n"
                "┃╭━╮┃╭┫┃┃┃╭╮┃\n"
                "┃╰━╯┃┃┃╰╯┃┃┃┃\n"
                "╰━━━┻╯╰━━┻╯╰╯\n")
        await message.edit(bruhq)


    async def unoqcmd(self, message):
        """Используй .unoq."""
        unoq = ("⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
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
        await message.edit(unoq)


    async def huyqcmd(self, message):
        """Используй .huyq <emoji>; ничего."""
        emoji = utils.get_args_raw(message)
        huyq = ("🍆🍆\n"
               "🍆🍆🍆\n"
               "  🍆🍆🍆\n"
               "    🍆🍆🍆\n"
               "     🍆🍆🍆\n"
               "       🍆🍆🍆\n"
               "        🍆🍆🍆\n"
               "         🍆🍆🍆\n"
               "          🍆🍆🍆\n"
               "          🍆🍆🍆\n"
               "      🍆🍆🍆🍆\n"
               " 🍆🍆🍆🍆🍆🍆\n"
               " 🍆🍆🍆  🍆🍆🍆\n"
               "    🍆🍆        🍆🍆")
        if emoji:
            huyq = huyq.replace('🍆', emoji)
        await message.edit(huyq)


    async def impsqcmd(self, message):
        """Используй .impsq <@ или реплай>."""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        if not args and not reply:
            user = await message.client.get_me()
        if reply:
            user = await utils.get_user(await message.get_reply_message())
        if args:
            user = await message.client.get_entity(args)
        impsq = ['wasn`t the impostor', 'was the impostor']
        impq = ("<code>.      　。　　　　•　    　ﾟ　　.      .     。\n"
               "　　.　　　.　　　  .　　　.　　　　　。　　   。　   .\n"
               "　.　　      。        ඞ   。　    .     　.　      •      .\n"
               f"•     {user.first_name} {choice(imps)} 。　   .\n"
               f"　 。     {randint(1, 5)} impostor(s) remains.　　　.　 　.\n"
               ",　　　　.　 .　　       .        •   •    。.\n"
               "。  •　   .   　ﾟ 　  •  　ﾟ .        .    　.</code>")
        await message.edit(impq)


    async def fqcmd(self, message):
        """Используй .fq"""
        r = random.randint(0, 6)
        logger.debug(r)
        if r == 0:
            await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        elif r == 2:
            await utils.answer(message,
                               "̫͍F̥̼F͈̫F͔̱F͓̤F̭̺F̙F͍͕F͚̩F̣̱F͖ͅF̣͙F̗͕F̦͚F̯͍ ̘͇F̰̹F̦̩F͙ͅF̙̹F̝͚ ̻F̥̙F ͙̹ ̩͔ ̘͈ ͍̭\n"
                               "̹̖F̲͔F̜ ̗͎F̭̰F̰̭F̼͍F̹̞F̱͉F͓͓F̬ ̼ͅF̤͔F̦͉Fм̟̙F̦̹F͚̠FF̪̝ ̩̗F͇͓F̟̙F͎͎F͉͚ ̥̟ ̙͚\n"
                               "̯̻F͓͈F̮͔F͉̫F͕̥ ͔̙ ̣ ͙г\n"
                               "̞̖F̝̗F͙͓F̟͓F̖̝ ̤͙\n"
                               "͔͓F̠F̖ͅF̰̹F ̠̟\n"
                               "͓͕F̹͙ ̲̩F̙̠F͇̯F̖̗ ̺ ̱͔ \n"
                               "̜͚F ̱̥F̥̝F̖̦F͇͔ ̜͓ ̪̹\n"
                               "̩̗F̬̟F̰F̙͇F F͉̖F̼ͅF̬͔F͇͖F̞̥F̙̺F̖̮ ̥̙F̜͔F̩̜F͎̣F̲̤F̪̙FF̰̫F̝̘ ̣̻F͙͎ ̜̱ ̠͈F̬̫ ̦̩ \n"
                               "͎͙F̘F͍̲ ̲ͅF͇͇F̜̥F͖͖F̪̟ ̤̩F̠̩F̬͕F̪ ̰̪F̫͍ ̺͓F͕̤F̰ͅ ̬̼F̮̼F ͎̯F͓̟F̻͔F̪F͈̭ ̠͓F̣̺ ̭F̮̩ ͖̣\n"
                               "̙F͎̞F̻ F͖͔F͕̮F̯͖FF̪͕F̫͚F̣̣ ̗̣F̩ ̫͍F̥F̗̮F̻̫F͍̺F̞͉F͚̩F͕̤ ͉̤FF̼͙ ͔͕ ͉ ͙\n"
                               "͍͙ F̯̬F̲̻F̥̟F̝̙ ̘\n"
                               "̦̝ ͔ ̝̬F̝͍F̖͚ F̥͚F̖͉ ̩͔ \n"
                               "͓̪F̝͉F̜ͅF̦ͅF͓͕ ̜̭\n"
                               "͖F ͎̩F̩͕F̻͖F̯̼ ̼̼ ̹͔\n"
                               "͍̱FF̹̥F̭͓F̦̺ ̖͎\n"
                               "̥̜F̞͎F̖̲F̦̹F̬̘ \n"
                               "̦̬F̺̭F͖̗F͕͍F̟͙ ͓͍")
        elif r == 3:
            await utils.answer(message, "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
        elif r == 4:
            await utils.answer(message, "┏━━━┓╋╋╋╋╋╋╋╋╋╋╋┏━━━┓\n"
                                        "┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋┃┏━━┛\n"
                                        "┃┗━┛┣━┳━━┳━━┳━━┓┃┗━━┓\n"
                                        "┃┏━━┫┏┫┃━┫━━┫━━┫┃┏━━┛\n"
                                        "┃┃╋╋┃┃┃┃━╋━━┣━━┃┃┃\n"
                                        "┗┛╋╋┗┛┗━━┻━━┻━━┛┗┛")
        elif r == 5:
            await utils.answer(message, "<code>FFFFFFFFFFFFFFFFFFFFFF\n"
                                        "F::::::::::::::::::::F\n"
                                        "F::::::::::::::::::::F\n"
                                        "FF::::::FFFFFFFFF::::F\n"
                                        "  F:::::F       FFFFFF\n"
                                        "  F:::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::::::::::::F\n"
                                        "  F:::::::::::::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::F\n"
                                        "  F:::::F\n"
                                        "FF:::::::FF\n"
                                        "F::::::::FF\n"
                                        "F::::::::FF\n"
                                        "FFFFFFFFFFF</code>")
        else:
            await utils.answer(message, "██████╗\n"
                                        "██╔═══╝\n"
                                        "████╗░░\n"
                                        "██╔═╝░░\n"
                                        "██║░░░░\n"
                                        "╚═╝░░░░")
