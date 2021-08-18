import graphing_utilities
import hundred_stats



batting_data = hundred_stats.import_csv_to_dict('batting.csv', 'batting')
bowling_data = hundred_stats.import_csv_to_dict('bowling.csv', 'bowling')
combined_data = hundred_stats.combine_lists(batting_data, bowling_data, 'Name')
combined_data = hundred_stats.improve_data(combined_data, ['Name', 'bowling-BB', 'match'])

# general variables
y = 'Name'
key = 'batting-Ave'
xlabel = 'xGAAPNMVWW - £ 1000s'
table_columns = ['Name', 'batting-Runs', key]
number_of_players = 20
colour_scheme = graphing_utilities.CreateColourGradientList (number_of_players, '#32c64a', '#ff0080')

# create graph 1 - actual goals per wage, with no constraints
title = 'Expected goals and assists per weekly wage'
constraints = [graphing_utilities.CreateConstraintsDict ('batting-Runs', '>', '70.0')]
# constraints = []
graphing_utilities.PlotHBarGraphAndPrintTable(combined_data, y, key, True, number_of_players, title, xlabel, constraints, table_columns, colour_scheme)
