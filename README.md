# Mini SymPy-to-C Transpiler

A Python tool that converts SymPy mathematical expressions into valid C code using recusrsion.

## Features

**Arithmetic**: It handles Add, Mul and Pow (converted to pow()).

**Interactive**: Takes user input via CLI.

**Scalable**: Easy to extend for trig functions and constants.

## Installation

1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the script and enter the math expression when prompted.

```bash
python transpile.py
# Input: x**2 + x*y
# Output: pow(x, 2) + x * y