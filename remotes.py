from errbot import BotPlugin, botcmd

from resources import Resources, MDResourcesTable


class Remote(object):

    def __init__(self, user, room, tag, url):
        self.user = user
        self.room = room
        self.tag = tag
        self.url = url

    @property
    def uuid(self):
        return self.tag


class Remotes(Resources):
    KEY = "remotes"
    RESOURCE_CLASS = Remote
    NAMESPACE = "Remotes"


class MDRemotesTable(MDResourcesTable):

    pass


class RemotesPlugin(BotPlugin):

    @botcmd
    def remotes(self, msg, args):
        """
        """
        table = MDRemotesTable(
            Remotes(self),
            "tag", "url")
        return str(table)

    @botcmd
    def remote(self, msg, args):
        """
        """
        args = args.split(" ")
        if not len(args) == 2:
            return "Hey @%s, do `remote $tag $repo_url`" % msg.frm
        remotes = Remotes(self)
        remotes.add(msg.frm.username, str(msg.frm.room), *args)
        return (
            "Added tagged remote for you @%s (%s:%s)"
            % (msg.frm, args[0], args[1]))
