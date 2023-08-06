[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Build Status](https://travis-ci.org/bsamseth/python-chess-engine-tester.svg?branch=master)](https://travis-ci.org/bsamseth/python-chess-engine-tester)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/bsamseth/python-chess-engine-tester.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bsamseth/python-chess-engine-tester/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/bsamseth/python-chess-engine-tester.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bsamseth/python-chess-engine-tester/alerts/)
[![Lines of Code](https://tokei.rs/b1/github/bsamseth/python-chess-engine-tester)](https://github.com/Aaronepower/tokei).
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/bsamseth/python-chess-engine-tester/blob/master/LICENSE)

# Chester - Chess Engine Tester

`chester` is a Python package that aims to provide a simple interface for running chess matches
between computer chess programs (referred to as engines). It makes it easy to
play 1v1 matches of any length, including running tournaments between a large
set of engines.

__Note__: This is not yet complete.

## Alternatives

The most mentioned alternative to this is
[cutechess](https://github.com/cutechess/cutechess). The downside of cutechess
is that it is less portable, and depends on the Qt framework. This has its
benefits, but also means a lot of dependencies. This project aims to be much
more portable, and just depending on a compatible version of Python. It does
_not_, however, have any intentions of becoming _feature complete_ and
supporting everything imaginable. Its aim is to provide a simple way to do a
simple task - testing chess engines against each other.

