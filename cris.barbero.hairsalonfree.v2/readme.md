# HairSalonFree

## Usage
```
python main.py
```

*Requires python 3.7* in order to support `dataclasses` and `f'strings`

## Status
Time 2 hours:
This is a mostly working sample.

ToDo:
- Finish the salon close functionality.  Currently the salon will close even if there is an active hair cut.
- Add dataclasses for the waiting_customers and active_hair_cuts instead of objects

Time 3 hours:
This is a fully working sample.

Notes:
- Customers are randomly generated between 1 and 20 minutes
- Haircuts will take between 20 and 40 minutes (determined randomly)
- The salon will open at 9:00, lock it's doors at 17:00 and close once all haircuts are finished


