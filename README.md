# Probability Project

## Overview

This program calculates the experimental probability of rolling a six by simulating dice rolls. It investigates the Law of Large Numbers, which states that as the number of rolls increases, the experimental probability tends to approach the theoretical probability. 

## Features
- Prompts the user to specify the number of simulations to run. 
- Generates a random integer from 1 to 6 to simulate a die roll and counts the number of sixes rolled.
- Every 100th simulation is appended to lists that track experimental probability, roll count, and absolute error. 
- Plots the experimental probability against the theoretical probability of rolling a six.
- Visualizes how the absolute error changes as the number of rolls increases. 

## Mathematical Concepts
- Theoretical Probability: The theoretical probability of rolling a six is equal to 1/6. This is because a fair, six-sided die has six equally likely outcomes, only one of which is rolling a six. The theoretical probability can be found by dividing the number of favorable outcomes by the total number of possible outcomes. 
- Experimental Probability: The program calculates experimental probability by dividing the number of sixes rolled by the total number of rolls. 
- Absolute Error: Absolute error measures the absolute difference between the experimental probability and the theoretical probability. The program calculates this value by taking the absolute value of the difference between these two probabilities.

## Requirements
- Python 3
- Matplotlib

## How to Run
From the project directory, run the following commands in the terminal.

Install Matplotlib: 
```bash
python -m pip install matplotlib
```

Launch the simulator: 
```bash 
python main.py
```