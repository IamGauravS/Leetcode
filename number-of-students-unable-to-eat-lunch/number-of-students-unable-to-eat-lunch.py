class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_queue = collections.deque(sandwiches)
        student_queue = collections.deque(students)
        
        while len(sandwich_queue):
            people_eat = 0
            for i in range(len(student_queue)):
                if sandwich_queue[0] == student_queue[0]:
                    sandwich_queue.popleft()
                    student_queue.popleft()
                    people_eat = 1
                else:
                    student_queue.append(student_queue.popleft())
                    
                    
            if people_eat == 0:
                return len(student_queue)
            
            
            
            
        return len(student_queue)
                    
                    