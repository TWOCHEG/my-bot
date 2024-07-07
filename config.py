# ──────────────────────────◄ ✓ bot ►──────────────────────────
BotId = YOURBOTID  # bot id
TOKEN = YOURBOTTOKEN  # bot token
CommandCooldown = 60  # commands delay
prefix = f'<@{BotId}>'  # prefix

# ──────────────────────────◄ ۩ currency ►──────────────────────────
# └─ List ▧︎
ListUpdatePreDelay = 300  # pre update delay
ListUpdateDelay = 60  # update delay
CurrencyListChannel = CHANNELID  # list channel
# └─ File
CurrencyFile = 'путь к пайчарму или хз/FluffBot/modules/FanModules/currency/currency.json'  # currency data file

# ──────────────────────────◄ ✎ AutoMod ►──────────────────────────
# └─ AntiSpam ⌨︎
MessageSpamCount = 3  # message
CtxSpamCount = 7  # ctx
MentionsSpamCount = 1  # mentions
# └─ Link ☴︎
LinkWhiteList = [
            'https://www.youtube.com/',
            'https://youtu.be/',
            'https://github.com/',
            'https://cdn.discordapp.com/',
            'https://stackoverflow.com/',
            'https://otvet.mail.ru/',
            'https://qna.habr.com/',
            'https://yandex.ru/games/',
            'https://media1.tenor.com/',
            'https://media.tenor.com/',
            'https://tenor.com/'
        ]

# ──────────────────────────◄ ▤ id ►──────────────────────────
OwnerId = YOURID  # your id
GuildId = YOURGUILDID  # guild id
GirlId = ID  # /sex age fix
VerifyRole = ROLEID  # роль которая должна выдаватся участнику после прохождения верификации
GodList = [BotId, OwnerId]  # участники на которых небудет работать авто мод и мут в рулетке

# ──────────────────────────◄ hello\goodbye ►──────────────────────────
MemberJoinChannel = CHANNELID  # join channel id
MemberRemoveChannel = CHANNELID  # remove channel id
AvatarTemp = 'путь к пайчарму или хз/FluffBot/modules/AvatarProces/avatar_temp/'  # avatar average color

# ──────────────────────────◄ ¾ iq ►──────────────────────────
iq = 'путь к пайчарму или хз/BOT/FluffBot/modules/FanModules/IQ/IQ.json'  # data file

# ──────────────────────────◄ оформление консоли ►──────────────────────────
console_bot = '[B] | '
console_event = '[E] | '
console_command = '[/] | '
