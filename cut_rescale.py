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


def  cut_rescale  (eaten, conditions):

    from  quantity_fields  import  quantity_fields

    eaten ['descriptions'] ['KCALS_personday'] = (
                       'The total kcals this person (seriali) ate on this DayNo, '
                              +  'before any rescaling.')

    eaten ['short_colnames'] ['KCALS_personday'] = 'kcal_day'

    kcals_per_day  =  {}

    for  e  in  eaten ['table']:
        kcals_per_day.setdefault ((e['seriali'], e['DayNo']), 0)
        kcals_per_day [(e['seriali'], e['DayNo'])]  +=  e['KCALS']

    new_e  =  []
    for  e  in  eaten ['table']:
        kcals  =  kcals_per_day [(e['seriali'], e['DayNo'])]
        if  kcals  >  conditions ['kcals_min']:
            e['KCALS_personday']  =  kcals
            rescale  =  conditions ['kcals_rescale'] / kcals
            for  a  in  quantity_fields:
                if  a  in  e:
                    e [a]  =  rescale  *  float (e [a])
            new_e.append (e)
    eaten ['table'] = new_e
    
    return  (eaten, len (kcals_per_day))
