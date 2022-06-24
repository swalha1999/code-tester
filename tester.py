import subprocess
import time
import multiprocessing 

strip_str = ". "
newline = '\n'

def communicator(file_name, input_list):
    try:
        in_stream = b""
        for inp in input_list:
            in_stream += bytes(inp + " ", encoding='utf-8')
        chiled = subprocess.Popen([file_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE) ##without memory leak check
        # chiled = subprocess.Popen(["valgrind",file_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE) ##with memory leak check
        res = chiled.communicate(in_stream)
        chiled.kill()
        return res[0].strip().decode(), res[1]
    except NameError as e:
        print(e)
        return e 


def getAns(s): 
    y=-1
    for i in range(len(s)):
        if s[i]==":":
            if i > y :
                y=i
    return s[y+1:].strip(strip_str).replace(newline, "").replace(" ", "")


def tester(file_name, input_list, result, res_type=str):
    test_res = communicator(file_name, input_list)
    ans = getAns(test_res[0])
    if test_res[1] or res_type(ans) != res_type(result.replace(" ", "")):
        return f"\033[1;31;40m Failed\033[0m Your Output: {ans} "
    return f"\033[1;32;40m Passed \033[0m -> "


def Printer(test):
    try:
        input = str(test[0]).replace(" ", "").replace("'", "") 
        output = str(test[1]).replace("\n", "")
        print(f"{tester(filename, test[0], test[1], test[2])}   input :{input} --> {output} ")
    except:
        print("faild")
    return 0

if __name__ == '__main__':
    start = time.time()
    filename = "./hw7_over_engineered"
    # filename = "./hw7"
    basic_tests = [
        [['3', '0'], "0", str],
        [['3', '1'], "1", str],
        [['3', '2'], "1", str],
        [['3', '3'], "2", str],
        [['3', '4'], "3", str],
        [['3', '5'], "5", str],
        [['3', '6'], "8", str],
        [['3', '7'], "13", str],
        [['3', '8'], "21", str],
        [['3', '9'], "34", str],
        [['3', '16'], "987", str],
        [['3', '32'], "2178309", str],
        [['3', '33'], "3524578", str],
        [['3', '44'], "701408733", str],
        [['3', '46'], "1836311903", str],
        [['1', '4', '4','1','2','3','4'], "3", str],
        [['1', '0', '6','0','0','0','0','0','0'], "0", str],
        [['1', '-3', '5','-5','-3','-3','-1','0'], "1", str],
        [['1', '4', '12','1','2','3','5','6','7','8','9','10','11','11','11'], "Does not exist", str],
        [['2', '2', '3','2','1','2','3','4','5','6','10','11','20','21','30','31'], "[140,146][320,335]", str],
        [['2', '3', '3','2','1','2','3','4','5','0','6','0','0','10','-10','20','-20','30','-30'], "[140,-140][140,-140][60,-60]", str],
        [['2', '4', '4','4','-3','-2','-1','0','1','2','3','4','-3','-2','-1','0','1','2','3','4','1','2','3','4','-3','-2','-1','0','1','2','3','4','-3','-2','-1','0'], "[2,-4,-10,-16][-14,-4,6,16][2,-4,-10,-16][-14,-4,6,16]", str],
    ]
    print("Base tests:")

    # de comment to run the test in MultiCore mode
    # pool = multiprocessing.Pool()
    # pool.map(Printer,basic_tests)
    # pool.close()

    # de comment to run the test in singleCore mode
    for test in basic_tests:
        Printer(test)

    print('That took {} seconds'.format(time.time() - start))

