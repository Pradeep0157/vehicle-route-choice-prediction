# Vehicle Route Choice Prediction using Bisection Method

This Python program predicts vehicle route choices for a given road network based on a user-defined demand and path parameters using the BPR (Bureau of Public Roads) function. The program calculates the equilibrium flow on two paths, ensuring the travel times on both paths are equal and minimized.

## Features
- Uses the Bisection method to find equilibrium flows (`x1` and `x2`) where the travel times on both paths are equal.
- Evaluates edge cases when bisection method doesn't converge.
  
## Mathematical Model
The travel time `ti(xi)` on path `i` is calculated using the BPR function:

$$
t_i(x_i) = f_i \left( 1 + \alpha_i \left( \frac{x_i}{C_i} \right)^{\beta_i} \right)
$$

Where:
- `fi` = Free-flow travel time for path `i` (min)
- `Ci` = Practical capacity of path `i` (vehicles per hour)
- `αi` and `βi` = Calibration parameters

### Assumptions
- The total demand (`d`) is divided between two paths, `x1` on path 1 and `x2` on path 2, such that `x1 + x2 = d`.
- Flows `x1` and `x2` are non-negative.

## Input Parameters
The user is prompted to input the following parameters within the specified ranges:

- **Total demand** (`d`) : [1000, 4000] vehicles per hour
- **Free-flow travel time** (`f1`, `f2`) : [1, 10] minutes
- **Sensitivity factor** (`α1`, `α2`) : [0.1, 1]
- **Capacity** (`C1`, `C2`) : [500, 2500] vehicles per hour
- **Flow exponent** (`β1`, `β2`) : [1, 4]

## Output
The program calculates and outputs the following under equilibrium condition:
- Flow on path 1 (`x1`) and path 2 (`x2`) in vehicles per hour.
- Travel time on path 1 (`t1`) and path 2 (`t2`) in minutes.

## Usage

1. **Run the program**:
   - The program will prompt you to input the values for the required parameters.
2. **Input the values**: Enter the values within the specified ranges as prompted.
3. **Output**: The program will display the calculated flows, travel times, and equilibrium conditions.

