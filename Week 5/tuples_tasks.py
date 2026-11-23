def step():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods
def run():
    likelihoods = step()
    good_steps = []
    bad_steps = []
    for step in likelihoods:
        if (step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"Good Steps: {len(good_steps)}, Bad Steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()

#DOES NOT WORK CURRENTLY  FIX ASAP  DO NOT UNDERSTAND  LIKELY EASY FIX BUT LOST RN