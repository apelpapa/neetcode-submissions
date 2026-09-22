class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0

        while counter != len(sandwiches) and len(students):
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                counter = 0
            else:
                students.append(students[0])
                del students[0]
                counter += 1
        
        return len(students)