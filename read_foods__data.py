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


column_descriptions = [
        ['ACAR','Alpha-carotene (μg)','acar'],
        ['ALCO','Alcohol (g)','Alcohol'],
        ['BCAR','Beta-carotene (μg)','BCar'],
        ['BCRYPT','Beta cryptoxanthin (μg)','BCrypt'],
        ['BIOT','Biotin (μg)','Biot'],
        ['CA','Calcium (mg)','Ca'],
        ['CHO','Carbohydrate (g)','Carb'],
        ['CHOL','Cholesterol (mg)','Chol'],
        ['CL','Chloride (mg)','Cl'],
        ['CMON','Cis-Monounsaturated fatty acids (g)','Mono'],
        ['CN3','Cis-n3 fatty acids (g)','Cn3'],
        ['CN6','Cis-n6 fatty acids (g)','Cn6'],
        ['CU','Copper (mg)','Cu'],
        ['ENGFIB','Englyst fibre (g)','Fibre'],
        ['FAT','Fat (g)','Fat'],
        ['FE','Iron (mg)','Fe'],
        ['FOLT','B9 (Folate) (μg)','B9'],
        ['FRUCT','Fructose (g)','Fruct'],
        ['GLUC','Glucose (g)','Gluc'],
        ['HFE','Haem iron (mg)','HFe'],
        ['I','Iodine (μg)','I'],
        ['K','Potassium (mg)','K'],
        ['KCALS','Energy (kcal)','kcal'],
        ['KJ','Energy (kJ)','kJ'],
        ['LACT','Lactose (g)','Lac'],
        ['MALT','Maltose (g)','Malt'],
        ['MG','Magnesium (mg)','Mg'],
        ['MILK','Intrinsic and milk sugars (g)','MilkSug'],
        ['MN','Manganese (mg)','Mn'],
        ['NA','Sodium (mg)','Na'],
        ['NCF','Nitrogen conversion factor','NCF'],
        ['NHFE','Non-haem iron (mg)','NhFe'],
        ['NIACEQU','B3 (Niacin equivalent) (mg)','B3'],
        ['NMILK','Non-milk extrinsic sugars (g)','NMilkSug'],
        ['OSUG','Other Sugars (g)','OSug'],
        ['P','Phosphorus (mg)','P'],
        ['PANTO','B5 (Pantothenic acid) (mg)','B5'],
        ['PROT','Protein (g)','Prot'],
        ['RET','Retinol (μg)','Ret'],
        ['RIBO','B2 (Riboflavin) (mg)','B2'],
        ['SATFA','Saturated fatty acids (g)','SatFa'],
        ['SE','Selenium (μg)','Se'],
        ['STAR','Starch (g)','Star'],
        ['SUCR','Sucrose (g)','Sucr'],
        ['THIA','B1 (Thiamin) (mg)','B1'],
        ['TOTCAR','Total carotene (μg)','TotCar'],
        ['TOTNIT','Total nitrogen (g)','TotNit'],
        ['TOTSUG','Total sugars (g)','TotSug'],
        ['TRANS','Trans fatty acids (g)','Trans'],
        ['VITA','Vitamin A (retinol equivalents) (μg)','A'],
        ['VITB12','Vitamin B12 (μg)','B12'],
        ['VITB6','Vitamin B6 (mg)','B6'],
        ['VITC','Vitamin C (mg)','C'],
        ['VITD','Vitamin D (μg)','D'],
        ['VITE','Vitamin E (mg)','E'],
        ['WATER','Water (g)','Water'],
        ['ZN','Zinc (mg)','Zn'],
        ['Fruit','Percentage of Fruit','Fruit'],
        ['DriedFruit','Percentage of Dried Fruit','DriedFruit'],
        ['FruitJuice','Percentage of Fruit Juice','FruitJuice'],
        ['SmoothieFruit','Percentage of Smoothie Fruit','SmoothieFruit'],
        ['Tomatoes','Percentage of Tomatoes','Tomatoes'],
        ['TomatoPuree','Percentage of Tomato Puree','TomatoPuree'],
        ['Brassicaceae','Percentage of Brassicaceae','Brassicaceae'],
        ['YellowRedGreen','Percentage of Yellow/Root Vegetables','YellowRedGreen'],
        ['Beans','Percentage of Beans and Pulses','Beans'],
        ['Nuts','Percentage of Nuts','Nuts'],
        ['OtherVeg','Percentage of Other Fruit/Veg','OtherVeg'],
        ['Beef','Percentage of Beef','Beef'],
        ['Lamb','Percentage of Lamb','Lamb'],
        ['Pork','Percentage of Pork','Pork'],
        ['ProcessRedMeat','Percentage of Processed Red Meat','ProcessRedMeat'],
        ['OtherRedMeat','Percentage of Other Red Meat','OtherRedMeat'],
        ['Burgers','Percentage of Burgers & Grill Steaks','Burgers'],
        ['Sausages','Percentage of Sausages','Sausages'],
        ['Offal','Percentage of Offal','Offal'],
        ['Poultry','Percentage of Poultry','Poultry'],
        ['ProcessedPoultry','Percentage of Processed Poultry','ProcessedPoultry'],
        ['GameBirds','Percentage of Game Birds','GameBirds'],
        ['WhiteFish','Percentage of White Fish','WhiteFish'],
        ['OilyFish','Percentage of Oily Fish','OilyFish'],
        ['CannedTuna','Percentage of Canned Tuna','CannedTuna'],
        ['Shellfish','Percentage of Shellfish','Shellfish'],
        ['CottageCheese','Percentage of Cottage Cheese','CottageCheese'],
        ['CheddarCheese','Percentage of Cheddar Cheese','CheddarCheese'],
        ['OtherCheese','Percentage of Other Cheese','OtherCheese'],

        ['AllCheese', 'Percentage of cheese (total)', 'cheese'],
        ['AllFish', 'Percentage of fish (total)', 'fish'],
        ['AllMeat', 'Percentage of meat (total)', 'meat'],
        ['AllAnimal', 'Percentage of cheese, fish, meat (total)', 'animal'],

        ['CO2e', 'CO2e (g)', 'CO2e'],
        ['CO2eRatio', 'kg CO2e / kg product', 'CO2eRatio'],
        ['CO2eRef', 'Reference information for the CO2e number used', 'CO2eRef'],
        ['CO2eGroup', 'index to a group of foods with similar CO2e', 'CO2eGroup'],

        ['FoodDescriptions', 'Graph/table -friendly food names', 'FoodDescriptions'],

        ['FoodAisle',
         'FoodAisle (a food categorisation used for grouping foods for plotting)',
        'FoodAisle']

]
