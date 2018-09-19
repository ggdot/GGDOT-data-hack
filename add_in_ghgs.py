#  MIT License
#
#  Copyright (c) 2018 ggdot
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


import csv
import copy


from  add_in_ghgs__data  import  data_1, data_2, data_3


def  add_in_ghgs  (foods,  clune_file,  kg_CO2e_per_kWh):

    # I had to remove the stray newline after ``Agri-Food Sector (LCA Food
    # 2010). Bari, Italy.''.  Ditto stray newline after ``Swedish plates?
    # Climate change emissions'' in 2 places and fix 8,93 to 8.93 ditto
    # 2,88 and 7,62 !!! fix the warning.
    #
    # Also removed thousands of empty rows and columns outside the data
    # matrix.
    #
    # Finally, the filename was changed to clune.tab.

    with  open (clune_file, encoding='ISO-8859-1')  as  input:
        ghgs  =  list (csv.DictReader (input, dialect='excel-tab'))

    print ('Read in ' + str(len(ghgs)) + ' lines of clune.tab (expected 1731).')

    for  a  in  ghgs:
        a ['CO2e']  =  a.pop ('kg CO2-eq/kg produce, BFM or L after conversion')
        a ['Notes'] =  a.pop (
                           'Notes (conventional farming assumed unless stated)')



    def  clune_average (clune_string, ghgs):
        a  =  0
        c  =  0
        for  g  in  ghgs:
            if  g ['Food type'].strip()  ==  clune_string:
                if  g['CO2e'] != ' '  and  g['CO2e'] != '':
                    a  +=  float (g ['CO2e'])
                    c  +=  1
        return  0  if  a == 0  else  a / c



    def  set_foods_table_from_clune  (food_group_codes,
                                      food_description, clune_string,
                                      factor, group_index):

        co2e_ratio  =  clune_average (clune_string, ghgs)

        for  a  in  foods ['table']:
            if  a ['FoodGroupCode'] in food_group_codes:
                a ['CO2eRatio']  =  co2e_ratio * factor
                a ['CO2eGroup']  =  group_index
                a ['FoodDescriptions']  =  food_description
                a ['CO2eRef']  =  ('Average of CO2e values for ' + clune_string
                                   +  ' from Clune et al 2017, multiplied by '
                                   +  str (factor))

    index = 0

    for  a  in  data_1:

        index = index + 1
        set_foods_table_from_clune  (a [0], a[1], a[2], a[3], index)


    def  set_foods_table_value  (food_group_codes, description,
                                 CO2eRatio, CO2eRef, group):
            
        for  f  in  foods ['table']:
            if  f ['FoodGroupCode']  in  food_group_codes:
                f ['FoodDescriptions'] =  description
                f ['CO2eRatio']        =  CO2eRatio
                f ['CO2eGroup']        =  group
                f ['CO2eRef']          =  CO2eRef


    for  a  in  data_3:
        index = index + 1
        set_foods_table_value  (a [0], a [1], a [2], a [3], index)
                  

    avg  =  clune_average  ('Butter', ghgs)
    ref  =  'Average of CO2e values for Butter from From Clune et al 2017'

    for  a  in  foods ['table']:
        if  a ['FoodName']  in  ['BUTTER SALTED',
                                 'SPREADABLE BUTTER (75-80% FAT)',
                                 'BUTTER UNSALTED',
                                 'LIGHT SPREADABLE BUTTER (60% FAT)',
                                 'SPREADABLE BUTTER (75-80% FAT) UNSALTED',
                                 'LIGHTEST SPREADABLE BUTTER (40% FAT)',
                                 'HALF FAT BUTTER, SALTED, WITH VITAMIN A AND D']:
            a ['FoodDescriptions']  =  'Butter'
            a ['CO2eRatio']  =  avg
            a ['CO2eRef']  =  ref

        elif  a ['FoodName']  ==  'HAM UNSPECIFIED NOT SMOKED NOT CANNED':
            a ['FoodDescriptions']  =  'Ham'
            a ['CO2eRatio']  =  float (a ['CO2eRatio']) + 2
            a ['CO2eRef']  =  'Same as pork but adding an extra 2 to account for processing, based on scaling <Consideration of the product quality in the life cycle assessment: case of a meat product treated by high pressure http://lcafood2014.org/papers/15.pdf>'

        elif  a ['FoodName']  ==  'BLACK PUDDING FRIED':
            a ['FoodDescriptions']  =  'Black pudding'
            a ['CO2eRatio']  =  1
            a ['CO2eRef']  =  'A guess assuming blood is free but there is some processing'


    for  a  in  data_2:
        foods ['table'] [a[0]-1] ['FoodDescriptions'] = a[1]
        foods ['table'] [a[0]-1] ['CO2eRatio'] = a[2]
        foods ['table'] [a[0]-1] ['CO2eRef'] = a[3]

    foods ['table'] [5389-1] ['FoodDescriptions']  =  'Vitamin B12 (1000mcg)'
    foods ['table'] [5389-1] ['CO2eRatio']  =  0

    for  a  in  foods ['table']:
        a ['CO2e']  =  float (a ['CO2eRatio'])  *  float (a ['Base'])


    def  add_partial_row  (entries):
        a  =  copy.deepcopy  (foods ['table'] [0])
        for  b  in  a:
            try:
                a [b] = float (a [b])
                a [b] = 0.0
            except ValueError:
                a [b] = 'dummy'
        for  e  in  entries:
            a [e]  =  entries [e]
        foods ['table'].append (a)


    add_partial_row  ({'FoodName':'2 kW of electricity',
                       'Base':60,
                       'Units':'Minutes',
                       'CO2e':2000 * kg_CO2e_per_kWh})

    add_partial_row  ({'FoodName':'Steel',
                       'Base':1,
                       'Units':'Grams',
                       'CO2e':5})

    add_partial_row  ({'FoodName':'PET',
                       'Base':1,
                       'Units':'Grams',
                       'CO2e':3.4})

    return  foods
