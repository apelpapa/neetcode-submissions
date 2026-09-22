class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = collections.deque()
        sandwich_queue = collections.deque()
        counter = 0

        for student in students:
            student_queue.append(student)

        for sandwich in sandwiches:
            sandwich_queue.append(sandwich)

        while counter != len(sandwich_queue) and len(student_queue):
            if student_queue[0] == sandwich_queue[0]:
                student_queue.popleft()
                sandwich_queue.popleft()
                counter = 0
            else:
                student_queue.append(student_queue[0])
                student_queue.popleft()
                counter += 1
        
        return len(student_queue)