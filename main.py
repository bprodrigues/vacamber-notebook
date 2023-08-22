from vacamber.suspension_types_v4 import DoubleWishbone

suspension = {
    'P1': {'name': 'Bottom Inner Wishbone Ball',
           'x': 138.0,
           'y': 138.0,
           'unit': 'mm'},
    'P2': {'name': 'Bottom Outer Wishbone Ball',
           'x': 854.0,
           'y': 150.0,
           'unit': 'mm'},
    'P3': {'name': 'Upper Inner Wishbone Ball',
           'x': 182.0,
           'y': 323.0,
           'unit': 'mm'},
    'P4': {'name': 'Upper Outer Wishbone Ball',
           'x': 815.0,
           'y': 400.0,
           'unit': 'mm'},
    'WC': {'name': 'Wheel Contact',
           'x': 900.0,
           'y': 0.0,
           'unit': 'mm'},
    'Camber': {'name': 'Camber angle',
               'value': -2,
               'unit': 'deg'},
}

if __name__ == '__main__':
    s = DoubleWishbone.from_dict(suspension)
    gd = s.geometry_dict()
    for key, value in gd.items():
        print(key, value)
