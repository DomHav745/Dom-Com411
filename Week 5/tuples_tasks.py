def likelihoods():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)

def run():
    probabilities = likelihoods()
    print(f"Maximum likelihood of falling is {probabilities[1]}%")
    print(f"Minimum likelihood of falling is {probabilities[0]}%")

if __name__ == "__main__":
    run()
