## Bottom Line Up Front

This post is any person or team who anticipates leading a series of tech projects for their business or organization. (e.g. building a new platform, migrating from one tool to another, etc.) The goal is to share a few perspectives on ‘automation imperatives’ to consider during such a project. Though there are several such imperatives, four are given here:

1.  Version control
    
2.  CI/CD pipelines
    
3.  Automated testing
    
4.  Infrastructure as Code (IAC)
    

## Overview

The vast majority of businesses, or even departments within businesses, do not have access to full-time development teams. As a result, when they want to take on a new tech project (e.g. building a platform), they typically have two options. They can hire an external development team or they can form an ad-hoc team from within the company for each specific initiative. Neither of these two options are inherently bad. However, it’s important to keep in mind there is always more risk in using temporary staffing models to execute tech projects. This is because there is not a permanent team in place who knows how to operate the technology.

In technology, embracing an automation-first mentality is a best practice. It is especially important, however, if you intend to leverage short-term teams to deliver IT projects. Of course, having an ‘automation-first mentality’ is not very specific! So I hope that by highlighting a few automation topic areas herein I can help support anyone who is assigned to contribute to or lead a tech project in their workplace.

## Version Control

The overwhelming majority of tech teams implement a version control strategy, so this topic is somewhat ‘low-hanging fruit.’ Nevertheless, it warrants a brief explanation, because it is an important aspect of working in technology, and is generally considered a ‘red flag’ if teams aren’t using it.

Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. Git is the most popular right now, and most people have probably a least heard of GitHub. In a manner of speaking, Git, or version control in general is sort of a commercial grade method for using the ‘save as’ feature. Having proper version control allows a team to roll back to different, or previous versions of a tool or model they are working on. It also allows them to collaborate on the code they are working on without fear of ruining each-others work.

For persons who think they’ll need to leverage temporary or ad-hoc teams to execute a tech project, having a decent version control strategy is an absolute must. Such a strategy will mitigate the risk of newly formed development teams not-deconflicting their work. And that’s not to say these teams are at all bad. Keep in mind, even development teams with years of experience working together make mistakes. That just how it goes. The important thing is to be able to adjust quickly from those mistakes.

## CI/CD Pipelines

For all the buzz-words about ‘tempo,’ ‘agile,’ and ‘sprints,’ there seems to be comparatively little emphasis on the capabilities that actually allow for this to occur. CI/CD is such a capability. CI/CD stans for Continuous Integration / Continuous Delivery. In non-tech terms, this means there is an automatic pipeline in place for deploying code. This is important because a team can only develop as fast as their ability to deploy code.

Netlify is a really good example of this. Netlify is a platform that allows user to deploy their websites from Git. This makes building and maintaining a website super simple, because all the developers need to do is push their changes to a GitHub profile and Netlify will automatically detect the files (or changes to files) and immediately push them to production. Not only is this convenient, it increases security. This site is just a series of static images on a GitHub account. So if anything breaks, I can reset the site to a previous file in a matter of minutes.

While CI/CD pipelines are the best case scenario, they are not an absolute requirement. The key is to ensure your development team has a simple, well documented process for deploying code. This is important because you will likely want to update, or make changes to, the work they delivered in the months or years after the work is completed. If there is not a super simple process in place for deploying those changes when they complete the project, there will be a lot of delays trying to figure it out after the fact.

If this concept is still a little tricky to visualize, please check out the pipeline demo above.

## Automated Tests

Not long ago, there was a generally accepted division of labor between the persons who wrote code and those who tested it (the quality assurance, or ‘testers’). That philosophy of working is becoming less and less common, however, in favor of the trend towards ‘shifting left.’ The idea behind ‘shifting left’ is that persons should test their code as early in the lifecycle as possible, and not wait until it reaches a tester to be validated.

There are, of course, several ways to test code. The most natural, and obvious, is to have a human visually inspect the it. This, however, does not scale. At some point, developers have to create a process for testing their code automatically. There several ways to do this, but the most frequently used are called ‘unit tests.’ A unit is the smallest testable part of any software. The purpose of unit tests, therefore are to validate that each unit works as designed. Savvy developers will often times write a unit test before they even write the code itself.

After unit tests there are additional tests like ‘integration tests’ and ‘GUI tests.’ The topic is so expansive that we will commit a separate white paper simply to this issue. For sake of this white paper, the key takeaway is that this is a discussion you simply must have with your developers, especially if they are a temporary team or contracted group. Ask them to document, review, and explain the testing strategy. Doing so will reduce the likelihood of introducing bugs into your project. It will also make it easier to maintain continuity on the code base after the tech team has completed their work.

## Infrastructure as Code (IaC)

It should come as no surprise that everything digital has to be built upon infrastructure. When developing spreadsheets at work, for instance, your laptop serves as the foundation for your infrastructure. But what happens when you are working with data that is too big for a spreadsheet, or need to have a proper work-flow tool? (e.g. an online tool for submitting expenses, building investment portfolios, etc.) In this case, larger, more ‘commercial grade’ infrastructure is required.

Not long ago, building such infrastructure meant hooking up a bunch of computers on-premise, and managing those computers much the same way we manage our laptops (installing updates, downloading needed software, etc.) But managing ‘on prem’ infrastructure takes a lot of effort and requires a lot of overhead costs. As a result, there is a strong trend towards moving infrastructure to the cloud, usually on AWS, GCP, or Microsoft Azure.

Nearly all cloud infrastructure providers have websites wherein you can click on the configuration you want for your infrastructure, and set up everything by visually inspecting the menu of options. This might work for a single iteration, but it does not at all scale. This means you’ll want to develop code for provisioning infrastructure. Infrastructure as Code is a massive topic for which I will dedicate a separate white paper. The key point here, however, is that like automated tests, this is something to talk to your development team about. Ask your team about the methods they are using to provision infrastructure to assess how scalable, and repeatable they are. Especially if your tech project team is a temporary one, the last thing you’ll want is for a non-scalable infrastructure process to be in place when they leave. Such a process will make iterating on the code extremely difficult after the team has left.

## Conclusion

Some big topics are covered in this white paper:

1.  Version control
    
2.  CI/CD pipelines
    
3.  Automated test
    
4.  Infrastructure as Code (IAC)
    

Everything covered here has been at an extremely high level, but that’s OK. I’ll do ‘deep dives’ on each of these topic separately. The main point from this is that these topics should be kept top of mind when working on a tech project, especially in instances wherein the project team is temporary. By maintaining an automation-first mentality, and executing well on these basic areas, you can significantly increase the likelihood of success on your project.