# NL_Assessment

Part 1 Q1

Write a regex to extract all the numbers with orange color background from the below text in italics.

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

Answer: using regular expression (regex) module we can simply extract numbers from the given list of string

Part 1 Q2 

From chrome reviews, goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. Deploy it using - Flask/Streamlit etc and share the live link.

1 : Read the data from CSV file using pandas .<br />
2. Drop unnecessery coloumns<br />
3. filtered revies with rating 1<br />
4. using SentimentIntensityAnalyzer by importing nltk , gave a sentiment_score for each review.
5. filtered good reviews by checking sentiment_score greater than 0.4
6. printed out finl result
7. used streamlit to deploy in website

Part 1 Q3
Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute. Suggested questions:

1.Is there any co-relation between short description, long description and ranking?
2.Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)? 
3.Does APP ID (Also known as package name) play any role in ranking? 4.Any other pattern or good questions that you can think of and answer?

