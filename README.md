# NL_Assessment

Part 1 Q1<br />

Write a regex to extract all the numbers with orange color background from the below text in italics.<br />

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

Answer: using regular expression (regex) module we can simply extract numbers from the given list of string<br />

Part 1 Q2 <br />

From chrome reviews, goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. Deploy it using - Flask/Streamlit etc and share the live link.

1. Read the data from CSV file using pandas .<br />
2. Drop unnecessery coloumns<br />
3. filtered revies with rating 1<br />
4. using SentimentIntensityAnalyzer by importing nltk , gave a sentiment_score for each review.<br />
5. filtered good reviews by checking sentiment_score greater than 0.4<br />
6. printed out finl result<br />
7. used streamlit to deploy in website<br />

Part 1 Q3
Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute. Suggested questions:

1.Is there any co-relation between short description, long description and ranking?<br />
2.Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)? <br />
3.Does APP ID (Also known as package name) play any role in ranking? 4.Any other pattern or good questions that you can think of and answer?<br />

Answer:

Concept followed:
  to find correlation between categorical values , we need to perform chi-square test and p-value test.introduce null and alternate hyopothesis and based on tests reach in final conclusion.

1. Read the data from CSV file using pandas .<br />
2. Find the missing values in table and resolved<br />
3. since coloumns are categorical. we need to perform chi-square correlation on required columns<br />
4. check chi-square value and p value to analyze  correlations<br />

Part 2 Q1
Check if the sentence is Grammatically correct: Please use any pre-trained model or use text from open datasets. Once done, please evaluate the English Grammar in the text column of the below dataset<br />

Answer:
    i used pre-trained language tool (language_tool_python) .I accept the input as pandas dataframe and keep only the review text column, and pass this text one by one to the language tool to evaluate the grammatical correctness. If there are no mistakes - we print no mistakes, else the number of mistakes detected would be printed
    

Part 2 Q2 : Write about any difficult problem that you solved
     When u work in a company we have to face lot of difficult problems. But I doubt that I faced some issue which is exactly specified like in this question. Also by saying difficult problem I’m not sure whether that means coding problem or real life situation. Anyway, one thing that comes to my mind when thinking about solving problem which is happened recently in my work place.I’m currently working in a EdTech company. recently I got chosen in to new content development project work as the part of new product launch. Where everything was new to everyone in this team. So someone had to take responsibility to coordinate and guide other team members who are new to this platform.in that situation I initiated to lead the group and guide them to move in right direction.By this experience I came to understand that key solution to approach a problem is taking initiative and quick response.

Part 2 Q3
Formally, a vector space V' is a subspace of a vector space V if V' is a vector space every element of V′ is also an element of V.
Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
The set of pairs (a, a + 1) for all real a
The set of pairs (a, b) for all real a ≥ b
The set of pairs (a, 2a) for all real a
The set of pairs (a, b) for all non-negative real a,b

Answer:All the above properties are subspace of V


 
