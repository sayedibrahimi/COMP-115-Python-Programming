# Bananaria Tax Calculator

## Overview

This Python script simulates a tax calculation system for the fictional Republic of Bananaria. It calculates tax based on user input and determines the minimal number of coins needed to pay the tax.

## Features

- User input for name and yearly income
- Random tax rate generation
- Tax calculation
- Coin denomination breakdown (1024¢, 256¢, 64¢, 16¢, 4¢, 1¢)
- Formatted output of coin counts and values

## Requirements

- Python 3.x
- `random` module (included in standard Python library)

## Usage

1. Run the script:
   ```
   python bananaria_tax_calculator.py
   ```
2. Enter your name when prompted.
3. Enter your yearly income as a floating-point number with two decimal places.
4. The program will calculate your tax and display the breakdown of coins needed to pay it.

## Input

- Name (string)
- Yearly income (float)

## Output

- Formatted table showing the number and value of each coin denomination needed
- Total number of coins and total tax amount
- Personalized message with the tax amount and total coin count

## Code Structure

- The script uses a `main()` function to encapsulate the core logic.
- Income is converted to cents (integer) to avoid floating-point arithmetic issues.
- Random tax rate is generated using `random.random()`.
- Coin calculations use integer division and modulo operations.

## Author

Sayed Abdul Ahad Ibrahimi

## Date

September 26, 2021

## Course

This project was created as an assignment for a programming course.
