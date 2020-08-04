# PokeBattle

## Problem Statement:
It is the year 2018, Ash Ketchum has still not won any Pokemon League yet and he’s treated with clinical depression. He realises he can’t be good enough to win by himself. He approaches Professor Oak for advice. You’re a good friend of Oak and he knows that you’re interested in Reinforcement Learning. Since Ash lacks talent and you don’t exist in the Pokemon world, he realises you both can help each other.
Your job is to design an RL agent which can learn how to play a Pokemon Battle and help Ash Ketchum win his first trophy! 
 
## Introduction:
- Enter the `pokebattle` folder for the code
	- `manager.py`: has a `GameManager` class which is responsible for **all** interactions between the agent(s) and the opponent.
	- `pokemon.py`: has a `Pokemon` class which describes the behaviour of a single pokemon. It's there for managing other stuff. At this point, we can manage without it but would be needed if we wanted to add more complexity. (in terms of more stats, status effects etc)
	- `agent.py`: has an `Agent` class which will need to be modified for the assignment. Some prenamed functions are given so that they have some context. I was thinking of drawing a table which specifies some major parts of the algorithm and which class they should ideally appear in. (have it in a notebook rn)
	- `opponent.py`: has the `Opponent` class which will have some rule-based/random AI. This can be replaced by another `Agent` or combined with the in some other way. For small use cases, can be done without. By default, it's entirely taken care of by the `GameManager`. If this is being used, replace `opp_step` in `GameManager` with its behaviour.
- Enter the `data` folder for some csv files
	- `stats.csv`, `moves.csv`: databases for the overall pokemon stats and all the moves respectively. Can be expanded further. Go through issues

## Where to start?
- Understand how Pokemon battles work. 
- Understand moves.csv, stats.csv (correct them with the correct info where required)
- Decide what state space and action space should be
- Add methods to complete the env. Classes can be modded freely as long as they retain Gym-like nomenclature (otherwise it'll be hard to keep track of all the different kinds of code)
- Design Opponent AI (needs to be at least random, not the same action every time)
- Reach out and contact mentors for clarifications.

## What to do?
- Go through the assignment PDF for the full questions
- Go through `Tutorial.md` and `Pointers.md`
- Implement an Agent which will finally be able to win every Pokemon Battle and help Ash to cheat his way to the trophy!

## Additional Pointers:
- Keep checking for updates on this repo, changes may be done
- As far as possible, for ease of reference and uniformity, stick to Gym standards for the `GameManager` class.
- Present your code as neatly as possible with docstrings and comments wherever possible.
- Use black on your code and adhere to flake8 linting
- Document whatever changes you're making in a separate doc or in the assignment submission doc

## Most importantly, Have Fun!!
