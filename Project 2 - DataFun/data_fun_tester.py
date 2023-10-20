import data_fun_student
import data_fun_solution
import sys
def main():
    test_nums = [42,18,25,57,152,3,-20]
    test_chars = ["E","B","5","&","C","a","^"]
    for i in range(len(test_nums)):
        print("My Solution",i+1)
        data_fun_solution.my_solution(test_nums[i],test_chars[i])
        print("")
        print("Student Solution",i+1)
        data_fun_student.student_solution(test_nums[i],test_chars[i])
        print("")

if __name__ == '__main__':
    sys.stdout = open('output.txt', 'w')
    main()
    sys.stdout.close()