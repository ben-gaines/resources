## Primer on 'Dorking'
~10 Min Read

'Dorking' is the term used for using lesser-known features on Google and Bing to mine data. In this case, it would be used to mine for businesses whose sites contained words of interest and, if possible, the contact info for those businesses. Rather than discuss 'dorking' on an abstract level, however, lets pick a specific use case and walk through it.

In this example, lets assume we want to 'dork' a list of email addresses which meet some basic criteria:

- Has profiles on: [Instagram, TikTok]
- Email domains: [gmail.com, yahoo.com]
- Locations: [Charlotte, Raleigh]
- Contains Key Words: [Dentist, Chiropractor]

The google search phrase we'd use to get one of these combos would be:

```
site:instagram.com "@gmail.com" AND "Charlotte" AND "Dentist"
```

You could do this manually on the Google website, but it would take a long time. The results are limited to 10 per page, so you'd have to click 'next' a zillion times. Even then you'd have to browse the text for each of the results, look for email addresses, and copy and paste them into a file. So we'll instead write a program to do this for us.

The program will run through all possible search combinations we provide it and:

'Click' through all results (usually 300-600 links)
Extract the text from those links
Extract the email addresses from that text
You'd end up with something like this (with many, many more rows):

```
id, url, email, text
                
                0, https://www.instagram.com/road_to_rainadee_dentistry/, Hellorainadee@_gmail.com, Hellorainadee@_gmail.com. 108 posts. 5,417 followers. 659 following ... Chelsea | Student _Dentist_ ... _Charlotte_ | Dental Student.
                
                1, https://www.instagram.com/opera.dental/, opera.dental.insta@_gmail.com, Professional opera singer turned dental student Ithaca College Harvard Penn Dental opera.dental.insta@_gmail.com_
```
From here, we'd simply just expand the inputs provided to the program and re-run. So perhaps something like:

- Has profiles on: [Instagram, TikTok, Facebook, LinkedIn, Google Business, etc.]
- Email domains: [gmail.com, yahoo.com, hotmail.com, *.com, etc.]
- Locations: [Charlotte, Raleigh, Wilmington, Greenville, etc.]
- Contains Key Words: [Dentist, Chiropractor, Massage Therapist, Acupuncture, etc.]
- Note: * is the 'wildcard' meaning 'any'

This approach yields actionable information in and of itself (in the form of a mass email list). You could always expand upon this corpus of data, however. A few top of mind thoughts on how to do so would be:

- Scraping their websites and parsing the text for phone numbers, additional names, key words, etc.
- Checking company and owner names against review sites for more info (Yelp, Google, Angie's list, etc.)
- Checking company and owner names against government databases to see if they have performed Govt contracts before (excellent way to infer company size and revenue)
- 'Dorking' is a fairly common practice for businesses, specifically data and sales teams within businesses. Usually, I'm over-the-top against things like this, because I'm a strong privacy advocate. In this case, however, I'm split. Here is why...

I would have to imagine that if I were say, a Dentist, in this example who desired a strong internet presence, I'd be fine with someone scraping my sites for marketing purposes. On the other hand, if I were just someone caught up on this because I mentioned the word 'dentist' in a random Instagram post, I'd feel surveilled. But frankly, I'm also slightly unsympathetic towards persons in the latter case. After all, why would anyone use social media at this point? Is there anyone left in the country who doesn't recognize how skeezy and low-brow social media companies are? It doesn't seem like one could reasonably expect to use social media and have privacy.