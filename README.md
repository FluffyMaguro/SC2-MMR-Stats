# SC2 MMR stats (seasons 47)

Playing around with various MMR stats provided by Nephest (https://www.nephest.com/sc2)

# Results

Distribution of MMR. League targets taken here (https://liquipedia.net/starcraft2/Battle.net_Leagues), though actual MMR ranges are quite close.


![Screenshot](./MMR_hist.png)

# 
When comparing different regions, we can see that KR is more shifted towards higher MMR. That's likely because of a lot more professional players, and fewer total players. MMR will shift toward higher ranges to accomodate a different player distribution.

![Screenshot](./MMR_dist_region_compare.png)

# 
MMR distribution across leagues for 1v1. The biggest skill differences can be found in Bronze and GM, followed up by the Master league.

![Screenshot](./MMR_dist_1v1.png)

#
Comparing MMR distribution between different modes. Chess data taken from here (https://www.chess.com/leaderboard/live/rapid), and adjusted `ELO = 2.2*MMR` (based on [this thread](https://www.reddit.com/r/starcraft/comments/6dn6jf/does_anybody_have_more_detailed_stats_on_mmr/)).

Both the type of game and the population affects how this charts looks. In this case we see that the biggest skill differences are visible in 1v1, followed by 2v2, 3v3 and 4v4. It's expected that in 1v1 a player will retain the most agency and the outcome will be the most affected by his skill. In 4v4 it will be the least.

The population seen in the chess data is even more diverse in terms of skill, and that's while being only a subset of actual chess players. This indicates fast chess is even more skill based than SC2, or that even the limited population is wider than that of SC2 ladder in terms of skill.


![Screenshot](./MMR_dist_comparing_modes.png)

#
An alternative visualization with winrates calculated based on the [difference in ELO](https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details). For MMR used the `ELO = 2.2*MMR` relation.

This shows even better the previous trends. Where there are big skill differences in player population: Fast chess > 1v1 > 2v2 > 3v3 > 4v4 (noisy, not enough games).

![Screenshot](./Winrate.png) 