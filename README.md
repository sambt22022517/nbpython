## Hướng dẫn cách chạy
1. Khởi động server để chạy hdfs
   ```
   service shh start
   ssh localhost
   start-all.sh
   ```
2. Chuẩn bị file hdfs \
   Thấy 3 file train.txt, test.txt, pred.txt không, cho hết chúng lên hdfs đi.
   ```
   hdfs dfs -mkdir /input
   hdfs dfs -copyFromLocal train.txt /input
   hdfs dfs -copyFromLocal test.txt /input
   hdfs dfs -copyFromLocal pred.txt /input
   hdfs dfs -mkdir /output
   ```
3. Chạy train, test, pred \
   Cú pháp chạy cả 3 ý hệt nhau: `sh <type>/<type>.sh <parent_folder_of_type.sh> <hdfs_input_file> <hdfs_output_folder>` \
   Với cả 3 file nếu chuẩn bị file đúng như 2 thì:
   ```
   sh train/train.sh train /input/train.txt /output
   sh test/test.sh test /input/test.txt /output
   sh pred/pred.sh pred /input/pred.txt /output
   ```
   ***Không biết sao, nhưng phải chạy ở parent_folder của `train`, `test`, `pred` thì mới được, nên là chú ý nha!!!***
5. Xem kết quả \
   Kết quả của từng quá trình được lưu tương ứng ở:
   - train: out_prior2, out_conditional
   - test: out_test
   - pred: out_pred \
   `hdfs dfs -cat <hdfs_output_folder>/part-00000`
6. Phụ lục
   * Có thể thay thế file train, test, pred bằng một file khác với quy định như sau:
     - Đối với train và test, từng dòng phải có cú pháp: `<label>\tab<sentence>`
     - Đối với pred: `<sentence>`
   * Đối với việc lỗi ở phân 1, khởi động server: Chịu rồi~~~
