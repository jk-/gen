

A bot that reads issue tickets on github and programatically completes a pull request.

	IE:
		ISSUE: "Update pip to 19"
		Bot reads the issue title
		Finds requirements.txt
		REGEX the pip line
		Hits PIP server to find latest 19 version
		Replaces version,
			commits
			pushes
			creates PULL REQUEST


name: KafkaConsumer

name: KafkaSchema

name: Config

name: Bot
	Connection Config(host):Config(port)
        on success send PASS Config(pass)
        on success send NICK Config(nick)
        on success Config(channels) send join channel
    Connection on recv
        KafkaSchema:JsonFormat {username: username, message: message}
            KafkaConsumer saves Config(twitch_topic)

name: CommandService
    KafkaConsumer on latest
        in Commands Connection send value

name: TwitchNLP
    kafkaConsumer on latest
        Twitch

name: JsonFormat
    dump data %data%


    Create a Twitch Bot that connects to twitch irc.
    Make sure to login with my username and password.
    On receiving a message save it to Kafka on the topic
    taco_bell in a json format. Also, connect to a kafka
    topic bot_messages. On receiving a message from bot_messages
    send that data to twitch.


python compile
    Go through YML files and parse connection tree

    Parse all name leveled tokens (JsonFormat, Connection, TWitchConnection, Kafka)

        Find gen.CLASS_NAME relative to yml files
            EXTEND if inherits is set
                and dive into tree ->>> connection.yml
                Generate tpl file
                extend from template
                    `class TwitchConnection(Connection):
                        pass`
        Parse methods and inject into generated file
            (SEE extends from template)
            Dive into tree of on_sucess (yml)
                and inject inherited classes (Expects in this case, maybe this
                    is pre-built into codegen)
                        `on_sucess(self, value):
                            return Expects(value, %s)
                            ``
                        --- How does method know return or set?
                        --- Can this be apart of Expects since it always is returned?
                        --- Is Expects in the wrong place?

python gen
    save each line of the files as an md5 has representation (see Docker Cache)
    Bot ---> md5(Bot)
        TwitchConnect --> md5(TWitchConnect).. etc maybe not md5, but a hashed value
    This allows us to only generate lines that have changed and can we inject this into the code?


Pre-built tokens:
    Expects - Two params value injected and value expected - if not 2nd, assume true
    Asserts (Accepts? no because we can parse yml??? seems excessive)
    Returns JsonFormat { }


Bot
	TwitchConnection
        connect
            success Config.channels send `channel`
            failure

Lower indent means relative to method chain above:
    do we use kwards to inject addition args?



Bot -> 1448e86d90e0feb307c2894c24e87767
    TalisConfig -> extends Config
	TwitchConnection -> 6e04ed33c4ce147b086b6b83b9eb52a4
        connect -> 62a9f7572d562fe17d35bf8f2bbc4664
        on success Config.channels join `channel` -> 950c717c7497ed54bb2b4f79db6c424e
        on recv
            Expects Config.log_level `debug`
            StdOut write `output`

    ... and we made a change to on_sucess ->
        on success join `jonthomask` -> bc0067c51521afe2499aa4aa6c94016f

    ... and what if we changed TalisConfig to TalisSuperConfig
        8cafd1218f812e0fca17501eae99fd22
        and kept all the getters the same?
        Then we can regex the md5 of TalisConfig and replace with Regex of TalisConfig



Bot
    TalisConfig
	TwitchConnection
        connect
        on success JoinIntial
            Expects TwitchConnection.connected
            TalisConfig.channels TwitchConnection.join `channel`
        on recv Log
            Expects TalisConfig.log_level `debug`
            StdOut write `output`
        on send Log
            StdOut write `output`


KafkaBot:
    Bot
        on recv:KafkaStore
            KafkaStore JsonFormat `{username: username, message: message}`









BotCommandService
    Kafka



- Need to register event handlers and method calls

namespacing with localized namespace ^^^

need to prefix the variable names with an incremental alphanumeric char
    a -> Z
    aa -> ZZ
    aaa -> ZZZ

bot.py
    import TwitchConnection
    import TalisConfig


    class Bot(object):
        def __init__(self, a_6e04ed33c4ce147b086b6b83b9eb52a4, b_cf0a6c82dc398060a3362abb257d6899):
            self.a_6e04ed33c4ce147b086b6b83b9eb52a4 = TwitchConnection()
            self.b_cf0a6c82dc398060a3362abb257d6899 = TalisConfig()

        def on_sucess_950c717c7497ed54bb2b4f79db6c424e(self):
            channels = self.b_cf0a6c82dc398060a3362abb257d6899.channels
            if channels:
                for channel in channels:
                    self.a_6e04ed33c4ce147b086b6b83b9eb52a4.join_channel(channel)

        def on_sucess_bc0067c51521afe2499aa4aa6c94016f(self, value):
            self.a_6e04ed33c4ce147b086b6b83b9eb52a4.join_channel(value)

        def on_recv_md5_hash():
            pass

if __name__ = "__main__":
    bot_1448e86d90e0feb307c2894c24e87767 = Bot()
    bot.connect()
    bot.on_sucess_950c717c7497ed54bb2b4f79db6c424e()
    bot.on_recv_md5_hash()


Will need to tokenize each word:

Top level token:
[
    'Bot' => gen.NAME,
    'TwitchConnection' => gen.CLASS_NAME,
    'send' => gen.METHOD_NAME
]






import SocketConnection


class TwitchBot(object):
    def __init__(self, host, port):
        # this will be md5 HASH
        self.socket_connect = SocketConnection(host, port)
        self.config = Config()

    # SocketConnection connect with context
    def a_bdfb71ffe65afed090a0c76e6d2f5825(self):
        self.socket_connect.connect()
        self.socket_connect.send(PASS self.config.pass)
        self.socket_connect.send(NICK self.config.nick)

    def a_on_sucess_f5801a3251f77490cd6a40011e5bf05a(self):
        capture = socket_connect.recv(1024)
        if capture == 001:
            self.connected = True



if __name__ = "__main__":
    bot = Bot()
    bot.a_bdfb71ffe65afed090a0c76e6d2f5825()
    bot.a_on_sucess_f5801a3251f77490cd6a40011e5bf05a()



TwitchBot SocketConnection Config(host):Config(port)
    SocketConnection connect
        send PASS Config(pass)
        send NICK Config(nick)
    SocketConnection:on_sucess
        Capture recv
        Expects Capture 001
        Set connected True    
        Config(channels) send join_channel channel
    SocketConnection:join_channel
        send JOIN :%s


Capture (Core) = variable assignment?
Expects (Core) = Asserting validation?
Spaced variables from object are methods
colon names are custom methods
Set (Core) = set an object level var


Bot
    TalisConfig
	TwitchConnection
        connect
        on success JoinIntial
            Expects TwitchConnection.connected
            TalisConfig.channels TwitchConnection.join `channel`
        on recv Log
            Expects TalisConfig.log_level `debug`
            StdOut write `output`
        on send Log
            StdOut write `output`
