

def load_data(file_name):
    final_data = []
    file = open(file_name, 'r')
    all_lines = file.readlines()
    for line in all_lines:
        faculty_data = line.split(',')
        final_data.append(faculty_data)
    return final_data


def get_key(faculty_member):
    return faculty_member[1]


def binary_search(faculty_data, id_to_find):
    if faculty_data == []:
        return None
    middle = len(faculty_data)//2
    middle_faculty_member = faculty_data[middle]
    faculty_id = int(middle_faculty_member[1])
    if faculty_id == id_to_find:
        return middle_faculty_member
    elif faculty_id > id_to_find:
        return binary_search(faculty_data[:middle], id_to_find)
    else:
        return binary_search(faculty_data[middle+1:], id_to_find)


def main():
    faculty_data = load_data("SampleData.txt")
    faculty_data.sort(key=get_key)
    id_to_find = int(input("What would you like to search for?"))
    faculty_record = binary_search(faculty_data, id_to_find)
    if faculty_record is None:
        print("Faculty member not found")
    print(f"Found {faculty_record[0]} who has been at BSU {faculty_record[2]} years")


if __name__ == '__main__':
    main()