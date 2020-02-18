import pandas as pd
import numpy as np

n = 50

df = pd.DataFrame({
    'distance': np.random.randint(0, 200_000, size=n),
    'fuel usage': 2 + 18*np.random.rand(n),
})


df.head()
# === ======== ===========
#     distance fuel usage
# === ======== ===========
# 0   5588     15.264853
# 1   99747    4.308231
# 2   97302    11.575376
# 3   117155   18.862744
# 4   73709    18.138283
# === ======== ===========


df.describe()
# ======= =============== ==========
#         distance        fuel usage
# ======= =============== ==========
# count   0.000000        50.000000
# mean    96794.320000    10.307848
# std     62282.663803    5.036276
# min     2143.000000     2.132470
# 25%     36741.500000    5.952677
# 50%     93007.000000    10.316452
# 75%     154008.500000   13.820076
# max     198046.000000   19.694027
# ======= =============== ==========


df.loc[df.fuel_usage < 5, 'brand'] = 'VW'
# == ======== ========== =====
#    distance fuel usage brand
# == ======== ========== =====
# 0  5588     15.264853  UAZ
# 1  99747    4.308231   VW
# 2  97302    11.575376  UAZ
# 3  117155   18.862744  UAZ
# 4  73709    18.138283  UAZ
# == ======== ========== =====

# Alternative solution
df['brand'] = pd.cut(df.fuel_usage, bins=[0, 5, 10, 100], labels=['VW', 'Ford', 'UAZ'])
# == ======== ========== =====
#    distance fuel usage brand
# == ======== ========== =====
# 0  5588     15.264853  UAZ
# 1  99747    4.308231   VW
# 2  97302    11.575376  UAZ
# 3  117155   18.862744  UAZ
# 4  73709    18.138283  UAZ
# == ======== ========== =====


df['origin'] = pd.cut(df.distance, bins=[0, 100, 1e5, np.inf], labels=['new', 'used', 'from germany'])

df.head()
# === ======== =========== ===== ===========
#     distance fuel usage  brand origin
# === ======== =========== ===== ===========
# 0   5588     15.264853   UAZ   used
# 1   99747    4.308231    VW    used
# 2   97302    11.575376   UAZ   used
# 3   117155   18.862744   UAZ   from germany
# 4   73709    18.138283   UAZ   used
# === ======== =========== ===== ===========


df.groupby(['brand', 'origin']).describe().T
# =================== ========================== ========================== ==========================
# brand               VW                         Ford                       UAZ
# origin              used         from germany  used         from germany  used         from germany
# =================== ========================== ========================== ==========================
# distance    count   5.000000     7.000000      11.000000    6.000000      13.000000    8.000000
#             mean    53130.600000 147559.285714 52263.909091 179048.000000 47688.615385 147846.375000
#             std     43207.205363 27935.718079  35514.114012 8345.607132   33578.183062 29669.603213
#             min     2988.000000  109498.000000 8550.000000  164217.000000 1746.000000  105497.000000
#             25%     20030.000000 130846.000000 23674.000000 176727.500000 14940.000000 122390.750000
#             50%     48931.000000 147778.000000 50347.000000 181309.500000 50751.000000 154775.500000
#             75%     93957.000000 164885.000000 85860.500000 183584.500000 73709.000000 166537.500000
#             max     99747.000000 184177.000000 99884.000000 187909.000000 97302.000000 192988.000000
# fuel usage    count    5.000000    7.000000      11.000000   6.000000       13.000000    8.000000
#             mean     3.508948    3.645898      7.409556    7.028662       14.566981    16.438332
#             std      1.068128    0.867709      1.636214    1.803311       3.030231     3.786771
#             min      2.486142    2.426900      5.123669    5.076044       10.143688    10.215177
#             25%      2.697416    3.021124      6.182025    5.648620       12.600224    15.449772
#             50%      3.108775    3.870043      7.442336    6.652541       13.524153    17.990315
#             75%      4.308231    4.245297      8.671341    8.621158       18.009058    18.933888
#             max      4.944177    4.691502      9.611147    9.199502       19.708519    19.580096
# =================== ========================== ========================== ==========================