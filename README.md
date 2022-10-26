### NLP-Disaster-Tweets
##### Problem Description
    This problem related to Predict which Tweets are about real disasters and which ones are not
    
    link : https://www.kaggle.com/competitions/nlp-getting-started/overview/description
    
##### Preprocessing text data 
     1. Remove punctuation
     2. make all words to lower case 
     3. take token(Word) From sentence
        Here i used TensorFlow to get a token, so Token class itself can do (1,2,3) step
##### create a model
     1. here i took Embedding layers to cluster similar kind of words 
     2. RNN to understand sequence pattern
     3. Dense layer
##### Evaluvation of the model
     got more than 73% accuracy in validation set
##### Save the model and preprocessing object using Pickle 

##### Use Flask to deploy the model
