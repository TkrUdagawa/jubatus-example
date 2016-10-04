# ボストン郊外の家賃予測
## 概要
jubaregressionを用いて家賃の予測を行う。

## Data
UCI Machine Learning Repositoryにて公開されている [Housing Data Set](https://archive.ics.uci.edu/ml/datasets/Housing) を利用。

## 使い方

- jubaregressionの起動
```
jubaregression -f config/AROW.json &
```
- pythonスクリプトの実行
```
python boston.py data/housing.data
```

データを5分割した5-fold CVの結果が表示される

## ベンチマーク結果

```
perceptron(learning_rate:0.0000001)
0, average_error: 7.818512663510765
1, average_error: 9.061207033856078
2, average_error: 14.493438488422054
3, average_error: 7.471988702528547
4, average_error: 6.446303516331285

PA(sensitivity:1.0)
0, average_error: 6.930944690137807
1, average_error: 9.624892684256677
2, average_error: 13.675553722192744
3, average_error: 6.750924747769195
4, average_error: 8.384036752375048

PA1(sensitivity: 1.0, regularization_weight: 0.1)
0, average_error: 6.9309446051569275
1, average_error: 9.62489216492908
2, average_error: 13.675555147983058
3, average_error: 6.750924861077035
4, average_error: 8.384036437385154

PA2(sensitivity: 1.0, regularization_weight: 0.1)
0, average_error: 6.930944718464767
1, average_error: 9.624892622881596
2, average_error: 13.675554354828181
3, average_error: 6.750924941336755
4, average_error: 8.384035638771437

CW(sensitivity: 1.0, regularization_weight: 0.01)
0, average_error: 4.698909892068052
1, average_error: 5.558364390323655
2, average_error: 6.540493751752498
3, average_error: 6.032211267830122
4, average_error: 13.968116860283477

AROW(sensitivity: 1.0, regularization_weight: 0.1)
0, average_error: 4.770141728325644
1, average_error: 8.567634939970356
2, average_error: 9.431066073049413
3, average_error: 4.763423338148852
4, average_error: 7.828405709904021

NHERD(sensitivity: 1.0, regularization_weight: 0.1)
0, average_error: 4.620869275839023
1, average_error: 7.289037596825325
2, average_error: 8.549463075694472
3, average_error: 7.791898671707304
4, average_error: 8.492799272395594

NN(method:lsh, nearest_neighbor_num:5, hash_num:256)
0, average_error: 22.35023978958576
1, average_error: 24.246441831673483
2, average_error: 29.78657178218582
3, average_error: 20.27616027229567
4, average_error: 16.042581992308456

cosine(nearest_neighbor_num:5)
0, average_error: 21.379422284234877
1, average_error: 23.30949099807456
2, average_error: 28.810803992559414
3, average_error: 19.3372816723172
4, average_error: 15.11391299030568

euclidean(nearest_neighbor_num:5)
0, average_error: 120.02288918825656
1, average_error: 179.29228290520086
2, average_error: 115.57568146356262
3, average_error: 252.4407271432404
4, average_error: 227.644220967812
```
