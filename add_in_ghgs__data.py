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


dishes_fraction = 0.8;   # Fraction of meat in a meat dish (or similarly
                         # fish or cheese) - a guess!!!


def  mean  (a):
    acc  =  0
    count  =  0
    for  i  in  a:
        acc = acc + i
        count = count + 1
    return  acc / count



data_1  =  [[['10R','11R','60R','12R','13A','13B','13R', '15A','15B',
              '15C','15D','15R','53R'],
             'Milk and cream',  'Cows Milk',  1],

            [['38A','38B','38C','38D','38R', '39A','39B','39R', '42R'],
             'Potato',  'Potatoes ',  1],

            [['26A','26R','27A','27B','27R'],
             'Chicken and turkey',  'Chicken',  dishes_fraction],

            [['8A','8B','8C','8D','8E','8R', '7A','7B','7R', '9A','9B',
              '9C','9D','9E','9F','9G','9H','9R'],
             'Cakes, biscuits, puddings',  'Wheat',  1],

            [['40A','40B','40C','40D','40E','40R','45R','61R'],
             'Fruit, fruit juice',  'Bananas',  1],

            [['14A','14B','14R', '17R','18A','18B','19A','19R','20A',
              '20B','20C','21A','21B'],
             'Cheese and butter',  'Cheese',  1],

            [['44R'],
             'Chocolate',  'Cows Milk',  1/0.6 * 426/227],
            # This assumes the dominant part of the GHGEs come from the milk
            # From media reports that Cadbury said on its website that 60% of carbon footprint of chocolate comes from the milk
            # "The equivalent of 426ml of fresh liquid milk in every 227g of milk chocolate." - https://www.cadbury.co.uk/products/cadbury-dairy-milk-11327 retrieved 19 Dec 2017

            [['1A','1D','1E', '2R','3R','59R','4A','4R', '5R','6R',
              '1R', '1C'],
             'Bread, pasta, cereal',  'Wheat',  1/0.8],

            [['33R','34A','34B','34C','34D','34E','34F','34G','34H',
              '35A','35B','35R'],
             'Fish',  'Haddock',  dishes_fraction],

            [['23A','23B','23R','24A','24B','24R', '29R'],
             'Beef and lamb',  'Beef',  dishes_fraction],

            [['22A','22B','22R','25A','25B','25R', '30A','30B','30R'],
             'Bacon, ham, pork',  'Pork',  dishes_fraction],

            [['28R','31A','31B','32A','32B','32R'],
             'Other meat',  'Chicken',  dishes_fraction],

            [['1B','1F','1G'],
             'Rice',  'Rice',  1],

            [['16A','16B','16C','16D'],
             'Eggs',  'Eggs',  1],

            [['37A','37B','37C','37I'],
             'Legumes, beans, pulses',  'Soybean',  1],

            [['37D','37E','37F','37G','37L','37M','37R','50C','50D','37K'],
             'Cooked vegetables',  'Carrots',  1],

            [['56R'],
             'Nuts and seeds',  'Almonds',  1],

            [['41B','41R'],
             'Jam, marmalade, other preserves, sweet spreads',
             'Strawberries',  0.4],

            [['36A','36B','36C'],
             'Salad and raw veg',  'Tomatoes (G)',  1] ]



data_2  =  [
                 [1670,
                      'Sesame seeds',
                      0.88,
                 'From Clune et al 2017 who cite Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf'],

                 [1669,
                      'Sunflower seeds',
                      1.41,
                 'From Clune et al 2017 who cite Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf'],

                 [ 1668,
                       'Pumpkin seeds',
                       1.41,
                 'Copy the value for Sunflower seeds in the absence of other info. Sunflower seeds number is from Clune et al 2017 who cite Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf'],

                 [  1687,
                        'Hazlenuts',
                 mean([0.43,1.50]),
                 'Average of values in Clune et al 2017'],

                 [  1677,
                        'Brazil nuts',
                 mean([1.06,1.37,1.51,2.27]), 
                 'Average of values for cashews from Clune et al 2017'],

                 [  23,
                        'Oats (rolled)',
                 mean([0.38,0.47]),
                 'Average of the two sources in Clune et al 2017'],

                 [ 22,
                       'Oatmeal',
                 mean([0.74,0.87,0.69]), 
                 'Average of the values in Clune et al 2017'],

                 [ 1516,
                       'Currants (dried)',
                       0.84, 
                 'Use the value for ``Currants and gooseberries\'\' from Clune et al 2017 who cite Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf'],

                 [  5582,
                        'Spinach (baby)',
                 mean([0.18,0.91]), 
                 'Average of the values from Clune et al 2017'],

                 [  1506,
                        'Blackcurrants (raw)',
                        0.84,
                 'From Clune et al 2017 ``Currants and gooseberries\'\' who cite Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf'],

                 [  1487,
                        'Banana',
                 mean([0.42,0.45,0.46,0.48,0.48,0.53,0.65,0.69,0.72,0.84,0.93,1.01,1.04,1.06,1.12,1.12,1.37]),
                 'Average of the values from Clune et al 2017'],

                 [ 109,
                       'Bread (wholemeal)',
                 mean([0.977,1.244])/0.8,
                 'From Espinoza-Orias, N., H. Stichnothe and A. Azapagic (2011). The carbon footprint of bread. - The International Journal of Life Cycle Assessment 16(4): 351-365. < The carbon footprint results range from 977 to 1,244 g CO2 eq. per loaf of bread. > per <one loaf of sliced bread (800 g) consumed at home >'],

                 [ 1871,
                       'Marmite',
                       1,
                 'No value found so defaulting to 1'],

                 [ 1293,
                       'Lentils',
                 mean([1.00,1.06]),
                 'Average of values from Clune et al 2017'],

                 [ 1449,
                       'Tomatoes (whole can)',
                       0.44,
                 'Average of the non-greenhouse tomatoes in Clune et al 2017. Note - this doesnt currently include energy for canning, or packaging.'],

                 [ 1440,
                       'Sweet potato (boiled)',
                 mean([0.08,0.08,0.09,0.10,0.12,0.14,0.16,0.16,0.16,0.17,0.17,0.18,0.18,0.18,0.19,0.20,0.21,0.23,0.26,0.26,0.29,0.30,0.32,0.35,0.36]),
                 'In the absence of better information, use the value for the only other tubers (potato) in Clune et al 2017. NB does not include energy used to boil'],

                 [ 1365,
                       'Roast potato',
                 mean([0.08,0.08,0.09,0.10,0.12,0.14,0.16,0.16,0.16,0.17,0.17,0.18,0.18,0.18,0.19,0.20,0.21,0.23,0.26,0.26,0.29,0.30,0.32,0.35,0.36]),
                 'From Clune et al 2017, NB does not include energy used to roast'],

                 [ 5593,
                       'Carrots (microwaved/steamed)',
                 mean([0.04,0.07,0.09,0.11,0.14,0.16,0.20,0.22,0.27,0.31,0.45]),
                 'From Clune et al 2017, NB does not include energy used to cook'],

                 [ 2377,
                       'Butternut squash (baked)',
                       2.22,
                 'From Audsley, E., M. Brander, J. Chatterton, D. Murphy-Bokern, C. Webster and A. Williams (2009). How low can we go? An assessment of greenhouse gas emissions from the UK food system and the scope to reduce them by 2050. London, FCRN-WWF. Accessed: 17/02/2015 from: An assessment of greenhouse gas emissions from the UK food system end and the scope to reduce them by 2050 wwf.org.uk/downloads/how_low_report_1.pdf, NB doesnt include energy to bake.'],

                 [  5391,
                        'Vitamin D (0.25mcg)',
                        0 , 
                 'Based on Audsley et al 2009 <However manufacturing vitamin supplementation appears to be trivial in energy and GHG terms owing to the very small quantities needed.>'],

                 [ 1705,
                       'Sugar (white)',
                       0.1, 
                 'Table 13 of Audsley et al 2010 - sugar beet 0.1, sugar cane 0.09. Not sure about processing']
            ]



data_3  =  [
                 [['47A','47B','48A','48B','48C','49A','49B','49C','49D','49E'],
                 'Alcoholic drinks',
                 0.93,
                 'Average of Tesco Lager (720 gCO2e Per litre i.e. 720/1000) and Navarro 2017 <The carbon footprint values of investigated wineries per RU (0.75 L of wine) in the present study are found in the range between 0.17 and 2.18 kg CO2-eq, the average being 0.85 kg CO2-eq/bottle of wine.>'],

                 [['57A','57B','57C','58A','58B','58C', '51D'],
                 'Soft drinks, bottled water',
                 170/330,
                 'Coca-cola website retrieved 20 Dec 2017: 170g for 330ml can = 0.51g/g (which is similar to Tesco 2012 Cola 12 X 330 ml can multipack gives 140/250 )'],

                 [['50R'],
                 'Savoury sauces, pickles, gravies & condiments',
                 1,
                 'No idea so default to 1 - likely from the processing?'],

                 [['41A', '43R', '55R'],
                 'Sugar, sweets, sweeteners',
                 3.1e1/29.8, 
                 'Taken from <Environmental impacts of food consumption in Europe - Notarnicola et al 2016> which says in Table 1 <29.8 Per-capita apparent consumption of the food product (as kg/inhabitant p.a.)> and Table 7 <3.1E01 kg CO2eq Results are reported for an average consumption of one EU-27 citizen in one year>. (This is larger than: "assuming the GWP of UK sugar of 0.38 kg CO2 eq./kg (CCaLC, 2013)." - which was in <The global warming potential of production and consumption of Kenyan tea - Adisa Azapagic et al>'],

                 [['50A','50B','50E'],
                 'Other drinks',
                 1,
                 'Dont know what to put here so put 1'],

                 [['51A'],
                 'Coffee',
                 0.07/0.1,
                 'From the abstract <emissions of 0.07 kg of CO2-eq> (for 1 dl of coffee = 0.1 kg) from Humbert et al 2009 in <Life cycle assessment of spray dried soluble coffee and comparison with alternatives (drip filter and capsule espresso)>'],

                 [['54A','54B','54C','54D','54E','54F','54G','54H','54I',
                     '54J','54K','54L','54M','54N','54O','54P','54Q','54R'],
                 'Dietary supplements',
                 0,
                 'Based on Audsley et al 2009 <However manufacturing vitamin supplementation appears to be trivial in energy and GHG terms owing to the very small quantities needed.>'],

                 [['52A','52R'],
                 'Commercial toddlers foods and drinks',
                 1,
                  'Dont know what to put here so put 1'],

                 [['51B','51C'],
                 'Tea',
                 42.5/250,
                  'From some reference (?!!! Agapazic??) I have noted: Fig 5 assuming 2x water boiled <Therefore, the GWP results for the functional unit of 1 kg of dry tea considered in this study have been converted to the GWP of 1 cup of tea (assuming, as before, 2 g of tea per bag and 250 ml of water).'],

                 [['51R'],
                 'Tap water',
                 0,
                  'Assume zero']

            ]
