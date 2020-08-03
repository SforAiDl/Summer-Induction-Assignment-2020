## Natural Language Processing

This question is based on natural language processing specifically, sequence classification or text classification. Text classification is a standard problem in NLP.

In this task, you will be given a dataset consisting of Reddit posts consisting of their content, title, author, and flair taken from a particular subreddit. You have to build an automated system that considers the provided data to detect the flair that should be assigned to a particular post, it is essentially a multi-class classification task.

For evaluation, F1 Scores [1] (micro average and macro average) will be considered.

Link to the dataset:
1.  [Train](data/train.csv)
2.  [Validation](data/val.csv)

  

### Complete the following tasks (In Order):

1. Design a Recurrent Neural Network (RNN / LSTM / GRU) based model utilizing Word Embeddings [2] to build a strong baseline.
2. Add an attention layer on top of LSTM outputs, and compare it with the baseline in Task 1. it is already implemented here.
3. Visualize the attention weights for some samples and write down a qualitative analysis.

  

### Important guidelines:

* A weak baseline performance for this question is given below, you must beat this baseline performance.

**Macro Averaged F1** | **Micro Averaged F1**
:-----:|:-----:
0.50|0.17

* The code won't be accepted without proper documentation and comments and mention your performance in the documentation.
* One should try to get the strongest baseline possible in Task-1
* There are various hyperparameters in RNN/LSTM/GRU layers, like hidden size, number of layers, dropout, directionality.
* Moreover, there can be various ways to take output from LSTM, last step, pooling, etc.
* You are given training and development datasets for analyzing your results however final evaluation will be done on a test set that will be made public at the end of the task.

### Bonus:
Improve the given model by making changes to the implementation in Task-1 and Task-2, you are free to use any techniques for improving your scores however usage of external datasets is not allowed.

### References:
1. https://en.wikipedia.org/wiki/F1_score
2. Introductory Blog to Word Embeddings
3. Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. “Neural machine translation by jointly learning to align and translate.” ICLR 2015.