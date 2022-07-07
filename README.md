# CUTE22




## Results

### Challenge #1

|Team| Accuracy  | granularity  | context  |  criteria | schedule | 
|---|---|---|---|---|---|
| LLF  | 84.9  | weight  | global  | large_final  | dsd |
| EE  | 82.00  | weight  | global  | large_final  | cos |
| NH  | 81.93  | ?  | ?  | ?  | ? |
| LB  | 81.39  | weight  | global  | large_final | onecycle |
| MM | 81.  | weight  | global  | large_final  | onecycle |
| VD | 80.7  | weight  | global  | large_final  | dsd |
| VS | 80.7  | weight  | global  | large_final  | lin |
| CF | 80.1  | weight  | local  | updating_movmag  | iterative |
| MEM | 79  | filter  | local  | large_final  | cos |






### Challenge #2

|Team| Accuracy  | loss  | layers  | weight |
|---|---|---|---|---|
| EE  | 88.2  | Attention  | layer1,2,3,4  | 0.2  |
| FR  | 85.6  | Attention  | layer1,2,4.0.conv1  | 0.95  |
| TR  | 84.9  | Attention  | layer3,4  | 0.5  |
| NH  | 84.62  | ?  | ?  | ?  |
| VD  | 84.24  | SoftTarget  | -  |  1 |
| HB  | 81.86  | Attention  | layer1,2,3,4  |  0.25 |


### Challenge #3

|Team| Accuracy  | granularity  | context  |  criteria | schedule | loss  | layers  | weight |
|---|---|---|---|---| --- | --- | --- | ---| 
| LLF  | 85.1 | weight  | global | large_final  | dsd | Attention | layer1,2,3,4  |  0.95  |
| FC  | 84.5 | weight  | global | large_final  | onecycle | Attention | layer1,2,3,4  |  0.95  |
| NH  | 83.42  |   |   |   | | | | |
| EE  | 82.14  | weight  | global | large_final  | cos | Attention | layer1,2,3,4  |  0.5  |
| VD  | 81.12  | weight  | global | large_final  | cos | Attention | layer1,2,3,4  |  0.4  |
| MEM  | 79  | kernel  | global | large_final  | cos | Attention | 3,4  |  0.9  |
|   |   |   |   |   | | | | |


### Challenge # 4


|Team| # parameters (10e6) | time (ms)  |
|---|---|---|
| NH  | 44.38  | 2.61 |
|   |   |   |
|   |   |   |
