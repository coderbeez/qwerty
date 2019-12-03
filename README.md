Milestone 3

Code Help
using url_for with subfolders https://stackoverflow.com/questions/16351826/link-to-flask-static-files-with-url-for

https://stackoverflow.com/questions/45845427/styling-an-integerfield-to-make-it-a-star-rating-system

https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo

Yes https://stackoverflow.com/questions/12831092/textarea-without-input-functionality

Yes https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo

Yes  https://stackoverflow.com/questions/40905579/flask-wtf-dynamic-select-field-with-an-empty-option
Yes https://www.goodreads.com/quotes/tag/programming?page=1
https://dzone.com/articles/more-inspirational-quotes-for-software-developers
https://dzone.com/articles/best-programming-jokes-amp-quotes
https://www.journaldev.com/240/my-25-favorite-programming-quotes-that-are-funny-too
https://twitter.com/CodeWisdom

https://www.canva.com/learn/100-color-combinations/

Photo by Yoann Siloine on Unsplash

<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@siloine?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Yoann Siloine"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Yoann Siloine</span></a>


https://www.color-hex.com/color-palette/81832

# Qwerty


![Header Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/header.jpg)


**[Qwerty](https://coderbeez.github.io/trigg4tables/)** *a website to assist coding students save notes and share links. Developed for Code Institute Milestone 3: Data Centric Development.*



## UX


Qwerty is a website developed to assist coding students studying HTML, CSS, JavaScript and Python languages under Code Institute’s Diploma in Full Stack Web Development. The site allows students to save notes and/or share links under similar topic headings to Code Institute.

1. **Notes** Students can register to host their own notes under familiar headings with the full range of CRUD operations. Registration and login are required for notes. 

2. **Links** Links tagged as instruct, practice, resource and other sites are grouped under familiar headings. Students can create a new link, flag an issue with, or add a star rating to an existing link. No registration or login is required for links.

3. **Distraction** Inspiration and motivation is provided by coding quotes, sample links, daily award site links and a Spotify playlist for those times when stack overflow just isn’t delivering.



### User Stories


User stories for potential visitors to the website include:

1. **Find Link** 

I’m struggling with the JavaScript automated testing topic and looking for some links for further study. I visit the Qwerty site, select JavaScript from the links dropdown. I’m presented with a familiar list of JavaScript topics – I select Jasmine. A list of link types opens – I select instruct. A list of links with star ratings and i buttons opens. After reading the description under additional information, I click a YouTube link. Having watched the video I go back and add my rating of 4 stars. I’m registered on the site already but I haven’t had to login to use links.


2. **Share Link**

I’ve come across a great YouTube video for PyMongo which I’d like to share with my fellow students. On Slack links can get lost unless they are pinned, so I open Qwerty and select Python from the links dropdown. I click add a new link. I enter the details, selecting MongoDB for topic, instruct for type and giving it a 5 star rating. It’s easy and quick – I don’t need to register or login to add a link.  I could have done a search for the word pymongo to check if the link already existed but the site will flag it and simply adding my star rating to the existing entry. 


3. **Online Notes**

Although I keep written notes when I’m studying at home, I want somewhere to jot down notes on my mobile when I’m on the commute or having a break at work. The language topic headings reflect Code Institute’s topics, making it easy to find my notes. I use the optional word search facility to pull notes covering more than 1 topic. Having to login means I know my notes are kept secure. I’m a dark mode fan and this is remembered on my mobile.


4. **Break Time**

When my brain is fried, motivation has dipped or its simply time for a coffee, I head to Qwerty’s distraction sidebar. The quote is randomly picked so chances are I haven’t seen this before. I check out today’s site of the day from the awwwards link. As I’m on the JavaScript milestone, I checkout the sample link for that language. I click on the Spotify link to start the playlist when I return to coding.



### Design


The look and feel of Qwerty was designed for simplicity and ease of use. 

1. **Simple** The site has been designed with minimal graphics, fonts and colours and a pared back navbar.

2. **Navigation** Navigation has been designed to allow as few clicks as possible to get from the home page to the desired note or link. Colour is used to identify links with links coloured red in light mode and orange in dark mode.

3. **Dark Mode** Given the site was aimed at coders and coding students, dark mode was incorporated into the design.

4. **Preparation** Microsoft Powerpoint was used to compile initial [planning documents](https://github.com/coderbeez/qwerty/blob/master/static/planning/planning.pdf) including Balsamiq wireframes, database collections and a pages flow diagram. During development several changes were made to the original design to simplify notes and distractions.



## Features


### Existing Features - *Components*


1. **Navbar** A pared back navbar with a home button and 2 simple dropdowns, notes and links, highlights the 2 main site sections. Both dropdowns allow user to select a language passing it to the relevant routes. The notes dropdown has an additional Register option if the user is not logged in and Logout if logged in.

2. **Image** Text over simple pencil graphic sets out the site name, function (save notes, share links) and extent (HTML, CSS, JavaScript and Python).

3. **Dark Mode** A toggle and slider allow the user to switch between light and dark mode. Local storage is used to keep track of users preference between pages and sessions???? CSS is used to style the slider while Jquery is used to apply and remove styles and check local storage.

4. **Distraction - Quote** A MongoDB collection of coding related quotes is sampled and 1 quote displayed at the start of each site visit???

5. **Distraction – Sample Links** The MongoDB links collection is sampled and 1 link displayed for each language at the start of each site visit??? Links that have flagged as having a problem or that have not been checked are not sampled.

6. **Distraction – Inspiration** Hard coded links to four site of the day web sites are included for design inspiration.

7. **Distraction – Spotify** A link to a Spotify playlist generated for the site opens in new page. The initial embedded playlist was removed as it resulted in problems with audio levels.

8. **Notes - Register** A sign up form with name, email, password and confirm password fields. Email rather than name is used for sign-in so that’s the only field checked against registered users. Flask-Bcrypt is used to hash passwords. If a user is successfully registered, Flask-Login is used to automatically log the user in and they are redirected to the home page with a message to select a language in the notes dropdown to begin creating notes. Once the user is logged in, the Register option in the notes drop down is replaced with a Logout option again managed by Flask-Login.

8. **Notes - Login** Although the w




### Existing Features - *Database Design*


As per Code Institute’s requirements as 

1. **Languages Collection** Using 

| **NAME** | **TYPE** | **EXAMPLE** |
| --- | --- | --- |
| _id | ObjectId | 5dbd76e01c9d440000cb52ae |
| language | String | JavaScript |
| topics | Array of Strings | Fundamentals, Dashboards, Jasmine, jQuery, Maps, SVGs |


2. **Links Collection**

| **NAME** | **DB TYPE** | **Form TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | *ObjectId* | - |  - | Auto |
| **language** | *String* | Select |Required | User |
| **topic** | *String* | Radio |Required | User |
| **url** | *String* | String | Required, URL | User |
| **link_name** | *String* | String | Required | User |
| **description** | *String* | Text Area | Optional | User |
| **ratings** | *Int Array* | Integer | Required | User |
| **check** | *Boolean* | - | Default True | Admin |
| **flag** | *Boolean* | - | Default False | Admin/User |






2. **Notes Collection** CSS 
![Notes Collection Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/notes.png)

3. **Links Collection** The
![Links Collection Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/links.png)

4. **Quote Collection** Using the
![Quotes Collection Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/quotes.png)



### Future Features 


1. **Password Reset** Facility to reset password.

2. **Language** Addition of Django and milestone 4 topics. 



## Technologies & Programmes Used


1. [Balsamiq](https://balsamiq.com/) A web based gui mock-up and website wireframe building application, Balsamiq was used to develop wireframes for the website.

2. [Microsoft Powerpoint](https://office.live.com/start/PowerPoint.aspx) A presentation programme, Microsoft PowerPoint was used to develop the initial proposal.

3. [Microsoft Publisher](https://www.microsoft.com/en-ie/p/publisher/cfq7ttc0k7c3?=&OCID=AID737190_SEM_et3dNWB5&MarinID=set3dNWB5|340720498529|microsoft+publisher|e|c||62634787164|aud-312771920869:kwd-11150981&lnkd=Google_O365SMB_Mixed&gclid=EAIaIQobChMIrN6k04Kh4gIVxrDtCh0N7QGzEAAYASAAEgJqDfD_BwE&activetab=pivot%3Aoverviewtab) A desktop publishing application, Microsoft Publisher was used to create the README header image, Bootstrap plan and flow diagram.

4. [Affinity Designer](https://affinity.serif.com/en-gb/) A vector graphics editor, Affinity Designer was used to edit images and identify hex colours for icons and backgrounds.

6. [Google Fonts](https://fonts.google.com/) A library of free licensed fonts, Google Fonts was used for all fonts.

7. [Font Awesome](https://fontawesome.com/) A font and icon toolkit, Font Awesome was used for all icons.

7. [Techsini](https://techsini.com/multi-mockup/index.php) A multi device website mockup generator, Techsini was use to generate the README header image.

8. [Visual Studio Code](https://code.visualstudio.com/) A source-code editor, Visual Studio Code was the IDE used.

9. [Git](https://git-scm.com/) A distributed version-control system for tracking changes in code during development, Git was used to track changes in Visual Studio Code.

10. [GitHub](https://github.com/) A web-based hosting service for version control using Git, GitHub was used to host the version control system and website content.

15. [Heroku](https://www.heroku.com/) A cloud platform as a service (PaaS) supporting several programming languages, Heroku was used here to host.

11. [HTML5](https://www.w3.org/) A document mark-up language, HTML was the language used.

12. [CSS3](https://www.w3.org/) A style sheet language, CSS was the style sheet used.

14. [Bootstrap4](https://getbootstrap.com/) A CSS framework directed at responsive, mobile-first front-end web development, Bootstrap was used primarily for layout and styling.

13. [JavaScript](http://www.ecma-international.org/) A high-level, interpreted programming language that conforms to the ECMAScript specification, Javascript was used to provide interactivity.

15. [jQuery](https://jquery.com/) A JavaScript library designed to manipulate HTML documents, JQuery was used here by Bootstrap, jCanvas and to manipulate the DOM.

15. [Python](https://www.python.org/) An interpreted, high-level, general-purpose programming language, Python was used here as the????

15. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) A cloud based NoSQL database service, MongoDB Atlas was the database service used.

15. [PyMongo](https://api.mongodb.com/python/current/) A Python distribution containing tools for working with MongoDB, PyMongo was used here to work with MongoDB from Python.

15. [Flask](https://palletsprojects.com/p/flask/) A micro web framework written in Python, Flask was the web application framework used.

15. [Jinja](https://palletsprojects.com/p/jinja/) A web template engine for Python and Flask’s default, Jinja was the template engine used here. 

15. [WTForms](https://jquery.com/) A flexible forms validation and rendering library for Python web development, WTForms was used here for form input handling and validation.

16. [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) A Flask extension that provides bcrypt hashing utilities, Flask-Bcrypt was used for hashing and decrypting user passwords.

15. [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Providing user session management for Flask, Flask-Login was used here to manage logging in, logging out, and remembering users’ sessions.



*Technology explanations from [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)** or technology’s own site.*



## Testing


### Validation & Manual Testing


**HTML**

[W3C Validation Service](https://validator.w3.org/) Used to test the validity of HTML – no errors found.


**CSS**

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Used to test the validity of CSS – no errors found.

[Autoprefixer CSS](https://autoprefixer.github.io/) Used to ensure all relevant vendor prefixes included.


**JAVASCRIPT**

[JSHint](https://jshint.com/) Used to test the validity of JavaScript functions – no errors found.


**PYTHON**
???


**MANUAL TESTING**

Throughout the development process Chrome developer tools were used to test for responsiveness on various screen sizes. After deployment android and iOS mobiles were used to test for functionality and layout, and Chrome, Edge and Firefox browsers to identify bugs.


After sign-off, structured manual testing of the site was carried out in various browsers and screens sizes following a user from start to finish. This single user path approach was adopted as users progress through the site in a very prescribed way. The detailed plan allowed for Python and Javascript code to be fully tested.


| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| Test Language | HTML | CSS | JS | Python| HTML | CSS | JS |
| Site Load | P | P | P | P | P | P | P |
| **DARK MODE** | --- | --- | --- | --- | --- | --- | --- |
| Dark Mode – On | P | P | P | P | P | P | P |
| Background - Grey | P | P | P | P | P | P | P |
| Font - Stone | P | P | P | P | P | P | P |
| List Item Bdr - Grey | P | P | P | P | P | P | P |
| List Item Bkg - Transparent | P | P | P | P | P | P | P |
| Link - Orange | P | P | P | P | P | P | P |
| Link Hover - Stone | P | P | P | P | P | P | P |
| Button – Stone + Grey Font | P | P | P | P | P | P | P |
| Button Hover - Orange Font| P | P | P | P | P | P | P |
| Dark Mode – Links Page | P | P | P | P | P | P | P |
| Dark Mode - Off | P | P | P | P | P | P | P |
| Background - Grey | P | P | P | P | P | P | P |
| Font - Stone | P | P | P | P | P | P | P |
| List Item Bdr - Grey | P | P | P | P | P | P | P |
| List Item Bkg - Transparent | P | P | P | P | P | P | P |
| Link - Orange | P | P | P | P | P | P | P |
| Link Hover - Stone | P | P | P | P | P | P | P |
| Button – Stone + Grey Font | P | P | P | P | P | P | P |
| Button Hover - Orange Font| P | P | P | P | P | P | P |
| **DISTRACTIONS** | --- | --- | --- | --- | --- | --- | --- |
| Quote | P | P | P | P | P | P | P |
| Sample Links | P | P | P | P | P | P | P |
| Inspiration | P | P | P | P | P | P | P |
| Music | P | P | P | P | P | P | P |
| **NOTES - Register** | --- | --- | --- | --- | --- | --- | --- |
| Nav – 4 + Register | P | P | P | P | P | P | P |
| Name - Validate| P | P | P | P | P | P | P |
| Email - Validate | P | P | P | P | P | P | P |
| Password - Validate | P | P | P | P | P | P | P |
| Confirm - Validate | P | P | P | P | P | P | P |
| Register -Home | P | P | P | P | P | P | P |
| Register -Message| P | P | P | P | P | P | P |
| Notes – Blank | P | P | P | P | P | P | P |
| Notes – Logout | P | P | P | P | P | P | P |
| **NOTES - Login** | --- | --- | --- | --- | --- | --- | --- |
| Test Language | HTML | CSS | JS | Python| HTML | CSS | JS |
| Login - Register | P | P | P | P | P | P | P |
| Login - Email | P | P | P | P | P | P | P |
| Login - Password | P | P | P | P | P | P | P |
| Login – Incorrect Message | P | P | P | P | P | P | P |
| Login – Correct Message | P | P | P | P | P | P | P |
| Login – Correct Language | P | P | P | P | P | P | P |
| Login – Correct Notes | P | P | P | P | P | P | P |
| Login – Nav – Register + Logout | P | P | P | P | P | P | P |
| Login – Next Language | P | P | P | P | P | P | P |
| Login – Back Language | P | P | P | P | P | P | P |
| **NOTES - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - List | P | P | P | P | P | P | P |
| Accordion – Level 1 | P | P | P | P | P | P | P |
| Accordion – Level 2 | P | P | P | P | P | P | P |
| Accordion – Level 3 | P | P | P | P | P | P | P |
| Accordion – Visible Target | P | P | P | P | P | P | P |
| Search Results – Message | P | P | P | P | P | P | P |
| Search Results – List | P | P | P | P | P | P | P |
| Search No Results – Message | P | P | P | P | P | P | P |
| Search Clear – Message | P | P | P | P | P | P | P |
| Search Clear – List | P | P | P | P | P | P | P |
| **NOTES - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| Edit | Topic | Title | Content | All | Topic | Title | Content |
| Message | P | P | P | P | P | P | P |
| Changed | P | P | P | P | P | P | P |
| **NOTES - DELETE** | --- | --- | --- | --- | --- | --- | --- |
| Message | P | P | P | P | P | P | P |
| Deleted | P | P | P | P | P | P | P |
| **NOTES - CREATE** | --- | --- | --- | --- | --- | --- | --- |
| Topic – List | P | P | P | P | P | P | P |
| Topic – Validate | P | P | P | P | P | P | P |
| Title – Validate | P | P | P | P | P | P | P |
| Content – Validate | P | P | P | P | P | P | P |
| Save – Message | P | P | P | P | P | P | P |
| Save – Saved | P | P | P | P | P | P | P |
| **LINKS - READ** | --- | --- | --- | --- | --- | --- | --- |
| Language | CSS | JS | Python | HTML| CSS | JS | Python |
| Accordion - List | P | P | P | P | P | P | P |
| Accordion – Level 1 | P | P | P | P | P | P | P |
| Accordion – Level 2 | P | P | P | P | P | P | P |
| Accordion – Level 3 | P | P | P | P | P | P | P |
| Accordion – Visible Target | P | P | P | P | P | P | P |
| Search Results – Message | P | P | P | P | P | P | P |
| Search Results – List | P | P | P | P | P | P | P |
| Search No Results – Message | P | P | P | P | P | P | P |
| Search Clear – Message | P | P | P | P | P | P | P |
| Search Clear – List | P | P | P | P | P | P | P |
| **LINKS - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| Rate - Hover | P | P | P | P | P | P | P |
| Rate – Time Delay | P | P | P | P | P | P | P |
| Rate – Message | P | P | P | P | P | P | P |
| Rate – Average & Total | P | P | P | P | P | P | P |
| Flag - Hover | P | P | P | P | P | P | P |
| Flag – Time Delay | P | P | P | P | P | P | P |
| Flag – Message | P | P | P | P | P | P | P |
| Flag – MongoDB | P | P | P | P | P | P | P |
| **LINKS - ADD** | --- | --- | --- | --- | --- | --- | --- |
| Topic– List | P | P | P | P | P | P | P |
| Topic– List | P | P | P | P | P | P | P |
| Type – Validate | P | P | P | P | P | P | P |
| URL – Validate | P | P | P | P | P | P | P |
| Name – Validate | P | P | P | P | P | P | P |
| Description– Validate | P | P | P | P | P | P | P |
| Rate– Validate | P | P | P | P | P | P | P |
| Save– Message | P | P | P | P | P | P | P |
| Save– Saved | P | P | P | P | P | P | P |
| **LOGIN MANAGER** | --- | --- | --- | --- | --- | --- | --- |
| Logout – Message| P | P | P | P | P | P | P |
| Logout- Home | P | P | P | P | P | P | P |
| Notes Navbar – 4 + Register| P | P | P | P | P | P | P |
| **DARK MODE** | --- | --- | --- | --- | --- | --- | --- |


*Italics* - Console Log 

P - Passed

N/A - Not Applicable

***11 12 13 14*** - Please see **Bug Log**



### Bug Log


1. **Touch Screen Keyboards** During development it quickly became apparent that relying on inbuilt keyboards on touch screen devices provided poor UX. Keypads were built into the website to avoid using device keyboards.


2. **iOS Tables** Initial keypad designs 


### Deployment


The website was developed in Visual Studio Code, stored in Git and pushed to the hosting platform GitHub.
To following steps were taken to deploy to GitHub:
1. Opened the qwerty *repository*.
2. Ensured the *master branch* was present.
3. Ensured the *html page* was named *index.html*.
4. Ensured the *readme.md* had some text.
5. Clicked the *settings* tab.
3. Under *github pages* selected *master branch* as *source*.
5. *”Your site is published at (https://coderbeez.github.io/trigg4tables/)”* became visible in the *github pages* header after approximately 5 minutes.



Readme
Heroku Deploy 
- 
- 
- Create a new app on heroku
- Link to github (verses push directly to heroku) Go to Heroku site/Deploy/Github/
- Choose manual or automatic deployment
- Heroku site/Settings - shows URL
TERMINAL ENV 
1. heroku
2. heroku login
3. not prompted for email & password???
press any key to open browser - enter username & password in browser
return to terminal when prompted
4. heroku apps (lists all apps)
5. python -m pip freeze --local > requirements.txt       Create requirements.txt  
6. echo web: python app.py > Procfile        Create Procfile
7. Ensure UTF-8

Add runtime.txt file to select correct python version during deployment (python-3.7.4)

8. Push requirements.txt and Procfile runtime.txt to github

browser - 

9. heroku ps:scale web=1 -a coderbeez-qwerty

- Set config vars on heroku
Heroku Site/Settings/Config Vars/ 
key is IP value is 0.0.0.0 
Add key is Port value is 5000/key
Add mongo uri key and value
Add secret key key and value

- Final steps to deploy

Heroku site - manual deploy




### Cloning 


The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).
1. Open the [trigg4tables](https://github.com/coderbeez/trigg4tables) repository.
2. Click the *clone or download* button.
3. In the *clone with HTTPs* pop-up, click the copy icon.
4. Open *git bash*.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type *git clone* and paste the URL copied earlier.
7. Press *enter*. 



## Credits


### Content

* Site concept and design by website developer.

* Language topics reflect Code Institute’s Diploma in Full Stack Web Development.



### Media

* Pencil image from [Unsplash](https://pixabay.com/users/Elionas-2345468/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1314467).

* Embedded YouTube by developer with video voiceover by Jack.



### Code
* JS stop reloading page with enter key from [Stack Overflow](https://stackoverflow.com/questions/8866053/stop-reloading-page-with-enter-key).

* JS audio set current time from [Stack Overflow](https://stackoverflow.com/questions/9563887/setting-html5-audio-position).

* JS random array sorting from [w3schools](https://www.w3schools.com/js/js_array_sort.asp).

* JS timer based on code from [Codepad](https://codepad.co/snippet/javascript-stopwatch-using-javascript-and-css).

* JS short date format from [Stack Overflow](https://stackoverflow.com/questions/8398897/how-to-get-current-date-in-jquery).

* JS canvas to blob and blob to png from [Stack Overflow](https://stackoverflow.com/questions/48054723/saving-canvas-as-blob-and-then-blob-as-file).

* JS value from selected radio button from [Stack Overflow](https://stackoverflow.com/questions/8622336/jquery-get-value-of-selected-radio-button).

* JS refresh page from [Stack Overflow](https://stackoverflow.com/questions/5404839/how-can-i-refresh-a-page-with-jquery).

* JS stop YouTube video with jQuery [Stack Overflow](https://stackoverflow.com/questions/2128535/stop-a-youtube-video-with-jquery).

* JS check element does not have class with jQuery [Stack Overflow](https://stackoverflow.com/questions/7841048/how-to-check-if-an-element-does-not-have-a-specific-class).

* JS multiple values in data element [Stack Overflow](https://stackoverflow.com/questions/34455085/can-i-have-multiple-values-in-one-html-data-element).
* JS preload images [thonky](https://www.thonky.com/javascript-and-css-guide/javascript-image-preload).

* JS unit test a document ready function using Jasmine [Stack Overflow](https://stackoverflow.com/questions/29153733/how-to-unit-test-a-document-ready-function-using-jasmine).

* JS calling an inner function [Stack Overflow](https://stackoverflow.com/questions/13218472/calling-a-function-defined-inside-another-function-in-javascript).

* CSS text shadow from [designshack](https://designshack.net/articles/css/12-fun-css-text-shadows-you-can-copy-and-paste/).
* CSS box shadow from [codepen](https://codepen.io/sdthornton/pen/wBZdXq).
* CSS colours from [color hex](https://www.color-hex.com/color/cfb4b2).
* CSS button press formatting [Stack Overflow](https://stackoverflow.com/questions/38377062/how-to-make-html-button-look-pressed-in-using-css).
* CSS iOS styling input field fix from [daretothink](https://www.daretothink.co.uk/stop-ios-styling-your-input-fields-and-buttons).

* CSS iOS styling radio buttons fix from [sitepoint](https://www.sitepoint.com/replacing-radio-buttons-without-replacing-radio-buttons/).

* HTML disable related videos on YouTube embed from [YouTube](https://www.youtube.com/watch?v=ZUTzJG212Vo).



### Acknowledgements

  * Many thanks to my mentor Ali Ashik and ***all*** on Slack who take the time to share useful links for their fellow students.

