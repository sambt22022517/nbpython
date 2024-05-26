#!/bin/bash
test_home=$1
hdfs_input_file=$2
hdfs_output_folder=$3

if $(hdfs dfs -test -d $hdfs_output_folder/out_posterior) ; then hdfs dfs -rm -r $hdfs_output_folder/out_posterior; fi

mapred streaming \
	-file $test_home/mapper_test.py \
	-file $test_home/reducer_test.py \
	-mapper mapper_test.py \
	-reducer reducer_test.py \
	-cacheFile $hdfs_output_folder/out_conditional/part-00000#conditional \
	-cacheFile $hdfs_output_folder/out_prior2/part-00000#prior \
	-input $hdfs_input_file \
	-output $hdfs_output_folder/out_posterior
