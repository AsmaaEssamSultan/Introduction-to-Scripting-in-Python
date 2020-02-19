"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    the_list_of_countries = []
    the_dic_of_countries = {}
    plot_countries_keys = list(plot_countries.keys())
    #print(plot_countries_keys)
    for item in plot_countries_keys:
        #print(item)
        the_value = plot_countries[item]
        #print(the_value)
        if the_value not in gdp_countries:
            the_list_of_countries.append(item)
            #print(the_list_of_countries)
        else:
            the_dic_of_countries[item] = the_value

    the_tuple = ( the_dic_of_countries , set(the_list_of_countries))


    return the_tuple

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
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

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    the_gdp_dictionary = {}
    the_list_of_no_year = []
    the_list_of_no_gdp = []
    the_dic_of_countries = read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'],
                                                   gdpinfo['separator'], gdpinfo['quote'])
    the_plot_countries_keys = list(plot_countries.keys())
    for item in the_plot_countries_keys:
        #print(item)
        the_country_name = plot_countries[item]
        if the_country_name in the_dic_of_countries:
            the_value_of_the_country = the_dic_of_countries[the_country_name]
            #print(the_value_of_the_country)
            for item2 in the_value_of_the_country:
                #print(item2)
                if item2 == year:
                    the_gdp = the_value_of_the_country[item2]
                    if the_gdp != "":
                        the_gdp_log = math.log10(int(the_gdp))
                        the_gdp_dictionary[item] = the_gdp_log
                    else:
                        the_list_of_no_gdp.append(item)
        else:
            the_list_of_no_year.append(item)


    return the_gdp_dictionary, set(the_list_of_no_year), set(the_list_of_no_gdp)



def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """

    return


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


