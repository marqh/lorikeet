#from cf_unit import Unit
# # class CFLorikeet(object):
# #     def __init__(self, name, unit):
        

# phenomena = {('air_temperature', '': ('coolwarm', [('K', (253, 323)),
#                                              ('degC', (-30, 40))]),
#             'air_pressure': ('brewer_Blues_09', [('Pa', (9e4, 1.1e5))]),
#             'air_pressure_at_sea_level': ('brewer_Blues_09',
#                                           [('Pa', (9e4, 1.1e5))]),
#             'surface_temperature': ('coolwarm', [('K', (253, 323)),
#                                                  ('degC', (-30, 40))]),
#             'specific_humidity': ('YlGnBu', [('kg kg-1',
#                                                          (0, 0.5))]),
#             } 

# (aname, aunit)

# dict(cmap='YlGnBu', vmin=7, vmax=25)

def base(pattern, updates=None):
    if updates is None:
        updates = {}
    d = _base_phenomena[pattern].copy()
    d.update(updates)
    return d

_base_phenomena = {('humidity'): {'cmap':'YlGnBu', 'vmin':7, 'vmax':25}}
                                
phenomena = {('specific_humidity', '1'): base(('humidity'),
                                              {'nlevels': 7, vmin: 7,
                                               vmax: 25}),
             ('relative_humidity', '%'): base(('humidity'),
                                              {'levels': [0.2, 0.4]}),
             }

