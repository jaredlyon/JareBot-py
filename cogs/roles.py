from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # returns a list of these roles: 
    # Light Blue, Dark Blue, Orange, Yellow, Blurple, Purple, Green, Peach, Pink, Red
    # teen that cares™, movie-goers, academia, aesthetic, coders, floofs, news, dinos, vc
    @commands.command()
    async def roles(self, ctx):
        await ctx.send("Light Blue, Dark Blue, Orange, Yellow, Blurple, Purple, Green, Peach, Pink, Red, teen that cares™, movie-goers, academia, aesthetic, coders, floofs, news, dinos, vc")

    # adds a role based on the string provided by the user
    # kicks back an error if the role doesnt exist
    @commands.command()
    async def addrole(self, ctx, role_name):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            await ctx.send("Role not found")
        else:
            await ctx.author.add_roles(role)
            await ctx.send("Role added")
    
    # removes a role based on the string provided by the user
    # kicks back an error if the role doesnt exist or if the user does not have the role
    @commands.command()
    async def removerole(self, ctx, role_name):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            await ctx.send("Role not found")
        else:
            await ctx.author.remove_roles(role)
            await ctx.send("Role removed")

def setup(bot):
    bot.add_cog(Roles(bot))