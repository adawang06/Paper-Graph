import pyspark
from pyspark.sql.window import Window
from pyspark.sql.types import *
from pyspark.sql.functions import udf, struct, col, rank
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.session import SparkSession

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

def get_title(line):
    # look for the title of the paper and return the tag 
    paper_title_tag = "\"title\""
    parenthesis = "\""
    
    title_label_start = line.find(paper_title_tag) # index for the title label start 
    title_tag_start = title_label_start + 9
    title_tag_end = line.find(parenthesis+",\"", title_tag_start) 
    title_tag = line[title_tag_start:title_tag_end]
    return title_tag

def adding_ids(df):
    add_ids = df.withColumn("id", get_id_udf(df.value))
    return add_ids

def get_title(line):
    '''
    This function takes the raw data dataframe and get the title column for the data
    ''' 
    paper_title_tag = "\"title\""
    parenthesis = "\""
    
    title_label_start = line.find(paper_title_tag) 
    title_tag_start = title_label_start + 9
    title_tag_end = line.find(parenthesis+",\"", title_tag_start) 
    title_tag = line[title_tag_start:title_tag_end]
    
    return title_tag

def adding_ids(df):
    '''
    This function takes the raw data dataframe and adds on an id column for the data
    '''
    add_ids = df.withColumn("id", get_id_udf(df.value))
    return add_ids

def adding_titles(df):
    '''
    This function takes the raw data dataframe and adds on an title column for the data
    '''
    add_titles = df.withColumn("title", get_title_udf(df.value))
    return add_titles


def drop_values(df):
    '''
    This function takes the dataframe and drops the value column
    '''
    return df.drop(df.value)

get_id_udf = udf(lambda line: get_id(line), StringType())
get_title_udf = udf(lambda line: get_title(line), StringType())

df = adding_ids(df)
df = adding_titles(df)
df = drop_values(df)

df.show()
df.cache()

from pyspark.ml import Pipeline
from pyspark.ml.feature import RegexTokenizer, NGram, HashingTF, MinHashLSH
import pyspark.sql.functions as f

model = Pipeline(stages = [RegexTokenizer(pattern = "", inputCol = "title", outputCol = "tokens", minTokenLength = 1), 
                           NGram(n = 3, inputCol = "tokens", outputCol = "ngrams"),HashingTF(inputCol = "ngrams", outputCol = "vectors"), MinHashLSH(inputCol = "vectors", outputCol = "lsh", numHashTables = 10)]).fit(df)

df_hashed = model.transform(df)


df_matches = model.stages[-1].approxSimilarityJoin(df_hashed, df_hashed, 0.9)

#show all matches (including duplicates)
df_matches.select(f.col('datasetA.id').alias('id_A'),
                 f.col('datasetB.id').alias('id_B'),
                 f.col('distCol')).show()

#show non-duplicate matches
df_matches.select(f.col('datasetA.id').alias('id_A'),
                 f.col('datasetB.id').alias('id_B'),
                 f.col('distCol')).filter('id_A < id_B').show()
