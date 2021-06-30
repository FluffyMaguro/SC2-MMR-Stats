# SC2 MMR stats (seasons 47)

Playing around with various MMR stats provided by Nephest (https://www.nephest.com/sc2)

#

![Screenshot](./MMR_hist.png)

Distribution of MMR. League targets taken from liquidpedia (https://liquipedia.net/starcraft2/Battle.net_Leagues). Actual MMR ranges are quite close to those calculated and shown here.

Silver, Gold and Platinum leagues are nicely tugged together but still spanning ~1300 MMR, meaning there is still a big range of skill in these leagues.

![Screenshot](./MMR_dist_region_compare.png)

When comparing different regions, we can see that KR is more shifted towards higher MMRs. That's likely because of a lot more professional players and fewer total players. MMR will shift toward higher ranges to accommodate a different player distribution.

![Screenshot](./MMR_dist_1v1.png)

MMR distribution across leagues for 1v1. The biggest skill differences can be found in Bronze and Grandmaster leagues, followed up by the Master league.

![Screenshot](./MMR_dist_comparing_modes.png)

Comparing MMR distribution between different modes. Fast chess data were taken from here (https://www.chess.com/leaderboard/live/rapid), and rescaled `MMR = 2.2*ELO` (based on [this thread](https://www.reddit.com/r/starcraft/comments/6dn6jf/does_anybody_have_more_detailed_stats_on_mmr/)).

Both a game, mode, and population affect how this chart looks. For StarCraft II, we see that the biggest skill differences in 1v1, followed by 2v2, 3v3 and 4v4. As expected, in 1v1 a single player skill has the biggest impact on the game's outcome. With more players the impact gets progressively smaller, and in 4v4 it's the smallest.

Fast chess population spans essentially the same MMR range as 1v1 in StarCraf II, however, the population is much more equally distributed between different MMR/ELO brackets. We don't see the same Bronze league that contains only a small number of players but with a major difference is in skill. That's likely because the (fast) chess population is bigger than what data obtained from the single site shows, and fast chess highlights the skill difference between players even better than 1v1 in StarCraft II.

| Game mode  | MMR range 
:---: |  :---:
|1v1 | 32 – 7280 |
|2v2 | 1154 – 5301 |
|3v3 | 1571 – 4809 |
|4v4 | 1872 – 4494 |
| Fast chess | – 7260 |


I'm guessing team games in StarCraft II are missing data from low MMR replays, 1v1 mode does have those.

![Screenshot](./Winrate.png) 

An alternative visualization of the previous data but with winrates calculated based on the [difference in ELO](https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details). The winrate based on an MMR difference was calculated the same way as ELO, but with `ΔELO = ΔMMR/2.2` conversion.

This chart shows the previous trend even better. From the highest skill differences in player population to the lowest: Fast chess > 1v1 > 2v2 > 3v3 > 4v4.