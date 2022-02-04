import datetime
import os
import csv
import numpy as np
from matplotlib import pyplot as plt

datastring = """
Model parameters: 

Population size, N: 100 
Min num of groups, gmin: 2 
Max num of groups, gmax: 20 
In-group success probability, qi: 1 
Out-group success probability, qo: 0.6 
In-group benefit, Bi 1 
Out-group benefit, Bo: 2 
Strength of selection, sigma: 1.0
Polarisation p: 1 
Number of trails, trials: 10000 
Min / max / steps of r: 0.8, 0.999, 20
Save to log?: False
Save figure?: True
Use matrix?: False
Matrix used if so: Aarhus

##############################
Val of r: 0.8
There is 19 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0001
For 3 groups.

The probability that zero polarisation takes over is:
0.0007
For 4 groups.

The probability that zero polarisation takes over is:
0.0022
For 5 groups.

The probability that zero polarisation takes over is:
0.0055
For 6 groups.

The probability that zero polarisation takes over is:
0.0113
For 7 groups.

The probability that zero polarisation takes over is:
0.0141
For 8 groups.

The probability that zero polarisation takes over is:
0.0215
For 9 groups.

The probability that zero polarisation takes over is:
0.0226
For 10 groups.

The probability that zero polarisation takes over is:
0.0277
For 11 groups.

The probability that zero polarisation takes over is:
0.0306
For 12 groups.

The probability that zero polarisation takes over is:
0.032
For 13 groups.

The probability that zero polarisation takes over is:
0.0358
For 14 groups.

The probability that zero polarisation takes over is:
0.0361
For 15 groups.

The probability that zero polarisation takes over is:
0.038
For 16 groups.

The probability that zero polarisation takes over is:
0.0429
For 17 groups.

The probability that zero polarisation takes over is:
0.0451
For 18 groups.

The probability that zero polarisation takes over is:
0.0459
For 19 groups.

The probability that zero polarisation takes over is:
0.0466
For 20 groups.

##############################
Val of r: 0.8104736842105263
There is 18 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0008
For 4 groups.

The probability that zero polarisation takes over is:
0.003
For 5 groups.

The probability that zero polarisation takes over is:
0.0072
For 6 groups.

The probability that zero polarisation takes over is:
0.0117
For 7 groups.

The probability that zero polarisation takes over is:
0.0165
For 8 groups.

The probability that zero polarisation takes over is:
0.0171
For 9 groups.

The probability that zero polarisation takes over is:
0.0229
For 10 groups.

The probability that zero polarisation takes over is:
0.0242
For 11 groups.

The probability that zero polarisation takes over is:
0.0313
For 12 groups.

The probability that zero polarisation takes over is:
0.0295
For 13 groups.

The probability that zero polarisation takes over is:
0.0346
For 14 groups.

The probability that zero polarisation takes over is:
0.0356
For 15 groups.

The probability that zero polarisation takes over is:
0.0398
For 16 groups.

The probability that zero polarisation takes over is:
0.0403
For 17 groups.

The probability that zero polarisation takes over is:
0.0434
For 18 groups.

The probability that zero polarisation takes over is:
0.0461
For 19 groups.

The probability that zero polarisation takes over is:
0.0453
For 20 groups.

##############################
Val of r: 0.8209473684210526
There is 17 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0006
For 4 groups.

The probability that zero polarisation takes over is:
0.0034
For 5 groups.

The probability that zero polarisation takes over is:
0.0069
For 6 groups.

The probability that zero polarisation takes over is:
0.0099
For 7 groups.

The probability that zero polarisation takes over is:
0.0158
For 8 groups.

The probability that zero polarisation takes over is:
0.019
For 9 groups.

The probability that zero polarisation takes over is:
0.022
For 10 groups.

The probability that zero polarisation takes over is:
0.0254
For 11 groups.

The probability that zero polarisation takes over is:
0.0317
For 12 groups.

The probability that zero polarisation takes over is:
0.0343
For 13 groups.

The probability that zero polarisation takes over is:
0.0314
For 14 groups.

The probability that zero polarisation takes over is:
0.0339
For 15 groups.

The probability that zero polarisation takes over is:
0.0397
For 16 groups.

The probability that zero polarisation takes over is:
0.0385
For 17 groups.

The probability that zero polarisation takes over is:
0.0485
For 18 groups.

The probability that zero polarisation takes over is:
0.0433
For 19 groups.

The probability that zero polarisation takes over is:
0.0412
For 20 groups.

##############################
Val of r: 0.831421052631579
There is 16 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0006
For 4 groups.

The probability that zero polarisation takes over is:
0.0033
For 5 groups.

The probability that zero polarisation takes over is:
0.0081
For 6 groups.

The probability that zero polarisation takes over is:
0.0122
For 7 groups.

The probability that zero polarisation takes over is:
0.0174
For 8 groups.

The probability that zero polarisation takes over is:
0.0203
For 9 groups.

The probability that zero polarisation takes over is:
0.0221
For 10 groups.

The probability that zero polarisation takes over is:
0.0249
For 11 groups.

The probability that zero polarisation takes over is:
0.0287
For 12 groups.

The probability that zero polarisation takes over is:
0.0332
For 13 groups.

The probability that zero polarisation takes over is:
0.0334
For 14 groups.

The probability that zero polarisation takes over is:
0.0397
For 15 groups.

The probability that zero polarisation takes over is:
0.0395
For 16 groups.

The probability that zero polarisation takes over is:
0.0389
For 17 groups.

The probability that zero polarisation takes over is:
0.0392
For 18 groups.

The probability that zero polarisation takes over is:
0.0446
For 19 groups.

The probability that zero polarisation takes over is:
0.0477
For 20 groups.

##############################
Val of r: 0.8418947368421053
There is 15 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0008
For 4 groups.

The probability that zero polarisation takes over is:
0.0028
For 5 groups.

The probability that zero polarisation takes over is:
0.0053
For 6 groups.

The probability that zero polarisation takes over is:
0.011
For 7 groups.

The probability that zero polarisation takes over is:
0.0138
For 8 groups.

The probability that zero polarisation takes over is:
0.0202
For 9 groups.

The probability that zero polarisation takes over is:
0.0246
For 10 groups.

The probability that zero polarisation takes over is:
0.0263
For 11 groups.

The probability that zero polarisation takes over is:
0.0317
For 12 groups.

The probability that zero polarisation takes over is:
0.0313
For 13 groups.

The probability that zero polarisation takes over is:
0.0338
For 14 groups.

The probability that zero polarisation takes over is:
0.0377
For 15 groups.

The probability that zero polarisation takes over is:
0.04
For 16 groups.

The probability that zero polarisation takes over is:
0.0416
For 17 groups.

The probability that zero polarisation takes over is:
0.043
For 18 groups.

The probability that zero polarisation takes over is:
0.0431
For 19 groups.

The probability that zero polarisation takes over is:
0.0473
For 20 groups.

##############################
Val of r: 0.8523684210526317
There is 14 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0007
For 4 groups.

The probability that zero polarisation takes over is:
0.0023
For 5 groups.

The probability that zero polarisation takes over is:
0.0077
For 6 groups.

The probability that zero polarisation takes over is:
0.0118
For 7 groups.

The probability that zero polarisation takes over is:
0.0135
For 8 groups.

The probability that zero polarisation takes over is:
0.0174
For 9 groups.

The probability that zero polarisation takes over is:
0.023
For 10 groups.

The probability that zero polarisation takes over is:
0.0255
For 11 groups.

The probability that zero polarisation takes over is:
0.0295
For 12 groups.

The probability that zero polarisation takes over is:
0.0339
For 13 groups.

The probability that zero polarisation takes over is:
0.0331
For 14 groups.

The probability that zero polarisation takes over is:
0.0376
For 15 groups.

The probability that zero polarisation takes over is:
0.0432
For 16 groups.

The probability that zero polarisation takes over is:
0.0415
For 17 groups.

The probability that zero polarisation takes over is:
0.0403
For 18 groups.

The probability that zero polarisation takes over is:
0.0418
For 19 groups.

The probability that zero polarisation takes over is:
0.0451
For 20 groups.

##############################
Val of r: 0.862842105263158
There is 13 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0005
For 4 groups.

The probability that zero polarisation takes over is:
0.0022
For 5 groups.

The probability that zero polarisation takes over is:
0.0061
For 6 groups.

The probability that zero polarisation takes over is:
0.011
For 7 groups.

The probability that zero polarisation takes over is:
0.0143
For 8 groups.

The probability that zero polarisation takes over is:
0.0182
For 9 groups.

The probability that zero polarisation takes over is:
0.0229
For 10 groups.

The probability that zero polarisation takes over is:
0.0252
For 11 groups.

The probability that zero polarisation takes over is:
0.0283
For 12 groups.

The probability that zero polarisation takes over is:
0.0333
For 13 groups.

The probability that zero polarisation takes over is:
0.0311
For 14 groups.

The probability that zero polarisation takes over is:
0.0348
For 15 groups.

The probability that zero polarisation takes over is:
0.0405
For 16 groups.

The probability that zero polarisation takes over is:
0.0409
For 17 groups.

The probability that zero polarisation takes over is:
0.0409
For 18 groups.

The probability that zero polarisation takes over is:
0.0444
For 19 groups.

The probability that zero polarisation takes over is:
0.0483
For 20 groups.

##############################
Val of r: 0.8733157894736843
There is 12 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0005
For 4 groups.

The probability that zero polarisation takes over is:
0.0017
For 5 groups.

The probability that zero polarisation takes over is:
0.0063
For 6 groups.

The probability that zero polarisation takes over is:
0.0109
For 7 groups.

The probability that zero polarisation takes over is:
0.015
For 8 groups.

The probability that zero polarisation takes over is:
0.0189
For 9 groups.

The probability that zero polarisation takes over is:
0.0242
For 10 groups.

The probability that zero polarisation takes over is:
0.0273
For 11 groups.

The probability that zero polarisation takes over is:
0.0272
For 12 groups.

The probability that zero polarisation takes over is:
0.0294
For 13 groups.

The probability that zero polarisation takes over is:
0.0348
For 14 groups.

The probability that zero polarisation takes over is:
0.0371
For 15 groups.

The probability that zero polarisation takes over is:
0.039
For 16 groups.

The probability that zero polarisation takes over is:
0.0418
For 17 groups.

The probability that zero polarisation takes over is:
0.0401
For 18 groups.

The probability that zero polarisation takes over is:
0.0441
For 19 groups.

The probability that zero polarisation takes over is:
0.0446
For 20 groups.

##############################
Val of r: 0.8837894736842106
There is 11 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0005
For 4 groups.

The probability that zero polarisation takes over is:
0.0032
For 5 groups.

The probability that zero polarisation takes over is:
0.0055
For 6 groups.

The probability that zero polarisation takes over is:
0.0097
For 7 groups.

The probability that zero polarisation takes over is:
0.0129
For 8 groups.

The probability that zero polarisation takes over is:
0.0153
For 9 groups.

The probability that zero polarisation takes over is:
0.0228
For 10 groups.

The probability that zero polarisation takes over is:
0.0265
For 11 groups.

The probability that zero polarisation takes over is:
0.0303
For 12 groups.

The probability that zero polarisation takes over is:
0.0298
For 13 groups.

The probability that zero polarisation takes over is:
0.0362
For 14 groups.

The probability that zero polarisation takes over is:
0.0395
For 15 groups.

The probability that zero polarisation takes over is:
0.0359
For 16 groups.

The probability that zero polarisation takes over is:
0.0376
For 17 groups.

The probability that zero polarisation takes over is:
0.0438
For 18 groups.

The probability that zero polarisation takes over is:
0.0459
For 19 groups.

The probability that zero polarisation takes over is:
0.0449
For 20 groups.

##############################
Val of r: 0.8942631578947369
There is 10 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0005
For 4 groups.

The probability that zero polarisation takes over is:
0.0023
For 5 groups.

The probability that zero polarisation takes over is:
0.0069
For 6 groups.

The probability that zero polarisation takes over is:
0.0095
For 7 groups.

The probability that zero polarisation takes over is:
0.0141
For 8 groups.

The probability that zero polarisation takes over is:
0.02
For 9 groups.

The probability that zero polarisation takes over is:
0.0217
For 10 groups.

The probability that zero polarisation takes over is:
0.0223
For 11 groups.

The probability that zero polarisation takes over is:
0.0319
For 12 groups.

The probability that zero polarisation takes over is:
0.0316
For 13 groups.

The probability that zero polarisation takes over is:
0.0356
For 14 groups.

The probability that zero polarisation takes over is:
0.0356
For 15 groups.

The probability that zero polarisation takes over is:
0.038
For 16 groups.

The probability that zero polarisation takes over is:
0.0407
For 17 groups.

The probability that zero polarisation takes over is:
0.0406
For 18 groups.

The probability that zero polarisation takes over is:
0.0452
For 19 groups.

The probability that zero polarisation takes over is:
0.0482
For 20 groups.

##############################
Val of r: 0.9047368421052632
There is 9 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0006
For 4 groups.

The probability that zero polarisation takes over is:
0.0026
For 5 groups.

The probability that zero polarisation takes over is:
0.0055
For 6 groups.

The probability that zero polarisation takes over is:
0.0114
For 7 groups.

The probability that zero polarisation takes over is:
0.0136
For 8 groups.

The probability that zero polarisation takes over is:
0.0192
For 9 groups.

The probability that zero polarisation takes over is:
0.0224
For 10 groups.

The probability that zero polarisation takes over is:
0.0247
For 11 groups.

The probability that zero polarisation takes over is:
0.0278
For 12 groups.

The probability that zero polarisation takes over is:
0.0286
For 13 groups.

The probability that zero polarisation takes over is:
0.0354
For 14 groups.

The probability that zero polarisation takes over is:
0.0324
For 15 groups.

The probability that zero polarisation takes over is:
0.0378
For 16 groups.

The probability that zero polarisation takes over is:
0.0407
For 17 groups.

The probability that zero polarisation takes over is:
0.0402
For 18 groups.

The probability that zero polarisation takes over is:
0.0428
For 19 groups.

The probability that zero polarisation takes over is:
0.0449
For 20 groups.

##############################
Val of r: 0.9152105263157895
There is 8 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0001
For 3 groups.

The probability that zero polarisation takes over is:
0.0002
For 4 groups.

The probability that zero polarisation takes over is:
0.0024
For 5 groups.

The probability that zero polarisation takes over is:
0.0051
For 6 groups.

The probability that zero polarisation takes over is:
0.009
For 7 groups.

The probability that zero polarisation takes over is:
0.0137
For 8 groups.

The probability that zero polarisation takes over is:
0.0196
For 9 groups.

The probability that zero polarisation takes over is:
0.0227
For 10 groups.

The probability that zero polarisation takes over is:
0.0251
For 11 groups.

The probability that zero polarisation takes over is:
0.0249
For 12 groups.

The probability that zero polarisation takes over is:
0.0312
For 13 groups.

The probability that zero polarisation takes over is:
0.0324
For 14 groups.

The probability that zero polarisation takes over is:
0.0334
For 15 groups.

The probability that zero polarisation takes over is:
0.0355
For 16 groups.

The probability that zero polarisation takes over is:
0.0402
For 17 groups.

The probability that zero polarisation takes over is:
0.0387
For 18 groups.

The probability that zero polarisation takes over is:
0.0435
For 19 groups.

The probability that zero polarisation takes over is:
0.0467
For 20 groups.

##############################
Val of r: 0.9256842105263158
There is 7 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0001
For 3 groups.

The probability that zero polarisation takes over is:
0.0004
For 4 groups.

The probability that zero polarisation takes over is:
0.0022
For 5 groups.

The probability that zero polarisation takes over is:
0.0049
For 6 groups.

The probability that zero polarisation takes over is:
0.0094
For 7 groups.

The probability that zero polarisation takes over is:
0.0126
For 8 groups.

The probability that zero polarisation takes over is:
0.019
For 9 groups.

The probability that zero polarisation takes over is:
0.0217
For 10 groups.

The probability that zero polarisation takes over is:
0.0249
For 11 groups.

The probability that zero polarisation takes over is:
0.0303
For 12 groups.

The probability that zero polarisation takes over is:
0.032
For 13 groups.

The probability that zero polarisation takes over is:
0.03
For 14 groups.

The probability that zero polarisation takes over is:
0.0373
For 15 groups.

The probability that zero polarisation takes over is:
0.0387
For 16 groups.

The probability that zero polarisation takes over is:
0.0373
For 17 groups.

The probability that zero polarisation takes over is:
0.0409
For 18 groups.

The probability that zero polarisation takes over is:
0.0446
For 19 groups.

The probability that zero polarisation takes over is:
0.0411
For 20 groups.

##############################
Val of r: 0.9361578947368421
There is 6 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0001
For 3 groups.

The probability that zero polarisation takes over is:
0.0002
For 4 groups.

The probability that zero polarisation takes over is:
0.0024
For 5 groups.

The probability that zero polarisation takes over is:
0.0049
For 6 groups.

The probability that zero polarisation takes over is:
0.0092
For 7 groups.

The probability that zero polarisation takes over is:
0.0134
For 8 groups.

The probability that zero polarisation takes over is:
0.0164
For 9 groups.

The probability that zero polarisation takes over is:
0.0187
For 10 groups.

The probability that zero polarisation takes over is:
0.0232
For 11 groups.

The probability that zero polarisation takes over is:
0.0273
For 12 groups.

The probability that zero polarisation takes over is:
0.03
For 13 groups.

The probability that zero polarisation takes over is:
0.0328
For 14 groups.

The probability that zero polarisation takes over is:
0.0318
For 15 groups.

The probability that zero polarisation takes over is:
0.0346
For 16 groups.

The probability that zero polarisation takes over is:
0.0346
For 17 groups.

The probability that zero polarisation takes over is:
0.0384
For 18 groups.

The probability that zero polarisation takes over is:
0.0375
For 19 groups.

The probability that zero polarisation takes over is:
0.0419
For 20 groups.

##############################
Val of r: 0.9466315789473685
There is 5 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0003
For 4 groups.

The probability that zero polarisation takes over is:
0.0017
For 5 groups.

The probability that zero polarisation takes over is:
0.0059
For 6 groups.

The probability that zero polarisation takes over is:
0.0075
For 7 groups.

The probability that zero polarisation takes over is:
0.0117
For 8 groups.

The probability that zero polarisation takes over is:
0.0154
For 9 groups.

The probability that zero polarisation takes over is:
0.0216
For 10 groups.

The probability that zero polarisation takes over is:
0.0243
For 11 groups.

The probability that zero polarisation takes over is:
0.0237
For 12 groups.

The probability that zero polarisation takes over is:
0.0282
For 13 groups.

The probability that zero polarisation takes over is:
0.0341
For 14 groups.

The probability that zero polarisation takes over is:
0.0315
For 15 groups.

The probability that zero polarisation takes over is:
0.0361
For 16 groups.

The probability that zero polarisation takes over is:
0.0377
For 17 groups.

The probability that zero polarisation takes over is:
0.0352
For 18 groups.

The probability that zero polarisation takes over is:
0.0366
For 19 groups.

The probability that zero polarisation takes over is:
0.0353
For 20 groups.

##############################
Val of r: 0.9571052631578948
There is 4 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0
For 4 groups.

The probability that zero polarisation takes over is:
0.0013
For 5 groups.

The probability that zero polarisation takes over is:
0.0038
For 6 groups.

The probability that zero polarisation takes over is:
0.0079
For 7 groups.

The probability that zero polarisation takes over is:
0.0107
For 8 groups.

The probability that zero polarisation takes over is:
0.0164
For 9 groups.

The probability that zero polarisation takes over is:
0.0206
For 10 groups.

The probability that zero polarisation takes over is:
0.0233
For 11 groups.

The probability that zero polarisation takes over is:
0.0252
For 12 groups.

The probability that zero polarisation takes over is:
0.0289
For 13 groups.

The probability that zero polarisation takes over is:
0.0274
For 14 groups.

The probability that zero polarisation takes over is:
0.0304
For 15 groups.

The probability that zero polarisation takes over is:
0.0312
For 16 groups.

The probability that zero polarisation takes over is:
0.0296
For 17 groups.

The probability that zero polarisation takes over is:
0.0321
For 18 groups.

The probability that zero polarisation takes over is:
0.031
For 19 groups.

The probability that zero polarisation takes over is:
0.0285
For 20 groups.

##############################
Val of r: 0.9675789473684211
There is 3 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0001
For 4 groups.

The probability that zero polarisation takes over is:
0.0014
For 5 groups.

The probability that zero polarisation takes over is:
0.0051
For 6 groups.

The probability that zero polarisation takes over is:
0.0076
For 7 groups.

The probability that zero polarisation takes over is:
0.0114
For 8 groups.

The probability that zero polarisation takes over is:
0.0146
For 9 groups.

The probability that zero polarisation takes over is:
0.018
For 10 groups.

The probability that zero polarisation takes over is:
0.0204
For 11 groups.

The probability that zero polarisation takes over is:
0.0233
For 12 groups.

The probability that zero polarisation takes over is:
0.0227
For 13 groups.

The probability that zero polarisation takes over is:
0.0234
For 14 groups.

The probability that zero polarisation takes over is:
0.0264
For 15 groups.

The probability that zero polarisation takes over is:
0.0227
For 16 groups.

The probability that zero polarisation takes over is:
0.0259
For 17 groups.

The probability that zero polarisation takes over is:
0.0229
For 18 groups.

The probability that zero polarisation takes over is:
0.0191
For 19 groups.

The probability that zero polarisation takes over is:
0.0187
For 20 groups.

##############################
Val of r: 0.9780526315789474
There is 2 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0001
For 4 groups.

The probability that zero polarisation takes over is:
0.0007
For 5 groups.

The probability that zero polarisation takes over is:
0.0035
For 6 groups.

The probability that zero polarisation takes over is:
0.0064
For 7 groups.

The probability that zero polarisation takes over is:
0.0108
For 8 groups.

The probability that zero polarisation takes over is:
0.011
For 9 groups.

The probability that zero polarisation takes over is:
0.015
For 10 groups.

The probability that zero polarisation takes over is:
0.014
For 11 groups.

The probability that zero polarisation takes over is:
0.0171
For 12 groups.

The probability that zero polarisation takes over is:
0.0137
For 13 groups.

The probability that zero polarisation takes over is:
0.0134
For 14 groups.

The probability that zero polarisation takes over is:
0.0126
For 15 groups.

The probability that zero polarisation takes over is:
0.0115
For 16 groups.

The probability that zero polarisation takes over is:
0.0099
For 17 groups.

The probability that zero polarisation takes over is:
0.0078
For 18 groups.

The probability that zero polarisation takes over is:
0.006
For 19 groups.

The probability that zero polarisation takes over is:
0.0057
For 20 groups.

##############################
Val of r: 0.9885263157894737
There is 1 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0001
For 4 groups.

The probability that zero polarisation takes over is:
0.001
For 5 groups.

The probability that zero polarisation takes over is:
0.0017
For 6 groups.

The probability that zero polarisation takes over is:
0.0036
For 7 groups.

The probability that zero polarisation takes over is:
0.0047
For 8 groups.

The probability that zero polarisation takes over is:
0.0034
For 9 groups.

The probability that zero polarisation takes over is:
0.0041
For 10 groups.

The probability that zero polarisation takes over is:
0.0026
For 11 groups.

The probability that zero polarisation takes over is:
0.0021
For 12 groups.

The probability that zero polarisation takes over is:
0.002
For 13 groups.

The probability that zero polarisation takes over is:
0.0006
For 14 groups.

The probability that zero polarisation takes over is:
0.0007
For 15 groups.

The probability that zero polarisation takes over is:
0.0005
For 16 groups.

The probability that zero polarisation takes over is:
0.0002
For 17 groups.

The probability that zero polarisation takes over is:
0.0004
For 18 groups.

The probability that zero polarisation takes over is:
0.0001
For 19 groups.

The probability that zero polarisation takes over is:
0.0001
For 20 groups.

##############################
Val of r: 0.999
There is 0 steps to go after this.


The probability that zero polarisation takes over is:
0.0
For 2 groups.

The probability that zero polarisation takes over is:
0.0
For 3 groups.

The probability that zero polarisation takes over is:
0.0
For 4 groups.

The probability that zero polarisation takes over is:
0.0
For 5 groups.

The probability that zero polarisation takes over is:
0.0
For 6 groups.

The probability that zero polarisation takes over is:
0.0
For 7 groups.

The probability that zero polarisation takes over is:
0.0
For 8 groups.

The probability that zero polarisation takes over is:
0.0
For 9 groups.

The probability that zero polarisation takes over is:
0.0
For 10 groups.

The probability that zero polarisation takes over is:
0.0
For 11 groups.

The probability that zero polarisation takes over is:
0.0
For 12 groups.

The probability that zero polarisation takes over is:
0.0
For 13 groups.

The probability that zero polarisation takes over is:
0.0
For 14 groups.

The probability that zero polarisation takes over is:
0.0
For 15 groups.

The probability that zero polarisation takes over is:
0.0
For 16 groups.

The probability that zero polarisation takes over is:
0.0
For 17 groups.

The probability that zero polarisation takes over is:
0.0
For 18 groups.

The probability that zero polarisation takes over is:
0.0
For 19 groups.

The probability that zero polarisation takes over is:
0.0
For 20 groups.
"""

results = []
lines = []
curr_line = ''

for char in datastring:
    if char != '\n':
        curr_line += char
    else:
        lines.append(curr_line)
        curr_line = ''

for i, line in enumerate(lines):
    if line == '##############################':
        results.append([])
    elif line == 'The probability that zero polarisation takes over is:':
        results[-1].append(float(lines[i + 1]))

gmin = 2
gmax = 20
rmin = 0.8
rmax = 0.999
steps = 20
N = 100
trials = 10000

newres = []

# dividing each val by the max in the row.
for row in results:
    newres.append([])
    mrow = max(row)
    for val in row:
        if mrow != 0:
            val = val / mrow
        newres[-1].append(val)

fig, ax = plt.subplots()

X, Y = np.meshgrid(range(gmin, gmax + 1), np.linspace(rmin, rmax, steps))

plot = ax.pcolormesh(X, Y, np.array(newres), shading='auto')
fig.colorbar(plot, label="p")
ax.set(title=f"Probability of fixation / max for row for N={N}, Trails={trials}",
       xlabel="Number of groups",
       ylabel="Value of r",
       xticks=list(range(gmin, gmax + 1))
       )

#plt.show()

dat = str(datetime.datetime.now().strftime('%Y-%m-%d'))

with open(f"Saved_data/Logs/Date_{dat}_log.csv", 'w+', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['N', 'Trials', 'rmin', 'rmax', 'steps', 'gmin', 'gmax'])
    csvwriter.writerow([N, trials, rmin, rmax, steps, gmin, gmax])
    csvwriter.writerow(['data'])
    csvwriter.writerows(results)
