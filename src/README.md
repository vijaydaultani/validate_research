# Repository Name
NLP Benchmarks Comparison

## Motivation
* Reproducible research
* Given the fact that NLP community has seen lot of work in almost every existing fields like text summarization, sentiment analysis etc. there is a strong need to bring all the proposed works to a common platform to get a clear picture of improvements over the years and possible improvements in the future.
* One such work is done by [Armstrong et.al.](https://e.humanities.uva.nl/ireval/papers/paper_2.pdf) which is a really good comparison of results published in a course of time.


## Data format

### Structure of this repository

* We have picked up a task of "text summarization" and focused on some papers which are mostly published in the last 15 years. Thanks to [this](https://github.com/mathsyouth/awesome-text-summarization) post which lists many papers in the field of text summarization very nicely.
* We have made a kind of master file named as "CITATIONS" which contains all the papers that are compared in this task.
* Inside 'Tasks' directory we have made 'TEXT SUMMARIZATION' section (in future more sections can be added) inside which there is a single file for every dataset that have results for in the papers listed in master file.
* Format of this file is shown below.

### Sample data from DUC2002 dataset file
| METHOD | PAPER NUMBER | PROPOSED | TASK (optional) | ROUGE-1 | ROUGE-2 | ROUGE-SU4 | F1-SCORE |
| ------------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| Peer 26 | 37 | 0 | 1 | 35.15 | 7.64 | | |
| SVR | 37 | 0 | 1 | 31.56 | 6.78 | | |
| R2N2 | 37 | 0 | 1 | 36.84 | 8.52 | | |
| NoTC | 37 | 1 | 1 | 34.02 | 7.39 | | |
| EmSim | 37 | 1 | 1 | 29.46 | 5.28 | | |
| SingleT | 37 | 1 | 1 | 36.54 | 8.44 | | |
| TCSum | 37 | 1 | 1 | 36.9 | 8.61 | | |

### Column meanings
* METHOD: All the method names that are referenced in a particular paper along with their own.
* PAPER NUMBER: In the CITATIONS file, a unique number is given all the papers which is referenced in this column.
* PROPOSED: If a method is propsed by that paper, this is 1, otherwise 0.
* TASK: This column is present only for those datasets which have a set of defined tasks and the the proposed results are for a partcular task like in DUC2002, DUC2004 etc.
* ROUGE-1, ROUGE-1, ROUGE-2, ROUGE-SU4, F1-SCORE: Metrics for those the results are presented in the papers.


## Using the code to generate plots

### Flags and Purpose
* dpi: The resolution of the plots to generate
* input: The directory name where all the files named after datasets are present.
* metadata\_file\_path: The file name of the dataset for which the plots are to be generated.
* out\_dir: The directory name where the plots are to be generated.
* metric\_start\_column: Column number in the dataset file from where the metrics start. For example in the above sample data, metrics start from column number 5.
* metric\_end\_column: Column number in the dataset file from where the metrics end. For example in the above sample data, metrics start from column number 8.


### single dataset command line example

### multiple datasets command line example

```
python main.py
--dpi 100
--input ROOT/datasets
--metadata_file_path ROOT/metadata/CITATIONS\ -\ Sheet1.csv
--out_dir ROOT/graphs
--metric_start_column 5
--metric_end_column 7
```

## Contributors
### Vijay Daultani
* Website:
* LinkedIn:
* Twitter:

### Mausam Jain
* [LinkedIn](www.linkedin.com/in/mausam-jain-b65a2a93)

