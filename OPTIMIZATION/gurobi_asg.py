#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     07/10/2014
# Copyright:   (c) admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



from gurobipy import *

try:

    # Create a new model
    m = Model("max_week7")

    # Create variables
    x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
    x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

    # Integrate new variables
    m.update()

    # Set objective
    m.setObjective(x1 + 2*x2, GRB.MAXIMIZE)

    # Add constraint: x1 + x2 <= 40
    m.addConstr(x1 + x2 <= 40, "c1")

    # Add constraint: 2x1 + x2 <= 60
    m.addConstr(2*x1 + x2 <= 60, "c2")

    # Add constraint: x1 >= 0
    m.addConstr(x1 >= 0, "c3")

    # Add constraint: x2 >= 0
    m.addConstr(x2 >= 0, "c4")

    m.optimize()

    for v in m.getVars():
        print v.varName, v.x

    print 'Obj:', m.objVal

except GurobiError:
    print 'Error reported'
