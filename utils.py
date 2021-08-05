import pandas as pd
from config import SLOT_SIZE


def read_parking_lots():
    data = pd.read_csv("parking.csv",
                       header=None,
                       index_col=0,
                       squeeze=True).to_dict()
    return data


def get_parking_vechicle(slot_num):
    parked_vechicle = read_parking_lots()
    return {'slot': slot_num,
            'vechicle_plate_num': parked_vechicle.get(slot_num)
            or 'No Such Vechicle'}


def park_vechicle(plate_num):
    parked_vechicle_nums = read_parking_lots().keys()
    slots = set(range(1, SLOT_SIZE+1))
    print('parked_vechicle_num', parked_vechicle_nums)
    print('slots', slots)
    empty_slots = sorted(list(slots - set(parked_vechicle_nums)))
    assigning_slot = empty_slots[0]
    parking_data_to_csv(assigning_slot, plate_num)
    return {'assigned_slot': assigning_slot,
            'vechicle_num': plate_num}


def parking_data_to_csv(assigning_slot, plate_num):
    data = read_parking_lots()
    data[assigning_slot] = plate_num
    df = pd.DataFrame.from_dict(data, orient="index")
    print(df)
    df.to_csv("parking.csv", header=None)
    return
