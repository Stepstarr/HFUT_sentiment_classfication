import pickle
import time
# 从文件加载结果
import pickle
# 从文件加载数据
with open("multi_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

# 将数据解构到原始变量
loaded_result = loaded_data["answer"]
loaded_result2 = loaded_data["answer2"]
loaded_result3 = loaded_data["answer3"]

def test_seg(Segmentation):
    i =0
    count = 0
    for comment,result_r in loaded_result.items():
        i=i+1
        print(f'-------------第{i}个测试项正在测试-------------')
        start_time = time.time()
        result_t=Segmentation(comment)
        end_time = time.time() 
        elapsed_time = end_time - start_time  # 计算经过的时间
        print(f"代码运行时长: {elapsed_time:.4f} 秒")
        score = calculate_similarity(result_t,result_r )
        print(f"代码得分: {score:.4f}")
        if score>80:
            print('通过')
            count+=1
        else:
            print('不通过')
    print(f'------------------最终结果------------------')
    print(f'通过率{count}/{i}')
def test_count(feature_count):
    i =0
    count = 0
    for comment,result_r in loaded_result2.items():
        i=i+1
        print(f'-------------第{i}个测试项正在测试-------------')
        start_time = time.time()
        result_t = feature_count(loaded_result[comment])
        end_time = time.time()
        elapsed_time = end_time - start_time  # 计算经过的时间
        print(f"代码运行时长: {elapsed_time:.4f} 秒")
        if result_t==result_r:
            count+=1
            print('通过')
        else:
            print('不通过')
    print(f'------------------最终结果------------------')
    print(f'通过率{count}/{i}')
def test_sentence_Vec1(Sentence_Vector):
    i = 0
    count = 0
    with open("feature_list.pkl", "rb") as f:
        feature_list = pickle.load(f)
    for comment, result_r in loaded_result3.items():
        i = i + 1
        print(f'-------------第{i}个测试项正在测试-------------')
        start_time = time.time()
        result_t = Sentence_Vector(comment,feature_list)
        end_time = time.time()
        elapsed_time = end_time - start_time  # 计算经过的时间
        print(f"代码运行时长: {elapsed_time:.4f} 秒")
        if result_t == result_r:
            count += 1
            print('通过')
        else:
            print('不通过')
    print(f'------------------最终结果------------------')
    print(f'通过率{count}/{i}')
import random
def F1_score_(evaluate_metrics):
    i = 0
    count = 0
    for _ in range(10):
        i=i+1
        print(f'-------------第{i}个测试项正在测试-------------')
        length = random.randint(50, 150)  # Random length between 5 and 15 for each list
        pre = [random.randint(0, 1) for _ in range(length)]
        test_y = [random.randint(0, 1) for _ in range(length)]
        f1_ = evaluate_metrics(pre, test_y)
        f1 = Test_evaluate_metrics(pre, test_y)
        if f1 == f1_:
            count += 1
            print('通过')
        else:
            print('不通过')
    print(f'------------------最终结果------------------')
    print(f'通过率{count}/{i}')


def Test_evaluate_metrics(pre: list, test_y: list) -> float:
    if len(pre) != len(test_y):
        raise ValueError("Input lists must have the same length.")

    TP = sum([1 for p, t in zip(pre, test_y) if p == 1 and t == 1])
    FP = sum([1 for p, t in zip(pre, test_y) if p == 1 and t == 0])
    FN = sum([1 for p, t in zip(pre, test_y) if p == 0 and t == 1])

    if TP + FP == 0:
        precision = 0.0
    else:
        precision = TP / (TP + FP)

    if TP + FN == 0:
        recall = 0.0
    else:
        recall = TP / (TP + FN)

    if precision + recall == 0:
        F1_score = 0.0
    else:
        F1_score = 2 * (precision * recall) / (precision + recall)

    return format(F1_score, '.4f')
from collections import Counter
def calculate_similarity(list1, list2):
    common_elements_count = sum((Counter(list1) & Counter(list2)).values())
    # 根据交集长度和列表长度计算相似度得分
    score = (common_elements_count / len(list2)) * 100
    return score

def ttt(Segmentation):
    print('OK')