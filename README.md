# COP4045 Assignment 1 -- Duncan McKinley

## 1. Great Lakes Depth Calculator
Pretty straightforward math problem. Took the volume of the Great Lakes and divided it by the area of the US. Had to look up the area of the contiguous US states (about 8 million km²). The depth comes out to 0.002822 km, which seems really small but makes sense given how huge the US is. Just a simple division of 22,810 km³ by 8,080,464 km² to get the average depth.

## 2. Voyager Distance Calculator
This one was trickier. Had to work with some big numbers and multiple unit conversions. Started with Voyager's position in 2009 and calculated how far it's traveled since then. Added error checking because negative days wouldn't make sense. The coolest part was calculating the communication time. I had to convert everything to meters and seconds for the speed of light calculation, then double it for the round trip. Its so crazy how far away it is.

## 3. Time Converter
Seconds to time conversion. Used integer division and modulo to break down the seconds into hours, minutes, and seconds. The trick was using // to get the hours (divide by 3600), then the leftover seconds get split into minutes (divide by 60), and whatever's left becomes the seconds. Added input validation to make sure the number is between 1 and 86400 (24 hours). Formatted the output to show both digital time (HH:MM:SS) and written format.

## 4. Current Date/Time
Simple but useful script using Python's datetime module. Just grabs the current time and formats it nicely using strftime with the pattern we want. The test case makes sure the format matches what we want (MM/DD/YYYY HH:MM:SS) by trying to parse it back into a date.

## 5. Chess Board Grain Calculator
This one was probably my favorite. Used 2^64 - 1 to get the total (looked up exponential growth formula). Also added the feature to calculate how deep the wheat would be if spread over an area. The numbers get big and you really need to use scientific notation to make any sense of it. I did some research about where this chess board example originated and found another example using pennies instead. I tested everyone in my office and they all said they wanted a million dollars over a single penny growing exponentially over 30 days. When I even tried explaining the numbers, they just didn't believe me. It really is hard to fathom exponential growth. For the depth calculation, I converted the grain count to weight in kg (each grain is 50mg), then divided by the area to see how deep it would be.

## 6. Paper Folding
Similar idea to the chess problem but with paper thickness. Starting with a 0.1mm sheet, each fold doubles the thickness. After 30 folds it gets ridiculous. Ihad to convert from mm to meters to kilometers just to make sense of it. Really shows how exponential growth can get out of hand fast.

## 7. Closest Number Game
Made a two player guessing game. The computer picks a random number, and players try to guess it. The trick was using absolute value to figure out who's closer. Then just subtract each guess from the secret number and see which difference is smaller. Added detailed output to show the differences so players can see how close they were. Also had to handle ties when both players are equally close.

## 8. Rock Paper Scissors
Classic game against the computer. Used random.choice() to get the computer's move from the list of options. The winning logic is just a bunch of if statements checking each combination (rock beats scissors, scissors beats paper, paper beats rock). Also made sure to handle ties when both pick the same thing.

## Testing
Added basic test cases to each script to catch obvious errors. Nothing fancy, just making sure the calculations are right and the logic works. Used try/except to handle bad inputs. Each program verifies its output against known correct values or checks that the logic is consistent. 