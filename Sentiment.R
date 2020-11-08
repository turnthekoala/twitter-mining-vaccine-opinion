#set the working diretory for the project
#setwd("~/R/630 project")

library(twitteR)
library(stringr)
library(tm)
library(ggmap)
library(ggplot2)
library(dplyr)
library(plyr)
library(wordcloud)
library(streamR)
library(graph)
library(Rgraphviz)
library(topicmodels)
library(SnowballC)
library(cluster) 
library(fpc)
library(syuzhet)
library(lubridate)
library(scales)
library(reshape2)

#create sentiment df to determine vaccine sentiment
mySentiment <- get_nrc_sentiment(tweets.df$text)

#calculate the sentiment score
sentimentTotals <- data.frame((mySentiment$positive - mySentiment$negative))

# Simple Bar Plot 
counts <- table(sentimentTotals)
barplot(counts, main="Sentiment Distribution", 
        xlab="<-----Negative ---------- Neutral ---------- Positive----->", col="#4d94ff")
