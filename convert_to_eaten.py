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


import  sys

def  convert_to_eaten  (eaten, foods, conditions):

    ret = {}

    eaten_fields = ['SurveyYear', 'Age', 'Sex', 'Country', 'DayofWeek',
                    'DayNo',  'DiaryDaysCompleted', 'MealTimeDescription',
                    'MealTime', 'MainFoodGroupCode', 'MainFoodGroupDesc',
                    'SubFoodGroupCode', 'SubFoodGroupDesc',
                    'RecipeMainFoodGroupCode', 'RecipeMainFoodGroupDesc', 
                    'RecipeSubFoodGroupCode', 'RecipeSubFoodGroupDesc',
                    'WhoWith', 'WhoWithOther', 'Where', 'WhereOther',
                    'WatchingTV', 'Table', 'diarymth', 'seriali']

    information_fields = ['FoodNumber', 'FoodGroupCode', 'FoodName',
                          'FoodCategory', 'Description', 'Dilution',
                          'Comment', 'EdiblePortion', 'CO2eRef',
                          'FoodAisle']
    #                      'FoodDescriptions', 'CO2eRatio','FoodAisle']

    from  quantity_fields  import  quantity_fields

    ret ['table'] = []
    count = 0
    top = str (int (len (eaten ['table']) / 1000))

    for  e  in  eaten ['table']:

        count = count + 1
        if  count % 1000 == 0:
            sys.stdout.write (str (int (count/1000)) + ' / ' + top
                                                         + '         \r')
            sys.stdout.flush ()

        if  (float (e ['Age']) >= conditions ['age_mineq']
                and   float (e ['Age']) <= conditions ['age_maxeq']
                and   float (e ['MealTime']) >= conditions ['meal_time_mineq']
                and   float (e ['MealTime']) < conditions ['meal_time_max']):

            number  =  int (e ['FoodNumber'])
            total_grams  =  float (e ['TotalGrams'])

            for  f  in  foods ['table']:
                if  int (f ['FoodNumber']) == number:
                    a  =  {}
                    for  f_  in  eaten_fields:
                        a [f_] = e [f_]
                    for  f_  in  information_fields:
                        a [f_] = f [f_]
                    for  q  in  quantity_fields:
                        if  q  in  f   and   f [q] != ' ':
                            a [q] = (float (total_grams) / float (f ['Base'])
                                        * float (f [q]))
                    a ['Base']  =  total_grams
                    a ['Units'] =  f ['Units']

                    ret ['table'].append (a)

    for  x  in  foods:
        if  x  !=  'table':
            ret [x] = {}

    for  f  in  information_fields + quantity_fields:
        for  x  in  foods:
            if  x  !=  'table':
                if  f  in  foods [x]:
                    ret [x] [f]  =  foods [x] [f]

    ret ['descriptions'] ['Units']  =  'Units'
    ret ['short_colnames'] ['Units']  =  'Units'
    ret ['descriptions'] ['Base']  =  'Quantity'
    ret ['short_colnames'] ['Base']  =  'Quantity'

    return ret
