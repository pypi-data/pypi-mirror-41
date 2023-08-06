[![PyPI version](https://badge.fury.io/py/chester.svg)](https://badge.fury.io/py/chester)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Build Status](https://travis-ci.org/bsamseth/python-chess-engine-tester.svg?branch=master)](https://travis-ci.org/bsamseth/python-chess-engine-tester)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/bsamseth/python-chess-engine-tester.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bsamseth/python-chess-engine-tester/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/bsamseth/python-chess-engine-tester.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bsamseth/python-chess-engine-tester/alerts/)
[![Lines of Code](https://tokei.rs/b1/github/bsamseth/python-chess-engine-tester)](https://github.com/Aaronepower/tokei)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/bsamseth/python-chess-engine-tester/blob/master/LICENSE)

# Chester - Chess Engine Tester

`chester` is a Python package that aims to provide a simple interface for running chess matches
between computer chess programs (referred to as engines). It makes it easy to
play 1v1 matches of any length, including running tournaments between a large
set of engines.

__Note__: This is not yet complete.

## Example Usage

The following example shows how to run a 2-player tournament between
[Stockfish](https://github.com/official-stockfish/Stockfish) and
[Goldfish](https://github.com/bsamseth/Goldfish). All players must be UCI compatible
chess engines.

```python
from chester.timecontrol import TimeControl
from chester.tournament import play_tournament

players = ["stockfish", "goldfish"]  # Each string is the name/path to an executable UCI engine.
time_control = TimeControl(initial_time=2, increment=0)  # 2 seconds on the clock, 0 seconds increment.
n_games = 2

for pgn in play_tournament(players, time_control, n_games=n_games):
    print(pgn, '\n')  # Print out the PGN for each game as they finish.
```

Which could output something like this:

``` text
[Event "?"]
[Site "?"]
[Date "2019-02-06"]
[Round "1"]
[White "Stockfish 10 64 POPCNT"]
[Black "Goldfish v1.8.1"]
[Result "1-0"]

1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Be2 Qg5 5. Nf3 Qxg2 6. Rg1 Qh3 7. d4 Bf5 8. Rg3 Qh5 9. Rg5 Qh3 10. Nd5 Kd8 11. Nf4 Bxc2 12. Qxc2 Qc8 13. Ne5 Nh6 14. Bc4 Nc6 15. Nxf7+ Nxf7 16. Bxf7 Nb4 17. Qe4 c6 18. Ne6+ Kd7 19. d5 h6 20. Bf4 hxg5 21. dxc6+ Qxc6 22. Rd1+ Nd5 23. Rxd5+ Kc8 24. Rd8# 1-0

[Event "?"]
[Site "?"]
[Date "2019-02-06"]
[Round "1"]
[White "Goldfish v1.8.1"]
[Black "Stockfish 10 64 POPCNT"]
[Result "0-1"]

1. e3 e5 2. Nc3 d5 3. Nf3 e4 4. Nd4 Nf6 5. Bb5+ c6 6. Be2 Bd6 7. a4 O-O 8. g3 Bh3 9. b3 c5 10. Ndb5 Be7 11. g4 a6 12. Na3 d4 13. exd4 cxd4 14. Na2 d3 15. cxd3 exd3 16. Bf3 Bxa3 17. Be4 Re8 18. f3 Nxe4 19. Rg1 Nc3+ 20. Kf2 Qh4+ 21. Rg3 Bc5# 0-1

[Event "?"]
[Site "?"]
[Date "2019-02-06"]
[Round "2"]
[White "Stockfish 10 64 POPCNT"]
[Black "Goldfish v1.8.1"]
[Result "1-0"]

1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Be2 Qg5 5. Bf3 Nc6 6. d4 Qf6 7. Nb5 Kd8 8. Ne2 Bf5 9. Bf4 Rc8 10. O-O a6 11. Nbc3 Qg6 12. Rc1 Nf6 13. d5 Nb4 14. Nd4 a5 15. a3 Na6 16. Ncb5 Bg4 17. Re1 Nxd5 18. Bxg4 Qxg4 19. Qxg4 e6 20. Nxe6+ fxe6 21. Bg5+ Be7 22. Qxe6 Ra8 23. Bxe7+ Ke8 24. Qxd5 c5 25. Bxc5# 1-0

[Event "?"]
[Site "?"]
[Date "2019-02-06"]
[Round "2"]
[White "Goldfish v1.8.1"]
[Black "Stockfish 10 64 POPCNT"]
[Result "0-1"]

1. e3 e5 2. Nc3 d5 3. Nf3 e4 4. Nd4 Nf6 5. Bb5+ c6 6. Be2 Bd6 7. a4 O-O 8. g3 Bh3 9. b3 c5 10. Ndb5 Be7 11. g4 a6 12. Na3 h6 13. Bb2 d4 14. exd4 cxd4 15. Na2 Nc6 16. Nc4 b5 17. axb5 axb5 18. g5 Nd5 19. gxh6 Bh4 20. Bg4 Qf6 21. Bxd4 Nxd4 22. h7+ Kxh7 23. Bf5+ Qxf5 24. Qb1 Qf3 25. Rf1 Qe2# 0-1
```

The result is `4` games are played. This is because the tournament will run
`n_games * len(list(permutations(players, 2)))!` games, i.e. each player plays
every other player both as white and as black, and all of this is repeated `n_games`
times.


## Alternatives

The most mentioned alternative to this is
[cutechess](https://github.com/cutechess/cutechess). The downside of cutechess
is that it is less portable, and depends on the Qt framework. This has its
benefits, but also means a lot of dependencies. This project aims to be much
more portable, and just depending on a compatible version of Python. It does
_not_, however, have any intentions of becoming _feature complete_ and
supporting everything imaginable. Its aim is to provide a simple way to do a
simple task - testing chess engines against each other.

