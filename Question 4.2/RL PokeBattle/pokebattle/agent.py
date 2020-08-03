import numpy as np


class Agent:
    """
    The Agent Class you will have to develop. Can use any RL algorithm you want.
    Clearly specify what you are using and the hyperparameters you are choosing
    in the answer doc itself.

    Model-free algorithms are preferred. Planning agents are not.
    """

    def __init__(self, game):
        self.game = game
        self.team = game.team
        self.opponent = game.opp_team

        # The array of all the agents moves
        self.moves = np.array(
            [
                [self.game.moves[self.team[i][j + 3]] for j in range(4)]
                for i in range(len(self.team))
            ]
        )

        # The index of the current pokemon is maintained by the GameManager
        self.current_pokemon = self.team[self.game.index]

    def make_model(self):
        """
        Use this to make the model of the Agent.
        It can be a Neural Network or a Table or a Decission tree etc
        (Neural Network is suggested due to high complexity of state space)

        Some factors to decide what to use:
        State Space
        Action Space
        """
        raise NotImplementedError

    def select_action(self, state):
        """
        Use this to select what action your agent can pick. Action Space from
        the environment/GameManager's perspective is the actual move you're
        going to make.

        How your agent decides what action to pick comes here.
        """
        # Example code, replace this with your logic:
        # Returns move which inflicts maximum damage
        action = self.moves[self.game.index].T[1].argmax()
        return action

    def update(self):
        """
        Use this to update your model (whether it be a table, policy,
        actor-critic network, Q-value etc)
        """
        pass

    def learn(self, num_epochs=10, episode_len=10):
        """
        This function can be used for the actual training loops. You can keep
        it here or have an external class for training loops.

        Args:
            num_epochs (int): Number of epochs to train the agent for
            episode_len (int): Number of timesteps (not including
                opponent timesteps) per pokebattle
        """
        # Example code given below

        for epoch in range(num_epochs):
            state = self.game.reset()
            episode_reward = 0

            for timestep in range(episode_len):
                action = self.select_action(state)
                next_state, reward, done, info = self.game.step(action)

                episode_reward += reward

                self.update()
                if done:
                    break

                state = next_state

            print("Episode: {}, Rewards: {}".format(epoch, episode_reward))
