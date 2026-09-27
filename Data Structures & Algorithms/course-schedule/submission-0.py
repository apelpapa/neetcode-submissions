class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = { i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        loop_set = set()

        def courseTest(course: int) -> bool:
            if course in loop_set:
                return False
            if len(course_map[course]) == 0:
                return True

            loop_set.add(course)

            for a_remaining_course in course_map[course]:
                if not courseTest(a_remaining_course):
                    return False
            
            loop_set.remove(course)
            course_map[course] = []
            return True

        for course in range(numCourses):
            if not courseTest(course):
                return False
        return True