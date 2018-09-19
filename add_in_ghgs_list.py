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


def  add_in_ghgs_list  (foods,  ghgs_file = './simple_LCA_based_GHGs_20180611.csv', kg_CO2e_per_kWh = 0.6):

    # import csv
    #ghgs_file = './simple_LCA_based_GHGs_20180611.csv'

    with  open (ghgs_file)  as  input:
        ghgs  =  list (csv.DictReader (input))

    print ('Read in ' + str(len(ghgs)) + ' lines of ' + ghgs_file +' (expected 5687).')

    # Now append the ghgs info to foods 

    # Extract the fieldnames from line 1 - in case there are lines without all the fieldnames - ideally use a python table to avoid this possibility?
    foods_line = foods['table'][1]
    foods_fieldnames = list(foods_line.keys())

    # Ditto for the GHGs file - but this time just keep the new ones for concatenation (check the redundant ones separately)
    ghgs_line = ghgs[1]
    ghgs_fieldnames = list(ghgs_line.keys())
    ghgs_fieldnames.remove('FoodNumber')
    ghgs_fieldnames.remove('FoodName')

    # initialise the 'table' with anything for now - overwrite this later
    new_foods = dict()
    new_foods['table'] = foods['table']
    # Overwrite the table lines one by one later - the above is just to initialise something the right kind of shape - I couldn't see how else to do it (SLB)
    new_foods['descriptions'] = foods['descriptions'] 
    new_foods['short_colnames'] = foods['short_colnames'] 

    # Now go through all the lines in the foods list and add the extra fields from the ghgs file
    empty_field_counter = 0
    n_food = len(foods['table'])
    First = True
    for i_food in range(n_food):
        foods_line = foods['table'][i_food] 

        # Check the FoodName matches between the two files
        # Ideally also check the FoodNumber here!
        ghgs_line = ghgs[i_food]
        # Don't worry if some of the quotes are different
        foods_FoodName = foods_line['FoodName'].replace('"','')
        ghgs_FoodName = ghgs_line['FoodName'].replace('"','')
        if (foods_FoodName != ghgs_FoodName):
            print ("Error matching GHGs to NDNS foods!!! foods_FoodName = " + foods_FoodName + "ghgs_FoodName = " + ghgs_FoodName)

        #print ('i_food = ', str(i_food) + '; FoodName = ' + foods_FoodName)

        # Create the concatenated line
        new_line = dict()
        for foods_fieldname in foods_fieldnames:
            value = foods_line.get(foods_fieldname)
            if (value is None):
                empty_field_counter += 1
                # NB this is necessary as there are some missing - not sure why!
                #?? ideally write something the same type as the rest of this fieldname... bytes = output.write(NaN)
                new_line[foods_fieldname] = -666
            else:
                new_line[foods_fieldname] = value
        #for ghgs_fieldname in ghgs_fieldnames:
        #    value = ghgs_line.get(ghgs_fieldname)
        #    new_line[ghgs_fieldname] = value
        # Not sure why I have to change this into a float here - SLB
        new_line['CO2e'] = float(ghgs_line.get('CO2e'))
        new_line['CO2eRef'] = ghgs_line.get('CO2eRef')

        new_foods['table'][i_food] = new_line


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
        new_foods ['table'].append (a)


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


    return  new_foods
