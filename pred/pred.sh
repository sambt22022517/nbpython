#!/bin/bash

pred_home=$1
input_file=$2
output_folder=$3


if $(hdfs dfs -test -d $output_folder/out_pred) ; then hdfs dfs -rm -r $output_folder/out_pred; fi

mapred streaming \
        -file $pred_home/mapper_pred.py \
        -file $pred_home/reducer_pred.py \
        -mapper mapper_pred.py \
        -reducer reducer_pred.py \
        -cacheFile /output/out_conditional/part-00000#conditional \
        -cacheFile /output/out_prior2/part-00000#prior \
        -input $input_file \
        -output $output_folder/out_pred
