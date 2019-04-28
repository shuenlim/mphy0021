Hello!

This package contains a library that helps alchemists work out how the substances in the shelves in their laboratories will react together.

Usage:

Invoke the tool with abracadabra <laboratory.yml> to output the result of the experiment with the lower and upper shelves in the laboratory and a yaml file containing the results (result.yml). The shelves of the library must be saved as a dictionary with the keys called 'upper' and 'lower'. For example:
laboratory = {'lower': ['A', 'B', 'antiC'], 'upper': ['antiA', 'C']}
Substances will be picked from left to right from the lower shelf and be randomly reacted with one of the possible products from the upper shelf.

Invoke abracadabra <laboratory.yml> --reactions to output only the number of reactions that occurred during the experiment.

If a laboratory with more than two shelves is used a TypeError will be raised as only two shelf laboratories are allowed. 
If a laboratory containing an antianti product is used a TypeError will be raised as antianti products don't exist!
Empty shelves in a laboratory are allowed.