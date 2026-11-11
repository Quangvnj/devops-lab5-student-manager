"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student

#sửa tất cả phần students thành student_list

def main():
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    student_list = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Thêm sinh viên mới
    student_list = add_student(student_list, "SV004", "Pham Thi D", 22, "K19")

    for student in student_list:
        print(f"  {student}")

    print(f"\nTotal: {len(student_list)} students")


if __name__ == "__main__":
    main()

def add_student(student_list: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách.

    Args:
        student_list: Danh sách sinh viên hiện tại
        student_id: Mã sinh viên
        name: Họ tên
        age: Tuổi
        grade: Khóa

    Returns:
        Danh sách sinh viên đã được cập nhật
    """
    # Kiểm tra trùng mã sinh viên
    for s in student_list:
        if s.student_id == student_id:
            print(f"❌ Mã sinh viên {student_id} đã tồn tại!")
            return student_list

    new_student = Student(student_id, name, age, grade)
    student_list.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return student_list