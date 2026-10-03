# tests/conftest.py
import pytest


@pytest.fixture(scope="session")
def valid_macs() -> list[str]:
    """Набор синтаксически корректных MAC-адресов."""
    return [
        "00:ff:33:77:00:ff",
        "00-FF-33-77-00-FF",
        "AA:BB:CC:DD:EE:FF",
        "a1:b2:c3:d4:e5:f6",
        "12-34-56-78-9A-BC",
        "00:00:00:00:00:00", 
        "FF:FF:FF:FF:FF:FF",  
    ]


@pytest.fixture(scope="session")
def invalid_macs() -> list[str]:
    """Набор заведомо некорректных MAC-адресов."""
    return [
        "",                         
        "00:ff:33:77:00",           
        "00:ff:33:77:00:ff:aa",     
        "00:ff:33:77:00:gg",        
        "00:ff:33:77:00:ff:",       
        "00:ff:33:77:00:ff\n",     
        "00:ff:33:77:00-ff",        
        "00:ff:33:77:00:ff:00",     
        "00:ff:33:77:00:f",         
        "00:ff:33:77:00:fff",      
    ]