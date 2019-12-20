"""
dcp#173
dip#126 (12/13/19)

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""


def flatten_dict(d, out, s=""):
    for k, v in d.items():
        if type(v) is dict:
            flatten_dict(v, out, s + "." + k)
        else:
            # note: remove intial period in string key
            out[(s + "." + k)[1:]] = v


d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

flat = {}
flatten_dict(d, flat)

print("\nInitial dict:\n{}".format(d))
print("\nFlattened dict:\n{}".format(flat))

