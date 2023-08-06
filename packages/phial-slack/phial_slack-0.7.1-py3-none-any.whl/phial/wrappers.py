from typing import Dict, Pattern, IO, Optional, List, Union

MessageAttachmentJson = Dict[str, Union[str, Union[str, Dict[str, str]]]]


class Message():
    '''
    Used by phial to store data about the message that initiated
    the command.

    Attributes:
        text(str): The message contents
        channel(str): The Slack channel ID the message was sent from
        user(str): The user who sent the message
        timestamp(str): The message's timestamp
        team(str): The Team ID of the Slack workspace the message was
                   sent from
        bot_id(str, optional): If the message was sent by a bot
                               the ID of that bot.
                               Defaults to None.
    '''
    def __init__(self,
                 text: str,
                 channel: str,
                 user: str,
                 timestamp: str,
                 team: str,
                 bot_id: Optional[str] = None) -> None:
        self.text = text
        self.channel = channel
        self.user = user
        self.timestamp = timestamp
        self.team = team
        self.bot_id = bot_id

    def __repr__(self) -> str:
        return "<Message: {0} in {1}:{2} at {3}>".format(self.text,
                                                         self.channel,
                                                         self.team,
                                                         self.timestamp)

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__


class Command():
    '''
    The command object used by Phial.

    Attributes:
        command_pattern(str): The regex used for matching the command
        channel(str): The Slack channel ID the command was called from
        args(dict): Any arguments passed to the command
        user(str): The Slack User ID of the user who intiated the command
        message(`Message`): The message that initiated the command
        message_ts(str): The timestamp of the message that initiated the
                         command
        team(str): The Team ID of the Slack workspace the command was
                   called from
    '''
    def __init__(self,
                 command_pattern: Optional[Pattern[str]],
                 channel: str,
                 args: Optional[Dict],
                 user: str,
                 message: Message,
                 team: str) -> None:
        self.command_pattern = command_pattern
        self.channel = channel
        self.args = args
        self.user = user
        self.message = message
        self.message_ts = message.timestamp
        self.team = team

    def __repr__(self) -> str:
        return "<Command: {0}, {1} in {2}:{3}>".format(self.message.text,
                                                       self.args,
                                                       self.channel,
                                                       self.team)

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__


class MessageAttachmentField():
    '''
    Displays field in message attachment

    Attributes:
        title(str): The title of the field
        value(str): The value of the field
        short(bool): If false, 2 fields will be displayed on the same line

    '''
    def __init__(self,
                 title: Optional[str] = None,
                 value: Optional[str] = None,
                 short: Optional[bool] = None) -> None:
        self.title = title
        self.value = value
        self.short = short

    def __repr__(self) -> str:
        return "<Message Attachment Field with title {0} >".format(self.title)


class MessageAttachment():
    '''
    Displays a message attachment

    Attributes:
        fallback(str): Plain text summary of the attachment
        color(str): Hex code beginning with a '#' for the side bar colour
        author_name(str): Small text to display the authors name
        author_link(str): URL for link on authors name
        author_icon(str): URL for 16x16 icon beside the authors name
        title(str): The title of the attachment
        title_link(str): A URL for the attachment title
        text(str): The main text body of an attachment
        image_url(str): URL to an image file that will be displayed with
                        an attachment
        thumb_url(str): URL to an image file that will be displayed as a
                        thumbnail on the right side of a message attachment
        fields(list): A list of MessageAttachmentFields to display on the
                      attachment
        footer(str): Small text to help contextualize and identify an
                     attachment
        footer_icon(str): URL for 16x16 icon beside the footer

    '''
    def __init__(self,
                 fallback: Optional[str] = None,
                 color: Optional[str] = None,
                 author_name: Optional[str] = None,
                 author_link: Optional[str] = None,
                 author_icon: Optional[str] = None,
                 title: Optional[str] = None,
                 title_link: Optional[str] = None,
                 text: Optional[str] = None,
                 image_url: Optional[str] = None,
                 thumb_url: Optional[str] = None,
                 fields: Optional[List[MessageAttachmentField]] = None,
                 footer: Optional[str] = None,
                 footer_icon: Optional[str] = None) -> None:
        self.fallback = fallback
        self.color = color
        self.author_name = author_name
        self.author_link = author_link
        self.author_icon = author_icon
        self.title = title
        self.title_link = title_link
        self.text = text
        self.image_url = image_url
        self.thumb_url = thumb_url
        self.fields = fields
        self.footer = footer
        self.footer_icon = footer_icon

    def __repr__(self) -> str:
        return "<Message Attachment with text {0} >".format(self.text)


class Response():
    '''
    When returned in a command function will send a message, or reaction to
    slack depending on contents.

    Attributes:
        channel(str): The Slack channel ID the response will be sent to
        text(str): The response contents
        original_ts(str): The timestamp of the original message. If populated
                          will put the text response in a thread
        reation(str): A valid slack emoji name. NOTE: will only work when
                      original_ts is populated
        attachments(Union[List[MessageAttachment],
                          List[Dict[str, Dict[str, str]]]]):
                          A list of MessageAttachment objects to be attached
                          to the message
        ephemeral(bool): Whether to send the message as an ephemeral message
        user(str): The user id to display the ephemeral message to

    Examples:
        The following would send a message to a slack channel when executed ::

            @slackbot.command('ping')
            def ping():
                return Response(text="Pong", channel='channel_id')

        The following would send a reply to a message in a thread ::

            @slackbot.command('hello')
            def hello():
                return Response(text="hi",
                                channel='channel_id',
                                original_ts='original_ts')

        The following would send a reaction to a message ::

            @slackbot.command('react')
            def react():
                return Response(reaction="x",
                                channel='channel_id',
                                original_ts='original_ts')

    '''
    def __init__(self,
                 channel: str,
                 text: Optional[str] = None,
                 original_ts: Optional[str] = None,
                 attachments: Optional[Union[List[MessageAttachment],
                                       List[MessageAttachmentJson]]] = None,
                 reaction: Optional[str] = None,
                 ephemeral: bool = False,
                 user: Optional[str] = None) -> None:
        self.channel = channel
        self.text = text
        self.original_ts = original_ts
        self.reaction = reaction
        self.attachments = attachments
        self.ephemeral = ephemeral
        self.user = user

    def __repr__(self) -> str:
        return "<Response: {0}>".format(self.text)

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__


class Attachment():
    '''
    When returned in a command function will send an attachment to Slack

    Attributes:
        channel(str): The Slack channel ID the file will be sent to
        filename(str): The filename of the file
        content(`io.BufferedReader`): The file to send to Slack. Open file
                                      using open('<file>', 'rb')

    '''
    def __init__(self,
                 channel: str,
                 filename: Optional[str] = None,
                 content: Optional[IO[bytes]] = None) -> None:
        self.channel = channel
        self.filename = filename
        self.content = content

    def __repr__(self) -> str:
        return "<Attachment in {0} >".format(self.channel)
