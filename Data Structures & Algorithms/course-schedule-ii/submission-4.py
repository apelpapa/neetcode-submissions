class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        taken = set()
        testing = set()
        order = []

        def testCourse(testing_course: int) -> bool:
            if testing_course in testing:
                return False
            if testing_course in taken:
                return True

            testing.add(testing_course)

            for course in course_map[testing_course]:
                if not testCourse(course):
                    return False
            
            testing.remove(testing_course)
            taken.add(testing_course)
            order.append(testing_course)
            return True
            
        
        for i in range(numCourses):
            if not testCourse(i):
                return []
        return order