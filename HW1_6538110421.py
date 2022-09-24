# EXAM_ROOM_SEATING (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main().

def is_inputs_valid(n_a, n_b, total_rows, seats_per_row, policy):
    # return True if all inputs are valid to continue
    #   otherwise return False
    # use the following error message to show that result
    error_student_number = 'ERROR: number of students must be 1 to 20.'
    error_total_rows = 'ERROR: total rows must be at least 4.'
    error_seats_per_row = 'ERROR: seats per row must be 4, 6 or 8.'
    error_not_enough_seat = 'ERROR: room is too small. Get a bigger exam room!'
    error_wrong_policy = 'ERROR: seating policy must be 0 or 1.'
    # Your code here
    if  not 1<=n_a<=20 or not 1<=n_b<=20: 
        print(error_student_number)
        return False
    elif total_rows<4: 
        print(error_total_rows)
        return False
    elif not (seats_per_row in [4,6,8]): 
        print(error_seats_per_row)
        return False
    elif (seats_per_row * total_rows)<(n_a+n_b) :
        print(error_not_enough_seat)
        return False
    elif not (policy in [0,1]): 
        print(error_wrong_policy)
        return False
    else: return True
#------------------------------------------------------------#
def generate_seat_ids(subject_code, n):
    # returns a list of seat ID for this subject which is the combine
    # of subject_code and sequence from 01, 02, ..., 0n
    # For example,
    # generate_seat_ids('Z', 5) should return
    # ['Z01', 'Z02', 'Z03', 'Z04', 'Z05']
    # Hint: using for loop to generate the combination of 
    #       subject_code and sequence

    # Your code here
    seat_ids = []
    for i in range(1,n+1):
      seat_ids.append(subject_code+str(str(i).zfill(2)))
    return seat_ids
#------------------------------------------------------------#
def generate_row_seating_sequence(group1, group2, total_rows, seats_p_row):
    # Hint: 
    # - find the seating_sequence size and create it
    # - use list slicing to assign seat id of each group to seating_sequence
    # Your code here
    seating_sequence = []





    return seating_sequence
#------------------------------------------------------------#    
def generate_column_seating_sequence(group1, group2, total_rows, seats_p_row):
    # Hint:
    # - find seating_sequence size and create it
    # - add empty seats to each group to have the size that fill half room
    # - using for loop to assign 2 columns per iteration:
    #     use list slicing to assign even column with group1
    #     use list slicing to assign odd column with group2

    # Your code here
    seating_sequence = []




    return seating_sequence
#------------------------------------------------------------#    
def display_seating_map(seating_sequence, total_rows, seats_per_row):
    # calculate line_len for display
    # display 'Exam Room' at center
    # use for loop to display each row in the room
    #   use str.join() to generate the output str from seating_sequence of each row

    # Your code here






    pass # remove this line when you finish this function
#------------------------------------------------------------#    
# DO NOT DELETE OR MODIFIED THE CODE BELOW
#------------------------------------------------------------#
def main(debug_mode=False):
    if debug_mode:
        n_A = 10
        n_B = 5
        total_rows = 4
        seats_per_row = 6
        seating_policy = 0
    else: 
        n_A = int(input('Number of students in subject A (1-20): '))
        n_B = int(input('Number of students in subject B (1-20): '))
        total_rows = int(input('Number of rows (must be at least 4): '))
        seats_per_row = int(input('Seats per row: 4, 6, 8: '))
        seating_policy = int(input('0-by_row, 1-by_column: '))
    
    if not is_inputs_valid(n_A, n_B, total_rows, seats_per_row, seating_policy):
        return
    
    # generate seating ID for subject A, B
    group_A = generate_seat_ids('A', n_A)
    group_B = generate_seat_ids('B', n_B)

    # generate seating sequence rowwise and columnwise
    if seating_policy == 0:
        seating_sequence = generate_row_seating_sequence(group_A, group_B, total_rows, seats_per_row)
    else:
        seating_sequence = generate_column_seating_sequence(group_A, group_B, total_rows, seats_per_row)

    # show exam room seating map
    display_seating_map(seating_sequence, total_rows, seats_per_row)

main(debug_mode=True) # uncomment this line if you want to speed up the input while dubuging
# main()

def test(expected, actual):
    print('Expected:\t', expected)
    print('Your result:\t', actual)
    print(50*'-')

def test_is_inputs_valid():
    print('--- is_inputs_valid ---')
    n_a = 10 # 1...20
    n_b = 5  # 1...20
    rows = 5   # >= 4
    seats_p_row = 6 # 4,6,8
    policy = 0 # 0,1
    expected = False # or True base on 5 inputs above
    test(expected, is_inputs_valid(n_a, n_b, rows, seats_p_row, policy))

def test_generate_seat_ids():
    print('--- generate_seat_ids ---')
    seat_ids = generate_seat_ids('A', 1)
    test("['A01']", seat_ids)
    seat_ids = generate_seat_ids('B', 6)
    test("['B01', 'B02', 'B03', 'B04', 'B05', 'B06']", seat_ids)
    seat_ids = generate_seat_ids('C', 19)
    exp = "['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19']"
    test(exp, seat_ids)
    seat_ids = generate_seat_ids('D', 20)
    exp = "['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20']"
    test(exp, seat_ids)

def test_generate_row_seating_sequence():
    print('--- generate_seating_sequence ---')
    # An example of test case is provided,
    # You should use this to create more test cases
    group_A = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10']
    group_B = ['B01', 'B02', 'B03', 'B04', 'B05']
    expected = ['A01', 'B01', 'A02', 'B02', 'A03', 'B03', 'A04', 'B04', 'A05', 'B05', 'A06', ' - ', 'A07', ' - ', 'A08', ' - ', 'A09', ' - ', 'A10', ' - ', ' - ', ' - ', ' - ', ' - ']
    test(expected, generate_row_seating_sequence(group_A, group_B, 4, 6))
    # You test case here
    pass

def test_generate_column_seating_sequence():
    print('--- generate_column_seating_sequence ---')
    # An example of test case is provided,
    # You should use this to create more test cases
    group_A = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10']
    group_B = ['B01', 'B02', 'B03', 'B04', 'B05']
    expected = ['A01', 'B01', 'A05', 'B05', 'A09', ' - ', 'A02', 'B02', 'A06', ' - ', 'A10', ' - ', 'A03', 'B03', 'A07', ' - ', ' - ', ' - ', 'A04', 'B04', 'A08', ' - ', ' - ', ' - ']
    test(expected, generate_column_seating_sequence(group_A, group_B, 4, 6))
    # You test case here
    pass

# test_is_inputs_valid()
# test_generate_seat_ids()
test_generate_row_seating_sequence()
#test_generate_column_seating_sequence()