# Tutorial for using PokeBattle

## GameManager:
- This is the environment for your RL problem
- All interaction between the agent and the opponent team goes through this
- It needs to be as Gym-like as possible
- A lot of different features can be added to this
- If in doubt, always add features here

## Agent:
- This is the agent class for your RL agent
- Should be able to interact with the `GameManager` and have a few standard functions as shown in `agent.py`
- Can be modified as much as you want
- Try to keep Agent as independent as possible from the environment (avoid using variables as `game.` as far as possible)

## Markov Decision Process:
- Figure out a way to formulate the problem as an MDP
- Must have the following components:
    - State Space
    - Action Space
    - Rewards Model
    - Transition/Dynamics Model

## Example code:

```python
from pokebattle import GameManager, Agent

game = GameManager()
player = Agent(game)

player.learn(num_epochs=20, episode_len=300)
```