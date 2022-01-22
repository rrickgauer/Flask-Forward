from __future__ import annotations
from dataclasses import dataclass

@dataclass
class SingleRequest:
    url     : str                = None
    headers : dict               = None
    files   : dict               = None
    data    : dict | str | bytes = None
    params  : dict               = None
    auth    : tuple              = None
    cookies : dict               = None
    hooks   : dict               = None
    method  : str                = None
    files   : dict | bytes       = None