# Validate Research
This is a repository for benchmarking state of the art research papers and proposed techniques for several machine learning tasks. Given there are hundreds if not thousands of machine learning tasks, we initially want to focus on deep learning tasks starting with NLP domain. 

## Table of Contents
* Motivation
* Data Format
	* Structure of this repository
	* Sample data from DUC2002 dataset.
	* Column meanings
* Usage
	* Command line example of the code
	* Flags and purpose
	* Sample config file
* Contributing
	* Step 1
	* Step 2
	* Step 3
* Reference
* Creators
* License


## Motivation
Given the fact that NLP community has seen lot of work in almost every existing fields like text summarisation, sentiment analysis e.t.c. there is a strong need to bring all the proposed works to a common platform to get a clear picture of improvements over the years and possible improvements in the future. One such work is done by [Armstrong et.al.](https://e.humanities.uva.nl/ireval/papers/paper_2.pdf) which is a good comparison of results published in a course of time for information retrieval tasks. We have picked a task of `text summarization` and focused on some papers which are mostly published in the last 15 years according to the citations (from google scholar) and the conferences in which papers got accepted.

## Data format

### Structure of this repository

* We have include some information and research that we did in the initial phase in a file named as `conferences_and_datasets.info`.
* The "data" directory has the metadata file named after the task as `text_summarization.meta`.
* A separate directory again named after the task as `text_summarization_datasets` where a separate file for each dataset name is present.
* For future addition of tasks, same format will be followed.
* Sample format of a dataset file is shown below.

### Sample data from DUC2002 dataset file
| METHOD | PAPER NUMBER | PROPOSED | TASK (optional) | ROUGE-1 | ROUGE-2 | 
| ------------- | -------- | -------- | -------- | -------- | -------- | 
| Peer 26 | 37 | 0 | 1 | 35.15 | 7.64 | 
| SVR | 37 | 0 | 1 | 31.56 | 6.78 | 
| R2N2 | 37 | 0 | 1 | 36.84 | 8.52 |
| NoTC | 37 | 1 | 1 | 34.02 | 7.39 |
| EmSim | 37 | 1 | 1 | 29.46 | 5.28 |
| SingleT | 37 | 1 | 1 | 36.54 | 8.44 |
| TCSum | 37 | 1 | 1 | 36.9 | 8.61 |

### Column meanings
* **METHOD:** All the method names that are referenced in a particular paper along with their own.
* **PAPER NUMBER:** In the CITATIONS file, a unique number is given all the papers which is referenced in this column.
* **PROPOSED:** If a method is proposed by that paper, this is 1, otherwise 0.
* **TASK:** This column is present only for those datasets which have a set of defined tasks and the the proposed results are for a particular task like in DUC2002, DUC2004 etc.
* **ROUGE-1, ROUGE-1, ROUGE-2, ROUGE-SU4, F1-SCORE:** Metrics for those the results are presented in the papers.


## Usage

### Command line example of the code
```
python main.py \
--dpi 100 \
--input data/text_summarization_datasets \
--metadata_file_path data/text_summarization.meta.csv \
--datasets_config_file_path config/config.yml
--out_dir graphs \
```

### Flags and Purpose
* **dpi:** The resolution of the plots to generate
* **input:** The directory name where all the `.csv` files of datasets are present.
* **metadata\_file\_path:** The file with `.meta.csv` extension one for each task.
* **datasets\_config\_file\_path:** A configuration file, as the name suggests, which has information about every dataset in terms of which task and metrics are involved (sample given below).
* **out\_dir:** The directory name where the plots are to be generated.

### Sample data of config.yml file (for DUC2002 dataset)
```
DUC_2002:
  tasks:
    - 1
    - 2
  metric:
    - ROUGE-1
    - ROUGE-2
    - ROUGE-SU4
    - F1-SCORE
```

## Reference
* Thanks to [this](https://github.com/mathsyouth/awesome-text-summarization) post which lists many papers in the field of text summarisation very nicely and so the necessary searching of the papers was not very much required for their initial selection.


## Contributing
### Step 1
* Option 1
	* Fork this repo.
* Option 2
	* Clone this repo at your local machine using `git clone https://github.com/vijaydaultani/validate_research`
	
### Step 2
* Make Directory for task you want add datasets for benchmarking in data directory.
* Create Dataset files in newly made or existing directory
* Create Meta data files in data/metadata directory
* Run Tests TODO: Make test cases

### Step 3
* Create a new pull request.

## Creators
### Vijay Daultani
* Personal Website: [here][Vijay Website]
* LinkedIn: [here][Vijay LinkedIn]
* Twitter: [here][Vijay Twitter]

### Mausam Jain
* LinkedIn: [here][Mausam LinkedIn]

## License
See the [LICENSE][] file here. 


[Vijay Website]: https://vijaydaultani.github.io/
[Vijay LinkedIn]: https://www.linkedin.com/in/vijaydaultani/
[Vijay Twitter]: https://twitter.com/vijaydaultani
[Mausam LinkedIn]: https://www.linkedin.com/in/mausam-jain-b65a2a93
[LICENSE]: https://github.com/vijaydaultani/validate_research/blob/master/LICENSE
[Github link]: https://github.com/vijaydaultani/validate_research