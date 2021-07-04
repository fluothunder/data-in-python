import pandas as pd
import numpy as np

# ========================================
# test_del_nan()
# ========================================
data1 = {'voivo': {44183: 24, 9964: 24, 33244: 32},
         'county': {44183: 1, 9964: 73, 33244: 10},
         'district': {44183: 1, 9964: 1, 33244: 3},
         'district_type': {44183: 'M', 9964: 'M', 33244: 'M-Gm'},
         'school_type': {44183: 'Centrum Kształcenia Ustawicznego - bez szkół',
                         9964: 'Przedszkole',
                         33244: 'Liceum ogólnokształcące'},
         'students': {44183: 0, 9964: np.nan, 33244: 42},
         'sections': {44183: np.nan, 9964: 3.0, 33244: 3.0},
         'rspo': {44183: 91962.0, 9964: 22498.0, 33244: 103565.0},
         'teachers': {44183: 0, 9964: 0, 33244: 14}}
df1 = pd.DataFrame(data1)
expected_data1 = {'voivo': {33244: 32},
                  'county': {33244: 10},
                  'district': {33244: 3},
                  'district_type': {33244: 'M-Gm'},
                  'school_type': {33244: 'Liceum ogólnokształcące'},
                  'students': {33244: 42.0},
                  'sections': {33244: 3.0},
                  'rspo': {33244: 103565.0},
                  'teachers': {33244: 14}}
expected_df1 = pd.DataFrame(expected_data1)

# ========================================
# test_del_schools_from_non_existing_districts()
# ========================================
dict2 = {(2, 1, 1): "foo", (14, 17, 1): "bar", (2, 1, 2): "foobar"}
data2 = {'voivo': {40747: 14, 18942: 32, 13280: 2},
         'county': {40747: 17, 18942: 3, 13280: 1},
         'district': {40747: 1, 18942: 4, 13280: 2},
         'district_type': {40747: 'M', 18942: 'M', 13280: 'Gm'},
         'school_type': {40747: 'Ośrodek dokształcania i doskonalenia zawodowego',
                         18942: 'Szkoła podstawowa',
                         13280: 'Szkoła podstawowa'},
         'students': {40747: 0, 18942: 68, 13280: 51},
         'sections': {40747: 0.0, 18942: 5.0, 13280: 7.0},
         'rspo': {40747: 57717.0, 18942: 123889.0, 13280: 92933.0},
         'teachers': {40747: 0, 18942: 22, 13280: 17}}
df2 = pd.DataFrame(data2)
expected_data2 = {'voivo': {40747: 14, 13280: 2},
                  'county': {40747: 17, 13280: 1},
                  'district': {40747: 1, 13280: 2},
                  'district_type': {40747: 'M', 13280: 'Gm'},
                  'school_type': {40747: 'Ośrodek dokształcania i doskonalenia zawodowego',
                                  13280: 'Szkoła podstawowa'},
                  'students': {40747: 0, 13280: 51},
                  'sections': {40747: 0.0, 13280: 7.0},
                  'rspo': {40747: 57717.0, 13280: 92933.0},
                  'teachers': {40747: 0, 13280: 17}}
expected_df2 = pd.DataFrame(expected_data2)

# ========================================
# test_del_zs()
# ========================================
data3 = {'voivo': {11249: 30, 19388: 14, 25955: 30, 33156: 30, 54696: 30},
         'county': {11249: 15, 19388: 34, 25955: 15, 33156: 64, 54696: 15},
         'district': {11249: 2, 19388: 9, 25955: 2, 33156: 1, 54696: 2},
         'district_type': {11249: 'M-Gm',
                           19388: 'M-Gm',
                           25955: 'M-Gm',
                           33156: 'M',
                           54696: 'M-Gm'},
         'school_type': {11249: 'Przedszkole',
                         19388: 'Szkoła podstawowa',
                         25955: 'Szkoła podstawowa',
                         33156: 'Liceum ogólnokształcące',
                         54696: 'Zespół szkół i placówek oświatowych'},
         'students': {11249: 35, 19388: 1004, 25955: 93, 33156: 72, 54696: 0},
         'sections': {11249: 2.0, 19388: 44.0, 25955: 8.0, 33156: 6.0, 54696: 0.0},
         'rspo': {11249: 118407.0,
                  19388: 53711.0,
                  25955: 118407.0,
                  33156: 30473.0,
                  54696: 118407.0},
         'teachers': {11249: 0, 19388: 81, 25955: 0, 33156: 10, 54696: 20}}
df3 = pd.DataFrame(data3)
expected_data3 = {'voivo': {0: 30, 1: 14, 2: 30, 3: 30},
                  'county': {0: 64, 1: 34, 2: 15, 3: 15},
                  'district': {0: 1, 1: 9, 2: 2, 3: 2},
                  'district_type': {0: 'M', 1: 'M-Gm', 2: 'M-Gm', 3: 'M-Gm'},
                  'school_type': {0: 'Liceum ogólnokształcące',
                                  1: 'Szkoła podstawowa',
                                  2: 'Przedszkole',
                                  3: 'Szkoła podstawowa'},
                  'students': {0: 72, 1: 1004, 2: 35, 3: 93},
                  'sections': {0: 6.0, 1: 44.0, 2: 2.0, 3: 8.0},
                  'rspo': {0: 30473.0, 1: 53711.0, 2: 118407.0, 3: 118407.0},
                  'teachers': {0: 10.0, 1: 81.0, 2: 4.0, 3: 16.0}}
expected_df3 = pd.DataFrame(expected_data3)

# ========================================
# test_del_zero()
# ========================================
data4 = {'voivo': {2939: 18, 47381: 14, 44632: 22},
         'county': {2939: 62, 47381: 62, 44632: 61},
         'district': {2939: 1, 47381: 1, 44632: 1},
         'district_type': {2939: 'M', 47381: 'M', 44632: 'M'},
         'school_type': {2939: 'Szkoła policealna',
                         47381: 'Niepubliczna placówka kształcenia ustawicznego i praktycznego',
                         44632: 'Niepubliczna placówka oświatowo-wychowawcza w systemie oświaty'},
         'students': {2939: 8, 47381: 2, 44632: 0},
         'sections': {2939: 2.0, 47381: 0.0, 44632: 0.0},
         'rspo': {2939: 6464.0, 47381: 262277.0, 44632: 129986.0},
         'teachers': {2939: 1.0, 47381: 0.0, 44632: 1.0}}
df4 = pd.DataFrame(data4)
expected_data4 = {'voivo': {2939: 18},
                  'county': {2939: 62},
                  'district': {2939: 1},
                  'district_type': {2939: 'M'},
                  'school_type': {2939: 'Szkoła policealna'},
                  'students': {2939: 8},
                  'sections': {2939: 2.0},
                  'rspo': {2939: 6464.0},
                  'teachers': {2939: 1.0}}
expected_df4 = pd.DataFrame(expected_data4)

# ========================================
# test_filter_key_types_of_schools()
# ========================================
data5 = {'voivo': {22492: 30, 11111: 12, 24803: 20, 30341: 2},
         'county': {22492: 17, 11111: 6, 24803: 10, 30341: 21},
         'district': {22492: 1, 11111: 15, 24803: 8, 30341: 8},
         'district_type': {22492: 'M', 11111: 'Gm', 24803: 'Gm', 30341: 'Gm'},
         'school_type': {22492: 'Szkoła policealna',
                         11111: 'Branżowa szkoła I stopnia',
                         24803: 'Punkt przedszkolny',
                         30341: 'Szkoła podstawowa'},
         'students': {22492: 69, 11111: 63, 24803: 25, 30341: 50},
         'sections': {22492: 5.0, 11111: 3.0, 24803: 1.0, 30341: 0.0},
         'rspo': {22492: 47504.0, 11111: 18158.0, 24803: 55069.0, 30341: 73121.0},
         'teachers': {22492: 14.0, 11111: 8.0, 24803: 2.0, 30341: 26.0}}
df5 = pd.DataFrame(data5)
expected_data5 = {'voivo': {30341: 2},
                  'county': {30341: 21},
                  'district': {30341: 8},
                  'district_type': {30341: 'Gm'},
                  'school_type': {30341: 'Szkoła podstawowa'},
                  'students': {30341: 50},
                  'sections': {30341: 0.0},
                  'rspo': {30341: 73121.0},
                  'teachers': {30341: 26.0}}
expected_df5 = pd.DataFrame(expected_data5)

# ========================================
# test_fix_school()
# ========================================
data6 = {'voivo': {18589: 14,
                   29240: 2,
                   32687: 28,
                   33422: 2,
                   48227: 2,
                   50281: 2,
                   54393: 28},
         'county': {18589: 15,
                    29240: 14,
                    32687: 8,
                    33422: 14,
                    48227: 14,
                    50281: 14,
                    54393: 8},
         'district': {18589: 3,
                      29240: 1,
                      32687: 1,
                      33422: 1,
                      48227: 1,
                      50281: 1,
                      54393: 1},
         'district_type': {18589: 'Gm',
                           29240: 'M',
                           32687: 'M',
                           33422: 'M',
                           48227: 'M',
                           50281: 'M',
                           54393: 'M'},
         'school_type': {18589: 'Szkoła podstawowa',
                         29240: 'Liceum ogólnokształcące',
                         32687: 'Liceum ogólnokształcące',
                         33422: 'Technikum',
                         48227: 'Branżowa szkoła I stopnia',
                         50281: 'Zespół szkół i placówek oświatowych',
                         54393: 'Zespół szkół i placówek oświatowych'},
         'students': {18589: 357,
                      29240: 92,
                      32687: 411,
                      33422: 457,
                      48227: 352,
                      50281: 0,
                      54393: 0},
         'sections': {18589: 18.0,
                      29240: 4.0,
                      32687: 17.0,
                      33422: 18.0,
                      48227: 13.0,
                      50281: 0.0,
                      54393: 0.0},
         'rspo': {18589: 87765.0,
                  29240: 7628.0,
                  32687: 28540.0,
                  33422: 7628.0,
                  48227: 7628.0,
                  50281: 7628.0,
                  54393: 28540.0},
         'teachers': {18589: 34,
                      29240: 0,
                      32687: 0,
                      33422: 0,
                      48227: 0,
                      50281: 66,
                      54393: 38}}
dict6 = {(28, 8, 1): "bla", (14, 5, 3): "blabla", (2, 14, 1): "blablabla"}
df6 = pd.DataFrame(data6)
expected_data6 = {'voivo': {0: 2, 1: 2, 3: 28},
                  'county': {0: 14, 1: 14, 3: 8},
                  'district': {0: 1, 1: 1, 3: 1},
                  'district_type': {0: 'M', 1: 'M', 3: 'M'},
                  'school_type': {0: 'Liceum ogólnokształcące',
                                  1: 'Technikum',
                                  3: 'Liceum ogólnokształcące'},
                  'students': {0: 92, 1: 457, 3: 411},
                  'sections': {0: 4.0, 1: 18.0, 3: 17.0},
                  'rspo': {0: 7628.0, 1: 7628.0, 3: 28540.0},
                  'teachers': {0: 7.0, 1: 33.0, 3: 38.0}}
expected_df6 = pd.DataFrame(expected_data6)
