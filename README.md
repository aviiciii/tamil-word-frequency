# Tamil Words Frequency Processing

This repository provides a Python script that allows for efficient filtering and processing of words and their frequencies in a CSV file. The script focuses on filtering non-Tamil words and removing trailing punctuation from a large dataset.

## Description

The Word Filtering and Frequency Processing script is designed to handle large datasets efficiently. It filters out non-Tamil words and removes trailing punctuation marks, resulting in a cleaner and more meaningful word-frequency dataset. The processed data can be used for various linguistic research, natural language processing tasks, and data analysis purposes.

## Features

- Word Filtering: The script filters out non-Tamil words from the input CSV file, providing a cleaner dataset for Tamil language analysis.
- Trailing Punctuation Removal: The script removes trailing punctuation marks from words, enhancing data quality and compatibility with natural language processing tasks.
- CSV Output: The processed words and their frequencies are saved in a CSV file, making it easy to integrate the results into downstream applications.

## Output Info

The latest version with 3 large datasets can be found in the `./output/v3` directory.

- It has tamil words ordered by frequency from top 100 to top 1,00,000.
- If you require a larger set of data (there is a lot). Reach me at [my email](mailto:laavesh1@gmail.com).

## Python Scripts
The collection of Python scripts that facilitate the processing, analysis, and generation of outputs from a dataset. The scripts are designed to perform specific tasks sequentially to achieve the desired results. The scripts included in this repository are as follows:

1. `pre-process.py` : This script is responsible for preprocessing the dataset to standardize the data. It prepares the input data for further processing by applying necessary transformations, cleaning steps, or standardization techniques.

2. `main_process.py` : The main functionality of this script is to calculate the frequencies of words in the preprocessed dataset. It analyzes the text and generates word frequency information, which can be useful for various applications such as text analysis, language modeling, or information retrieval.

3. `clean_output.py` (Optional): If the dataset contains non-Tamil words, punctuations, or any unwanted characters, this script can be used to clean the output. It provides functionality to remove non-Tamil words, punctuation marks, or any specified set of characters from the dataset.

4. `add_frequencies.py` : This script allows you to add the frequencies of the existing output to the new output. It merges or combines the word frequencies from different sources to provide a comprehensive analysis of the entire dataset.

5. `post_process.py` : The primary purpose of this script is to generate a new release of outputs. It sorts the output based on frequency or any other specified criteria and creates a summary of the processed data. This script provides options to customize the sorting order and control the summary generation process.


## Dataset Credits

Total count of words: 45,91,656 🚀

This project utilizes multiple datasets (thank YOU!)

1. https://www.kaggle.com/datasets/praveengovi/tamil-language-corpus-for-nlp
2. https://github.com/KaniyamFoundation/all_tamil_words/blob/master/words_and_frequency.tar.bz2
3. https://github.com/ajithalbus/TamilCorpus/


If you use this dataset, please provide appropriate credits and citations to the above sources for their contribution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Please note that this repository is intended to provide a general-purpose script and utilizes external datasets. Contributions related to algorithm optimization, code enhancements, and additional features are highly appreciated.

