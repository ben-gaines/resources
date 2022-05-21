## Thanks to S.T.O.P. for Inspiring This Post

Many of the perspectives put forth in this white paper were inspired through a lecture I attended by the [Surveillance Technology Oversight Project](https://www.stopspying.org/). I have tremendous respect for the members of S.T.O.P. Accordingly, I would encourage anyone to visit their site to learn more about their work and to support their efforts in ending discriminatory surveillance.

## Bottom Line Up Front

There are several ethical causes for concern with Artificial Intelligence (AI). Yet the use of AI will continue to rise over the coming decades. Ethical Review Boards (ERBs) are an effective means to mitigate these concerns. ERBs are standing review boards which occur during the development or implementation of AI-powered tools. The four components of ERBs include:

1.  Fairness Testing
    
2.  Human-Impact Assessments
    
3.  Human Control Assessments
    
4.  Transparency & Clarity Testing
    

## Overview

The purpose of this post is to share a perspective on AI Ethical Review Boards, an effective technique for combatting the ethical hazards of working with AI. This post covers:

1.  A brief overview of AI
    
2.  Two major causes for concern with AI
    
3.  A few examples of AI doing harm
    
4.  Ethical Review Boards
    

## A Brief Overview of AI

Artificial Intelligence simply means using computer systems to perform tasks that typically require human intelligence. The top of mind example of AI for most people is self-driving cars. While this certainly is an example, it is a sophisticated use case. Simple tools like autocorrect, autofill, and chatbots are also examples of AI, though they often aren’t considered as such. In fact, AI is all around us and is a major factor in our daily lives. The recommendations pages on Netflix, the routes determined on Google Maps, the spam filters in email services… all of these are AI.

Because there are so many uses cases under the AI umbrella, a good way to think about AI is to consider its use cases in terms of the type of data used: structured or unstructured. Structured data is derived from standardized, repeatable procedures and lends itself well to automation. Unstructured data is derived from multiple, often unique procedures and requires significantly more effort to develop tools with. AI is predominately concerned with the use of unstructured data.

## Two Major Causes for Concern with AI

Search for “AI Concerns,” “AI Risk,” or any such term and it doesn’t take long to notice that there are a lot of blog posts about the AI-powered machines turning “evil” or “corrupt.” Such blogs are red-herrings. The real concern with AI isn’t about malevolence, but competence. The danger with AI in our present time are its uses in areas wherein it is not sufficiently developed or qualified. Specifically, there are two areas of concern:

1.  Unfair algorithms
    
2.  Biased models
    

These concerns are similar, but they are not one and the same. I will share a few examples of these later in this post. But it first makes sense to give an overview of what we mean by these terms.

Unfair algorithms is an emerging term that, like “Artificial Intelligence,” lacks a commonly accepted definition. Generally speaking, unfair algorithms are systemic flaws in an algorithm that create unfair outcomes like privileging one group of persons above another. More often than not, such algorithms are not designed to be unfair. Rather, they evolve and become unfair because they fail to account for unintended consequences in the way data is collected, coded, and selected to be used to train the algorithm.

Biased models also create unfair outcomes. They do so not because a systemic flaw in an algorithm, but instead because of a non-representative sample of a given type of data in the model. The statistical term for such misrepresentation of data in a model is “Selection Bias.” I try not to get too anchored in academic terms, however. Instead, I like to represent this statistical concept with the simple phrase – Garbage in, Garbage out. In short, if a model is being populated with data that already reflects human bias, the model will reflect that bias. Similarly, if a model is overly-populated with certain data features, it will overly-return those features.

## Examples of AI Doing Harm

There are several examples of AI doing harm, and I’d encourage anyone to research this on their own. To add clarity to the above points on unfair algorithms and biased models, however, here are two examples:

1.  Search Engines and [Data Voids](https://datasociety.net/wp-content/uploads/2018/05/Data_Society_Data_Voids_Final_3.pdf)
    
2.  [COMPAS recidivism](https://github.com/propublica/compas-analysis)
    

A “data void” is an emerging term to indicate a search term for which the available relevant data is limited, non-existent, or deeply problematic. The Data and Society white paper linked above does an outstanding job of explaining data voids. (Thank you to Michael Golebiewski and Danah Boyd for your thoughtful work.) I strongly suggest reading their white paper and intend to provide additional commentary in future white posts of my own. For this post, however, I simply wish to reference data voids insofar as they relate to increasingly unfair search algorithms.

In short, search algorithms (AI) draw upon available information from URLs to make a prediction on what content a user will most likely find relevant. The protocols used by search engines generally the same for any term entered into the engine. In that regard, one could easily claim that search engines are “fair.”

The algorithms that power these search engines, however, fail to account for the unintended consequences of data voids. As explained in Data and Society’s white-paper, the term “black on white crime” is a data void. When searched, it returns deeply problematic, racist content. This is because the majority of content around this phrase is being generated by white supremist communities. Yet the average search engine returns this content to a user all the same. In doing so, they unwittingly allow for the spread of biased, hateful speech and opinions.

Another example of AI doing harm can be found through an analysis of the COMPAS recidivism algorithm by Jeff Larson, Surya Mattu, Lauren Kirchner and Julia Angwin (linked above). COMPAS is an acronym for Correctional Offender Management Profiling for Alternative Sanctions. COMPAS software uses an algorithm to assess potential recidivism risk and can be used by judges during sentencing.

In the aforementioned analysis, it was demonstrated that black defendants were often predicted to be at a higher risk of recidivism than they actually were. In fact, the analysis showed that black defendants who did not recidivate over a two-year period were nearly twice as likely to be misclassified as higher risk compared to their white counter parts (45% vs. 23%). In contrast, white defendants were often predicted to be less risky than they were. The analysis showed that white defendants who re-offended within the next two years were mistakenly labeled low risk almost twice as often as black re-offenders (48% vs. 28%.)

Clearly a reliance on such a model to assess judgement on an individual is hazardous.

## Ethical Review Boards

To mitigate ethical risk and concerns when working with AI, I suggest implementing what I have termed “Ethical Review Boards,” or ERBs for short. ERBs are simply standing meetings that occur during the development or implementation of AI-powered tools. The purpose of these meetings is not to assess the functionality of such tools, but rather their ethical implications. Of course, this is a huge topic, meaning such a meeting could become unstructured and misguided quite quickly if not properly managed. I therefore suggest focusing ERBs in four areas:

1.  Fairness Testing
    
2.  Human-Impact Assessments
    
3.  Human Control Assessments
    
4.  Transparency & Clarity Testing
    

I suggest conducing fairness testing in three ways:

1.  Exclude all racial, gender, sexual orientation, etc. features from the data and compare the results against a model which includes them
    
2.  Test error rates for protected groups in the model and compare them against error rates from non-protected groups
    
3.  Test positive outcomes for protected groups against positive outcomes for non-protected groups
    

We suggest discussing and evaluating the human-impact of the tools developed during ERBs. A few questions for discussion could include:

1.  Would people be upset if they found out they are a part of this model?
    
2.  What are the consequences of a positive or negative prediction?
    
3.  If this tool/model works, will people be better for it?
    

I also suggest using ERBs for discussing and evaluating the human-control of AI tools under development or in implementation. A few questions for consideration include:

1.  Do users have an option for opting in/out of this tools?
    
2.  Does this tool have human oversight?
    
3.  Can the tool/model be retrained in a timely manner if predictions are wrong?
    

Lastly, ERBs should be used to assess the transparency and clarity of tools. For example:

1.  Can the factors that played a role in this decision be easily understood/explained?
    
2.  Can users of the tools understand/explain the decisions from the tool?
    
3.  Is there a process for fixing errors in understanding?
    

## Conclusion

Like most forms of engineering, working with AI has inherent risks. Some of them are ethical. There are several ways to combat these ethical concerns, Ethical Review Boards are but one. What I like so much about ERBs is that, when done consistently, they can bolster the overall ethical decision making culture of a firm. Furthermore, implementing ERBs is fairly easy to do. I therefore encourage any firm working with AI to add ERBs to their standard operating procedures, and hope the questions included in this white paper help structure the conversation.