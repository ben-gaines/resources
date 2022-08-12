## Using Word + Excel + Outlook for Mass Email Campaigns 
When it comes to mass email tools, small and medium businesses are at a disadvantage. The majority of 'solutions' today are set up with large enterprises in mind. As a result, they are usually over priced, over featured, and overly complicated for use in small and medium businesses. 

Fortunately, if you use Microsoft, as many SMBs do, there is a way to send mass emails using the built in features from Word, Excel, and Outlook. This solution is free and, in our opinions, easier and more effective than 99% of the options on the market anyhow. Here is how to do it. 

##### Step 1 | Open an excel document and create the following column names (and enter in info similar to what is displayed here). Save the file when complete

| name       | email                                       | column\_1 | column\_2 |
| ---------- | ------------------------------------------- | --------- | --------- |
| fruits     | [fruits@test.com](mailto:fruits@test.com)   | apple     | banana    |
| vegetables | [veggies@test.com](mailto:veggies@test.com) | carrot    | cabbage   |

##### Step 2 | Open a word document, then copy and paste the following text into it

```
Dear Reader,

This is a quick demo to show how to use word and outlook to send mass emails from data in a spreadsheet or database.

In this example, we’ll use a spreadsheet with names, emails, and a few other points of data to form a mass email campaign. For sake of this demo: all data points will display below:

-   Name: {name}

-   Email: {email}

-   Column 1: {column_1}

-   Column 2: {column_2}
```

##### Step 3 | Connect the word document with the excel document
- [ ] Click 'mailings' on the top ribbon (found five words over from the 'home' button)
- [ ] Click the dropdown arrow on the 'Start  Mail  Merge' icon (found just below and to the right of the 'home' button)
- [ ] Click 'email message' (You'll notice that the view format will change)
- [ ] Click the drowdown arrove on the 'Select Recepients' icon (just to the right of the 'start mail merge' icon)
- [ ] Click 'Use an existing list...'
- [ ] Click on the excel file you just created
- [ ] (You may be given a prompt asking you if you trust the file. If so, click yes)
- [ ] An open workbook dialogue box will apear. Do not change anything. Click OK.

##### Step 4 | Format the word document with the excel document inputs
- [ ] Highlight the {name} characters ( to include the { and } )
- [ ] Click the dropdown arrow on the 'Insert Mege Field' icon (to the right of the 'Select Recepients' icon)
- [ ] Click name. You'll notice that the highlighted text will be replaced with "<<" name ">>"
- [ ] Highlight the {email} characters ( to include the { and } )
- [ ] Click the dropdown arrow on the 'Insert Mege Field' icon (to the right of the 'Select Recepients' icon)
- [ ] Click email. You'll notice that the highlighted text will be replaced with "<<" email ">>"
- [ ] Highlight the {column_1} characters ( to include the { and } )
- [ ] Click the dropdown arrow on the 'Insert Mege Field' icon (to the right of the 'Select Recepients' icon)
- [ ] Click column_1. You'll notice that the highlighted text will be replaced with "<<" column_1 ">>"
- [ ] Highlight the {column_2} characters ( to include the { and } )
- [ ] Click the dropdown arrow on the 'Insert Mege Field' icon (to the right of the 'Select Recepients' icon)
- [ ] Click column_1. You'll notice that the highlighted text will be replaced with "<<" column_2 ">>"

##### Step 5 | Preview the results (optional)
- [ ] Click the 'Preview Results' icon (to the right of the 'Insert Merge Field' icon). You'll notice that the "<<" ">>" variables were replaced with the info from your spreadsheet. This is how your email will appear to readers.
- [ ] To toggle through and inspect the messages you'll be sending, click the < and > arrows to the right of the 'Preview Results icon. 
- [ ] If you have a large spreadsheet, and want to jump straight to a specific row without using the < and > toggle arrows, click 'Find Recepient' (found below the toggle arrows). Select the column you want to search (e.g. 'name'), enter the value you are looking for, and click submit. Of note: this search does not support 'fuzzy searching,' meaning you have to search for the info exactly as it appears in the spreadsheet

##### Step 6 | Send the emails
- [ ] Click the dropdown arrow on the 'Finish & Merge' icon
- [ ] Click 'Merge to Email'. A dialogue box titled 'Mail Recepient' will appear
- [ ] In the 'to' dropdown menu, select 'email'
- [ ] Type a subject in the subject text field 
- [ ] In the 'send as' dropdown  menu, select 'HTML Message'

##### Step 7 | Save your word document for future use (optional)

##### Optional Feature | How to add unique notes to selected names in the mass email campaign 
If there are a handful of messages you'd like to customize from the mass email campaign:

- [ ] Click the dropdown arrow on the 'Rules' icon (to the left of the 'Preview Results' icon)
- [ ] Click 'If...Then...Else'
- [ ] Select the field name, comparrison, and compare to values (for the demo, try 'name', 'Equal To', and 'vegetables')
- [ ] Enter the message in the 'insert this text' field (for the demo try 'This should only appear in the vegetables message')
- [ ] Click OK. Now if you scroll to that particular message you'll see that your custom note was added. 

Of note: this logic can be quite powerful and sophisticated, especially because you can filter for greater than, less than, text contains, and blank values for the rows of your spreadsheet.  In effect, this means you could set up multiple word document templates on your computer, which you can open and click 'send' from time to time based on specific scenarios. Things like late payments, follow-ups, new announcements, etc. immediately come to mind but the use cases are wide and varied. 


