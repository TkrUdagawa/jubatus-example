from jubatus.common import Datum
from jubatus.regression.client import Regression
import sys
import math

def read_file(filename):
    with open(filename) as f:
        return f.readlines()

def make_datum(line):
    crim, zn, indus, chas, nox, rm ,age, dis, rad, tax, ptratio, b, lstat, medv = line.split()
    d = Datum({"crim": float(crim),
               "zn": float(zn),
               "indus": float(indus),
               "chas": str(chas),
               "nox": float(nox),
               "rm": float(rm),
               "age": float(age),
               "dis": float(dis),
               "rad": float(rad),
               "tax": float(tax),
               "ptratio": float(ptratio),
               "b": float(b),
               "lstat": float(lstat)})
    return [float(medv), d]

def train(training_data):
    client = Regression("127.0.0.1", 9199, "boston")
    client.clear()
    for data in training_data:
        score, d = make_datum(data)
        client.train([[score, d]])

def analyze(test_data):
    client = Regression("127.0.0.1", 9199, "boston")
    errors = []
    for data in test_data:
        score, d = make_datum(data)
        predict = client.estimate([d])
        errors.append(score - predict[0])
    return errors

def split_data(data_list, num = 5):
    chunck_length = int(len(data_list)/num)
    return [data_list[i*chunck_length:(i + 1) * chunck_length] for i in range(0, num)]

def make_training_data(index, splited_data):
    training_data = []
    for i, data in enumerate(splited_data):
        if i != index:
            training_data.extend(data)
    return training_data

if __name__ == "__main__":
    data = read_file(sys.argv[1])
    splited_data = split_data(data)
    results = []
    for i, d in enumerate(splited_data):
        training_data = make_training_data(i, splited_data)
        train(training_data)
        errors = analyze(d)
        results.append(errors)

    for i, res in enumerate(results):
        total_error = sum(map(math.fabs, res))
        average_error = total_error/len(res)
        print("{}, total_error: {}, average_error: {}".format(i, total_error, average_error))
