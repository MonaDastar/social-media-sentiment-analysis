# Twitter Sentiment Analysis Project

This project analyzes Twitter data to determine the sentiment of tweets based on positive and negative word lists. It calculates positive scores, negative scores, and net scores for each tweet, and stores the results in a CSV file.

## Project Files

- `sentiment_analysis.py`: The main Python script for analyzing Twitter data.
- `project_twitter_data.csv`: Input CSV file containing Twitter data (Number of Retweets, Number of Replies, Tweet Text).
- `positive_words.txt`: List of positive words used for sentiment analysis.
- `negative_words.txt`: List of negative words used for sentiment analysis.
- `resulting_data.csv`: Output CSV file containing the analyzed data.

## Usage

1. Make sure you have the necessary input files (`project_twitter_data.csv`, `positive_words.txt`, and `negative_words.txt`).
2. Run the `sentiment_analysis.py` script.
3. The script will generate a new file called `resulting_data.csv` containing the analyzed data.

## How it Works

1. **strip_punctuation(wrd):** Removes punctuation characters from a word.
2. **get_pos(sentences):** Counts the number of positive words in a sentence.
3. **get_neg(sentences):** Counts the number of negative words in a sentence.

The main script reads Twitter data from `project_twitter_data.csv`, analyzes the sentiment of each tweet, and writes the results to `resulting_data.csv`.

## Result Columns

- **Number of Retweets**
- **Number of Replies**
- **Positive Score**
- **Negative Score**
- **Net Score**

## Example Command

```bash
python sentiment_analysis.py
# social-media-sentiment-analysis
