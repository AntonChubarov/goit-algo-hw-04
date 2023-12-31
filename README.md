# ДЗ Алгоритми сортування

Зведемо результати вимірів часу у таблицю:

Integers:

|    N | Insertion Sort Time (s) | Merge Sort Time (s) | Builtin Sorted Sort Time (s) |
|-----:|:-----------------------:|:---------------------:|:----------------------------:|
|   10 |   3.90e-05              |     0.0002102         |           1.14e-05           |
|  100 |        0.0004695        |     0.0039625         |           7.27e-05           |
| 1000 |         0.0265          |     0.04442           |           0.001886           |

Strings:

|    N | Insertion Sort Time (s) | Merge Sort Time (s) | Builtin Sorted Sort Time (s) |
|-----:|:-----------------------:|:---------------------:|:-----------------------------:|
|   10 |  3.46e-05               |     0.0002350         |      1.01e-05                |
|  100 |        0.0005400        |     0.0036868         |      0.0001449               |
| 1000 |         0.0345          |     0.05273           |      0.003868                |

## Висновки

1. Сортування вставкою досить добре працює для малих (N≈10) наборів даних;
2. Сортування злиттям дещо повільніше за сортування вставкою, але судячи з характеру зростання часової складності, для розміру вхідних даних 10000+ сортування вставкою буде повільнішим;
3. Сортування вбудованим алгоритмом Python на порядок швидше за сортування злиттям та вставкою.