import random

import numpy as np
import pandas as pd


class GameManager:
    """
    This is the GameManager class which will act as the environment for the
    assignment.

    Some features:
        There are 2 folders: stats, moves. These contain some common pokemon
            data and moves data. You can refer to these or even add to them if
            you want to. (do note down all changes you make and mention them
            in the answer doc)
        There is the type chart. The type chart is a damage multiplier chat.
        There is a separate file to hold the Opponent class but it isn't nec
    """

    def __init__(self, stats=None, moves=None, poke_per_team=3):
        # Get the database of all pokemon (their names, types,
        # hps and available moves)
        self.stats = (
            pd.read_csv("data/stats.csv")
            if stats is None
            else pd.read_csv("{}".format(stats))
        )
        # Get the database of moves
        self.moves_dict = (
            pd.read_csv("data/moves.csv")
            if moves is None
            else pd.read_csv("{}".format(moves))
        )

        self.moves = self.moves_dict.copy()
        # Row corresponds to attacker, column corresponds to defender
        # Read up on how this works if you're interested
        self.type_chart = np.array(
            [
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 0.5, 0.5, 1.0, 2.0, 2.0],
                [1.0, 2.0, 0.5, 1.0, 0.5, 1.0],
                [1.0, 1.0, 2.0, 0.5, 0.5, 1.0],
                [1.0, 0.5, 2.0, 1.0, 0.5, 1.0],
                [1.0, 0.5, 0.5, 1.0, 2.0, 0.5],
            ]
        )
        # Define some common lists for printing and debugging purposes
        self.types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice"]
        self.poke_list = list(self.stats["pokemon"])
        self.moves_list = list(self.moves["move"])

        # Replace the columns with numbers
        self.moves["move"] = range(len(self.moves))
        self.moves["type"] = pd.Series(
            [self.types.index(i) for i in self.moves["type"]]
        )
        self.moves = self.moves.to_numpy()

        # Replace string pokemon names with their respective numerical indices
        self.stats["pokemon"] = self.stats.index
        self.stats["type"] = pd.Series(
            [self.types.index(i) for i in self.stats["type"]]
        )
        for i in range(4):
            key = "move" + str(i + 1)
            self.stats[key] = pd.Series(
                [self.moves_list.index(j) for j in self.stats[key]]
            )

        # Number of pokemon per team
        self.poke_per_team = poke_per_team

        # Initialise both teams
        self.team = self._init_team()
        self.opp_team = self._init_team()

        # Initialise the starting pokemon of each team
        self.index = random.randint(0, self.poke_per_team - 1)
        self.opp_index = random.randint(0, self.poke_per_team - 1)

        # True if it's the player's turn, False if it's the opponent's turn
        # By default, the player plays first with 50% probability
        self.turn = True if np.random.uniform() < 0.5 else False

    @property
    def action_space(self):
        """
        Defines the action space of the game. It will be the indices of all the
        values in num of moves + 2 extra actions to allow switching of pokemon
        """
        return tuple(range(6))

    def _init_team(self):
        """
        Helper function to initialise the teams
        """
        indices = random.sample(range(len(self.stats)), self.poke_per_team)
        team = np.array([self.stats.iloc[index] for index in indices]).astype(int)
        return team

    def reset(self):
        """
        Performs env.reset() like in Gym Environments
        """
        self.index = random.randint(0, self.poke_per_team - 1)
        self.opp_index = random.randint(0, self.poke_per_team - 1)
        self.turn = True if np.random.uniform() < 0.5 else False

        self.team, self.opp_team = self._init_team(), self._init_team()

        # It's upto you what you define the state space to be.
        # This is an example (not a very good one)
        state = np.array([self.team, self.opp_team])
        return state

    def validate_hp(self, player=True):
        """
        Validates the HP. You can add other validation checks here.

        Args:
            player (bool): True if the Player's HP needs to be checked
        """
        if player:
            hp = self.team[self.index][2]
        else:
            hp = self.opp_team[self.opp_index][2]
        return hp > 0

    def opp_step(self):
        """
        Performs env.step() like in Gym Environments for the Opponent AI
        """
        # The Opponent AI here basically picks the move with the highest damage
        # It won't switch until it's out of HP
        actions = self.opp_team[self.opp_index][3:]
        damages = np.array([self.moves[i][2] for i in actions])
        action = np.argmax(damages)

        assert self.index in range(3) and self.opp_index in range(
            3
        ), "Index: {}, Opp Index: {}".format(self.index, self.opp_index)

        if action == len(self.moves):  # Switches to the pokemon to the right
            self.opp_index = (
                self.opp_index + 1 if self.opp_index < self.poke_per_team else 0
            )
            self.damage = 0
        elif action == len(self.moves) + 1:  # Switches to the pokemon to the left
            self.opp_index = (
                self.opp_index - 1 if self.opp_index > 0 else self.poke_per_team - 1
            )
            self.damage = 0
        else:
            # A proper move is performed and the damage inflicted
            # needs to be calculated
            _, move_type, power, _, acc = self.moves[action]
            type_factor = self.type_chart[self.opp_team[self.opp_index][1]][
                int(move_type)
            ]
            self.damage = power * acc * type_factor
            self.team[self.index][2] -= self.damage

        for _ in range(3):
            if self.validate_hp():
                break
            # By default, if the current Pokemon is out of HP, the pokemon
            # to the right is chosen
            self.index = self.index + 1 if self.index < self.poke_per_team - 1 else 0

    def step(self, action):
        """
        Performs env.step() like in Gym Environments for the Agent

        Args:
            action (np.ndarray): Action to be taken
                0, 1, 2, 3: Moves of the pokemon
                4: Switch to the pokemon on the left (if there's no pokemon on
                    the left, it'll switch to the pokemon on the extreme right)
                5: Switch to the pokemon on the right (opposite of the above
                    in the extreme case)
        """
        if not self.turn:
            self.opp_step()

        if action == 4:  # Switches to the pokemon to the right
            self.index = self.index + 1 if self.index < self.poke_per_team - 1 else 0
            self.damage = 0
            type_factor = 1
        elif action == 5:  # Switches to the pokemon to the left
            self.index = self.index - 1 if self.index > 0 else self.poke_per_team - 1
            self.damage = 0
            type_factor = 1
        else:
            # A proper move is performed and the damage inflicted
            # needs to be calculated
            move = self.team[self.index][3 + action]
            _, move_type, power, _, acc = self.moves[move]
            assert self.index in range(3) and self.opp_index in range(3)
            type_factor = self.type_chart[self.team[self.index][1]][int(move_type)]
            self.damage = power * acc * type_factor
            self.opp_team[self.opp_index][2] -= self.damage

        self.turn = not self.turn

        # The following is again just example code. All this can be modified.
        # Document all the changes you're making
        reward = self.damage / 100
        next_state = np.array([self.team, self.opp_team])

        # This defines the game over status. In this case, this is simply set
        # to True if the current pokemon's HP goes less than 0
        for _ in range(3):
            if self.validate_hp(False):
                done = False
                break
            self.opp_index = (
                self.opp_index + 1 if self.opp_index < self.poke_per_team - 1 else 0
            )
        else:
            done = True

        info = {}  # Can be used to store any additional variables for training

        return next_state, reward, done, info
