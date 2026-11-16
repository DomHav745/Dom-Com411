def escape_by(plan):
    plan = input()
    if plan == "Jumping over":
        print("That won't work! It's too big!")
    if plan == "Running around":
        print("That won't work! It's too fast!")
    if plan == "Cross the bridge":
        print("That might work, let's go!")
escape_by("Jumping over")
escape_by("Running around")
escape_by("Cross the bridge")
