# scripts/run_simulation.py

"""
Epidemiological Model Simulation Script

This script (containing the main function) allows users to run simulations of an epidemiological model and visualize the results.

Author: Babak Mahdavi Ardestani
Date: 3 January 2023
Contact: babak.m.ardestani@gmail.com

Description:
- Parses command-line arguments for simulation parameters.
- Calls the simulation and visualization functions from the src directory.
- Creates the output directory for visualization results.

Usage:
- Run this script from the command line to simulate and visualize epidemiological dynamics.

Example:
$ python3 run_simulation.py --N 40000 --beta 4 --sigma 1 --init_infect 10 --dt 0.01 --sim_ts 500 --output_dir output

"""

import argparse
import sys
import os
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.simulation import simulate_epidemiological_dynamics
from src.visualization import plot_epi_dynamics

def parse_arguments():
    """
    Parse command-line arguments for simulation parameters.

    Returns:
    - args: Namespace containing parsed arguments.
    """
    # Argument parser setup
    parser = argparse.ArgumentParser(description='Epidemiological Model')
    parser.add_argument('--N', type=int, default=1000, help='Total population')
    parser.add_argument('--beta', type=float, default=10, help='Infection rate per interaction')
    parser.add_argument('--sigma', type=float, default=1, help='Recovery rate')
    parser.add_argument('--init_infect', type=int, default=10, help='Initial infected individuals')
    parser.add_argument('--dt', type=float, default=0.01, help='Duration of each time step in simulation')
    parser.add_argument('--sim_ts', type=int, default=500, help='Number of simulation time steps')
    parser.add_argument('--output_dir', type=str, default='output', help='Output directory for visualization')

    return parser.parse_args()

def main():
    """
    Main function to run the epidemiological simulation and visualize the results.
    """
    args = parse_arguments()

    # Ensure the output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Run the epidemiological simulation
    epi_dynamics = simulate_epidemiological_dynamics(args.N, args.beta, args.sigma, args.init_infect, args.dt, args.sim_ts)
    
    # Visualize the results
    plot_epi_dynamics(epi_dynamics, args.dt, output_dir=args.output_dir, args=args)

if __name__ == '__main__':
    main()
