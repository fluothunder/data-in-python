import pandas as pd
import numpy as np

# ========================================
# test_create_dict_of_districts():
# ========================================

data1 = {'qty': {5: 657,
                 6: 645,
                 7: 670,
                 8: 647,
                 9: 651,
                 10: 658,
                 11: 742,
                 12: 712,
                 13: 679,
                 14: 628,
                 15: 654,
                 16: 591,
                 17: 596,
                 18: 594,
                 19: 575,
                 20: 613,
                 21: 576,
                 35: 968,
                 36: 844,
                 37: 866,
                 38: 896,
                 39: 944,
                 40: 952,
                 41: 1001,
                 42: 995,
                 43: 988,
                 44: 869,
                 45: 818,
                 46: 800,
                 47: 787,
                 48: 838,
                 49: 834,
                 50: 865,
                 51: 881},
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
                   35: 2,
                   36: 2,
                   37: 2,
                   38: 2,
                   39: 2,
                   40: 2,
                   41: 2,
                   42: 2,
                   43: 2,
                   44: 2,
                   45: 2,
                   46: 2,
                   47: 2,
                   48: 2,
                   49: 2,
                   50: 2,
                   51: 2},
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
                    35: 62,
                    36: 62,
                    37: 62,
                    38: 62,
                    39: 62,
                    40: 62,
                    41: 62,
                    42: 62,
                    43: 62,
                    44: 62,
                    45: 62,
                    46: 62,
                    47: 62,
                    48: 62,
                    49: 62,
                    50: 62,
                    51: 62},
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
df1 = pd.DataFrame(data1)
expected_data11 = {'qty': {2015.0: 657,
                           2014.0: 645,
                           2013.0: 670,
                           2012.0: 647,
                           2011.0: 651,
                           2010.0: 658,
                           2009.0: 742,
                           2008.0: 712,
                           2007.0: 679,
                           2006.0: 628,
                           2005.0: 654,
                           2004.0: 591,
                           2003.0: 596,
                           2002.0: 594,
                           2001.0: 575,
                           2000.0: 613,
                           1999.0: 576},
                   'voivo': {2015.0: 2,
                             2014.0: 2,
                             2013.0: 2,
                             2012.0: 2,
                             2011.0: 2,
                             2010.0: 2,
                             2009.0: 2,
                             2008.0: 2,
                             2007.0: 2,
                             2006.0: 2,
                             2005.0: 2,
                             2004.0: 2,
                             2003.0: 2,
                             2002.0: 2,
                             2001.0: 2,
                             2000.0: 2,
                             1999.0: 2},
                   'county': {2015.0: 61,
                              2014.0: 61,
                              2013.0: 61,
                              2012.0: 61,
                              2011.0: 61,
                              2010.0: 61,
                              2009.0: 61,
                              2008.0: 61,
                              2007.0: 61,
                              2006.0: 61,
                              2005.0: 61,
                              2004.0: 61,
                              2003.0: 61,
                              2002.0: 61,
                              2001.0: 61,
                              2000.0: 61,
                              1999.0: 61},
                   'district': {2015.0: 1,
                                2014.0: 1,
                                2013.0: 1,
                                2012.0: 1,
                                2011.0: 1,
                                2010.0: 1,
                                2009.0: 1,
                                2008.0: 1,
                                2007.0: 1,
                                2006.0: 1,
                                2005.0: 1,
                                2004.0: 1,
                                2003.0: 1,
                                2002.0: 1,
                                2001.0: 1,
                                2000.0: 1,
                                1999.0: 1},
                   'Szkoła podstawowa': {2015.0: np.nan,
                                         2014.0: np.nan,
                                         2013.0: np.nan,
                                         2012.0: np.nan,
                                         2011.0: 0.12248353715898401,
                                         2010.0: 0.12380056444026341,
                                         2009.0: 0.1396048918156162,
                                         2008.0: 0.13396048918156162,
                                         2007.0: 0.1277516462841016,
                                         2006.0: 0.11815616180620885,
                                         2005.0: 0.12304797742238946,
                                         2004.0: 0.11119473189087488,
                                         2003.0: np.nan,
                                         2002.0: np.nan,
                                         2001.0: np.nan,
                                         2000.0: np.nan,
                                         1999.0: np.nan},
                   'Przedszkole': {2015.0: 0.2508591065292096,
                                   2014.0: 0.24627720504009165,
                                   2013.0: 0.25582283314242077,
                                   2012.0: 0.24704085528827796,
                                   2011.0: np.nan,
                                   2010.0: np.nan,
                                   2009.0: np.nan,
                                   2008.0: np.nan,
                                   2007.0: np.nan,
                                   2006.0: np.nan,
                                   2005.0: np.nan,
                                   2004.0: np.nan,
                                   2003.0: np.nan,
                                   2002.0: np.nan,
                                   2001.0: np.nan,
                                   2000.0: np.nan,
                                   1999.0: np.nan},
                   'Liceum ogólnokształcące': {2015.0: np.nan,
                                               2014.0: np.nan,
                                               2013.0: np.nan,
                                               2012.0: np.nan,
                                               2011.0: np.nan,
                                               2010.0: np.nan,
                                               2009.0: np.nan,
                                               2008.0: np.nan,
                                               2007.0: np.nan,
                                               2006.0: np.nan,
                                               2005.0: np.nan,
                                               2004.0: np.nan,
                                               2003.0: np.nan,
                                               2002.0: 0.3333333333333333,
                                               2001.0: 0.3226711560044893,
                                               2000.0: 0.3439955106621773,
                                               1999.0: np.nan},
                   'Technikum': {2015.0: np.nan,
                                 2014.0: np.nan,
                                 2013.0: np.nan,
                                 2012.0: np.nan,
                                 2011.0: np.nan,
                                 2010.0: np.nan,
                                 2009.0: np.nan,
                                 2008.0: np.nan,
                                 2007.0: np.nan,
                                 2006.0: np.nan,
                                 2005.0: np.nan,
                                 2004.0: np.nan,
                                 2003.0: np.nan,
                                 2002.0: 0.25190839694656486,
                                 2001.0: 0.24385072094995758,
                                 2000.0: 0.2599660729431722,
                                 1999.0: 0.24427480916030533},
                   'Gimnazjum': {2015.0: np.nan,
                                 2014.0: np.nan,
                                 2013.0: np.nan,
                                 2012.0: np.nan,
                                 2011.0: np.nan,
                                 2010.0: np.nan,
                                 2009.0: np.nan,
                                 2008.0: np.nan,
                                 2007.0: np.nan,
                                 2006.0: np.nan,
                                 2005.0: np.nan,
                                 2004.0: np.nan,
                                 2003.0: 1.0,
                                 2002.0: np.nan,
                                 2001.0: np.nan,
                                 2000.0: np.nan,
                                 1999.0: np.nan}}
expected_data12 = {'qty': {2015.0: 968,
                           2014.0: 844,
                           2013.0: 866,
                           2012.0: 896,
                           2011.0: 944,
                           2010.0: 952,
                           2009.0: 1001,
                           2008.0: 995,
                           2007.0: 988,
                           2006.0: 869,
                           2005.0: 818,
                           2004.0: 800,
                           2003.0: 787,
                           2002.0: 838,
                           2001.0: 834,
                           2000.0: 865,
                           1999.0: 881},
                   'voivo': {2015.0: 2,
                             2014.0: 2,
                             2013.0: 2,
                             2012.0: 2,
                             2011.0: 2,
                             2010.0: 2,
                             2009.0: 2,
                             2008.0: 2,
                             2007.0: 2,
                             2006.0: 2,
                             2005.0: 2,
                             2004.0: 2,
                             2003.0: 2,
                             2002.0: 2,
                             2001.0: 2,
                             2000.0: 2,
                             1999.0: 2},
                   'county': {2015.0: 62,
                              2014.0: 62,
                              2013.0: 62,
                              2012.0: 62,
                              2011.0: 62,
                              2010.0: 62,
                              2009.0: 62,
                              2008.0: 62,
                              2007.0: 62,
                              2006.0: 62,
                              2005.0: 62,
                              2004.0: 62,
                              2003.0: 62,
                              2002.0: 62,
                              2001.0: 62,
                              2000.0: 62,
                              1999.0: 62},
                   'district': {2015.0: 1,
                                2014.0: 1,
                                2013.0: 1,
                                2012.0: 1,
                                2011.0: 1,
                                2010.0: 1,
                                2009.0: 1,
                                2008.0: 1,
                                2007.0: 1,
                                2006.0: 1,
                                2005.0: 1,
                                2004.0: 1,
                                2003.0: 1,
                                2002.0: 1,
                                2001.0: 1,
                                2000.0: 1,
                                1999.0: 1},
                   'Szkoła podstawowa': {2015.0: np.nan,
                                         2014.0: np.nan,
                                         2013.0: np.nan,
                                         2012.0: np.nan,
                                         2011.0: 0.12813899823537397,
                                         2010.0: 0.12922492194923307,
                                         2009.0: 0.13587620469662007,
                                         2008.0: 0.13506176191122574,
                                         2007.0: 0.13411157866159903,
                                         2006.0: 0.11795846341794489,
                                         2005.0: 0.11103569974209312,
                                         2004.0: 0.10859237138591014,
                                         2003.0: np.nan,
                                         2002.0: np.nan,
                                         2001.0: np.nan,
                                         2000.0: np.nan,
                                         1999.0: np.nan},
                   'Przedszkole': {2015.0: 0.27084499160604364,
                                   2014.0: 0.23614997202014548,
                                   2013.0: 0.24230554001119195,
                                   2012.0: 0.2506994963626189,
                                   2011.0: np.nan,
                                   2010.0: np.nan,
                                   2009.0: np.nan,
                                   2008.0: np.nan,
                                   2007.0: np.nan,
                                   2006.0: np.nan,
                                   2005.0: np.nan,
                                   2004.0: np.nan,
                                   2003.0: np.nan,
                                   2002.0: np.nan,
                                   2001.0: np.nan,
                                   2000.0: np.nan,
                                   1999.0: np.nan},
                   'Liceum ogólnokształcące': {2015.0: np.nan,
                                               2014.0: np.nan,
                                               2013.0: np.nan,
                                               2012.0: np.nan,
                                               2011.0: np.nan,
                                               2010.0: np.nan,
                                               2009.0: np.nan,
                                               2008.0: np.nan,
                                               2007.0: np.nan,
                                               2006.0: np.nan,
                                               2005.0: np.nan,
                                               2004.0: np.nan,
                                               2003.0: np.nan,
                                               2002.0: 0.3303113914071738,
                                               2001.0: 0.32873472605439497,
                                               2000.0: 0.34095388253843123,
                                               1999.0: np.nan},
                   'Technikum': {2015.0: np.nan,
                                 2014.0: np.nan,
                                 2013.0: np.nan,
                                 2012.0: np.nan,
                                 2011.0: np.nan,
                                 2010.0: np.nan,
                                 2009.0: np.nan,
                                 2008.0: np.nan,
                                 2007.0: np.nan,
                                 2006.0: np.nan,
                                 2005.0: np.nan,
                                 2004.0: np.nan,
                                 2003.0: np.nan,
                                 2002.0: 0.2451726155646577,
                                 2001.0: 0.24400234055002926,
                                 2000.0: 0.25307197191339964,
                                 1999.0: 0.2577530719719134},
                   'Gimnazjum': {2015.0: np.nan,
                                 2014.0: np.nan,
                                 2013.0: np.nan,
                                 2012.0: np.nan,
                                 2011.0: np.nan,
                                 2010.0: np.nan,
                                 2009.0: np.nan,
                                 2008.0: np.nan,
                                 2007.0: np.nan,
                                 2006.0: np.nan,
                                 2005.0: np.nan,
                                 2004.0: np.nan,
                                 2003.0: 1.0,
                                 2002.0: np.nan,
                                 2001.0: np.nan,
                                 2000.0: np.nan,
                                 1999.0: np.nan}}
df11 = pd.DataFrame(expected_data11).rename_axis(None, axis=1).rename_axis('born', axis=0)
df12 = pd.DataFrame(expected_data12).rename_axis(None, axis=1).rename_axis('born', axis=0)
expected_dict1 = {(2, 61, 1): df11, (2, 62, 1): df12}

# ========================================
# test_compute_ratio()
# ========================================

data2 = {'voivo': {5152: 24, 4846: 14},
         'county': {5152: 69, 4846: 5},
         'district': {5152: 1, 4846: 5},
         'district_type': {5152: 'M', 4846: 'Gm'},
         'school_type': {5152: 'Przedszkole', 4846: 'Gimnazjum'},
         'students': {5152: 67, 4846: 60},
         'sections': {5152: 3.0, 4846: 3.0},
         'rspo': {5152: 9505.0, 4846: 9035.0},
         'teachers': {5152: 13.0, 4846: 6.0}}
df2 = pd.DataFrame(data2)
expected_data2 = {'voivo': {5152: 24, 4846: 14},
                  'county': {5152: 69, 4846: 5},
                  'district': {5152: 1, 4846: 5},
                  'district_type': {5152: 'M', 4846: 'Gm'},
                  'school_type': {5152: 'Przedszkole', 4846: 'Gimnazjum'},
                  'students': {5152: 67, 4846: 60},
                  'sections': {5152: 3.0, 4846: 3.0},
                  'rspo': {5152: 9505.0, 4846: 9035.0},
                  'teachers': {5152: 13.0, 4846: 6.0},
                  'ratio_students_per_teacher': {5152: 5.153846153846154, 4846: 10.0}}
expected_df2 = pd.DataFrame(expected_data2)