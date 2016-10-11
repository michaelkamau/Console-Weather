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
