import pandas as pd
from config import SLOT_SIZE


def read_parking_lots() -> list[dict]:
    """
        read_parking_lots - read data from parking.csv
        @Parmas: None
        returns: list of dictionary(slot, vechicle_number)
    """
    data = pd.read_csv("parking.csv",
                       header=None,
                       index_col=0,
                       squeeze=True).to_dict()
    return data


def get_parking_vechicle(slot_num: str) -> dict:
    """
        get_parking_vechicle - Get the parked vechicle in a given slot
        @params slot_num: Slot number of parked vechicle
        retuns          : dict
    """
    parked_vechicle = read_parking_lots()
    return {'slot': slot_num,
            'vechicle_plate_num': parked_vechicle.get(int(slot_num))
            or 'No Such Vechicle'}


def park_vechicle(plate_num: str) -> dict:
    """
        park_vechicle     - Park vechicle in a free slot
        @params plate_num : plate_num of parking vechicle
        returns: dict contains assigned slot and vechicle number
    """
    parked_vechicle_nums = read_parking_lots().keys()
    slots = set(range(1, SLOT_SIZE+1))
    empty_slots = sorted(list(slots - set(parked_vechicle_nums)))
    assigning_slot = empty_slots[0]
    parking_data_to_csv(assigning_slot, plate_num)
    return {'assigned_slot': assigning_slot,
            'vechicle_num': plate_num}


def parking_data_to_csv(assigning_slot: str, plate_num: str) -> None:
    """
        parking_data_to_csv    - add parked vechicle details to csv
        @params assigning_slot: slot number to be assigned
        @params plate_num     : plate number of a vechicle
        returns None
    """
    parked_vechicles = read_parking_lots()
    parked_vechicles[assigning_slot] = plate_num
    df = pd.DataFrame.from_dict(parked_vechicles, orient="index")
    df.to_csv("parking.csv", header=None)
    return


def unpark_vechicle(plate_num):
    """
        unpark_vechicle - Unpark given vechicle
        @params plate_num : plate_num of unparking vechicle
        returns: dict contains slot and vechicle number and status as success
    """
    output_data = {'slot': '', 'vechicle_num': ''}
    parked_vechicles = read_parking_lots()
    for slot, vechicle_num in parked_vechicles.items():
        if vechicle_num == plate_num:
            output_data['slot'] = slot
            output_data['vechicle_num'] = plate_num
            output_data['status'] = 'successfully removed'
            break
    del parked_vechicles[output_data['slot']]
    df = pd.DataFrame.from_dict(parked_vechicles, orient="index")
    df.to_csv("parking.csv", header=None)
    return output_data
