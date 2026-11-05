
import pandas as pd

marks = pd.Series([50,90, 45,85, 95], index=["rifa","Rita", "keya","Mita", "amit"])
print(marks)

# updating amit's marks
marks['amit']= 35

# size fun - gives no. of elements
print("size:",marks.size)

# mean fun - avg marks
print("mean:", marks.mean())

# only marks above 50
print(marks[marks> 50])