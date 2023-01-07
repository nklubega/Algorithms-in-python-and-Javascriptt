def three_sum(nums):
    # Sort the input array in ascending order
    nums.sort()

    # Initialize an empty list to store the triplets
    triplets = []

    # Initialize a set to store the unique values
    unique_values = set()

    # Iterate through the array and fix the value of nums[i]
    for i in range(len(nums)):
        # Skip the iteration if the current value of nums[i] is in the set of unique values
        if nums[i] in unique_values:
            continue

        # Add the current value of nums[i] to the set of unique values
        unique_values.add(nums[i])

        # Initialize two pointers, j and k, to point to i+1 and the end of the array, respectively
        j = i+1
        k = len(nums)-1

        # While j is less than k, do the following:
        while j < k:
            # If nums[i] + nums[j] + nums[k] is equal to 0, add the triplet [nums[i], nums[j], nums[k]] to the result and increment j and decrement k to move to the next unique pair
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            # If nums[i] + nums[j] + nums[k] is less than 0, increment j
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            # If nums[i] + nums[j] + nums[k] is greater than 0, decrement k
            else:
                k -= 1

    # Return the result
    return triplets
