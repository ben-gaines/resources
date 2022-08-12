## Bottom Line Up Front

Data Dictionaries describe the content, format, and structure of a database as well as the relationship of elements within it. Developing and maintaining them is a critical aspect of working with data. I therefore urge those working with data, especially leaders, to consider maintaining data dictionaries a part of their team’s standard operating procedures. In doing so, I suggest including (at a minimum) the following information for each term in a database:

1.  Meaning of the Term
    
2.  Purpose of the Term
    
3.  Where the Term is Used
    
4.  Who Generates Data for the Term
    
5.  Info Specific to the Term
    

## A Shockingly Common Scenario…

To being to explain why data dictionaries are so important, consider the following (extremely common) scenario. A business leader commissions an external team to build a tool for their business. The team builds the tool, but doesn’t document any of their work. Over the next year, the users of the tool generate a wealth of data, but don’t document the terms or structure of the data they are creating either.

Seeing how successful and widely used the tool was used over the last year, the same business leader commissions another external team to build upon the tool and add new features. This team, however, is immediately confused. When they first look at the tool’s database, they find hundreds of terms which are unclear. Terms like these:

1.  User_ID_Ref_#
    
2.  Ref_Number_b
    
3.  Temp_ID_c
    
4.  Temp_ID_e
    
5.  Proj_CM_%
    

When the newly commissioned team asks questions of the data, they quickly find there is no single individual who can explain these terms. The tool the company has been using has hundreds of users, but no single individual has been made responsible for documenting the terms and data being created within the tool by its users.

The external team is under pressure to deliver the new features, however, so they simply guess at what each of these terms means and move on. They never fully understand what was meant by a “User_ID_Ref_#” nor the difference between a “Temp_ID_c” or a “Temp_ID_e.” And as for the ambiguous “Proj_CM_%”, they make an incredibly dangerous assumption it is a reference to “Projected Contribution Margin.” Like the team who built the tool to begin with, they too do not document their work.

The tool that was so widely used by the company over the last year is now subject to data entropy. It is using and generating data that is not documented and is poorly understood. Accordingly, it will acquire “technical debt” at an alarming rate and will eventually become the source of complaints and frustration for the company.

## Data Dictionaries to the Rescue!

The above scenario could have been mitigated by implementing and maintaining a data dictionary. The purpose of a data dictionary is to enable the use of a tool/model/etc. by providing context and meaning behind each of the terms in the underlying data. Admittedly, maintaining a data dictionary can be hard work, especially if it is being built from nothing. But I cannot stress enough how important this work is. Working with data and not maintaining the data dictionary is sort of like running a car and never changing the oil… it’s just a matter of time until it breaks.

Though there are a lot of entries which could be included in a data dictionary, I suggest including (at a minimum) the information below for each term in the database. Of note, I will provide examples for each term by referring to the ambiguous “Proj_CM_%” field from the previous example.

1.  “Meaning of Term” – Most importantly, include a plainly worded and completely clear description of what is meant by that term. (For example: “The ‘Proj_CM_%’ field indicates the contribution margin percentage of a given project. A contribution margin is the total revenue of a project minus its variable costs as a percentage of the total revenue.”)
    
2.  “Purpose of the Term” - It is also important to add contextual information behind the purpose of each term. (For example: “The ‘Proj_CM_%’ field is used by leadership in evaluating the financial health of a project. It allows leaders to make decisions about project-specific expenses.”)
    
3.  “Where the Term is Used” – Explaining where a given term is used within the business, in context, is not obvious and can add valuable insight to anyone working with that data. Though this can be hard to do sometimes, I suggest including this info in the dictionary. (For example: “The ‘Proj_CM_%’ term is used in two reports/updates. First, project managers use this in their monthly update reports to the CFO. Also, the CFO’s team uses the term in their costing analysis reports.”)
    
4.  “Who Generates Data for the Term” – It is also worth noting who is generating the data captured for each term. Is the customer? A member of the business? An entire team? (For example: Data in the ‘Proj_CM_%’ field is generated only by project managers”
    
5.  “Info Specific to the Term” – This is sort of the catch all part of the dictionary. Though there are infinite possibilities for what could be included in this aspect of the dictionary, I suggest keeping it to things that are critical, but not at all obvious, about each term. Time zones and multiples are top of mind examples of this. Time zones can be captured in many ways, and often create confusion when working with data from multiple time zones. Multiples, too, can create confusion, especially when different multiples are applied to different terms. (For example: "Please note the ‘Proj_CM_%’ is derived as a percentage of total project revenue. The accounting department, however, has an allowance for doubtful receivables multiplier of .99 they apply to total revenue. Accordingly, be on the lookout for discrepancies when comparing the induvial project CMs reported by project managers versus the total CMs reported by accounting.")
    

## A Few More Tips

1.  Keep it simple - Data dictionaries can be a lot of work, but that doesn’t mean they have to be fancy. These could be built and kept in google sheets, excel, word… whatever gets the job done. The important thing is simply to keep and maintain a dictionary!
    
2.  Business/domain experts should take charge of data dictionaries - There is nothing “technical” about building a dictionary, so there is no excuse to avoid doing so. Anyone can do it, but I think this is a perfect job for the business/domain expert on the team.
    
3.  Building and maintaining dictionaries should be factored into workload planning - Just as machinery needs maintenance, so too does code. Accordingly, the dictionary being referenced by those who are developing code will need to be updated from time to time. I suggest adding “maintenance days” to the calendar well in advance, and sticking to them, to ensure this gets done.
    

## Conclusion

I firmly believe great teams, in any capacity, are forged through a relentless pursuit of mastering the basics. Data dictionaries represent exactly that. They are a basic, foundational element to be maintained when working with data. In and of themselves, they are not “game changers,” but they make an organization significantly more capable of using their data. They reduce the amount of “technical debt” accrued by an organization by making it easier to maintain and update code that would otherwise be on a path to become obsolete “legacy code.”