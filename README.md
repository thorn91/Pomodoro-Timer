# Pomodoro.  Not spaghetti sauce
Put in your time in minutes, see the countdown in seconds, take automatic breaks until you're done, try not to cry over how it looks.  Popups ensure you will never miss a break.

## Instructions

* Enter the desired work time in minutes (will get converted and displayed as seconds b/c math is for losers)
* Each _time cycle_ will repeat 3 times.  The first 2 breaks are 5 minutes, the last is 15 minutes.  
* Popup (message) boxes pause the program after each cycle allowing you to finish your work or break before going to the next cycle.
* The interface is real bad because it was only supposed to be the popup, then I decided at the end to have varying timer amounts.
  
## Caveats

* Python was used because I didn't have Java or VisualStudio installed on this laptop, so just deal with the interface.  You only have to put in 1 number.  It's the best my minimum effort will get you.

## Instructions 4 Install (assuming you're starting from scratch)

* Make sure you have updated Python and added to path.  If you're on macOS/Linux, add your shebang line to the very top `#!/usr/bin/env python`
* This does not use any non-standard packages because it is very simple, but if your attention span as bad or worse than mine (or close) it may be useful.  Because screw in-app purchaes or webapps being the only option.
* Make your directory, open a terminal in it, and clone the link to it. Type:

    `init git`

    `git clone https://github.com/hortw1991/Pomodoro-Timer.git`

    Or fork it and do your thing, this is about convenience, not breakthrough. Then type:
  
    `cd whereeveryouputit`

    Go ahead and install the required packages (none, honestly, for this program?).

    `pip install -r requirements.txt`

    If you're on Linux or macOS, type your command, otherwise:

    `python pomodoro.py`