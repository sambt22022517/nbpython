#!/bin/bash
train_home=$1
input_file=$2
output_folder=$3

if $(hdfs dfs -test -d $output_folder/out1); then hdfs dfs -rm -r $output_folder/out1; fi
if $(hdfs dfs -test -d $output_folder/out2); then hdfs dfs -rm -r $output_folder/out2; fi
if $(hdfs dfs -test -d $output_folder/out_prior); then hdfs dfs -rm -r $output_folder/out_prior; fi
if $(hdfs dfs -test -d $output_folder/out_prior2); then hdfs dfs -rm -r $output_folder/out_prior2; fi
if $(hdfs dfs -test -d $output_folder/out_conditional); then hdfs dfs -rm -r $output_folder/out_conditional; fi

mapred streaming \
	-file $train_home/mapper.py \
	-file $train_home/reducer.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-input $input_file \
	-output $output_folder/out1

mapred streaming \
	-file $train_home/mapper2.py \
	-file $train_home/reducer2.py \
	-mapper mapper2.py \
	-reducer reducer2.py \
	-input $output_folder/out1/part-00000 \
	-output $output_folder/out2

mapred streaming \
	-file $train_home/mapper_prior.py \
	-file $train_home/reducer_prior.py \
	-mapper mapper_prior.py \
	-reducer reducer_prior.py \
	-input $input_file \
	-output $output_folder/out_prior

mapred streaming \
	-file $train_home/mapper_prior2.py \
	-file $train_home/reducer_prior2.py \
	-mapper mapper_prior2.py \
	-reducer reducer_prior2.py \
	-input $output_folder/out_prior/part-00000 \
	-output $output_folder/out_prior2

mapred streaming \
	-file $train_home/mapper_conditional.py \
	-file $train_home/reducer_conditional.py \
	-mapper mapper_conditional.py \
	-reducer reducer_conditional.py \
	-input $output_folder/out1/part-00000 \
	-input $output_folder/out2/part-00000 \
	-output $output_folder/out_conditional
