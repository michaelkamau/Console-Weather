def degrees_to_direction(angle):
    """
    This function converts an angle (in degrees) to a compass direction

    REFERENCE : http://climate.umn.edu/snow_fence/components/winddirectionanddegreeswithouttable3.htm
    :param angle:

    :return: compass cardinal direction
    """
    if 348.75 > angle <= 11.25:
        return 'North'
    elif angle <= 33.75:
        return 'North North East'
    elif angle <= 56.25:
        return 'North East'
    elif angle <= 78.75:
        return 'East North East'
    elif angle <= 101.25:
        return 'East'
    elif angle <= 123.75:
        return 'East South East'
    elif angle <= 146.25:
        return 'South East'
    elif angle <= 168.75:
        return 'South South East'
    elif angle <= 191.25:
        return 'South'
    elif angle <= 213.75:
        return 'South South West'
    elif angle <= 236.25:
        return 'South West'
    elif angle <= 258.75:
        return 'West South West'
    elif angle <= 281.25:
        return 'West'
    elif angle <= 303.75:
        return 'West North West'
    elif angle <= 326.25:
        return 'North West'
    elif angle <= 348.75:
        return 'North North West'




