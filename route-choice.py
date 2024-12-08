# Calculate travel time for a given flow.
def getTravelTime(x1, f1, alpha1, C1, beta1):
    return f1 * (1 + alpha1 * (x1 / C1) ** beta1)

# Find equilibrium flows or evaluate edge cases when no equilibrium exists.
def getFlows(d, f1, alpha1, C1, beta1, f2, alpha2, C2, beta2, tol=1e-6, max_iter=100):
    low, high = 0, d
    for _ in range(max_iter):
        mid = (low + high) / 2
        x2 = d - mid
        t1_mid = getTravelTime(mid, f1, alpha1, C1, beta1)
        t2_mid = getTravelTime(x2, f2, alpha2, C2, beta2)
        if abs(t1_mid - t2_mid) < tol:
            return mid, x2, t1_mid, t2_mid
        elif t1_mid > t2_mid:
            high = mid
        else:
            low = mid

    # If solution did not converge, calculate edge cases
    # Case 1: All demand on link 1 (x1 = d, x2 = 0)
    t1_all = getTravelTime(d, f1, alpha1, C1, beta1)
    t2_zero = getTravelTime(0, f2, alpha2, C2, beta2)

    # Case 2: All demand on link 2 (x1 = 0, x2 = d)
    t1_zero = getTravelTime(0, f1, alpha1, C1, beta1)
    t2_all = getTravelTime(d, f2, alpha2, C2, beta2)

    # Compare total travel times for both cases
    case_1_time = max(t1_all, t2_zero)  # Both links must be compared for equilibrium
    case_2_time = max(t1_zero, t2_all)

    if case_1_time < case_2_time:
        #Equilibrium condition is when all flow is on path 1.
        return d, 0, t1_all, 0
    else:
        #Equilibrium condition is when all flow is on path 2.
        return 0, d, 0, t2_all

#Get and validate user input.
def get_input(prompt, valid_range):
    while True:
        try:
            value = float(input(prompt))
            if valid_range[0] <= value <= valid_range[1]:
                return value
            else:
                print(f"Input must be within the range {valid_range}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("Enter the inputs within the specified ranges:")
    d = get_input("Enter total demand (d) [1000, 4000]: ", (1000, 4000))
    f1 = get_input("Enter free-flow travel time for path 1 (f1) [1, 10]: ", (1, 10))
    alpha1 = get_input("Enter alpha for path 1 (alpha1) [0.1, 1]: ", (0.1, 1))
    C1 = get_input("Enter capacity for path 1 (C1) [500, 2500]: ", (500, 2500))
    beta1 = get_input("Enter beta for path 1 (beta1) [1, 4]: ", (1, 4))
    f2 = get_input("Enter free-flow travel time for path 2 (f2) [1, 10]: ", (1, 10))
    alpha2 = get_input("Enter alpha for path 2 (alpha2) [0.1, 1]: ", (0.1, 1))
    C2 = get_input("Enter capacity for path 2 (C2) [500, 2500]: ", (500, 2500))
    beta2 = get_input("Enter beta for path 2 (beta2) [1, 4]: ", (1, 4))

    try:
        x1, x2, t1_time, t2_time = getFlows(d, f1, alpha1, C1, beta1, f2, alpha2, C2, beta2)
        print("The equilibrium condition for all used route is:")
        print(f"Flow on path 1(x1) = {x1:.3f} veh/hr")
        print(f"Flow on path 2(x2) = {x2:.3f} veh/hr")
        print(f"Travel time on Path 1: {t1_time:.3f} min")
        print(f"Travel time on Path 2: {t2_time:.3f} min")
    except ValueError as e:
        print(e)


# Run the program
if __name__ == "__main__":
    main()
