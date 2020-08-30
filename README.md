# Aggressive Bus Arrival
Have you used the various bus apps in Singapore and thought: I wish the apps were more aggressive! It needs more ***precision*** (even if meaningless), it needs to ***refresh more***, I want to know when it comes now! Look no further than this script.

## Why this script
The usual bus apps only give up to 1 minute precision (as per recommendation from LTA). However the actual response from their API is precise to the nearest second!. That's 60 whole seconds of wasted information! Why not create a script that shows the exact best given timing rather than rounding to the nearest minute?

## What it does

 1. Shows the remaining seconds to bus arrival
 2. Refreshes the bus arrival time every 30 seconds
 3. Shows the exact given arrival time as given by LTA

## What I plan to do

 1. Add map feature to further track the location of the bus
 2. Add better error handling feature for the responses
 3. Make it easier to find the bus stop of interest

## How to use
Run the script in `python.py`. Enter the bus stop code. Enter the bus number. Wait for response.
