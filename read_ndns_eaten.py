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


import  csv


def  read_ndns_eaten  (file_name, year):

    with  open (file_name, encoding='ISO-8859-1')  as  input:
        eaten  =  list (csv.DictReader (input, dialect='excel-tab'))

    day = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
    for  a  in  range (0, len (days)):
        day [days [a]]  =  a+1   

    tv  = {'Yes': 1, 'No': 0, 'Not Specified': -1}
    nan = float('nan')

    return_table   =  [];

    for  a  in  eaten:
        y  =  int (a ['SurveyYear'] [len (a ['SurveyYear']) - 1:])
        if  y == year:
            a ['SurveyYear']  =  y
            m  =  a ['MealTime']
            m1 = m.find (':')
            m2 = m.find (':', m1+1)
            a ['MealTime']    =  (int (m [0:m1]) + int (m [m1+1:m2]) / 60
                                      + int (m [m2+1:]) / 3600)
            a ['DayofWeek']   =  day [a ['DayofWeek']]
            # a ['WatchingTV']  =  tv.get (a ['WatchingTV'], nan)
            # a ['Table']       =  tv.get (a ['Table'], nan)
            return_table.append (a)
    
    return  {'table':          return_table,
             'descriptions':   {key: key   for   key in return_table [0]},
             'short_colnames': {key: key   for   key in return_table [0]}}
