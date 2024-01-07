# tests/test_simulation.py

"""
Unit tests for the epidemiological simulation functions.

These tests cover various scenarios and parameters to ensure the correctness
of the simulate_epidemiological_dynamics function.

Author: Babak Mahdavi Ardestani
Date: 6 January 2024
"""

import unittest
import numpy as np
from src.simulation import simulate_epidemiological_dynamics

class TestSimulationFunctions(unittest.TestCase):

    # Set a fixed seed for NumPy random number generation for reproducibility
    # If rs is not set, it may be posible that an assertion will rarely not pass
    #np.random.seed(9)

    def test_simulation_with_initial_infections(self):
        """
        Test simulation with a nonzero initial number of infected individuals.

        Steps:
        1. Run the simulation with specified parameters.
        2. Check that the initial number of infected individuals is correct.
        3. Check that there are no infected individuals at the end of the simulation.

        Note: The 'result' array has the following structure:
              result[0, :] -> Susceptible individuals over time
              result[1, :] -> Infected individuals over time
              result[2, :] -> Recovered individuals over time

        The '-1' index refers to the last time step in the simulation.

        Returns:
        - None
        """
        # Run simulation
        result = simulate_epidemiological_dynamics(
            N=1000,                     # Total population size
            beta=10,                    # Infection rate
            sigma=1,                    # Recovery rate
            initial_infected=10,        # Initial number of infected individuals
            dt=0.01,                    # Duration of each time step in the simulation
            sim_ts=1500                 # Total number of simulation time steps
        )

        # Assertions
        self.assertLessEqual(result[1, 0], 15)  # Check initial infected individuals (which would be beetwen 10 to 14)
        self.assertEqual(result[1, -1], 0)  # Check no infected individuals at the end

    def test_fast_and_slow_spreading_epidemics(self):
        """
        Test fast-spreading and slow-spreading epidemics with different infection rates.

        Steps:
        1. Run the simulation with specified parameters for fast-spreading epidemic.
        2. Check that some individuals are infected at the end of the fast-spreading epidemic.
        3. Run the simulation with specified parameters for slow-spreading epidemic.
        4. Check that some infected individuals are present at the end of the slow-spreading epidemic.
        5. Check that the number of infected individuals is relatively low at the end of the slow-spreading epidemic.

        Note: The 'result_fast' and 'result_slow' arrays have the same structure as described in the previous note.

        Returns:
        - None
        """
        # Run simulation for fast-spreading epidemic
        result_fast = simulate_epidemiological_dynamics(
            N=1000,                   # Total population size
            beta=0.2,                 # Infection rate (fast) <<< (high relative to slow)
            sigma=0.05,               # Recovery rate
            initial_infected=10,      # Initial number of infected individuals
            dt=0.1,                   # Duration of each time step in the simulation
            sim_ts=50                 # Total number of simulation time steps
        )

        """
        The rate of infection is high (fast sparding), & the expectation is that the epidemic spreads 
        quickly, leading to a significant number of infections after relatively a short time
        """
        # Assertions for fast-spreading epidemic
        self.assertGreater(result_fast[1, -1], 10)  # Check some individuals are still infected at the end (fast)

        # Run simulation for slow-spreading epidemic
        result_slow = simulate_epidemiological_dynamics(
            N=1000,                   # Total population size
            beta=0.02,                # Infection rate (slow) <<< (low relative to fast-spearding)
            sigma=0.05,               # Recovery rate
            initial_infected=10,      # Initial number of infected individuals
            dt=0.1,                   # Duration of each time step in the simulation
            sim_ts=50                 # Total number of simulation time steps
        )
        
        """
        Due to the slower rate of infection, the total number of infections 
        should be limited after the same nuber of simulation period.
        """
        # Assertions for slow-spreading epidemic
        self.assertGreater(result_slow[1, -1], 0)  # Check some infected individuals are present at the end
        self.assertLess(result_slow[1, -1], 13)  # Check the number of infected individuals is relatively low (slow)

if __name__ == '__main__':
    unittest.main()
