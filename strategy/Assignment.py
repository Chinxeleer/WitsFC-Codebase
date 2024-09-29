import numpy as np


def euclidean_distance(teammate_positions, formation_positions):

    array1 = np.array(teammate_positions)
    array2 = np.array(formation_positions)
    cost_matrix = np.sqrt(np.sum((array1[:, np.newaxis] - array2) ** 2, axis=2))
    return cost_matrix


def hungarian_cost_assignment(cost_matrix):
    cost_matrix = cost_matrix.copy()
    num_rows, num_cols = cost_matrix.shape

    # Step 1: Subtract the smallest element in each row from all elements in that row
    cost_matrix -= cost_matrix.min(axis=1)[:, np.newaxis]

    # Step 2: Subtract the smallest element in each column from all elements in that column
    cost_matrix -= cost_matrix.min(axis=0)

    # Initialize cover arrays and zero marking arrays
    row_covered = np.zeros(num_rows, dtype=bool)
    col_covered = np.zeros(num_cols, dtype=bool)
    masked_zeros = np.zeros((num_rows, num_cols), dtype=bool)
    optimalcost_zeros = np.zeros((num_rows, num_cols), dtype=bool)

    # Function to find the first uncovered zero
    def find_a_zero():
        for i in range(num_rows):
            for j in range(num_cols):
                if cost_matrix[i, j] == 0 and not row_covered[i] and not col_covered[j]:
                    return (i, j)
        return None

    # Star a zero (assign)
    def mask_zero(row, col):
        masked_zeros[row, col] = True

    # Cover the column of a starred zero
    def cover_column_with_starred_zero(col):
        col_covered[col] = True

    # Cover all columns containing a starred zero
    def cover_columns():
        for j in range(num_cols):
            if np.any(masked_zeros[:, j]):
                cover_column_with_starred_zero(j)

    # Find the star in a given row
    def find_star_in_row(row):
        star_col = np.where(masked_zeros[row])[0]
        return star_col[0] if len(star_col) > 0 else -1

    # Find the prime in a given row
    def find_optimal_zero_in_row(row):
        prime_col = np.where(optimalcost_zeros[row])[0]
        return prime_col[0] if len(prime_col) > 0 else -1

    # Find the star in a given column
    def find_star_in_col(col):
        star_row = np.where(masked_zeros[:, col])[0]
        return star_row[0] if len(star_row) > 0 else -1

    # Prime a zero (mark a zero that could lead to an optimal assignment)
    def optimal_zero(row, col):
        optimalcost_zeros[row, col] = True

    # Uncover all rows and columns
    def uncover_all_rows_and_columns():
        row_covered[:] = False
        col_covered[:] = False

    # Adjust the matrix by adding/subtracting the minimum uncovered value
    def adjust_matrix():
        minimum_uncovered = np.min(cost_matrix[~row_covered][:, ~col_covered])
        cost_matrix[~row_covered] -= minimum_uncovered
        cost_matrix[:, col_covered] += minimum_uncovered

    # Initial step: star all uncovered zeros and cover corresponding columns
    for i in range(num_rows):
        for j in range(num_cols):
            if cost_matrix[i, j] == 0 and not row_covered[i] and not col_covered[j]:
                mask_zero(i, j)
                row_covered[i] = True
                col_covered[j] = True

    # Reset row and column covers
    row_covered[:] = False
    col_covered[:] = False

    cover_columns()

    # Main loop: continue until all columns are covered
    while np.sum(col_covered) < num_cols:
        zero_pos = find_a_zero()
        while zero_pos is None:
            adjust_matrix()
            zero_pos = find_a_zero()

        row, col = zero_pos
        optimal_zero(row, col)

        star_col = find_star_in_row(row)
        if star_col == -1:
            # If there's no starred zero in the primed zero's row, augment the path
            path = [(row, col)]
            while True:
                star_row = find_star_in_col(col)
                if star_row == -1:
                    break
                path.append((star_row, col))
                col = find_optimal_zero_in_row(star_row)
                path.append((star_row, col))

            # Augment the path: toggle the starred/primes along the path
            for r, c in path:
                masked_zeros[r, c] = not masked_zeros[r, c]

            # Reset covers and primes
            uncover_all_rows_and_columns()
            optimalcost_zeros[:] = False
            cover_columns()
        else:
            # Cover the row of the primed zero and uncover the column of the starred zero
            row_covered[row] = True
            col_covered[star_col] = False

    # Get final assignment: positions of starred zeros
    row_ind, col_ind = np.where(masked_zeros)
    return list(zip(row_ind, col_ind))


def role_assignment(teammate_positions, formation_positions):

    # Input : Locations of all teammate locations and positions
    # Output : Map from unum -> positions
    # -----------------------------------------------------------#

    point_preferences = {}

    cost_matrix = euclidean_distance(teammate_positions, formation_positions)
    assignments = hungarian_cost_assignment(cost_matrix)
    for i in range(1, 12):
        point_preferences[i] = formation_positions[assignments[i - 1][1]]
    return point_preferences


def pass_reciever_selector(player_unum, teammate_positions, final_target):

    # Input : Locations of all teammates and a final target you wish the ball to finish at
    # Output : Target Location in 2d of the player who is recieveing the ball
    # -----------------------------------------------------------#

    # Example
    pass_reciever_unum = (
        player_unum + 1
    )  # This starts indexing at 1, therefore player 1 wants to pass to player 2

    if pass_reciever_unum != 12:
        target = teammate_positions[
            pass_reciever_unum - 1
        ]  # This is 0 indexed so we actually need to minus 1
    else:
        target = final_target

    return target
