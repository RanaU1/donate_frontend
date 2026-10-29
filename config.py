"""
config.py

All the things you will edit live here. Change values, run `python3 build.py`.
"""

from dataclasses import dataclass
from urllib.parse import quote


@dataclass(frozen=True)
class Site:
    url: str
    name: str
    handle: str
    title: str
    description: str
    bio: str


@dataclass(frozen=True)
class Images:
    # Put your own images in static/image/. Missing file = placeholder shown.
    photo: str = "static/image/me.png"
    upi_qr: str = "static/image/upi_qr.jpg"


@dataclass(frozen=True)
class Links:
    portfolio: str
    telegram: str
    facebook: str
    youtube: str
    whatsapp: str  # https://wa.me/<country code + number>, no + or spaces
    email: str
    razorpay: str
    paypal: str


@dataclass(frozen=True)
class Upi:
    id: str
    payee: str

    @property
    def link(self) -> str:
        return f"upi://pay?pa={quote(self.id)}&pn={quote(self.payee)}&cu=INR"


@dataclass(frozen=True)
class Bank:
    account_holder: str
    bank: str
    account_number: str
    ifsc: str
    branch: str

    def rows(self) -> list[tuple[str, str]]:
        """
        (label, value) pairs shown on the page, in this order.
        """
        return [
            ("Account holder", self.account_holder),
            ("Bank", self.bank),
            ("Account number", self.account_number),
            ("IFSC", self.ifsc),
            ("Branch", self.branch),
        ]


@dataclass(frozen=True)
class Project:
    icon: str
    title: str
    text: str
    url: str = ""  # empty = card is not a link


@dataclass(frozen=True)
class Goal:
    show: bool = False  # keep False until the numbers are real
    monthly_cost: int = 3000
    raised: int = 0

    @property
    def pct(self) -> int:
        return (
            min(100, round(self.raised / self.monthly_cost * 100))
            if self.monthly_cost
            else 0
        )


# ----------------------------- EDIT BELOW -----------------------------

SITE = Site(
    url="https://donate.rana49.online",
    name="Rana",
    handle="RanaUniverse",
    title="Support Rana: Keep Free Bots, Website & Tools Running",
    description=(
        "I build free Telegram bots and websites. Servers cost money every month. "
        "Your donation keeps them alive."
    ),
    bio=(
        "👨‍💻 Hey, I'm Rana Universe — a self-appointed Python backend developer "
        "from my own little universe 🌌😂\n\n"
        "🤖 I build Telegram automation bots, websites, and useful tools "
        "to make human life a little easier (and maybe save a few clicks). 🪄\n\n"
        "🌍 I believe in free, open-source projects that anyone can use. "
        "No paywalls, just code and chaos. 💻✨\n\n"
        "💸 The code is free. The servers? Not so much. 🥲 "
        "If you like what I build, help keep my tiny digital universe alive! 🚀❤️"
    ),
)

IMAGES = Images(
    photo="static/image/me.png",
    upi_qr="static/image/upi_qr.jpg",
)

LINKS = Links(
    portfolio="https://rana49.online",
    facebook="https://www.facebook.com/RanaUniverse",
    youtube="https://www.youtube.com/@RanaUniverse",
    whatsapp="https://wa.me/917044394156",
    telegram="https://t.me/RanaUniverse",
    email="RanaUniverse321+donate@gmail.com",
    razorpay="https://razorpay.me/@RanaUniverse",
    paypal="https://paypal.me/RanaUniverse321",
)

UPI = Upi(
    id="RanaUniverse@upi",
    payee="Manik Kumar Rana",
)

BANK = Bank(
    account_holder="Manik Kumar Rana",
    bank="Jio Payments Bank",
    account_number="003520391382509",
    ifsc="JIOP0000001",
    branch="Jio Payments Bank IMPS / RTGS HO",
)

PROJECTS = [
    Project(
        "🤖",
        "Telegram bots",
        "Useful Automation Bots that save you time. Free to use.",
        url="https://t.me/SunoAiSongDownloadBot",
    ),
    Project(
        "🎵",
        "Suno AI Song Download",
        "Download your Suno songs from a simple website or Bot.",
        url="https://sunoaisongdownload.online",
    ),
    Project(
        "🌐",
        "Web tools",
        "Let's Learn Python Backend Technologies.",
        url="https://rana49.online",
    ),
]

GOAL = Goal(
    show=True,
    raised=50,
    monthly_cost=3000,
)
