class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = {i:[] for i in range(numCourses)}
        order = []

        for course, prereq in prerequisites:
            req[course].append(prereq)

        checking = set()
        taken = set()

        def checkCourse(course: int) -> bool:
            if course in checking:
                return False
            if course in taken:
                return True
            
            checking.add(course)

            for prereq in req[course]:
                if not checkCourse(prereq):
                    return False
            
            checking.remove(course)
            taken.add(course)
            order.append(course)
            return True

        for i in range(numCourses):
            if not checkCourse(i):
                return []
        return order
            