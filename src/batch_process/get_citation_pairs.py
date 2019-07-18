import pyspark
from pyspark.sql.window import Window
from pyspark.sql.types import *
from pyspark.sql.functions import udf, struct, col, rank
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import explode

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

df = spark.read.text("/Users/adawang/Desktop/sample-s2-records")

def get_id(line):
    parenthesis = "\"" 
    paper_id_tag = "\"id\""
    id_label_start = line.find(paper_id_tag)
    id_tag_start = id_label_start + 6
    id_tag_end = line.find(parenthesis, id_tag_start)
    id_tag = line[id_tag_start -1 :id_tag_end + 1] 
    return id_tag

def get_citations_list(line):
    '''
    Get the citation from the values 
    '''
    paper_citation_tag = "\"inCitations\"" # find the occurence of "inCitations"
    bracket = r"]" # look for "]"
    
    citation_label_start = line.find(paper_citation_tag) # index that the citation label starts  
    citation_tag_start = citation_label_start + 15 # index that the citation tag starts
    citation_tag_end = line.find(bracket, citation_tag_start)  # this is the index that the citation tag ends 
    if citation_tag_start == citation_tag_end: # if there are no citations: 
        num_citations = 0
        citation_list = []
    else:
        #citation_list = line[citation_tag_start:citation_tag_end].split(",") # make it a list, count number of entries
        #num_citations = len(citation_list) # number of citations 
        citation_list = line[citation_tag_start: citation_tag_end]
        
    #for citation in citation_list:
        
    return citation_list

def adding_ids(df):
    '''
    This function takes the raw data dataframe and adds on an id column for the data
    '''
    add_ids = df.withColumn("id", get_id_udf(df.value))
    return add_ids

def adding_citations_list(df):
    '''
    This function takes the raw data dataframe and adds on a citation column for the data
     '''
    add_citations_list = df.withColumn("citations_list", get_citations_list_udf(df.value))
    return add_citations_list

def drop_values(df):
    '''
    This function takes the dataframe and drops the value column"
    '''
    return df.drop(df.value)

get_id_udf = udf(lambda line: get_id(line), StringType())
get_citations_list_udf = udf(lambda line:get_citations_list(line), StringType())

df = adding_ids(df)
df = adding_citations_list(df)
df = drop_values(df)

df.createOrReplaceTempView("filtered_df")
df.printSchema()
results = spark.sql("SELECT * FROM filtered_df")
results.show()


from pyspark.sql.functions import col, split
results_new = results.select(col("id"), split(col("citations_list"), ",\s*").alias("citations_list"))

from pyspark.sql.functions import arrays_zip, col

results_explode = results_new.withColumn("citations_list", explode("citations_list"))

results_explode.show(500, False)
