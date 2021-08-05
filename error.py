from config import SLOT_SIZE
from utils import read_parking_lots


def is_valid_slot_num(slot_num: str) -> bool:
    """
        is_valid_slot_num - Check the given slot number is valid
        @params slot_num  - the given slot number
        returns True      - If the slot number is valid
    """
    if slot_num.isdecimal() and int(slot_num) <= SLOT_SIZE:
        return True


def is_slot_free(slot_num: str) -> bool:
    """
        is_slot_free      - Check the given slot number is free
        @params slot_num  - the given slot number
        returns True      - If the slot number is free
    """
    parked_vehicles = read_parking_lots()
    if slot_num.isdecimal() and \
            not parked_vehicles.get(int(slot_num)):
        return True


def is_any_free_slot():
    """
        is_any_free_slot  - Check there is any free slot
        @params None
        returns True      - If there is free slot
    """
    if len(read_parking_lots()) < SLOT_SIZE:
        return True


def is_vechicle_already_parked(vechicle_num: str) -> bool:
    """
        is_vechicle_already_parked - Check vechicle is parked
        @params vechicle_num       - the given vechicle number
        returns True               - If vechicle is parked
    """
    if vechicle_num in list(read_parking_lots().values()):
        return True
