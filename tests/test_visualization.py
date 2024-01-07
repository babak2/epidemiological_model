# tests/test_visualization.py

"""
Unit tests for the visualization module.

Author: Babak Mahdavi Ardestani
Date: 6 January 2024

Description:
- This file contains unit tests for the visualization module.

Usage:
- Run this file to execute the unit tests.

Note:
- Ensure that the visualization module is working as expected.
"""

import unittest
import argparse
import numpy as np
import os
from src.visualization import plot_epi_dynamics
from src.visualization import generate_filename

class TestVisualizationFunctions(unittest.TestCase):

    def create_mock_args(self):
        """
        Create mock arguments for testing purposes.

        Returns:
        - argparse.Namespace: Mock arguments.
        """

        # Mock arguments for testing
        return argparse.Namespace(N=1000, beta=0.5, sigma=0.5, init_infect=10, dt=0.1, sim_ts=100, output_dir='test_output')

    def test_visualization_in_run_simulation(self):
        """
        Test the visualization function in the context of a simulated run of the epidemiological simulation.

        Steps:
        1. Set up mock arguments.
        2. Create a simulated epi_dynamics array.
        3. Ensure the output directory exists.
        4. Call the plot_epi_dynamics function.
        5. Check if the visualization file has been created.

        Returns:
        - None
        """
        # Set up mock arguments
        mock_args = self.create_mock_args()

        # Set up a simulated epi_dynamics array
        simulated_epi_dynamics = np.array(
            [[1000, 900, 800, 700],   # Susceptible individuals at different time points
            [50, 40, 30, 20],         # Infected individuals at different time points
            [20, 30, 40, 50]]         # Recovered individuals at different time points
        )

        """    
        At the initial time point:
            1000 individuals are susceptible,
            50 individuals are infected,
            20 individuals have recovered.

        At the second time point:
            900 individuals are susceptible,
            40 individuals are infected,
            30 individuals have recovered.

        ...and so on.
        """

        # Making sure the output directory exists
        os.makedirs(mock_args.output_dir, exist_ok=True)

        # Generates the expected filename based on the mock arguments
        expected_filename = generate_filename(mock_args.output_dir, mock_args)

        print("The expected_filename : ", expected_filename, "\n")

        # Call the plot_epi_dynamics function
        plot_epi_dynamics(simulated_epi_dynamics, dt=mock_args.dt, output_dir=mock_args.output_dir, args=mock_args)

        # Check if the visualization file has been created with the expected filename
        self.assertTrue(os.path.exists(expected_filename), f"Visualization file '{expected_filename}' should exist")


if __name__ == '__main__':

    unittest.main()
