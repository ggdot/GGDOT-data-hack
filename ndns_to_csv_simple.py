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


                                                #  0.6 from SEWTHA.
def  mash_files  (ndns_dir,  tag,  kg_CO2e_per_kWh = 0.6) :

    #ndns_dir  =  '/Users/mbesssb5/Dropbox/scratch/food/NDNS/UKDA-6533-tab/tab/'
    #tag  =  '_20180607_1923'
    #kg_CO2e_per_kWh = 0.6

    from  read_foods  import  read_foods
    foods  =  read_foods (ndns_dir + 'ndns_yr6_nutrientdatabank.tab')
    # NB Year 6 is currently hard-coded - want to fix this 


    #from  add_in_ghgs  import  add_in_ghgs
    #foods  =  add_in_ghgs  (foods,  './clune.tab',  kg_CO2e_per_kWh)
    from  add_in_ghgs_list  import  add_in_ghgs_list
    foods  =  add_in_ghgs_list  (foods,  './Intake24_based_GHGs_20180611.csv',  kg_CO2e_per_kWh)
    #foods  =  add_in_ghgs_list  (foods,  './simple_LCA_based_GHGs_20180611.csv',  kg_CO2e_per_kWh)


    from  define_food_aisles__data  import  food_aisles_data
    for  (aisle, codes)  in  food_aisles_data:
        for  f  in  foods['table']:
            if  f ['FoodGroupCode'] in codes:
                f ['FoodAisle']  =  aisle


    from  set_nutrient_RDAs__data  import  nutrient_RDAs_data
    for  attr  in  ['rda_m', 'rda_f', 'rda_m_7_10', 'rda_f_7_10',
                    'ul_m', 'ul_f']:
        foods [attr] = {}
        for  (column, rda)  in  nutrient_RDAs_data:
            if  attr  in  rda:
                foods [attr] [column]  =  rda [attr]


    conditions  =  {'age_mineq'       : 19,
                    'age_maxeq'       : 64,
                    'meal_time_mineq' : 0,
                    'meal_time_max'   : 24,
                    'kcals_min'       : 1000,
                    'kcals_rescale'   : 2500}


    from  read_ndns_eaten   import  read_ndns_eaten
    from  convert_to_eaten  import  convert_to_eaten
    eaten  =  convert_to_eaten  (
                  read_ndns_eaten (
                      ndns_dir + 'ndns_rp_yr5-6a_foodleveldietarydata.tab',
                      6),    #  !! Year 6 hard-wired - note other filenames correspond to this number!!!
                  foods,
                  conditions)


    from  cut_rescale  import  cut_rescale
    (eaten, n_person_day)  =  cut_rescale  (eaten, conditions)


    from  make_aisle_table  import  make_aisle_table
    aisle  =  make_aisle_table  (eaten,  n_person_day)


    def write_table_pair (base_name, table):

        # Write the table itself (with header row)
        output = open('./' + base_name + tag + '.csv', 'w') 

        # Write the header
        first = True
        line = table['table'][1]
        fieldnames = line.keys()
        for fieldname in fieldnames:
            if first:
                first = False
            else: 
                bytes = output.write(', ') 
            bytes = output.write(fieldname.replace(',', '.'))

        bytes = output.write('\n')

        # Write the table contents
        empty_field_counter = 0
        for line in table['table']:
            first = True
            for fieldname in fieldnames:
                if first:
                    first = False
                else: 
                    bytes = output.write(', ') 
                value = line.get(fieldname)
                if (value is None):
                    empty_field_counter += 1
                    #?? ideally write something the same type as the rest of this fieldname... bytes = output.write(NaN)
                else:
                    if isinstance(value, str):
                        bytes = output.write('"%s"' % value.replace(',', '.'))
                    else:
                        # Assume its a float if its not a string - could do better here!
                        bytes = output.write('%10.7g' % value)
            bytes = output.write('\n')

        output.close() 


        # Write the other info per column into another file 
        output = open('./' + base_name + '_column_info' + tag + '.csv', 'w') 

        # Write the header 
        fieldnames = list(table.keys())
        fieldnames.remove ('table')
        fieldnames = ['Names'] + fieldnames
        first = True
        for fieldname in fieldnames:
            if first:
                first = False
            else: 
                bytes = output.write(', ') 
            bytes = output.write(fieldname.replace(',', '.'))

        bytes = output.write('\n')

        # Write the table contents
        fieldnames = list(table.keys())
        fieldnames.remove ('table')
        for col in table ['descriptions']:
            bytes = output.write('"%s"' % col)
            for  fieldname in  fieldnames:
                bytes = output.write(', ') 
                value = table [fieldname].get (col, 'dummy')
                if (value is None):
                    empty_field_counter += 1
                else:
                    if isinstance(value, str):
                        output.write('"%s"' % value.replace(',', '.'))
                    else:
                        bytes = output.write('%10.7g' % value)
            bytes = output.write('\n')

        output.close() 

    write_table_pair ('eaten_table', eaten)
    write_table_pair ('foods_table', foods)
    write_table_pair ('eaten_table_aisle', aisle)


if __name__ == '__main__':
    mash_files  (ndns_dir  =  '[path/to...]/UKDA-6533-tab/tab/',
                 tag  =  '_[your_tag]')
