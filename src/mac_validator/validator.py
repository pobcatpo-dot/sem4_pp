# src/mac_validator/validator.py
import re

MAC_PATTERN = re.compile(r"^[0-9A-Fa-f]{2}(?P<sep>[:-])(?:[0-9A-Fa-f]{2}(?P=sep)){4}[0-9A-Fa-f]{2}$")

def is_valid_mac(mac: str) -> bool:
    """
    Проверяет, является ли строка корректным MAC-адресом.
    
    Поддерживаемые форматы:
    - 00:ff:33:77:00:ff
    - 00-ff-33-77-00-ff
    """
    if not isinstance(mac, str):
        return False
    return bool(MAC_PATTERN.fullmatch(mac))
