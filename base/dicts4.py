measures = {
    'талия': 60,
    'бёдра': 90,
    'грудь': 90,
}

# >>> id(measures)
# 1553345946944
# >>>
# >>> new_measures = {'талия': 62, 'бёдра': 90, 'грудь': 90}
# >>>
# >>> measures.update(new_measures)
# >>> measures
# {'талия': 62, 'бёдра': 90, 'грудь': 90}
# >>>
# >>> id(measures)
# 1553345946944
# >>>
# >>> measures |= {'талия': 61, 'бёдра': 89, 'грудь': 90}
# >>> measures
# {'талия': 61, 'бёдра': 89, 'грудь': 90}
# >>>
# >>> id(measures)
# 1553345946944

