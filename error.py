from config import SLOT_SIZE


def is_valid_slot_num(slot_num):
    if slot_num.isdecimal() and int(slot_num) <= SLOT_SIZE:
        return True
