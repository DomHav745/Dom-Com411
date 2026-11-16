def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining < steps_crossed:
        print("Still some ways to go...")
    else:
        print("We're almost there!")
climb_ladder(5, 2)
climb_ladder(3, 5)
