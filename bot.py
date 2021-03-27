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
    
            embed1 = discord.Embed(
                colour = discord.Colour.orange()
            )
    
            embed1.set_author(name='Categorie Utiles :')
            embed1.add_field(name='Mc!info', value = 'Informations utiles', inline = False)
            embed1.add_field(name='Mc!invite', value = "Obtenir un lien d'invitation", inline = False)
            embed1.add_field(name='Mc!status', value = 'Affiche la disponibilité du bot', inline = False)
    
    
    
            await ctx.send( embed=embed )
            await ctx.send( embed=embed1 )
            await ctx.send( "Taper `Mc!help <command>` pour plus d'infos sur une commande" )
                
            print("-----\nHelp envoyé\n-----")
            
        elif len(parameters) > 0 :
            
            command = parameters[0]
            Help_dict = {}
            
            #Help_dict["add"] = ("Ne pas Utiliser","Pas encore disponible")
            Help_dict["doc"] = ("Mc!doc <Minecraft Command Name>","Renvoie la documentation Minecraft du mot-clé selectionné")
            Help_dict["exemple"] = ("Mc!exemple <Minecraft Command Name>","Donne les exemples disponibes de la commande sélectionnée")
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
                await ctx.send( embed = embed )
                print("-----\nHelp",command,"envoyé\n-----")
            else :
                await ctx.send(":red_circle: Cette commande n'existe pas ou n'est pas disponible")
                
            
            
    
    @bot.command(pass_context = True,category = "Help")
    async def doclist(ctx):
        """Return the list of all Minecraft commands available"""
                
        url = "https://fr-minecraft.net/61-guide-des-commandes-minecraft.php"
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        raw_data = soup.find_all("a", class_="content_popup_link")
        commandslist = ', '.join(["`"+i.text[1:]+"`" for i in raw_data if i.text[0] == '/'])
  
        list_of_commands = ":books: Voici ce que vous avez demandé :\n" + commandslist
        
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
        
        list_of_commands = ":gear: Voici les paramètres de recherche disponibles :\n" + to_send
        
        await ctx.send(list_of_commands)
    

    @bot.command(pass_context = True,category = "Help")
    async def exemple(ctx,*parameters):
        """Return a minecraft exemple for the selected command"""
        cmd = parameters[0]

        url = "https://fr-minecraft.net/commande-"+cmd+".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        examples = str(soup.find_all("div", class_="cmd_exemple")[0])

        exsoup = BeautifulSoup(examples, 'html.parser')
        commands = [i.text for i in exsoup.find_all("textarea", class_="input-exemple")]
        comments = [BeautifulSoup(i.split('<textarea')[0],'html.parser').text for i in examples.split('</textarea>') if BeautifulSoup(i.split('<textarea')[0],'html.parser').text!=""]
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
                
                    to_return = ":books: Voici la documentation de la commande */" + com + "* :```" + docu + "```" + description
                    
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
                await ctx.send("Rien n'a été trouvé")
                print("-----\nRessource non trouvée\n-----")
                
        else : 
            await ctx.send("Merci de rentrer au moins un argument, `Mc!help doc` pour plus d'informations")
        
    @bot.command(pass_context = True,category = "Help")
    async def search(ctx, *tags):
        """Comme une recherche Internet, mais avec des commandes Minecraft"""
        
        doc = open('./data/exemples.txt','r',encoding='utf-8')
        
        exemples = doc.read()
        exemples = eval(exemples)
        
        doc.close()
        
        dico_return = {}
        
        if len(tags) > 5 :
            await ctx.send("Vous avez dépassé le nombre maximum d'arguments (5)")
        
        if len(tags) < 1 :
            await ctx.send("Merci de rentrer au minimum un argument `Mc!help search` pour plus d'informations")
        
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
            
                await ctx.send("Aucune information n'a été trouvée, entrez `Mc!taglist` pour la liste des tags disponibles")
            
            else :
                
                to_return = "Voici :"
                
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
                    
            await ctx.send(":gear: Cette commande n'est pas disponible pour le moment")
                
            
            
            doc = open('./data/exemples.txt','r',encoding='utf-8')
            
            exemples = doc.read()
            exemples = eval(exemples)
            
            tags = tuple(tags)
            
            doc.close()
            
            exemples[description] = (command,(tags))
        
            doc = open('./data/exemples.txt','w',encoding='utf-8')
            
            doc.write(str(exemples))
            
            doc.close()
            
            await ctx.send("Fonction enregistrée, merci de votre contribution :white_check_mark:")
            
        else : await ctx.send("Merci d'entrer au moins un argument, `Mc!help add` pour plus d'informations")
        
        
class Useful() :
    """Commandes permettant de contacter le personnel du bot"""

    @bot.command(pass_context = True,category = "Help")
    async def off(ctx,*command) :
        """turns off the bot"""
        
        if ctx.author.id == 522304532756037633 :
            
            game = discord.Game("💤 Sleeping")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            await ctx.message.add_reaction("white_check_mark")
            
            time.sleep(10)
            
            quit()
            
            
        else :
            print(ctx.author.id,"tried to shutdown the bot")
            await ctx.send("Tu n'as pas les permissions requises pour effectuer cette action")
        
        
    
    @bot.command()
    async def info(ctx):
        """Useful Informations"""
        
        doc = open('./data/Help.txt','r',encoding='utf-8')
        
        helped = doc.read()
        helped = eval(helped)
        
        doc.close()
        
        to_send = "\n\n:robot: Actuellement dans " + str(len([s for s in bot.guilds])) + " Serveurs"
        
        to_send = to_send + "\n:books: Nombre d'aides de type documentation données : " + str(helped[0])
        to_send = to_send + "\n:gear: Nombre d'aides de type exemples données : " + str(helped[1])
        
        await ctx.send(to_send)
        
        
        print("-----\nInfos envoyées\n-----")
        
        
    @bot.command()
    async def invite(ctx):
        """Obtain an Invit link"""
                
        await ctx.send(":link: Voici le lien pour m'ajouter dans un autre serveur discord : \n https://discord.com/oauth2/authorize?client_id="+str(bot.user.id)+"&scope=bot&permissions=0")
        
        print("-----\nInvitation envoyée\n-----")

@bot.command()
async def status(ctx):
    """Display current status"""
    
    await ctx.send("`En ligne` :white_check_mark:")
    print("-----\nStatut : en ligne\n-----")
    


bot.run(TOKEN)
