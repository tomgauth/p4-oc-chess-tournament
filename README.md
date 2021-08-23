# Openclassrooms Project 4
# Manage a Chess Tournament

This app is created to manage Swiss style chess tournaments with 8 players (by default)

The project was designed for the specific needs of the project 2 on Openclassrooms' track "Python App Developper"

## Installation

Download the repository on your computer.

Make sure that you're using the right requirements by running the following command:

```bash
pip install -r requirements.txt
```

## Launch the app

```bash
python main.py
```

## Navigation

Use number inputs to select what you want to do in a given menu.

For example:
```
MAIN MENU
=========

Select an option:
1. Tournaments
2. Players
3. Reports
4. Quit
=>
```
enter '1' + presse enter to select Tournaments

## Creating a tournament

First, you will be prompted with the information to give for the tournament
Then you will be prompted with the information to give for the 8 players.
Once all the players are added, the tournament and players are saved and you
will be redirected to the tournament menu.

## Run a tournament

In the tournament menu, after creating the tournament and adding the players,
select "Start a tournament"
The first round will be generated following the algorithm.
You will be prompted to type "start" to start each round
Once each match of the round is over, type "end" to finish the round
You will send see the list of matches with the outcome printed on the screen.
Enter "start" to start the next round, repeat the cycle until all the rounds are
over.
Once all the rounds are over, you will see the ranking of the tournament's
players, sorted by score.

## Generate a report

You can generate the following reports in the "reports menu":

```
1. Show all players (alphabetically)
2. Show all players (by ranking)
3. Show all players of a tournament (alphabetically)
4. Show all players of a tournament (by ranking)
5. Show all tournaments
6. Show all rounds of a tournament
7. Show all matches of a tournament
```

## Generate a flake8 report

In order to generate a flake8 report, use the following command:

```
$ flake8 .

```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Name: Tom Gauthier
Github: https://github.com/tomgauth
