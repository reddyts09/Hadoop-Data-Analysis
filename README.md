# Hadoop Data Analysis
This assignment wants us to use hadoop to build mapper and reducer scripts that analyze the csv file and then yield summary counts for each vehicle

# Configuration Details:
1. To connect to the Hadoop Web Server:
- ssh reddyts@hadoop-gate-0.eecs.uc.edu

2. Use git command to clone the project from github:
- git clone https://github.com/reddyts09/cloud4.git

3. Change the directory to access the mapper and reducer script files:
- cd cloud4

4. Add the reducer and mapper script files to the hadoop cluster:
- hadoop fs -put mapper_tarun.py ./mapper_tarun.py
- hadoop fs -put reducer_tarun.py ./reducer_tarun.py

5. Run the twp scripts using the following hadoop mapreduce command:
- hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper_tarun.py -mapper mapper_tarun.py -file reducer_tarun.py -reducer reducer_tarun.py -input /user/tatavag/nyc.data -output /user/reddyts/tarunop/

6. In order to get the output type the following command:
- hadoop fs -get tarunop

7. To view the output type:
- cd tarunop
- cat part-00000

# Built With
- Hadoop: Web Cluster
- Python: Programming Language used
- Github: Repository for code

# Acknowledgements
I Thank Prof.Giridhar for provding me with the opportunity to work on this assignment that deals with hands on experience with Hadoop Cluster and Python Programming.
