from pprint import pprint
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# https://www.chess.com/leaderboard/live/rapid

chess_data = {
    100: 153998,
    200: 331911,
    300: 546477,
    400: 809310,
    500: 1046349,
    600: 1242352,
    700: 1326306,
    800: 1356145,
    900: 1221835,
    1000: 1059184,
    1100: 839186,
    1200: 663214,
    1300: 477409,
    1400: 330034,
    1500: 217951,
    1600: 140428,
    1700: 88209,
    1800: 55258,
    1900: 32832,
    2000: 21342,
    2100: 11453,
    2200: 6176,
    2300: 3171,
    2400: 1487,
    2500: 597,
    2600: 214,
    2700: 81,
    2800: 29,
    2900: 11,
    3000: 1,
    3100: 1,
    3200: 1
}


def get_chess_data():
    x = []
    y = []
    total_players = 0
    for elo, players in chess_data.items():
        total_players += players
        x.append(total_players)
        y.append(elo)
    return x, y



def get_chess_data_smoothed():
    x, y = get_chess_data()

    spl = make_interp_spline(x, y, k=3)
    M = sum(chess_data.values())
    xnew = list(range(0,M, int(M/100000)))
    ynew = spl(xnew)

    return xnew, ynew

    # # plt.scatter(x, y, label='O')
    # plt.plot(xnew, ynew, label='N')
    # plt.show()