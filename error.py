from config import SLOT_SIZE
from utils import read_parking_lots


def is_valid_slot_num(slot_num):
    if slot_num.isdecimal() and int(slot_num) <= SLOT_SIZE:
        return True


def is_slot_free(slot_num):
    parked_vehicles = read_parking_lots()
    if slot_num.isdecimal() and \
            not parked_vehicles.get(int(slot_num)):
        return True


def is_any_free_slot():
    if len(read_parking_lots()) < SLOT_SIZE:
        return True


def is_vechicle_already_parked(vechicle_num):
    if vechicle_num in list(read_parking_lots().values()):
        return True
