import org.apache.spark.sql.types._
import org.apache.spark.ml.feature._
import org.apache.spark.ml.linalg._

val df = spark.read.option("delimiter","\t").csv("/Users/adawang/Desktop/sample-s2-records")
val dfUsed = df.select(col("_c1").as("id"), col("_c2").as("title")).filter(col("title") !== null)
dfUsed.show()

// Tokenize
val tokenizer = new Tokenizer().setInputCol("title").setOutputCol("tokens")

// 3gram
val ngram = new NGram().setN(3).setInputCol("tokens").setOutputCol("ngrams")

// vectorization
val vectorizer = new CountVectorizer().setInputCol("ngrams").setOutputCol("vectors")

// final pipeline
val pipelineTV = new Pipeline().setStages(Array(tokenizer, ngram, vectorizer))

val modelTV = pipelineTV.fit(dfused)

val isNoneZeroVector = udf({v: Vector => v.numNonzeros > 0}, DataTypes.BooleanType)

val df_TV = modelTV.transform(dfUsed).filter(isNoneZeroVector(col("features")))

val lsh = new MinHashLSH().setNumHashTables(10).setInputCol("features").setOutputCol("hashValues")
val pipelineLSH = new Pipeline().setStages(Array(lsh))
val modelLSH = pipelineLSH.fit(df_TV)

val df_hashed = modelLSH.transform(df_TV)

val df_matches = modelLSH.stages.last.asInstanceOf[MinHashLSHModel].approxSimilarityJoin(df_hashed, df_hashed, 0.9)
df_matches.show()
