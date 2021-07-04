import pandas as pd

data1 = {'voivo': {0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2},
         'county': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1},
         'district': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1},
         'district_type': {0: 'M', 1: 'M', 2: 'M', 3: 'M', 4: 'M', 5: 'M', 6: 'M'},
         'school_type': {0: 'Przedszkole',
                         1: 'Przedszkole',
                         2: 'Przedszkole',
                         3: 'Przedszkole',
                         4: 'Przedszkole',
                         5: 'Przedszkole',
                         6: 'Przedszkole'},
         'students': {0: 125, 1: 122, 2: 125, 3: 125, 4: 73, 5: 99, 6: 134},
         'sections': {0: 5, 1: 5, 2: 5, 3: 5, 4: 3, 5: 4, 6: 6},
         'rspo': {0: 34719,
                  1: 34720,
                  2: 34721,
                  3: 34723,
                  4: 34724,
                  5: 34725,
                  6: 40746},
         'teachers': {0: 14, 1: 10, 2: 13, 3: 11, 4: 8, 5: 8, 6: 20}}
expected_df1 = pd.DataFrame(data1)

data2 = {'qty': {5: 657.0,
                 6: 645.0,
                 7: 670.0,
                 8: 647.0,
                 9: 651.0,
                 10: 658.0,
                 11: 742.0,
                 12: 712.0,
                 13: 679.0,
                 14: 628.0,
                 15: 654.0,
                 16: 591.0,
                 17: 596.0,
                 18: 594.0,
                 19: 575.0,
                 20: 613.0,
                 21: 576.0,
                 35: 2930.0,
                 36: 3029.0,
                 37: 2977.0,
                 38: 2963.0,
                 39: 2980.0,
                 40: 3273.0,
                 41: 3482.0,
                 42: 3375.0,
                 43: 3292.0,
                 44: 2935.0,
                 45: 2828.0,
                 46: 2799.0,
                 47: 2747.0,
                 48: 2781.0,
                 49: 2920.0,
                 50: 2701.0,
                 51: 2829.0},
         'born': {5: 2015.0,
                  6: 2014.0,
                  7: 2013.0,
                  8: 2012.0,
                  9: 2011.0,
                  10: 2010.0,
                  11: 2009.0,
                  12: 2008.0,
                  13: 2007.0,
                  14: 2006.0,
                  15: 2005.0,
                  16: 2004.0,
                  17: 2003.0,
                  18: 2002.0,
                  19: 2001.0,
                  20: 2000.0,
                  21: 1999.0,
                  35: 2015.0,
                  36: 2014.0,
                  37: 2013.0,
                  38: 2012.0,
                  39: 2011.0,
                  40: 2010.0,
                  41: 2009.0,
                  42: 2008.0,
                  43: 2007.0,
                  44: 2006.0,
                  45: 2005.0,
                  46: 2004.0,
                  47: 2003.0,
                  48: 2002.0,
                  49: 2001.0,
                  50: 2000.0,
                  51: 1999.0},
         'voivo': {5: 2,
                   6: 2,
                   7: 2,
                   8: 2,
                   9: 2,
                   10: 2,
                   11: 2,
                   12: 2,
                   13: 2,
                   14: 2,
                   15: 2,
                   16: 2,
                   17: 2,
                   18: 2,
                   19: 2,
                   20: 2,
                   21: 2,
                   35: 4,
                   36: 4,
                   37: 4,
                   38: 4,
                   39: 4,
                   40: 4,
                   41: 4,
                   42: 4,
                   43: 4,
                   44: 4,
                   45: 4,
                   46: 4,
                   47: 4,
                   48: 4,
                   49: 4,
                   50: 4,
                   51: 4},
         'county': {5: 61,
                    6: 61,
                    7: 61,
                    8: 61,
                    9: 61,
                    10: 61,
                    11: 61,
                    12: 61,
                    13: 61,
                    14: 61,
                    15: 61,
                    16: 61,
                    17: 61,
                    18: 61,
                    19: 61,
                    20: 61,
                    21: 61,
                    35: 61,
                    36: 61,
                    37: 61,
                    38: 61,
                    39: 61,
                    40: 61,
                    41: 61,
                    42: 61,
                    43: 61,
                    44: 61,
                    45: 61,
                    46: 61,
                    47: 61,
                    48: 61,
                    49: 61,
                    50: 61,
                    51: 61},
         'district': {5: 1,
                      6: 1,
                      7: 1,
                      8: 1,
                      9: 1,
                      10: 1,
                      11: 1,
                      12: 1,
                      13: 1,
                      14: 1,
                      15: 1,
                      16: 1,
                      17: 1,
                      18: 1,
                      19: 1,
                      20: 1,
                      21: 1,
                      35: 1,
                      36: 1,
                      37: 1,
                      38: 1,
                      39: 1,
                      40: 1,
                      41: 1,
                      42: 1,
                      43: 1,
                      44: 1,
                      45: 1,
                      46: 1,
                      47: 1,
                      48: 1,
                      49: 1,
                      50: 1,
                      51: 1}}
expected_df2 = pd.DataFrame(data2)