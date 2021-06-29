regions = {1: 'NA', 2: 'EU', 3: 'KR', 5: 'CN'}
game_modes = {201 : '1v1', 202: '2v2', 203: '3v3', 204: '4v4', 206: 'Archon'}


def load_data():
    """ Loads data from CSV files into a dictionary
    Not loading arranged teams at the moment """

    data = dict()
    for region, sregion in regions.items():
        data[sregion] = dict()
        for game_mode, sgame_mode in game_modes.items():
            path = f"data/47-{region}-1-{game_mode}-0.csv"
            with open(path,'r') as f:
                data[sregion][sgame_mode] = [int(i.strip()) for i in f.readlines()]
    return data