import logging

from aiogram import types

from WangWangBot.utils import docker

from WangWangBot.config import Config
from WangWangBot.utils import docker

def services_button() -> tuple:
    """
    所有服务的按钮

    :return: tuple of buttons
    """
    text_and_data = (
        ("up", "services:up"),
        ("down", "services:down"),
        ("ps", "services:ps"),
        ("top", "services:top"),
        ("pull", "services:pull")
    )    
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    return row_btns


def service_button(service_name:str) -> tuple:
    """
    单个服务的按钮
    """
    text_and_data = (
        ("up", f"servic_up:{service_name}"),
        ("logs", f"servic_logs:{service_name}"),
        ("返回", f"servic_back")
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    return row_btns

def service_list_keyboard() -> types.InlineKeyboardMarkup:
    """
    :param service_list: list of services
    :return: InlineKeyboardMarkup
    """
    service_list = docker.check_dir_service_list(Config.DOCKER_COMPOSE_DIR)
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(*services_button())
    for service in service_list:
        row_btns = (types.InlineKeyboardButton(service.name, callback_data="service_{service.name}") for service in service_list)
        keyboard_markup.add(*row_btns)
    return keyboard_markup