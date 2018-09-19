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


def   make_aisle_table  (eaten,  n_person_day):

    from  quantity_fields  import  quantity_fields

    information_fields  =  ['Units', 'FoodAisle' ]

    ret = {}
    ret ['table'] = []
    ret ['descriptions'] = {}
    ret ['short_colnames'] = {}

    aisle = {}

    for  e  in  eaten ['table']:

        aisle.setdefault (e['FoodAisle'], {})

        for  i  in  information_fields:
            aisle [e['FoodAisle']].setdefault (i, (e[i], 0, 0))

        for  q  in quantity_fields:
            if  q  in e:
                aisle [e['FoodAisle']].setdefault (q, (0, 0, 0))
                if  e[q] != float('nan'):
                    aisle [e['FoodAisle']] [q]  =  (
                                 aisle [e['FoodAisle']] [q] [0] + e[q],
                                 aisle [e['FoodAisle']] [q] [1] + 1,
                                 aisle [e['FoodAisle']] [q] [2] + 1)
                else:
                    aisle [e['FoodAisle']] [q]  =  (
                           aisle [e['FoodAisle']] [q] [0],
                           aisle [e['FoodAisle']] [q] [1] + 1,
                           aisle [e['FoodAisle']] [q] [2])

    for  a  in  aisle:
        row = {}
        for  f  in  aisle [a]:
            if  f  in  quantity_fields:
                row [f] = (aisle [a] [f] [0]
                              / (n_person_day * aisle [a] [f] [2]
                                    / aisle [a] [f] [1]))
            else:
                row [f] = aisle [a] [f] [0]
        ret ['table'].append (row)

    for  i  in  aisle [list (aisle.keys ()) [0]]:
        ret ['descriptions'] [i]  =  eaten ['descriptions'] [i]
        ret ['short_colnames'] [i]  =  eaten ['short_colnames'] [i]

    return ret
