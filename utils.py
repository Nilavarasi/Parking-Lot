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
    print(parked_vechicle)
    return {'slot': slot_num,
            'vechicle_plate_num': parked_vechicle.get(int(slot_num))
            or 'No Such Vechicle'}


def park_vechicle(plate_num):
    parked_vechicle_nums = read_parking_lots().keys()
    slots = set(range(1, SLOT_SIZE+1))
    empty_slots = sorted(list(slots - set(parked_vechicle_nums)))
    assigning_slot = empty_slots[0]
    parking_data_to_csv(assigning_slot, plate_num)
    return {'assigned_slot': assigning_slot,
            'vechicle_num': plate_num}


def parking_data_to_csv(assigning_slot, plate_num):
    parked_vechicles = read_parking_lots()
    parked_vechicles[assigning_slot] = plate_num
    df = pd.DataFrame.from_dict(parked_vechicles, orient="index")
    df.to_csv("parking.csv", header=None)
    return


def unpark_vechicle(plate_num):
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
