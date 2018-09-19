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


def  read_foods (file_name):

    with  open (file_name, encoding='ISO-8859-1')  as  input:
        foods  =  list (csv.DictReader (input, dialect='excel-tab'))

    print ('Read in ' + str(len(foods)) + ' lines of nutrition (expected 5684).')

    short_colnames  =  {key: key   for   key in foods [0]}
    descriptions    =  {key: key   for   key in foods [0]}

    from  read_foods__data  import  column_descriptions

    for  (item, desc, short_name)  in  column_descriptions:
        short_colnames [item]  =  short_name
        descriptions [item]  =  desc
        
    def  replace  (x):
        for  a  in  [['capsule', 'Capsule'], ['tablet', 'Capsule'],
                     ['Tablet', 'Capsule'], ['TABLET', 'Capsule'],
                     ['G', 'Grams'], ['g', 'Grams'], ['gram', 'Grams'],
                     ['teaspoon', 'Teaspoon'], ['GRAMS', 'Grams'],
                     ['grams', 'Grams'], ['CAPSULE', 'Capsule'],
                     ['Gram', 'Grams'], ['GRAM', 'Grams'],
                     ['Teaspoon', 'Teaspoon']]:
            if  x == a [0]:
                return  a[1]
        return  x

    for  f  in  foods:
        f ['Units']   =  replace (f ['Units'])

    def  aggregate  (new_col, old_cols):
        for  f  in  foods:
            a  =  0
            for  i  in  old_cols:
                a  +=  float (f [i])
            f [new_col]  =  a

    aggregate ('AllCheese', ['CottageCheese', 'CheddarCheese', 'OtherCheese'])

    aggregate ('AllFish', ['WhiteFish', 'OilyFish', 'CannedTuna', 'Shellfish'])

    aggregate ('AllMeat', ['Beef', 'Lamb', 'Pork', 'ProcessRedMeat',
                           'OtherRedMeat', 'Burgers', 'Sausages',
                           'Offal', 'Poultry', 'ProcessedPoultry',
                           'GameBirds'])

    aggregate ('AllAnimal', ['AllCheese', 'AllFish', 'AllMeat'])

    return  {'table': foods,
             'descriptions': descriptions,
             'short_colnames': short_colnames}
