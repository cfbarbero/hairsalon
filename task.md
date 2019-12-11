Goal

Your task is to simulate a hair salon. Fun!

Rules

The hair salon is open for 8 hours, from 9am to 5pm. You don't want your program to take that long to run, so you'll need to somehow simulate real time.

When the salon opens, there are 4 hair stylists who start their shift:
Anne, Ben, Carol, and Derek.

On average, a new customer enters once every ten minutes. Their arrivals are random. Customers are named successively starting at Customer-1. The salon can only hold 15 total customers; if a customer arrives when the salon is full, they leave impatiently.

Otherwise, the client waits for a stylist. A stylist can only cut one person's hair at a time, and takes between 20 and 40 minutes to do so. After a stylist is done with a customer, the customer leaves satisfied.

A customer will wait up to 30 minutes for a free stylist; if time's up and none can be found, the customer leaves unfulfilled.

Stylists work 4 hour shifts, so the first shift of stylists is allowed to go home at 1pm. They end their shift as soon as they can, unless they are busy with a client. In that case, they wait until they finish with that client, and then end their shift.

At 1pm, the second shift of stylists starts:
Erin, Frank, Gloria, and Heber.
They also work a 4 hour shift, and can go home after 5pm. Like the morning shift, if they're busy with a customer, they need to finish up before leaving.

A customer who enters after 5pm is turned away, and leaves cursing themselves.

When all the stylists and customers have gone home, the salon closes. If there are any customers left waiting for a stylist, they are kicked out, and leave furious.

Input/Output

Your program should print the below events in chronological order. [Time] is salon-time in the format HH:MM, not real time.

[Time] Hair salon [opened/closed]
[Time] [Stylist] [started/ended] shift
[Time] [Customer] entered
[Time] [Customer] left [impatiently/satisfied/unfulfilled/cursing themselves/furious]
[Time] [Stylist] [started/ended] cutting [Customer]'s hair

Tests

There are no tests provided for this task as of yet, it is up to you to verify that the behavior is correct.

Submission Guidelines

For this task you may code up your solution using this online IDE (CodeSignals) or if you prefer you can write your solution on your computer and email the hiring manager your solution. We ask that you email your solution 2 hours after you begin the task and then, if you choose to continue past 2 hours, email your final solution you are happy with.

Guidelines

Use your choice of language. Use only standard libraries (libraries for random number generation and time handling are also acceptable). Use whatever resources you'd like, apart from asking about the question itself online.

Focus on correctness, not efficiency.

Code should be well-documented, clear, and concise. At the same time, try not to over-engineer this. Working code >> pretty non-functioning code.

If you have time left over, write tests instead of improving efficiency.

If you don’t use CodeSignals please provide instructions on how to (compile and) run your code.

Before submitting, write a few sentences in your submission about what works and what doesn't. e.g. “I tried to get X to work but couldn’t. Y and Z are working correctly though.” This helps us know where a gap in your solution can be attributed to a lack of understanding or lack of time.

Please don't share the question with others.

Thanks for taking the time to do it!

    [execution time limit] 60 seconds (py3)

