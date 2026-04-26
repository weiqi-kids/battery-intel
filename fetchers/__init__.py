"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .albemarle import AlbemarleFetcher
from .basf import BasfFetcher
from .byd import BydFetcher
from .catl import CatlFetcher
from .eve import EveFetcher
from .ganfeng import GanfengFetcher
from .lg_energy import LgEnergyFetcher
from .nio import NioFetcher
from .panasonic import PanasonicFetcher
from .pilbara import PilbaraFetcher
from .rivian import RivianFetcher
from .samsung_sdi import SamsungSdiFetcher
from .sk_on import SkOnFetcher
from .sqm import SqmFetcher
from .tesla import TeslaFetcher
from .umicore import UmicoreFetcher
from .volkswagen import VolkswagenFetcher

FETCHERS = {
    "albemarle": AlbemarleFetcher,
    "basf": BasfFetcher,
    "byd": BydFetcher,
    "catl": CatlFetcher,
    "eve": EveFetcher,
    "ganfeng": GanfengFetcher,
    "lg_energy": LgEnergyFetcher,
    "nio": NioFetcher,
    "panasonic": PanasonicFetcher,
    "pilbara": PilbaraFetcher,
    "rivian": RivianFetcher,
    "samsung_sdi": SamsungSdiFetcher,
    "sk_on": SkOnFetcher,
    "sqm": SqmFetcher,
    "tesla": TeslaFetcher,
    "umicore": UmicoreFetcher,
    "volkswagen": VolkswagenFetcher,
}
