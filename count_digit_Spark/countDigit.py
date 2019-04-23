#!/usr/bin/env python
# coding: utf-8

# In[44]:


from pyspark import SparkConf, SparkContext
    

if __name__ == "__main__":
    
    # create Spark Context
    sc = SparkContext.getOrCreate()
    
    # read .txt file
    lines = sc.textFile("sqrt(2).txt")
    lines = lines.map(lambda x: x.replace(" ","").replace(".",""))

    counts = lines.map(lambda x:[(c,1)for c in x])
    for row in counts.collect():
        print(sc.parallelize(row).reduceByKey(lambda x,y:x+y).sortByKey(ascending = True).collect())
        


# In[ ]:





# In[ ]:




