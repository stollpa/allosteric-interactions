

-*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:07:40 2018

@author: stollpa
sol.fluxes.to_json('fluxes.json') # save fluxes
"""
## how do I save the fluxes in a json file? So far I just figured out how to save the model.


import cobra
from escher import Builder

model = cobra.io.read_sbml_model('core_patricia.xml')
cobra.io.save_json_model(model, 'model.json')  # also save fluxes? how

## constraints, ...
"""
print(model.metabolites.ac_e.summary())
const_flux = model.problem.Constraint(
    model.reactions.ACt2r.flux_expression, lb=-10, ub=-10)
model.add_cons_vars(const_flux)
sol=model.optimize()
print(sol)
print(sol.fluxes['ACt2r'],
      sol.objective_value)
cobra.io.save_json_model(model, "test.json")
"""
## change carbon source:
print("")
print("changing carbon source: ")
#model.reactions.ACt2r.lower_bound = -10
#model.reactions.ACt2r.upper_bound = -10
model.reactions.EX_glc__D_e.lower_bound = 0
model.reactions.EX_glc__D_e.upper_bound = 0
model.reactions.EX_fru_e.lower_bound = -1000
model.reactions.EX_fru_e.upper_bound = 1000
sol=model.optimize()
print(model.summary())
#b = Builder(model=model)
#b = Builder(map_name="iJO1366.Central metabolism") #test works
#b.display_in_browser() # does not work, why?

sol.fluxes.to_json('fluxes.json') # save fluxes
