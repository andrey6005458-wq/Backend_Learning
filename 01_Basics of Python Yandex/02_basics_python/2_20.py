places = [input(), input(), input()]
places.sort()
for place in places:
    if "зайка" in place:
        print(place, len(place))
        break
