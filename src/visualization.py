# src/visualization.py

"""
Epidemiological Model Visualization Module

This module provides functions for visualizing the results of an epidemiological simulation.

Author: Babak Mahdavi Ardestani
Date: 5 January 2023

Description:
- `generate_filename`: Function to generate filenames based on simulation model parameters.
- `plot_epi_dynamics`: Function to plot and save epidemiological dynamics.

Usage:
- Import this module and use the provided functions for visualization.

"""


import os
import numpy as np
import matplotlib.pyplot as plt
import argparse

def generate_filename(output_dir, args, prefix='f', extension='png'):
    """
    Generate a filename based on provided arguments.

    Parameters:
    - output_dir: Output directory for saving the file.
    - args: Namespace containing simulation parameters.
    - prefix: Prefix for the filename.
    - extension: File extension for the filename.

    Returns:
    - filepath: Full path to the generated filename.
    """
    # If args is not provided, use a simple default filename
    if args is None:
        count = 1
        base_filename = f"{prefix}_{count}.{extension}"
        filepath = os.path.join(output_dir, base_filename)

        while os.path.exists(filepath):
            count += 1
            base_filename = f"{prefix}_{count}.{extension}"
            filepath = os.path.join(output_dir, base_filename)

        return filepath

    # If args is provided, use the parameter values to generate a filename
    filename = f"{prefix}_N{args.N}_beta{args.beta}_sigma{args.sigma}_initial{args.init_infect}_dt{args.dt}_ts{args.sim_ts}.{extension}"
    filepath = os.path.join(output_dir, filename)

    # Add a numbering scheme if the file already exists
    count = 1
    while os.path.exists(filepath):
        filename = f"{prefix}_N{args.N}_beta{args.beta}_sigma{args.sigma}_initial{args.init_infect}_dt{args.dt}_ts{args.sim_ts}_{count}.{extension}"
        filepath = os.path.join(output_dir, filename)
        count += 1

    return filepath

def plot_epi_dynamics(epi_dynamics, dt, output_dir='output', args=None):
    """
    Plot and save the epidemiological dynamics.

    Parameters:
    - epi_dynamics: Simulation results array.
    - dt: Duration of each time step in simulation.
    - output_dir: Output directory for saving the plot.
    - args: Namespace containing simulation parameters.

    Returns:
    - None
    """
    time_points = np.arange(0, epi_dynamics.shape[1] * dt, dt)
    
    plt.plot(time_points, epi_dynamics[0], label='Susceptible')
    plt.plot(time_points, epi_dynamics[1], label='Infected')
    plt.plot(time_points, epi_dynamics[2], label='Recovered')
    
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Epidemiological Model')

    # Generate filename and save in the output directory
    filepath = generate_filename(output_dir, args)
    print(f"Visualization saved to: {filepath}")

    # Print parameter values
    print(f"Parameters: N={args.N}, beta={args.beta}, sigma={args.sigma}, initial_infected_individuals={args.init_infect}, dt={args.dt}, sim_ts={args.sim_ts}")

    plt.savefig(filepath)
    plt.show()
