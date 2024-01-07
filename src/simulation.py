# src/simulation.py

"""
Epidemiological Simulation Module

This module contains functions for running stochastic simulations of an epidemiological model.

Author: Babak Mahdavi Ardestani
Date: 5 January 2023

Functions:
- sim: Run a stochastic epidemiological simulation.
- simulate_epidemiological_dynamics: Wrapper function for simulation.

Usage:
- Import this module to access the simulation functions.

Example:
from simulation import simulate_epidemiological_dynamics

"""

import numpy as np


def sim(N, beta, sigma, initial_infected, dt, sim_ts):

    """
    Run a stochastic epidemiological simulation.

    Parameters:
    - N: Total population
    - beta: Infection rate per interaction
    - sigma: Recovery rate
    - initial_infected: Initial infected individuals
    - dt: Duration of each time step in simulation
    - sim_ts: Number of simulation time steps

    Returns:
    - epi_dynamics: Simulation results
    """

    #TODO, change variable names to more meaniful names: 
    S = N - initial_infected  # Susceptible = total population - intial infected individuals 
    I = initial_infected  # Infected = intial infected individuals 
    R = 0  # Recovered = 0 

    # array of 3 rows and sim_ts columns to keep the simulaiton results of 
    # Susceptible, Infected, and Recovered values at each simulation iteration 
    epi_dynamics = np.zeros((3, sim_ts))
    
    for t in range(sim_ts):
       
        # infection probability 
        infection_prob = 1 - np.exp(-beta * I / N * dt)

        # number of individuals who move from `S` to new `I` as a binomial draw with infection_prob 
        new_infections = np.random.binomial(S, infection_prob)


        # recovery probability 
        recovery_prob = 1 - np.exp(-sigma * dt)

        # number of recoveries movements from `I` to new `R` as a binomial draw with recovery_prob 
        new_recoveries = np.random.binomial(I, recovery_prob)
        
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries
        
        epi_dynamics[:, t] = [S, I, R]
    
    return epi_dynamics

def simulate_epidemiological_dynamics(N, beta, sigma, initial_infected, dt, sim_ts):
    """
    Wrapper function for simulation.

    Parameters:
    - N: Total population
    - beta: Infection rate per interaction
    - sigma: Recovery rate
    - initial_infected: Initial infected individuals
    - dt: Duration of each time step in simulation
    - sim_ts: Number of simulation time steps

    Returns:
    - epi_dynamics: Simulation results

    Potential future expansion (which may or may not affect sim function):
    - Introducing parallelization options
    - Adding additional simulation parameters for investigating various interventions (e.g. vaccination rates, social distancing, interaction networks, or spatial information)
    - Providing an option to choose different simulation models in addition to SIR (e.g. SEIR, SIRS, or more complex models)
    - Adding an optional deterministic differential equations implementation
    - Allowing users to choose the format of the output (e.g. pandas DataFrame)
    - ...
    """
    return sim(N, beta, sigma, initial_infected, dt, sim_ts)
