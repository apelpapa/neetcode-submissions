class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_to_take = deque()
        courses_with_prereqs = {}
        courses_taken = []
        completed = [False] * numCourses

        for course in range(numCourses):
            courses_to_take.append(course)
            courses_with_prereqs[course] = []

        for course, prereq in prerequisites:
            courses_with_prereqs[course].append(prereq)

        courses_to_take.reverse()

        while courses_to_take:
            taken_before = len(courses_taken)

            for _ in range(len(courses_to_take)):
                course = courses_to_take.pop()

                if all(completed[prereq] for prereq in courses_with_prereqs[course]):
                    courses_taken.append(course)
                    completed[course] = True
                else:
                    courses_to_take.appendleft(course)

            if len(courses_taken) == taken_before:
                return []

        return courses_taken
