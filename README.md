## recent-stes-txt2lists

Convert url per line in seperate .txt files to a list on webpage (localhost:200/index) for easier browsing

- Why? 
 - Because I hate using in-browser bookmarking. Can't organise it for the life of me.
 - And I use multiple browsers (safari / opera) that don't sync out-of-the-box.
 - And this is more customisable.
- Customisable?
 - Yes. 
 - e.g. Different .txt files for different categories.
 - You can even repeat urls in different .txt files if you want
- TODOs
 - DB backend to store extra information like notes / priority etc. (redis hashes?)
 - Requests to display 'title' of page instead of url ? (won't work with arXiv links - all PDFs!)
 - Cronjob scp (security issues with scp on crontasks?) tumbleweed/work lists
 - E-mail updates of lists - python SMTP mail server, make file if doesn't exist, new line for each url in email body. Useful for mobile!
