# Assignment: (#1): 
# Author(s): Sayed Abdul Ahad Ibrahimi
# Due Date: (09/26/2021)
#
# Description: The goal of this project is about input, functions, computation and formated  output.
#              We are asked the user to enter their name and yearly income as an input and then multiply by a random percentage using random module to determine the tax value. 
#              We are then asked to compute the given tax value in a way that the user can pay their tax using the minimal number of coins needed. 
# Comments: (I experimented with local define functions but instead I did all my computation under main functions.)
# 
# Honor Pledge: I have abided by the Wheaton Honor Code and 
# all work below was performed by (Ahad Ibrahimi).

import random

# The Inputs
name = input("""Hello, welcome to the Republic of Bananaria.
Please enter your name to start. """)

print("Thank you, {0}.".format (name))
yearly_income = float(input("""Please enter your yearly income in a valid 
floating-point number with two decimals:""")) * 100   # Switching to integer right from the beginning!

def main():
        
        tax_percent = random.random()  # Random decimal between 0 and 1
        tax = tax_percent * yearly_income
        
        # Using integers for operations rather than float
        remain_1024 = tax % 1024
        remain_256 = remain_1024 % 256
        remain_64 = remain_256 % 64
        remain_16 = remain_64 % 16
        remain_4 = remain_16 % 4
        remain_1 = remain_4 % 1
        
        print("-"*45)
        
        print(f"{'Coin':>5}{'Number':>18}{'Value':>21}")
        
        # num_1024 to num_1 are the number of 1024¢ to 1¢ coins.
        # val_1024 to val_1 are the value of the coin (1024¢ to 1¢) when multiplied by number of that particular coin.
        # formatted output in the form of coin, number of coins and the value.
        
        num_1024 = tax // 1024 
        val_1024 = num_1024 * 10.24
        print(f"{'1024¢'}{num_1024:>18.0f}{val_1024:>21.2f}")
              
        
        num_256 = remain_1024 // 256
        val_256 = num_256 * 2.56
        print(f"{'256¢':>5}{num_256:>18.0f}{val_256:>21.2f}")           
        
        num_64 = remain_256 // 64
        val_64 = num_64 * 0.64
        print(f"{'64¢':>5}{num_64:>18.0f}{val_64:>21.2f}")
        
        num_16 = remain_64 // 16
        val_16 = num_16 * 0.16
        print(f"{'16¢':>5}{num_16:>18.0f}{val_16:>21.2f}")
        
        num_4 = remain_16 // 4
        val_4 = num_4 * 0.04
        print(f"{'4¢':>5}{num_4:>18.0f}{val_4:>21.2f}")              
        
        num_1 = remain_4 // 1
        val_1 = num_1 * 0.01
        print(f"{'1¢':>5}{num_1:>18.0f}{val_1:>21.2f}")
        
        print("-"*45)
        
        # the computation and output of the total number of coins and the sum of the value 
        total_num = num_1024 + num_256 + num_64 + num_16 + num_4 + num_1
        sum_val = (val_1024 + val_256 + val_64 + val_16 + val_4 + val_1)
        
        print(f"{'Totals:'}{total_num:>16.0f}{sum_val:>21.2f}")

        print(f"\nCongratulations, {name}, you need to pay ${sum_val:.2f} tax with {total_num:.0f} coins.")


if __name__ == "__main__":
        main()
