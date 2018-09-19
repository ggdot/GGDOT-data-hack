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
# Currently not tested with ndnd_year != 6
def  mash_files  (ndns_dir,  tag,  kg_CO2e_per_kWh = 0.6, ndns_year = 6) :


    from  read_foods  import  read_foods
    foods  =  read_foods (ndns_dir + 'ndns_yr6_nutrientdatabank.tab')

    #from  add_in_ghgs  import  add_in_ghgs
    #foods  =  add_in_ghgs  (foods,  './clune.tab',  kg_CO2e_per_kWh)

    from  add_in_ghgs_list  import  add_in_ghgs_list
    foods  =  add_in_ghgs_list  (foods,
                                 './Intake24_based_GHGs_20180611.csv',
                                 kg_CO2e_per_kWh)

    #foods  =  add_in_ghgs_list  (foods,
    #                             './simple_LCA_based_GHGs_20180611.csv',
    #                             kg_CO2e_per_kWh)


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
                      ndns_year),  # Currently not tested with ndns_year != 6
                  foods,
                  conditions)


    from  cut_rescale  import  cut_rescale
    (eaten, n_person_day)  =  cut_rescale  (eaten, conditions)


    from  make_aisle_table  import  make_aisle_table
    aisle  =  make_aisle_table  (eaten,  n_person_day)


    import csv

    def  write_table_pair  (base_name, table):

        with  open ('./' + base_name + tag + '.csv', 'w')  as  output:
            writer  =  csv.DictWriter (output,
                                       fieldnames=table ['table'] [0].keys (),
                                       extrasaction='ignore',
                                       quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader ()
            writer.writerows (table ['table'])

        with  open ('./' + base_name + '_column_info' + tag + '.csv',
                    'w')  as  output:
            f  =  list (table.keys ())
            f.remove ('table')
            writer  =  csv.DictWriter (output,
                                       fieldnames=['Names'] + f,
                                       extrasaction='ignore',
                                       quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader ()
            for  col  in  table ['descriptions']:
                row = {'Names': col}
                for  b  in  f:
                    row [b]  = table [b].get (col, float ('nan'))
                writer.writerow (row)


    write_table_pair ('eaten_table', eaten)
    write_table_pair ('foods_table', foods)
    write_table_pair ('eaten_table_aisle', aisle)



if __name__ == '__main__':
    mash_files  (ndns_dir  =  '[path/to...]/UKDA-6533-tab/tab/',
                 tag  =  '_[your_tag]')
