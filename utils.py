import pandas as pd


def read_parking_lots():
    data = pd.read_csv("parking.csv",
                       header=None,
                       index_col=0,
                       squeeze=True).to_dict()
    return data


def get_parking_vechicle(slot_num):
    parked_vechicle = read_parking_lots()
    return {'slot': slot_num,
            'vechicle_plate_num': parked_vechicle.get(int(slot_num))
            or 'No Such Vechicle'}
