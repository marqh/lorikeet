import cf_unit
import lorikeet.cf_names as cf_names




def cf_mpl(name, unit):
    """
    Returns matplotlib kwargs for a given name and unit.

    """
    kwarg_dict = {}
    if (name, cf_unit.Unit(unit)) in cf_names.phenomena:
        kwarg_dict = cf_names.phenomena.get((name, cf_unit.Unit(unit)), {})


