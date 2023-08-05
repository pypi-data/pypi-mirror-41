import numpy as np

"""
    This class contains some MAB's algorithms.

    @author Alison Carrera

"""


class UCB1(object):
    def __init__(self, n_arms):
        """
            UCB1 constructor.

            n_arms: Number of arms which this instance need to perform.
        """
        self.number_of_selections = np.zeros(n_arms).astype(np.float)
        self.rewards = np.zeros(n_arms).astype(np.float)

    def select(self):
        """
            This method selects the best arm chosen by UCB1.

            return: Return selected arm number.
                    Arm number returned is (n_arm - 1).
        """

        arm_dont_usage = np.where(self.number_of_selections == 0)[0]
        if len(arm_dont_usage) > 0:
            self.number_of_selections[arm_dont_usage[0]] += 1
            return arm_dont_usage[0]

        average_reward = self.rewards / self.number_of_selections
        total_counts = np.sum(self.number_of_selections)

        ucb_values = self._factor_importance_each_arm(
            total_counts,
            self.number_of_selections,
            average_reward
            )
        chosen_arm = np.argmax(ucb_values)

        self.number_of_selections[chosen_arm] += 1

        return chosen_arm

    def _factor_importance_each_arm(self, counts, num_selections, avg_reward):
        """
            This method represents the core of the UCB1 algorithm.

            return: An array with the importance of all arms.
        """

        exploration_factor = np.sqrt(2 * np.log(counts) / num_selections)
        return avg_reward + exploration_factor

    def reward(self, chosen_arm):
        """
            This method gives a reward for a given arm.

            chosen_arm: Value returned from select().
        """
        self.rewards[chosen_arm] += 1


class UCBTuned(UCB1):
    def __init__(self, n_arms):
        """
            UCB1 constructor.

            n_arms: Number of arms which this instance need to perform.
        """
        super().__init__(n_arms)

    def _factor_importance_each_arm(self, counts, num_selections, avg_reward):
        """
            This method represents the core of the UCB-Tuned algorithm.

            return: An array with the importance of all arms.
        """
        variance = (np.sum(np.square(self.rewards - avg_reward)))
        variance_factor = (1/num_selections) * variance

        tuned = np.sqrt(2 * np.log(counts) / num_selections)
        tuned_factor = variance_factor + tuned

        explo = np.minimum(1/4, tuned_factor)
        exploration_factor = np.sqrt((np.log(counts) / num_selections) * explo)

        return avg_reward + exploration_factor


class ThompsomSampling:
    def __init__(self, n_arms):
        """
            Thompsom Sampling constructor.

            n_arms: Number of arms which this instance need to perform.
        """
        self.number_reward_0 = np.zeros(n_arms).astype(np.float)
        self.number_reward_1 = np.zeros(n_arms).astype(np.float)

    def select(self):
        """
            This method selects the best arm chosen by Thompsom Sampling.

            return: Return selected arm number.
                    Arm number returned is (n_arm - 1).
        """
        theta_value = np.random.beta(
            self.number_reward_1 + 1, self.number_reward_0 + 1
            )
        chosen_arm = np.argmax(theta_value)
        return chosen_arm

    def reward(self, chosen_arm):
        """
            This method gives a reward for a given arm.

            chosen_arm: Value returned from select().
        """
        self.number_reward_1[chosen_arm] += 1

    def penalty(self, chosen_arm):
        """
            This method gives a penalty for a given arm.
            It should be used in a onDestroy() event from a banner,
            for example.
            The arm was selected, showed to the user, but no interation
            was realized until the end of the arm cycle.

            chosen_arm: Value returned from select().
        """
        self.number_reward_0[chosen_arm] += 1
