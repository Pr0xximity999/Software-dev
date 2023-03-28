for uur in range(1, 25):

    if uur < 12: print(f"{uur}:00 am")
    elif uur == 12: print(f"{uur}:00 pm")
    elif uur == 24: print(f"{uur - 12}:00 am")
    else: print(f"{uur - 12}:00 pm")