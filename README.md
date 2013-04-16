# Show Focus App
This python script will show which application currently has the focus 
under Windows.
I built this script to find out which (invisible) app is stealing my
focus every 30 minutes.

As i am using Win dll calls with ctypes, it will not work under Lunix but 
it should not be a big deal(tm) to fix this (even though you might not know the 
problem anyway).

# Prerequirements

- [psutils](http://code.google.com/p/psutil/downloads/list)

# Usage

    python ./getfg.py

# License

The code is under WTFPLv2. If the software was helpful and we meet some day,
buy me a Club Mate.
