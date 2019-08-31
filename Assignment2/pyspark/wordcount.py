#!/usr/bin/env python

import pyspark
import sys

if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]

sc = pyspark.SparkContext()
spamInput = inputUri + "/spam"
hamInput = inputUri + "/ham"

spam = sc.textFile(spamInput)
ham = sc.textFile(hamInput)

spamWords = spam.map(lambda email: email.split())
hamWords = ham.map(lambda email: email.split())

spamWords.saveAsTextFile(sys.argv[2] + "/spam_output")
hamWords.saveAsTextFile(sys.argv[2] + "/ham_output")
