"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import string
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table ={}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    the_values_list = []
    max_year = int(gdpinfo["max_year"])
    min_year = int(gdpinfo["min_year"])
    #print(gdpdata)
    the_years = gdpdata.keys()
    for item in the_years:
        #print(item)
        if (str.isdigit(item)) and (min_year <= int(item) <= max_year):
            if gdpdata[item] != "" :
                tup_of_values = (int(item), float(gdpdata[item]))
                the_values_list.append(tup_of_values)
                #print(the_values_list)


    return the_values_list


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    the_country_year_dic = {}

    the_dic = read_csv_as_nested_dict( gdpinfo['gdpfile'], gdpinfo['country_name']
                                        , gdpinfo['separator'], gdpinfo['quote'])
    the_countries_name = the_dic.keys()
    for item in country_list:
        for item2 in the_countries_name:
            if item == item2:
                the_years_dic = {}
                the_valueofcou = the_dic[item2]
                for item3 in the_valueofcou:
                    if str.isdigit(item3):
                        the_years_dic[item3] = the_valueofcou[item3]
                the_list_of_tup = build_plot_values(gdpinfo,the_years_dic)
                the_list_of_tup.sort(key = lambda pair: pair[0])
                the_country_year_dic[item2] = the_list_of_tup
        if item not in the_countries_name:
            the_country_year_dic[item] = []

    return the_country_year_dic


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    the_dic_of_countries = build_plot_dict(gdpinfo, country_list)
    for item in country_list:
        the_list_of_years = the_dic_of_countries[item]
        coords = [(xval, yval) for xval, yval in the_list_of_years]
        xyplot = pygal.XY(height=500)
        xyplot.title = plot_file
        xyplot.add("Data", coords)
        xyplot.render_in_browser()

def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")


