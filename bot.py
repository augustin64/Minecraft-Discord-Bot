# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:10:57 2020

@author: https://github.com/augustin64
"""
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import discord
import time
import csv

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

    game = discord.Game("⚙️ En développement | Mc!help")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event
async def on_guild_join(guild):

    """ j = " "
    for i in guild.channels :
        if i.name == "general" or i.name == "général" :
            j = i
            break
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Message de bienvenue')
    embed.add_field(name="Bonjour, je suis votre nouveau bot d'aide à l'utilisation des commandes minecraft", value = '`Mc!help` pour voir la liste des actions disponibles', inline = False)


    if j != " " :
        await j.send(embed=embed)
    else :
        for i in guild.channels :
            break
        await i.send(embed=embed)"""
    print("-----\nNouveau Serveur rejoint :",guild.name,"\n-----")


class Help() :
    """Série de commandes permettant d'apporter une aide simple, et efficace"""
    
    @bot.command(pass_context = True,category = "Help")
    async def help(ctx,*parameters) :
        """returns help message"""

        if len(parameters) == 0 :
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
            embed.add_field(name='Mc!exemple',value='Renvoie les exemples disponibles de la commande sélectionnée')

            embed1 = discord.Embed(
                colour = discord.Colour.orange()
            )
    
            embed1.set_author(name='Categorie Utiles :')
            embed1.add_field(name='Mc!info', value = 'Informations utiles', inline = False)
            embed1.add_field(name='Mc!invite', value = "Obtenir un lien d'invitation", inline = False)
            embed1.add_field(name='Mc!status', value = 'Affiche la disponibilité du bot', inline = False)
            embed1.add_field(name='Astuce', value = "Taper `Mc!help <command>` pour plus d'infos sur une commande", inline = False)
    
    
    
            await ctx.send(embed=embed)
            await ctx.send(embed=embed1)
            print("-----\nHelp envoyé\n-----")
            
        elif len(parameters) > 0 :
            
            command = parameters[0]
            Help_dict = {}
            
            #Help_dict["add"] = ("Ne pas Utiliser","Pas encore disponible")
            Help_dict["doc"] = ("Mc!doc <Minecraft Command Name>","Renvoie la documentation Minecraft du mot-clé selectionné")
            Help_dict["exemple"] = ("Mc!exemple <Minecraft Command Name> [nombre d'exemples]","Donne les exemples disponibles de la commande sélectionnée")
            Help_dict["doclist"] = ("Mc!doclist","Renvoie la liste des mots-clés disponibles pour la commande `Mc!doc <command>`")
            Help_dict["search"] = ("Mc!search <tag1> [tag2] [tag3] [tag4] [tag5]","Comme une recherche Internet, mais avec des commandes Minecraft (En utilisant non pas le nom des commandes, mais des mots clés)\n`Mc!taglist` vous donnera la liste des tags disponibles")
            Help_dict["taglist"] = ("Mc!taglist","Renvoie la liste des tags disponibles pour la commande Mc!search <command>")
            
            Help_dict["info"] = ("Mc!info","Informations utiles")
            Help_dict["invite"] = ("Mc!invite","Obtenir un lien d'invitation")
            Help_dict["status"] = ("Mc!status","Affiche la disponibilité du bot, ne fonctionne pas si le bot est éteint")
            Help_dict["help"] = ("Mc!help [command]","Affiche l'aide de la commande demandée\nou la liste d'aide si tu n'entres pas le paramètre `[command]`")
            
            if command in Help_dict :
                
                name = "```" + Help_dict[command][0] + "```"
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                    )

                embed.set_author(name="Mc!" + command)
                embed.add_field(name=Help_dict[command][1], value = name, inline = False)
                await ctx.send(embed = embed )
                print("-----\nHelp",command,"envoyé\n-----")
            else :
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )

                embed.set_author(name='Mc!help')
                embed.add_field(name="❌ Cette commande n'existe pas ou n'est pas disponible", value = "`Mc!help` pour voir la liste des commandes disponibles", inline = False)

                await ctx.send(embed=embed)
                
            
            
    
    @bot.command(pass_context = True,category = "Help")
    async def doclist(ctx):
        """Return the list of all Minecraft commands available"""
                
        url = "https://fr-minecraft.net/61-guide-des-commandes-minecraft.php"
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        raw_data = soup.find_all("a", class_="content_popup_link")
        commandslist = ', '.join(["`"+i.text[1:]+"`" for i in raw_data if i.text[0] == '/'])
        
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Mc!doclist')
        embed.add_field(name=':books: Voici la liste des commandes minecraft disponibles :', value = commandslist, inline = False)

        await ctx.send(embed=embed)
        
        
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
        
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Mc!taglist')
        embed.add_field(name=':gear: Voici les paramètres de recherche disponibles :', value = to_send, inline = False)

        await ctx.send(embed=embed)
    

    @bot.command(pass_context = True,category = "Help")
    async def exemple(ctx,*parameters):
        """Return a minecraft exemple for the selected command"""
        cmd = parameters[0]

        url = "https://fr-minecraft.net/commande-"+cmd+".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')
        examplessoup=soup.find_all("div", class_="cmd_exemple")
        if len(examplessoup)>0:
            examples = str(examplessoup[0])

            exsoup = BeautifulSoup(examples, 'html.parser')
            commands = [i.text for i in exsoup.find_all("textarea", class_="input-exemple")]
            comments = [BeautifulSoup(i.split('<textarea')[0],'html.parser').text for i in examples.split('</textarea>') if BeautifulSoup(i.split('<textarea')[0],'html.parser').text!=""]

            embed = discord.Embed(
                        colour = discord.Colour.orange()
                    )
            
            embed.set_author(name="Mc!exemple 🔧 Exemples pour la commande "+cmd)
            
            if len(parameters)>1:
                if int(parameters[1]) < len(comments) :
                    number_of_commands = int(parameters[1])
                else :
                    number_of_commands = len(comments)
            else:
                number_of_commands = len(comments)

            for i in range(number_of_commands):
                embed.add_field(name=comments[i], value = '```'+commands[i]+'```', inline = False)

            await ctx.send(embed=embed)

            with open('./data/Help.txt','r',encoding='utf-8') as doc:
                helped = eval(doc.read())

            helped[1] = helped[1] + 1
        
            with open('./data/Help.txt','w',encoding='utf-8') as f:
                f.write(str(helped))
        else:
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name='aucun exemple disponible pour cette commande, vérifiez son existence avec la commande `Mc!doclist`')
            await ctx.send(embed=embed)

            print("+1 exemple")


    @bot.command(pass_context = True,category = "Help")
    async def doc(ctx,*parameters):
        """Return the minecraft documentation of the selected command"""
            
        if len(parameters) > 0 :

            parameters
            com = ''.join([i.lower() for i in parameters[0] if i!=" " and i !="/"])
            
            url = "https://fr-minecraft.net/commande-"+com+".html"

            r = requests.get(url)
            soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')
            cmd_syntax = soup.find_all("div", class_="cmd-syntaxe")[0]
            docu=cmd_syntax.text.split("Légende")[0].replace('\n'," ").replace('\r',"").replace('Syntaxe : ',"")
            description = soup.find_all("div", class_="description")[0].text

            if description != "" :
                
                if str(type(docu)) == "<class 'str'>" :
                
                    embed = discord.Embed(
                        colour = discord.Colour.orange()
                    )

                    embed.set_author(name='Mc!doc 📚 Voici la documentation de la commande /'+com)
                    embed.add_field(name='`'+docu+'`', value = description, inline = False)

                    await ctx.send(embed=embed)

                else : 
                    embed = discord.Embed(
                        colour = discord.Colour.orange()
                    )
                    embed.set_author(name="erreur interne: "+type(docu))
                    await ctx.send(embed=embed)
                
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
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
                embed.set_author("Rien n'a été trouvé")
                await ctx.send(embed=embed)
                print("-----\nRessource non trouvée\n-----")
                
        else : 
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author("Merci de rentrer au moins un argument, `Mc!help doc` pour plus d'informations")
            await ctx.send(embed=embed)
        
    @bot.command(pass_context = True,category = "Help")
    async def search(ctx, *tags):
        """Comme une recherche Internet, mais avec des commandes Minecraft"""
        
        doc = open('./data/exemples.txt','r',encoding='utf-8')
        
        exemples = doc.read()
        exemples = eval(exemples)
        
        doc.close()
        
        dico_return = {}
        
        if len(tags) > 5 :
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Mc!search")
            embed.add_field(name="❌ Vous avez dépassé le nombre maximum d'arguments (5)",value = "`Mc!taglist` pour la liste des tags disponibles", inline=False)
            await ctx.send(embed=embed)
        
        if len(tags) < 1 :
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Mc!search")
            embed.add_field(name="❌ Merci de rentrer au minimum un argument",value = "`Mc!taglist` pour la liste des tags disponibles", inline=False)
            await ctx.send(embed=embed)
        
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
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
                embed.set_author(name="Mc!search")
                embed.add_field(name="❌ Aucune information n'a été trouvée",value = "`Mc!taglist` pour la liste des tags disponibles", inline=False)
                await ctx.send(embed=embed)
            
            else :
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
                embed.set_author(name="Mc!search | résultats de la recherche")
                embed.add_field(name="Commande",value = "```"+dico_return[i][0]+"```", inline=False)
                embed.add_field(name="Description",value = i, inline=False)
                embed.add_field(name="Tags",value = "`"+"`, `".join(dico_return[i][1])+"`", inline=False)
                await ctx.send(embed=embed)

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
    async def add(ctx, *commands):
        """Work in progress"""
        """Mc!add '<description>' '<tag1, tag2, tag3>' <command arguments>"""
        if len(commands) > 2 : 
            description = commands[0]
            tags = commands[1]
            
            commands = [i for i in commands[2:]]
            
            command = ""
            
            for i in commands :
                command = command + " " + i
            
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name="⚙️ Cette commande n'est pas disponible pour le moment")
            await ctx.send(embed=embed)
                
            
            
            doc = open('./data/exemples.txt','r',encoding='utf-8')
            
            exemples = doc.read()
            exemples = eval(exemples)
            
            tags = tuple(tags)
            
            doc.close()
            
            exemples[description] = (command,(tags))
        
            doc = open('./data/exemples.txt','w',encoding='utf-8')
            
            doc.write(str(exemples))
            
            doc.close()
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name="Fonction enregistrée, merci de votre contribution ✅")
            await ctx.send(embed=embed)

        else : 
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Mc!add")
            embed.add_field(name="❌ Merci d'entrer au moins trois arguments",value = "`Mc!help add` pour plus d'informations", inline=False)
            
            await ctx.send(embed=embed)
        
class Useful() :
    """Commandes Utiles"""

    @bot.command(pass_context = True,category = "Help")
    async def off(ctx,*command) :
        """turns off the bot"""
        
        if ctx.author.id == 522304532756037633 :
            
            game = discord.Game("💤 Sleeping")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            await ctx.message.add_reaction("✅")
            
            time.sleep(10)
            
            quit()
            
            
        else :
            print(ctx.author.id,"tried to shutdown the bot")
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name="❌ Tu n'as pas les permissions requises pour effectuer cette action")
            
            await ctx.send(embed=embed)
        
        
    
    @bot.command()
    async def info(ctx):
        """Useful Informations"""
        
        doc = open('./data/Help.txt','r',encoding='utf-8')
        helped = doc.read()
        helped = eval(helped)
        doc.close()

        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Mc!info')
        embed.add_field(name="🤖 Actuellement dans :", value = str(len([s for s in bot.guilds])) + " Serveurs", inline = False)
        embed.add_field(name="📚 Nombre d'aides de type documentation données :", value = str(helped[0]) + " Messages de documentation", inline = False)
        embed.add_field(name="⚙️ Nombre d'aides de type exemples donnés : ", value = str(helped[1]) + " Exemples", inline = False)

        await ctx.send(embed=embed)
        
        print("-----\nInfos envoyées\n-----")
        
            
    @bot.command()
    async def invite(ctx):
        """Obtain an Invit link"""
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Mc!invite')
        embed.add_field(name="🔗 Voici le lien pour m'ajouter dans un autre serveur discord :", value = "https://discord.com/oauth2/authorize?client_id="+str(bot.user.id)+"&scope=bot&permissions=0", inline = False)
        await ctx.send(embed=embed)
        print("-----\nInvitation envoyée\n-----")

    @bot.command()
    async def status(ctx):
        """Display current status"""
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name="En ligne ✔️")
        await ctx.send(embed=embed)
        print("-----\nStatut : en ligne\n-----")
        


bot.run(TOKEN)
