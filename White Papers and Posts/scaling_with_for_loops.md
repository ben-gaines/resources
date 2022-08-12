## Bottom Line Up Front

Most businesses and organizations understand the advantages of “scalable” processes. Unfortunately, this term can be broad and there are few useful frameworks for evaluating processes to estimate how they might be made more scalable. One technique I often suggest is to narrow the scope of the question. Instead of asking “How can this process be made more scalable?”, I suggest asking “How can this process be executed in a for loop?”

## Overview

The purpose of this post is to provide a mental model to assess & improve processes to make them more scalable. The post is divided into three parts:

1.  Explanation of the term “scalable”
    
2.  Overview of “for loops”
    
3.  Designing processes as “for loops”
    

## What Does it Mean to be “Scalable?”

Like so many terms in technology, “scalable” does not have a standardized definition. I use it here to indicate a technology, application, or process that can complete larger volumes of work without needing to add a commensurate amount of resources. To clarify this definition, consider a few examples in education:

1.  **Monitoring Exams is an Example of a Non-Scalable Process** Most schools and/or standardized test agencies have a required ratio between test-takers and monitors. Generally, for every ~30 students taking a test, there must be at least one qualified individual physically present to supervise the exam. Accordingly, there is no way to expand the capacity for monitoring test-takers without adding the requisite amount of monitors. The process of monitoring a test could therefore be considered non-scalable.
    
2.  **Grading Multiple Choice Exams is an Example of a Scalable Process** Multiple choice exams have a clearly defined answer key and a finite number of possible answers. Grading these exams by hand is, of course, not scalable for the same reasons that monitoring exams isn’t scalable. When the grading is automated, however, the process becomes completely scalable. An algorithm that is capable of grading 30 multiple choice exams is just as capable of grading 300,000. No additional resources would be needed to complete larger volumes of work (grading exams).
    

Admittedly, the above examples are simplistic. They do, however, identify the fundamental issue behind assessing scalability in processes: the ratio of resources needed to output generated. One monitor can observe ~30 test-takers, but one algorithm can grade a nearly infinite amount of multiple choice exams.

Great, data-driven, organization find ways to make as many processes as possible scalable. A good way approach this endeavor is to determine if/how a process can be incorporated into a for loop.

## Overview of “For Loops”

For Loops are a relatively common practice in programming and are quite useful when applied in data science. Any programmers reading this post should already be familiar with Loops. For anyone new to the concept, however, the best way to explain For Loops is through a series of short questions. Consider, then the following:

What is the largest number in the following list?:

[88, 97, 95, 94, 81, 95, 92, 89, 82, 91]

Pretty straight-forward question, right? But consider how you realized 97 was the greatest number in this list. If you are like most people, you probably didn’t have a pre-conceived idea of what the largest number is. That’s to say you started off with 0 in mind. You then looked at the first number: 88. This number was greater than 0, so 88 became the largest number. You then looked at the second number: 97. This number was greater than 88, so 97 became the largest number. You then looked at the third number: 95. This number was not greater than 97, so 97 remained the largest number. You then repeated this process until you had looked through the entire list.

This process works on small lists of numbers, but what about this list:

[101957375, 101997647, 101966556, 101861556, 101924259,101932989, 101873667, 101893963, 101976584, 101948335, 101942355, 101910514, 101903144, 101970232, 101897938, 101926983, 101943788, 101854411, 101913103, 101902817, 101938990, 101870298, 101854341, 101888667, 101941060, 101929071, 101948146, 101992676, 101855023, 101908734]

Obviously, this list isn’t as easy, and it is still only 30 numbers. Though the aforementioned process for finding the largest number clearly works, it is easy to see that there are limits to how far a human can take it.

Fortunately, For Loops work basically the same way people do. They just don’t face the same limitations. Here is how the first question would be solved by a for loop:

--------------------

list = [88, 97, 95, 94, 81, 95, 92, 89, 82, 91]

max = 0

for number in list:

    if number > max:

        max = number

    else:

        continue

print(max)

97

--------------------

If you aren’t familiar with code, don’t be dizzied by the above statement. Look at it line by line; it is the exact same logic used previously. First, a list was given to the program. With it, a variable, “Max” was set to zero. Then the program simply states to look at each number in the list. If that number is bigger than “Max” (which was set to zero to start), then “Max” becomes that number. If the number is not bigger than “Max,” continue on to the next number in the list. Lastly, the program says to print “Max” when it is done comparing it to each number in the list. This, of course, prints 97, because it is the largest number in the list.

Unlike people, the For Loop is capable of running this logic on massive scale. Passing a list of 30 number, 300 number, and 3000 numbers is all the same. Here is the same program applied to the larger set of 30 numbers:

--------------------

list = [101957375, 101997647, 101966556, 101861556, 101924259, 101932989, 101873667, 101893963, 101976584, 101948335, 101942355, 101910514, 101903144, 101970232, 101897938, 101926983, 101943788, 101854411, 101913103, 101902817, 101938990, 101870298, 101854341, 101888667, 101941060, 101929071, 101948146, 101992676, 101855023, 101908734]

max = 0

for number in list:

    if number > max:

        max = number

    else:

        continue

print(max)

101997647

--------------------

## Connecting Business Processes to “For Loops”

The above example highlights how a process – finding the largest number – can be made scalable by placing it in a for loop. Following this logic, truly savvy businesses seek to make all of their processes scalable. Integrating them into For Loops is a great way to do so. To make this point more clear, here is an example from some work I did for a client in Private Equity.

As a private equity firm, my client continuously seeks to find new opportunities to invest in privately held businesses. Most of these opportunities come from business brokers who have entered into seller listing agreements with business (think real estate agents, but for businesses). The process most private equity firms use for finding business brokers is what one might expect. First, they leverage their networks to see if anyone in their network is aware of suitable deals. Secondly, and just as frequently, they browse business broker websites to look for interesting listings. Like the initial example of finding the largest number, this process doesn’t scale. A person can only browse so many business broker websites. So my forward-thinking client asked me to help them scale this process. Just like the example of finding the largest number in a list, I scaled their process for finding deals by working it into a For Loop. In doing so, I followed the same process they use, but made sure every step is in a scalable for loop.

First, I took a list of the websites which provide registries of business brokers. I wrote a For Loop to visit each of those sties and return another list with all of the business broker names and websites from the initial list. (This is called “scraping” a site, and will be addressed in a separate post). Then I took the second list of business broker names and websites and wrote another For Loop to visit each of their sites and return the text from the websites into a database.

Though this is a simplification, one can see how these For Loops are similar to the ones in the initial example.

--------------------

broker_registry_list = [“https://cvbba.com/CVBBA/” , “https://www.ibba.org/find-a-business-broker/” , https://www.businessbroker.net/brokers, etc…]

broker_website_list = [ ]

for registry in broker_registry_list:

    get_broker_websites_()

    add_websites_to_broker_website_list()

--------------------

Now with a list of broker websites, execute another For Loop

--------------------

broker_website_list = [“https://www.advancedbusinessbrokerage.com”, “https://www.dcbusinessbroker.com” , https://www.sunbeltwnc.com, etc… ]

for websites in broker_website_list:

    scrape_websites()

    add_website_text_to_database()

--------------------

Lastly, I wrote a machine learning program to use the text data in the database to match the most relevant brokers to our clients deal criteria.

Instead of having to hire more and more people to find additional brokers, my client has a scalable process. There are tens of thousands of business broker websites, so having such a process allows them to identify more deals than they could by simply scouring the web manually.

## Conclusion

The term “scalable” can be broad. When evaluating processes, I advise against asking how a process can be made more scalable, and instead asking how it can be executed in a for loop. The above example highlights one such way a business can reinforce their business development efforts by working their processes into For Loops.