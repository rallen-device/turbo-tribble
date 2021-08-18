import operator
import matplotlib.pyplot as plt

def CheckConstraints (player, constraints):
    # constraints are passed as a dictionary of
    # {'key': value, 'operator': value, 'number', value}
    # for loop goes through all constraints and returns false if
    # any are true
    for c in constraints:
        # create a function from the dictionary as a string
        function = '{:} {:} {:}'.format (player [c ['key']],\
                                                c ['operator'],\
                                                c ['number'])
        # takes the string and runs eval to convert it to
        # real code
        try:
            if (eval (function) == False):
                return False
        # if the eval doesn't work then print out the error
        except:
            print ('********** {:} missing {:} **********'.format (player ['name'], c ['key']))  
        return False
    
    # if none of the constraints have returned false 
    # then the player should be added so return true
    return True

def PrintHtmlTableLine (s, cols):
    # print an html table row with each column seperated by a <td>
    line = '<tr>'
    for c in cols:
        if type (s [c]) is float:
            line += '<td> {:0.2f} </td>' .format (s [c])
        else:
            line += '<td> {:} </td>' .format (s [c])
    line += '</tr>'
    print (line)


def PlotHBarGraphAndPrintTable (players_list, y_axis, x_axis, reverse, number_items, title, xlabel, constraints, table_columns, cs):
    # start by sorting the list of dictionaries by the chosen key
    sorted_list = sorted (players_list, key=operator.itemgetter(x_axis), reverse=reverse)
    # created two new empty lists for the x and y axis
    y = []
    x = []
    count = 0
    # go through list and select the top x number of players defined
    for s in sorted_list:
        # check the data exists on the x_axis and then check the constraints
        # allow the player to be added
        if s [x_axis] != 0 and CheckConstraints (s, constraints):
        # if so then add the player and the chosen stat to the x and y list
        # then print the html row
            y.append (s [y_axis])
            x.append (s [x_axis])
        PrintHtmlTableLine (s, table_columns)
        # count is incremented if a player is added, 
        count += 1
        # if the count is equal to the number of items request then 
        # stop and break out of the loop
        if count == number_items:
            break
    # x and y need reversing so the top item is actually at the top
    x.reverse ()
    y.reverse ()
    # draw the graph
    with plt.rc_context({'axes.edgecolor':'#F4F4F9',\
                        'xtick.color':'#493657', \
                        'ytick.color':'#493657',\
                        'text.color':'#493657',\
                        'axes.labelcolor':'#493657',\
                        'figure.figsize': (20, 10)}):
        plt.barh (y, x, color=cs)
        plt.grid(which='both', axis='x', color='#F4F4F9')
        plt.title (title)
        plt.xlabel (xlabel)
        plt.savefig (title + '.png', dpi=500)
        plt.show ()



def CreateConstraintsDict (key, operator, number):
    # used to create a constraint dictionary so its always
    # in a standard format
    return {'key' : key, 'operator' : operator, 'number' : number}

def CreateColourGradientList (num, colora, colorb):
    # seperate color a
    colora_list = []
    for i in range (1, 7, 2):
        colora_list.append (int (colora [i:i+2], base=16))

    # seperate color b
    colorb_list = []
    for i in range (1, 7, 2):
        colorb_list.append (int (colorb [i:i+2], base=16))

    # create distance list
    dist_list = []
    for i in range (3):
        dist_list.append ((colora_list [i] - colorb_list [i]) / (num - 1)) 

    # create the colour gradient list
    ret = []
    for i in range (0, num):
        ret.append ('#{:02x}{:02x}{:02x}'.format (int (colorb_list [0] + (i * dist_list [0])), \
                                                int (colorb_list [1] + (i * dist_list [1])), \
                                                int (colorb_list [2] + (i * dist_list [2]))))
    
    ret.reverse()
    return ret