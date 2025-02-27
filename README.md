# Election Data Analysis

## Overview
This project analyzes the 2024 election results using Python. It processes election data to visualize and summarize key statistics, including party-wise seat distribution, the number of contested constituencies, winning margins, and the closest election battles.

## Features
- **Party-wise Seat Distribution:** Bar chart showing the number of seats won by each political party.
- **Constituencies Contested by Each Party:** Bar chart visualizing how many constituencies each party has contested.
- **Top 10 Closest Contests:** List of the 10 constituencies with the smallest winning margins.
- **Top 10 Largest Victory Margins:** List of the 10 constituencies with the highest winning margins.
- **Winning Margin Distribution:** Histogram to analyze the distribution of winning margins across constituencies.

## Data
The analysis is performed on `election_results_2024.csv`, which contains:
- **Constituency** - The name of the constituency
- **Leading Candidate** - The candidate who won
- **Leading Party** - The party of the winning candidate
- **Trailing Candidate** - The runner-up candidate
- **Trailing Party** - The party of the runner-up
- **Margin** - The difference in votes between the winner and runner-up

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/election-data-analysis.git
   cd election-data-analysis
   ```
2. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. **Run the Analysis:**
   ```bash
   python election_analysis.py
   ```

## Output
- `party_wise_seat_distribution.png` - Bar chart of party-wise seat distribution.
- `party_wise_constituencies_contested.png` - Bar chart of party-wise contested constituencies.
- `margin_distribution.png` - Histogram of winning margins.
- `election_analysis_results.csv` - Processed election results.

## Contribution
Feel free to contribute by submitting issues or pull requests. Suggestions for improvement are always welcome!

## License
This project is open-source under the MIT License.

## Author
Developed by **Pratik** 🚀

