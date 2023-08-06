# `steamleaderboards`

A package designed to help developers access the leaderboards of various Steam games.

It was created with the Isaac Daily Run scoreboards in mind, but it can be used for other games as well.

## Usage

To use `steamleaderboards`, first create a `LeaderboardGroup` for the desired game.

```python
import steamleaderboards as sl
lbgroup = sl.LeaderboardGroup(STEAM_APP_ID)
```

Once you have created the `LeaderboardGroup`, you can retrieve the desired leaderboards by using the `LeaderboardGroup.get` method.  
You can specify the name, the display name or the id of the leaderboard to retrieve.

```python
leaderboard_a = lbgroup.get(name=LEADERBOARD_NAME)
leaderboard_b = lbgroup.get(lbid=LEADERBOARD_ID)
leaderboard_c = lbgroup.get(display_name=LEADERBOARD_DISPLAY_NAME)
```

When you have the `Leaderboard` object, you can find all the entries in the `Leaderboard.entries` field, or you can search for a specific one through the `Leaderboard.find_entry` method.

```python
all_scores = leaderboard_a.entries
my_score = leaderboard_a.find_entry(MY_STEAMID_1)
first_place_score = leaderboard_a.find_entry(rank=1)
last_place_score = leaderboard_a.find_entry(rank=-1)
```