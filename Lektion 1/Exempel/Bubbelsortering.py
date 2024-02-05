@ -3,3 +3,27 @@ Vi börjar med listan:
[5, 2, 8, 1, 3]

Första itereringen:
    [5 och 2] [byte]
    [5 och 8] [inget byte]
    [8 och 1] [byte]
    [8 och 3] [byte]

[2, 5, 1, 3, 8]

Andra itereringen:
    [2 och 5] [inget byte]
    [5 och 1] [byte]
    [5 och 3] [byte]
    [5 och 8] [inget byte]

[2, 1, 3, 5, 8]

Tredje itereringen:
    [2 och 1] [byte]
    [2 och 3] [inget byte]
    [3 och 5] [inget byte]
    [5 och 8] [inget byte]

[1, 2, 3, 5, 8]

Fjärde iterering som visar att alla värden är sorterade.
