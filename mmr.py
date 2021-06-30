import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from chess import get_chess_data, get_chess_data_smoothed
from load_data import load_data, regions
from winrate_calc import cwinrate

data = load_data()
plt.rcParams['figure.dpi'] = 150

league_target = {
    'Bronze': 0.04,
    'Silver': 0.23,
    'Gold': 0.23,
    'Platinum': 0.23,
    'Diamond': 0.23,
    'Master': 0.033,
    'GM': 1
}


def plot_histogram(data):
    data = sorted(data)
    start = 0
    for league, target in league_target.items():

        end = start + int(target * len(data))
        league_data = data[start:end]
        plt.hist(league_data,
                 int((league_data[-1] - league_data[0]) / 30),
                 label=league,
                 alpha=0.8)

        plt.text(
            (league_data[-1] + league_data[0]) / 2,
            20 * len(league_data) / (league_data[-1] - league_data[0]) + 300,
            league,
            rotation=90,
            ha="center")
        print(
            f"{league:10} \t{len(league_data)}\t{(len(league_data))/len(data):.2%}"
        )
        start = end

    plt.legend()
    plt.title("MMR distribution (1v1, all regions)")
    plt.xlabel("MMR")
    plt.ylabel("Player count")
    plt.grid(alpha=0.2)
    plt.savefig('MMR_hist.png')


plot_histogram(data['NA']['1v1'] + data['EU']['1v1'] + data['KR']['1v1'] +
               data['CN']['1v1'])


def compare_regions():
    plt.figure().clear()
    r = dict()
    for region in regions.values():
        r[f"{region} ({np.mean(data[region]['1v1']):.0f} mean)"] = data[
            region]['1v1']
    sns.histplot(r,
                 kde=True,
                 element='poly',
                 stat="density",
                 common_norm=False,
                 fill=True,
                 alpha=0.3)

    plt.xlabel("MMR")
    plt.title("MMR distribution (1v1)")
    plt.ylabel("Player count (density)")
    plt.grid(alpha=0.2)
    plt.savefig('MMR_dist_region_compare.png')


compare_regions()


def plot_curve(data):
    plt.figure().clear()
    data = sorted(data)
    start = 0

    for league, target in league_target.items():
        end = start + int(target * len(data))
        end = end if end < len(data) else len(data)
        league_data = data[start:end]

        plt.scatter(list(range(start, start + len(league_data))),
                    league_data,
                    s=2)
        plt.text((end + start) / 2 - 9000,
                 np.mean(league_data) + 300,
                 league,
                 rotation=90,
                 ha="center")

        print(
            f"{league:10} \t{start} \t{end} \t{(len(league_data))/len(data):.2%}"
        )

        start = end

    # Change xticks to percents
    percents = []
    percents_loc = []
    for percentile in range(0, 101, 10):
        percents.append(f"{percentile}%")
        percents_loc.append(int(len(data) * percentile / 100))
    plt.xticks(percents_loc, percents)

    plt.xlabel("Players")
    plt.title("MMR distribution (1v1, all regions)")
    plt.ylabel("MMR")
    plt.grid(alpha=0.2)
    plt.savefig('MMR_dist_1v1.png')


plot_curve(data['NA']['1v1'] + data['EU']['1v1'] + data['KR']['1v1'] +
           data['CN']['1v1'])


def plot_mmrs():
    plt.figure().clear()

    ndata = dict()
    for region in data:
        for mode in data[region]:
            if mode == 'Archon':
                continue
            if mode in ndata:
                ndata[mode] += data[region][mode]
            else:
                ndata[mode] = data[region][mode].copy()

    M = max((len(ndata[key]) for key in ndata))

    for mode in ndata:
        values = sorted(ndata[mode])
        x = [i * M / len(values) for i in range(len(values))]
        plt.plot(x, values, label=mode)

    xchess, ychess = get_chess_data()
    chess_max_players = max(xchess)
    xchess = [i * M / chess_max_players for i in xchess]
    ychess = [i * 2.2 for i in ychess]
    plt.plot(xchess, ychess, label='Fast chess')

    # Change xticks to percents
    percents = []
    percents_loc = []
    for percentile in range(0, 101, 10):
        percents.append(f"{percentile}%")
        percents_loc.append(int(M * percentile / 100))
    plt.xticks(percents_loc, percents)

    plt.xlabel("Players")
    plt.title("MMR distribution (all regions)")
    plt.ylabel("MMR")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.savefig('MMR_dist_comparing_modes.png')


plot_mmrs()


def plot_winrate():
    plt.figure().clear()

    ndata = dict()
    for region in data:
        for mode in data[region]:
            if mode == 'Archon':
                continue
            if mode in ndata:
                ndata[mode] += data[region][mode]
            else:
                ndata[mode] = data[region][mode].copy()

    for mode in ndata:
        ndata[mode] = sorted(ndata[mode])

    M = max((len(ndata[key]) for key in ndata))
    offset_percent = 0.2

    # Plot modes
    for mode, ldata in ndata.items():
        winrates = []
        positions = []
        for idx, player in enumerate(ldata):
            if idx / len(ldata) < offset_percent:
                continue
            lower_position = int(idx - len(ldata) * offset_percent)
            winrate = cwinrate(player - ldata[lower_position])
            winrates.append(winrate)
            positions.append(M * idx / len(ldata))

        plt.plot(positions, winrates, label=mode)

    # Chess
    xchess, ychess = get_chess_data_smoothed()
    chess_max_players = max(xchess)
    xchess = [i * M / chess_max_players for i in xchess]
    winrates = []
    positions = []
    for idx, player in enumerate(ychess):
        if idx / len(ychess) < offset_percent:
            continue
        lower_position = int(idx - len(ychess) * offset_percent)
        winrate = cwinrate(player - ychess[lower_position], coef=1)
        winrates.append(winrate)
        positions.append(M * idx / len(ychess))

    plt.plot(positions, winrates, label='Fast chess')

    plt.plot([M * offset_percent, M], [1, 1],
             label='Fully determined game',
             linestyle='dashed')
    plt.plot([M * offset_percent, M], [0.5, 0.5],
             label='Fully random game',
             linestyle='dashed')

    # Change xticks to percents
    percents = []
    percents_loc = []
    for percent in range(int(offset_percent * 100), 101, 10):
        percents.append(f"{percent}%")
        percents_loc.append(int(M * percent / 100))

    plt.xticks(percents_loc, percents)
    plt.yticks([i / 10 for i in range(5, 11)],
               [f"{i*10}%" for i in range(5, 11)])

    plt.title(
        f"Winrate against someone {offset_percent:.0%} lower in population")
    plt.xlabel("Players")
    plt.ylabel(f"Winrate")
    plt.grid(alpha=0.2)
    plt.legend(fontsize=8)
    plt.savefig("Winrate.png")


plot_winrate()