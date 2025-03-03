from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import LinkPreviewOptions
from aiogram.enums import ParseMode


class Database:  # TODO: write database class
    def __init__(self):
        pass


class BeanBotDefaults(DefaultBotProperties):
    def __init__(self):
        super().__init__()
        self.parse_mode = ParseMode.MARKDOWN_V2
        self.disable_notification = False
        # protect_content: Optional[bool] = None
        # """Protects content from copying."""
        self.link_preview = LinkPreviewOptions(is_disabled=True)
        self.link_preview_is_disabled = True
        # link_preview_prefer_small_media: Optional[bool] = None
        # link_preview_prefer_large_media: Optional[bool] = None
        # link_preview_show_above_text: Optional[bool] = None
        self.show_caption_above_media = False


class BeanBot(Bot):
    def __init__(self, token: str, db: Database, *args):
        self.db = db
        self.debug = False

        defaults = BeanBotDefaults()

        super().__init__(token=token, default=defaults, *args)
