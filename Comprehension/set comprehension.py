"""Set Comprehension:

Syntax:
var_name={expression for variable in sequence}


Syntax:
var_name={expression for variable in sequence if condition}

syntax:
var={exp1 if condition else exp2 for for var in sequence}
"""

sq={1,2,3,4,5}
sq={i**2 for i in sq}
print(sq)