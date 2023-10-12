import data_fun
import sys
def main():
    test_nums = [42,18,25,57]
    test_chars = ["E","B","5","&"]
    for i in range(len(test_nums)):
        print("My Solution",i+1)
        data_fun.my_solution(test_nums[i],test_chars[i])
        print("")
        print("Student Solution",i+1)
        data_fun.student_solution(test_nums[i],test_chars[i])
        print("")

if __name__ == '__main__':
    sys.stdout = open('output.txt', 'w')
    main()
    sys.stdout.close()