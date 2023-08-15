# acme-overlapping-hours
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data.

### Example

```
INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU19:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
MARIO=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
LUIGI=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 2
RENE-ANDRES: 2
RENE-MARIO: 2
RENE-LUIGI: 2
ASTRID-ANDRES: 3
ASTRID-MARIO: 3
ASTRID-LUIGI: 3
ANDRES-MARIO: 3
ANDRES-LUIGI: 3
MARIO-LUIGI: 3
```

