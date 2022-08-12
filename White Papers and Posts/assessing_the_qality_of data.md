## Bottom Line Up Front

To gain a better appreciation and understanding of the quality of a given dataset, I suggest asking questions in three categories:

Fundamental Questions

-   Can the data be used for its intended purpose?
    
-   Is the acquisition, storage, and management of the data sustainable?
    

Basic Questions

-   Is the data malformed?
    
-   Is the data encoded properly?
    

Advanced Questions

-   Can the data be trusted?
    
-   Is there alignment about terms in the data?
    
-   Are there data gaps?
    

## Intro

“Data is the new gold” is an expression that is becoming so common it is on the verge of being cliché. Indeed, virtually every individual, team or organization in our society recognizes the value of data. But most don’t know how to assess the quality of their data.

The purpose of this post is to share a perspective on how to assess data quality. Specifically, I outline three categories of questions to ask of data to help gain a better understanding of its utility.

1.  Fundamental questions on the intended use of the data
    
2.  Basic questions on the data itself
    
3.  Advanced questions on the context and understanding of the data
    

## Fundamental Questions

While it might seem obvious, the most important and basic question to ask of data is if it can be used for its intended purpose. This is not a trivial question, as it is quite easy to pay for data, either directly or through labor costs, that wouldn’t be useable even if it were in perfect condition.

For instance, consider the standoff that is currently taking place between many grocery store chains and Instacart. Instacart is a web application that allows shoppers to grocery stop online, then have a personal shopper pick up the goods in person on their behalf. This seems like it would be a great deal for grocery stores, but not quite. Instacart keeps the data on the individual shoppers, meaning grocery stores do not have the opportunity to study individual level shopper preferences. As a result, the grocery stores lose out on the opportunity to improve their business with this data (e.g. advertising, forecasting demand, etc.)

Many grocery stores are therefore seeking to break ties with Instacart. This is ironic, as grocery stores have a reputation for poor investment in technology. Many of the firms who are seeking to de-list with Instacart do not have a well-developed digital marketing capability, meaning they won’t be able to optimize the use of customer-level shopping data if they get it anyhow.

The main point: such firms are most likely not able to use the data for the purposes for which it would be intended. Thus, the most fundamental question of data is this simple: can I use it?

Another related, fundamental question of data is if its acquisition, storage, and management is sustainable. For instance:

1.  Is the cost/benefit analysis intact?
    
2.  Is the data in a proprietary database?
    
3.  Is the SLA appropriate?
    

Note that these three basic questions are not “IT” questions, but rather business decisions. Alignment in service level agreements (SLAs), for example, requires close collaboration between financial leaders, legal experts, and data experts. To highlight this point, consider the following: If a company enters into a service level agreement with a third party who agrees to provide them data every 24 hours, but the company needs to make decisions with that data every 15 minutes, then the company will almost certainly not be able to fully use that data. Conversely, if a company enters into a service level agreement with a third party who agrees to provide them with data every 15 minutes, but the company only needed that data every 24 hours, then the company will almost certainly be overpaying in that agreement.

## Basic Questions

Simply put, if your data looks like this….

ñÃ`?ÍÊÀ/È/%??,Ë%Ñ,ÁÈÇÑË`?ÍÎÁÅ?ÈøÊ?Â%Á_

…then you’ve got a problem. And even if it seems legible, it does not necessarily mean all the data is encoded the same way. One has to check to confirm.

To a computer, data is just a string of ones and zeros. But to be able to interpret the data properly we need to know exactly how to turn those ones and zeros into text. This is not always obvious, because there are lots of different encodings out there (utf-8, ascii, latin1, windows, unix, mac, etc).

Because data is often derived from multiple sources throughout the world, it is common to find data with multiple types of encodings. For example, when you go to a website and see bizarre characters interspersed with regular English characters, that's usually an encoding/decoding problem.

The next level of questions to ask of data, therefore, are simply around its encoding. Specifically:

1.  Is the data malformed?
    
2.  Is the data encoded/decoded properly?
    

Like the previously mentioned fundamental questions, these basic questions may seem obvious, but encoding inconsistencies are surprisingly frequent. Data gleaned from Microsoft Excel spreadsheets, for instance, are notorious for having encoding problems. In particular, data gleaned from Excel docs in multi-national companies can be especially troublesome. These questions are therefore a vital question when assessing data quality.

## Advanced Questions

Assuming you can use the data, and that it is encoded properly, you still have to be able to trust the data and understand it in context. There must necessarily be alignment on assumptions and definitions of the data.

Consider a financial advisory company, for example. Data on a “user” could mean different things to different teams. A finance team would probably only consider a “user” to be someone who is actually exchanging services (paying) with the company. A marketing team, however, might define a “user” as anyone who listens to the company’s free podcasts on financial advice. Such misunderstandings among terminology can create significant confusion when recording and working with data.

Because issues of this type are so common and are such a challenge to effectively using data, we have covered some best practices to avoid them in a separate podcast and white paper titled “Brilliance in the Basics.” Both the podcast and paper are freely available on our website and Patreon page.

Another important question to consider is the completeness of data. Are there gaps and, if so, are the gaps on a regular interval or are they episodic? Gaps in data are fairly common, so do not necessarily mean data is unusable. They do, however, present challenges which must be carefully considered. There are numerous approaches to working through gaps in data, none of which are inherently good or bad, but must be considered in relation to each specific situation.

A good summary of contextual questions on data quality, therefore, follows:

1.  Can you trust the data?
    
2.  Is there alignment around the terms?
    
3.  Do you share the same assumptions as the program/person who generate the data?
    
4.  Are there gaps in the data and, if so…
    
5.  How much data is missing?
    
6.  Are the gaps regular or episodic?
    

## Summary

This post articulates a framework of categories for assessing data quality:

1.  Fundamental questions
    
2.  Basic questions
    
3.  Advanced questions
    

The questions listed within each of the categories are valuable, but are included simply to add clarity to our main points. These questions are not meant to be a comprehensive analysis. Such an analysis would be dependent on the specific data sources in question.