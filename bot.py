# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:10:57 2020

@author: augus_0olo4w
"""

import time
import csv
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

TOKEN = 'My_Token_Here'

description = '''Bot Python to help you in Minecraft command edit'''
bot = commands.Bot(command_prefix='Mc!', description=description)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    table = []
    lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
    for ligne in lecteur:
        table.append(ligne)
    
    for guildofthebot in bot.guilds :
        guild = guildofthebot
        print(guild.name,":",guild.owner,":",guild.id)
        a = 0
        for i in table :
            if str(guildofthebot.id) == i[0] :
                a = 1
        if a == 0 :
            table.append([str(guildofthebot.id),"en"])
    
    doc = open("./data/language.csv" , "w", encoding="utf-8")
    doc.write("")
    doc.close() 
    
    doc = open("./data/language.csv" , "a", encoding="utf-8")

    for i in range(len(table)):

        for j in range(len(table[0])):

            doc.write(str(table[i][j]))
            if j != len(table[0])-1 :
                doc.write(",")
        doc.write("\n")
    doc.close()
    
    game = discord.Game("⚙️ Mc!help ✅")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event
async def on_guild_join(guild):
    table = []
    lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
    for ligne in lecteur:
        table.append(ligne)

        for guildofthebot in bot.guilds :
            if not ( guildofthebot in table ) :
                table.append([str(guildofthebot),"en"])
    
    doc = open("./data/language.csv" , "w", encoding="utf-8")
    doc.write("")
    doc.close() 
    
    doc = open("./data/language.csv" , "a", encoding="utf-8")

    for i in range(len(table)):

        for j in range(len(table[0])):

            doc.write(str(table[i][j]))
            if j != len(table[0])-1 :
                doc.write(",")
        doc.write("\n")
    doc.close()

    j = " "
    for i in guild.channels :
        if i.name == "general" or i.name == "général" :
            j = i
            break
    to_send = "Hello everyone, \nI'm here to help you in your minecraft projects.\n```Mc!help for more infos```"
    if j != " " :
        await j.send(to_send)
    else :
        for i in guild.channels :
            break
        await i.send(to_send)
    print("-----\nNouveau Serveur rejoint :",guild.name,"\n-----")


class Help() :
    """Série de commandes permettant d'apporter une aide simple, et efficace"""
    
    @bot.command(pass_context = True,category = "Help")
    async def help(ctx,*command) :
        """returns help message"""
        
        if len(command) == 0 :
            
            table = []
            lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
            for ligne in lecteur:
                table.append(ligne)
            
            for i in table :
                if str(ctx.guild.id) == i[0] :
                    lang = i[1]
                    
            if lang == "fr" :
                
        
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
        
                embed.set_author(name='Categorie Aide :')
                embed.add_field(name='Mc!help', value = 'Renvoie ce message', inline = False)
                embed.add_field(name='Mc!add', value = 'En développement, ne pas utiliser', inline = False)
                embed.add_field(name='Mc!doc', value = 'Renvoie la documentation Minecraft du mot-clé selectionné', inline = False)
                embed.add_field(name='Mc!doclist', value = 'Renvoie la liste des mots-clés disponibles pour la commande Mc!doc <command>', inline = False)
                embed.add_field(name='Mc!search', value = "Comme une recherche Internet, mais avec des commandes Minecraft (En utilisant non pas le nom des commandes, mais des mots clés)", inline = False)
                embed.add_field(name='Mc!taglist', value = 'Renvoie la liste des tags disponibles pour la commande Mc!search <command>', inline = False)
        
                embed1 = discord.Embed(
                    colour = discord.Colour.blue()
                )
        
                embed1.set_author(name='Categorie Utiles :')
                embed1.add_field(name='Mc!info', value = 'Informations utiles', inline = False)
                embed1.add_field(name='Mc!invite', value = "Obtenir un lien d'invitation", inline = False)
                embed1.add_field(name='Mc!status', value = 'Affiche la disponibilité du bot', inline = False)
                embed1.add_field(name='Mc!language <en|fr>', value = 'Changer ou afficher la langue actuelle', inline = False)
        
        
        
                await ctx.send( embed=embed )
                await ctx.send( embed=embed1 )
                await ctx.send( "Taper `Mc!help <command>` pour plus d'infos sur une commande" )
                
            else :
        
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
        
                embed.set_author(name='Category Help :')
                embed.add_field(name='Mc!help', value = 'Return this message', inline = False)
                embed.add_field(name='Mc!add', value = 'In developpment, do not use', inline = False)
                embed.add_field(name='Mc!doc', value = 'Return the minecraft documentation of the selected keyword', inline = False)
                embed.add_field(name='Mc!doclist', value = 'Return the list of all Minecraft keywords available for the Mc!doc command', inline = False)
                embed.add_field(name='Mc!search', value = "As an internet research, but with minecraft commands (using tags, not command's names)", inline = False)
                embed.add_field(name='Mc!taglist', value = 'Return the list of all the tags you can use in the Mc!search command', inline = False)
        
                embed1 = discord.Embed(
                    colour = discord.Colour.blue()
                )
        
                embed1.set_author(name='Category Utils :')
                embed1.add_field(name='Mc!info', value = 'Useful Informations', inline = False)
                embed1.add_field(name='Mc!invite', value = 'Obtain an Invit link', inline = False)
                embed1.add_field(name='Mc!status', value = 'Display current status', inline = False)
                embed1.add_field(name='Mc!language <en|fr>', value = 'Change or display current language', inline = False)
        
        
        
                await ctx.send( embed=embed )
                await ctx.send( embed=embed1 )
                await ctx.send( "Type `Mc!help <command>` for more info on a command (:grin: Available now !)" )
            
            
            print("-----\nHelp envoyé\n-----")
            
        elif len(command) > 0 :
            
            a = command[0]
        
            
            print(command)
            
            Help_dict = {}
            
            table = []
            lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
            for ligne in lecteur:
                table.append(ligne)
            
            for i in table :
                if str(ctx.guild.id) == i[0] :
                    lang = i[1]
                    
            if lang == "fr" :
            
                Help_dict["add"] = ("Ne pas Utiliser","Pas encore disponible")
                Help_dict["doc"] = ("Mc!doc <Minecraft Command Name>","Renvoie la documentation Minecraft du mot-clé selectionné")
                Help_dict["doclist"] = ("Mc!doclist","Renvoie la liste des mots-clés disponibles pour la commande `Mc!doc <command>`")
                Help_dict["search"] = ("Mc!search <tag1> [tag2] [tag3] [tag4] [tag5]","Comme une recherche Internet, mais avec des commandes Minecraft (En utilisant non pas le nom des commandes, mais des mots clés)\n`Mc!taglist` vous donnera la liste des tags disponibles")
                Help_dict["taglist"] = ("Mc!taglist","Renvoie la liste des tags disponibles pour la commande Mc!search <command>")
                
                Help_dict["info"] = ("Mc!info","Informations utiles")
                Help_dict["invite"] = ("Mc!invite","Obtenir un lien d'invitation")
                Help_dict["status"] = ("Mc!status","Affiche la disponibilité du bot, ne fonctionne pas si le bot est éteint")
                Help_dict["help"] = ("Mc!help [command]","Affiche l'aide de la commande demandée\nou la liste d'aide si tu n'entres pas le paramètre `[command]`")
                Help_dict["language"] = ("Mc!language <en|fr>","Changer ou afficher la langue actuelle")
            
            else :
                
                Help_dict["add"] = ("Do not use","Work In Progress")
                Help_dict["doc"] = ("Mc!doc <Minecraft Command Name>","Return the minecraft documentation of the selected keyword")
                Help_dict["doclist"] = ("Mc!doclist","Return the list of all Minecraft keywords available for the `Mc!doc` command")
                Help_dict["search"] = ("Mc!search <tag1> [tag2] [tag3] [tag4] [tag5]","Like an internet research, but with minecraft commands\n`Mc!taglist` gives you the list of availables tags")
                Help_dict["taglist"] = ("Mc!taglist","Return the list of all the tags you can use in the `Mc!search` command")
                
                Help_dict["info"] = ("Mc!info","Useful Informations")
                Help_dict["invite"] = ("Mc!invite","Obtain an Invit link")
                Help_dict["status"] = ("Mc!status","Display current status, doesn't work when the bot is off")
                Help_dict["help"] = ("Mc!help [command]","Displays the help for the desired command\nor the help list if you don't enter a `[command]` parameter")
                Help_dict["language"] = ("Mc!language <en|fr>","Change or display the current language of the server")
                        
            
            if a in Help_dict :
                
                name = "```" + Help_dict[command[0]][0] + "```"
            
                embed = discord.Embed(
                    colour = discord.Colour.green()
                )
    
                embed.set_author(name="Mc!" + command[0])
                embed.add_field(name=Help_dict[command[0]][1], value = name, inline = False)
            
                await ctx.send( embed = embed )
                
                print("-----\nHelp",command[0],"envoyé\n-----")
            
            else :
                
                table = []
                lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
                for ligne in lecteur:
                    table.append(ligne)
                
                for i in table :
                    if str(ctx.guild.id) == i[0] :
                        lang = i[1]
                        

                
                if lang == "fr" :
                    
                    await ctx.send(":red_circle: Cette commande n'existe pas ou n'est pas enregistrée")
                    
                else :
                
                    await ctx.send(":red_circle: This command doesn't exist or isn't referenced")
                
                
            
            
    
    @bot.command(pass_context = True,category = "Help")
    async def doclist(ctx):
        """Return the list of all Minecraft commands available"""
        
        doc = open('./data/commands.txt','r',encoding='utf-8')

        docu = doc.read()
        docu = eval(docu)
        
        doc.close()
        
        list_of_commands = ""
        
        for i in docu.keys() :
            list_of_commands = list_of_commands + "`" + i + "`, "
            

        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
                
        if lang == "fr" :
            
            list_of_commands = ":books: Voici ce que vous avez demandé :\n" + list_of_commands
        
        else :
        
            list_of_commands = ":books: Here it is :\n" + list_of_commands
        

        
        
        await ctx.send(list_of_commands)
        
        
    @bot.command(pass_context = True,category = "Help")
    async def taglist(ctx):
        """Return the list of all the tags you can use in the Mc!search command"""
        
        doc = open('./data/exemples.txt','r',encoding='utf-8')

        docu = doc.read()
        docu = eval(docu)
        
        doc.close()
        
        list_of_commands = []
        
        for i in docu.keys() :
            for j in docu[i][1] :
                if j not in list_of_commands :
                    list_of_commands.append(j)
        
        to_send = ""
        
        for i in list_of_commands :
            to_send = to_send + "`" + i + "`, "
        
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
                
        
        if lang == "fr" :
            
            list_of_commands = ":gear: Voici les paramètres de recherche disponibles :\n" + to_send
            
        else :
        
            list_of_commands = ":gear: Here it is :\n" + to_send
        
        
        await ctx.send(list_of_commands)
    

    @bot.command(pass_context = True,category = "Help")
    async def exemple(ctx,*Nom_de_la_Commande):
        """Return a minecraft exemple for the selected command"""
        cmd = Nom_de_la_Commande[0]

        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]

        url = "https://fr-minecraft.net/commande-"+cmd+".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        examples = str(soup.find_all("div", class_="cmd_exemple")[0])

        exsoup = BeautifulSoup(examples, 'html.parser')
        commands = [i.text for i in exsoup.find_all("textarea", class_="input-exemple")]
        comments = [i for i in examples.split('<br/>') if '</' not in i ]
        print(comments)
        print(commands)

        embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
        
        embed.set_author(name="🔧 Exemples pour la commande "+cmd)
        

        for i in range(len(comments)):
            embed.add_field(name='`'+commands[i]+'`', value = comments[i], inline = False)

        await ctx.send(embed=embed)


    @bot.command(pass_context = True,category = "Help")
    async def doc(ctx,*Nom_de_la_Commande):
        """Return the minecraft documentation of the selected command"""
        com = ""
        
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
            
        if len(Nom_de_la_Commande) > 0 :

            Nom_de_la_Commande = Nom_de_la_Commande[0]
            
            for i in str(Nom_de_la_Commande):
                if i != " " and i != "/" :
                    com = com + i.lower()
            
            url = "https://fr-minecraft.net/commande-"+com+".html"

            r = requests.get(url)
            soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')
            cmd_syntax = soup.find_all("div", class_="cmd-syntaxe")[0]
            docu=cmd_syntax.text.split("Légende")[0].replace('\n'," ").replace('\r',"").replace('Syntaxe : ',"")
            description = soup.find_all("div", class_="description")[0].text

            if description != "" :
                
                if str(type(docu)) == "<class 'str'>" :
                
                    if lang == 'fr' : 
                        to_return = ":books: Voici la documentation du mot-clé *" + com + "* :```" + docu + "```" + description
                        
                    else : 
                        to_return = ":books: Here is the documentation of the *" + com + "* keyword :```" + docu + "```" + description
                        
                    await ctx.send(to_return)

                else : await ctx.send("error: ",type(docu))
                
                doc = open('./data/Help.txt','r',encoding='utf-8')
            
                helped = doc.read()
                helped = eval(helped)
            
                doc.close()
                
                helped[0] = helped[0] + 1
                
                doc = open('./data/Help.txt','w',encoding='utf-8')
            
                doc.write(str(helped))
            
                doc.close()
                
                print("-----\nAide envoyée\n-----")
            
            
            else :
                if lang == 'fr' :
                    await ctx.send("Rien n'a été trouvé")
                else : 
                    await ctx.send("Nothing Found")
                print("-----\nRessource non trouvée\n-----")
                
        else : 
            if lang == 'fr' :
                await ctx.send("Merci de rentrer au oins un argument, `Mc!help doc` pour plus d'informations")
            else : 
                await ctx.send("Please enter at least one argument `Mc!help doc` for more help")
        
    @bot.command(pass_context = True,category = "Help")
    async def search(ctx, *tags):
        """As an internet research, but with minecraft commands"""
        
        doc = open('./data/exemples.txt','r',encoding='utf-8')
        
        exemples = doc.read()
        exemples = eval(exemples)
        
        doc.close()
        
        dico_return = {}
        
        if len(tags) > 5 :
            await ctx.send("You exceeded the maximum number of arguments (5)")
        
        if len(tags) < 1 :
            await ctx.send("Please enter at least one argument `Mc!help search` for more help")
        
        else : 
            for i in exemples.keys() :
                if tags[0] in exemples[i][1] :
                    dico_return[i] = exemples[i]
                    
            if len(tags) > 1 :
                
                for i in dico_return.keys() :
                    if not (tags[1] in dico_return[i][1]) :
                        del dico_return[i]
                        
            if len(tags) > 2 :
                
                for i in dico_return.keys() :
                    if not (tags[2] in dico_return[i][1]) :
                        del dico_return[i]
                        
            if len(tags) > 3 :
                
                for i in dico_return.keys() :
                    if not (tags[3] in dico_return[i][1]) :
                        del dico_return[i]
                        
            if len(tags) > 4 :
                
                for i in dico_return.keys() :
                    if not (tags[4] in dico_return[i][1]) :
                        del dico_return[i]
                        
            if len(dico_return) == 0 : 
            
                await ctx.send("Nothing found, the documentation is actually a work-in-progress, try again later, or use `Mc!taglist` for the list of the available tags")
            
            else :
                
                to_return = "Here it is :"
                
                for i in dico_return.keys() :
                    
                    to_return = to_return + "\n```" + dico_return[i][0] + "```" + i
                    
                await ctx.send(to_return)
                
                doc = open('./data/Help.txt','r',encoding='utf-8')
        
                helped = doc.read()
                helped = eval(helped)
        
                doc.close()
            
                helped[1] = helped[1] + 1
            
                doc = open('./data/Help.txt','w',encoding='utf-8')
        
                doc.write(str(helped))
        
                doc.close()
                
        print("-----\nrecherche de Tag lancée\n-----")
        
    @bot.command(pass_context = True,category = "Help")
    async def add(ctx, description, tags, *commands):
        """Work in progress"""
        
        if len(commands) > 2 : 

            description = commands[0]
            
            tags = commands[0]
            
            del commands[0]
            del commands[1]
            
            
            
            command = ""
            
            for i in commands :
                command = command + " " + i
            
            table = []
            lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
            for ligne in lecteur:
                table.append(ligne)
            
            for i in table :
                if str(ctx.guild.id) == i[0] :
                    lang = i[1]
                    
            if lang == "en" :
            
                await ctx.send(":gear: This command is not disponible yet, \nbut you can send us an email :\n:e_mail: minecraft.discord.bot.help@gmail.com")
            
            elif lang == "fr" :
        
                await ctx.send(":gear: Cette commande n'est pas encore fonctionnelle, \nmais vous pouvez nous envoyer un e-mail :\n:e_mail: minecraft.discord.bot.help@gmail.com")
                
            
            
            doc = open('./data/exemples.txt','r',encoding='utf-8')
            
            exemples = doc.read()
            exemples = eval(exemples)
            
            tags = tuple(tags)
            
            doc.close()
            
            exemples[description] = (command,(tags))
        
            doc = open('./data/exemples.txt','w',encoding='utf-8')
            
            doc.write(str(exemples))
            
            doc.close()
            
            if lang == "en" :
                await ctx.send("Function registered, thanks a lot :white_check_mark:")
                
            elif lang == "fr" :
                await ctx.send("Fonction enregistrée, merci de votre contribution :white_check_mark:")
            
        else : await ctx.send("Please enter at least one argument, `Mc!help add` for more help")
        
        
class Useful() :
    """Commandes permettant de contacter le personnel du bot"""
    
    
    @bot.command(pass_context = True,category = "Useful")
    async def language(ctx, *newlanguage):
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
                
        if len(newlanguage) == 0 :
            
            #display the current language
            
            if lang == None :
                await ctx.send("Unknow Error, staff knows it")
                print("-----\nError : Server",ctx.guild.id,":",ctx.guild.name,"not found\n-----")
                
            elif lang == "fr" :
                await ctx.send("Ce serveur est actuellement configuré en Français")
            
            elif lang == "en" :
                await ctx.send("This server language is actually English, if you want to turn to French, ask an Administrator to type `Mc!language fr`")
            
        else :
            
            
            if (ctx.author.guild_permissions.administrator) :
                #modify the current language
                
                a = newlanguage[0][0] + newlanguage[0][1]
                newlanguage = a.lower()
                
                if newlanguage == 'fr' :
                    await ctx.send("La langue de ce serveur a bien été basculée en Français")
                    for i in range(len(table)) :
                        if str(ctx.guild.id) == table[i][0] :
                            break
                    table[i][1] = 'fr'
                    
                elif newlanguage == 'en' :
                    await ctx.send("The current language of this server is now `English`")
                    for i in range(len(table)) :
                        if str(ctx.guild.id) == table[i][0] :
                            break
                    table[i][1] = 'en'
                    
                else :
                    await ctx.send("Unknow Error, staff knows it")
                    print("-----\nError : Server",ctx.guild.id,":",ctx.guild.name,newlanguage,"not found\n-----")
                    
                doc = open("./data/language.csv" , "w", encoding="utf-8")
                doc.write("")
                doc.close() 
                
                doc = open("./data/language.csv" , "a", encoding="utf-8")
            
                for i in range(len(table)):
            
                    for j in range(len(table[0])):
            
                        doc.write(str(table[i][j]))
                        if j != len(table[0])-1 :
                            doc.write(",")
                    doc.write("\n")
                doc.close()

            
            else : 
                if lang == 'fr' :
                    await ctx.send("Tu n'as pas les permissions requises, contactes un Administrateur pour changer la langue de ce serveur")
                else :
                    await ctx.send("You don't have the permission, you must be Administrator to do that")
        
    @bot.command(pass_context = True,category = "Help")
    async def off(ctx,*command) :
        """turns off the bot"""
        
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
        
        if ctx.author.name == "augustin64" :
            
            game = discord.Game("💤 Sleeping")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            
            
            await ctx.send(":white_check_mark:")
            
            time.sleep(10)
            
            quit()
            
            
        else :
            
            if lang == 'fr' :
                await ctx.send("Tu n'as pas les permissions requises")
            else :
                await ctx.send("You don't have the permission, you are not Bot's Administrator")
        
        
    
    @bot.command()
    async def info(ctx):
        """Useful Informations"""
        
        doc = open('./data/Help.txt','r',encoding='utf-8')
        
        helped = doc.read()
        helped = eval(helped)
        
        doc.close()
        
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
                
        if lang == "en" :
        
            to_send = ":e_mail: Mail : minecraft.discord.bot.help@gmail.com \n:alarm_clock: Hours : Monday-friday, from 9h to 20h (will change in the future)"
            to_send = to_send + "\n\n:robot: Actually in " + str(len([s for s in bot.guilds])) + " Servers"
            
            to_send = to_send + "\n:books: Number of documentation type aids given : " + str(helped[0])
            to_send = to_send + "\n:gear: Number of exemples type aids given : " + str(helped[1])
            
            await ctx.send(to_send)
        
        elif lang == "fr" :
            
            to_send = ":e_mail: Mail : minecraft.discord.bot.help@gmail.com \n:alarm_clock: Horaires : Lundi-Vendredi, de 9h à 20h (changera dans le futur)"
            to_send = to_send + "\n\n:robot: Actuellement dans " + str(len([s for s in bot.guilds])) + " Serveurs"
            
            to_send = to_send + "\n:books: Nombre d'aides de type documentation données : " + str(helped[0])
            to_send = to_send + "\n:gear: Nombre d'aides de type exemples données : " + str(helped[1])
            
            await ctx.send(to_send)
        
        
        print("-----\nInfos envoyées\n-----")
        
        
    @bot.command()
    async def invite(ctx):
        """Obtain an Invit link"""
        
        table = []
        lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
        for ligne in lecteur:
            table.append(ligne)
        
        for i in table :
            if str(ctx.guild.id) == i[0] :
                lang = i[1]
                
        if lang == "en" :
        
            await ctx.send(":link: here the link to put me in another discord server : \n https://discord.com/oauth2/authorize?client_id=721288945639620650&scope=bot&permissions=0")
        
        elif lang == "fr" :
            
            await ctx.send(":link: Voici le lien pour m'ajouter dans un autre serveur discord' : \n https://discord.com/oauth2/authorize?client_id=721288945639620650&scope=bot&permissions=0")
        
        print("-----\nInvitation envoyée\n-----")

@bot.command()
async def status(ctx):
    """Display current status"""
    
    table = []
    lecteur=csv.reader(open('./data/language.csv','r',encoding='utf-8'))
    for ligne in lecteur:
        table.append(ligne)
    
    for i in table :
        if str(ctx.guild.id) == i[0] :
            lang = i[1]
            
    if lang == "en" :
    
        await ctx.send("Current Status : `Online` :white_check_mark:")
    
    elif lang == "fr" :
        
        await ctx.send("Actuellement : `En ligne` :white_check_mark:")
    
    
    print("-----\nStatut : en ligne\n-----")
    


bot.run(TOKEN)
