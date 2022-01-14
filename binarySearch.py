import time
import binary
import random

if __name__ == "__main__":
    # Create set so numbers don't repeat
    numSet = set()
    # Add 1k values to the set
    while len(numSet) < 1000:
        numSet.add(random.randint(1,100000))
    # Turn the set into a list, sort the list from least to greatest
    sortedList = sorted(list(numSet))

    # Choose a random number from the list
    randomNum = random.choice(sortedList)

    # Time how long it takes for each method of finding some number  
    start = time.time()
    print("The value is at index:", sortedList.index(randomNum))          # .index
    end = time.time()

    print(f"Time for index method: {end - start}")

    start = time.time()
    naiveResult = binary.naiveSearch(sortedList, randomNum)        # naive 
    end = time.time()

    print(f"Time for naive method: {end - start}")

    start = time.time()
    binaryResult = binary.binarySearch(sortedList, randomNum)      # binary
    end = time.time()

    print(f"Time for binary method: {end - start}")


    print(f"The naive result is index {naiveResult}")
    print(f"The binary result is index {binaryResult}")
