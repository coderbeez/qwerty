# Qwerty


![Header Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/header.jpg)


**[Qwerty](https://coderbeez.github.io/trigg4tables/)** *a website to assist coding students save notes and share links. Developed for Code Institute's Milestone 3: Data Centric Development.*



## UX


Qwerty is a website developed to assist coding students studying HTML, CSS, JavaScript and Python languages under Code Institute’s Diploma in Full Stack Web Development. The site allows students to save notes and/or share links under similar topic headings to Code Institute.

1. **Notes** Students can register to host their own notes under familiar headings with the full range of CRUD operations. Registration and login are required for notes. 

2. **Links** Links tagged as instruct, practice, resource and other sites are grouped under familiar headings. Students can create a new link, flag an issue with, or add a star rating to an existing link. No registration or login is required for links.

3. **Distraction** Inspiration and motivation is provided by coding quotes, sample links, daily award site links and a Spotify playlist for those times when stack overflow just isn’t delivering.



### User Stories


User stories for potential visitors to the website include:

**Find Link** 

I’m struggling with the JavaScript automated testing topic and looking for some links for further study. I visit the Qwerty site, select JavaScript from the links dropdown. I’m presented with a familiar list of JavaScript topics – I select Jasmine. A list of link types opens – I select instruct. A list of links with star ratings and i buttons opens. After reading the description under additional information, I click a YouTube link. Having watched the video I go back and add my rating of 4 stars. I’m registered on the site already but I haven’t had to login to use links.


**Share Link**

I’ve come across a great YouTube video for PyMongo which I’d like to share with my fellow students. On Slack links can get lost unless they are pinned, so I open Qwerty and select Python from the links dropdown. I click add a new link. I enter the details, selecting MongoDB for topic, instruct for type and giving it a 5 star rating. It’s easy and quick – I don’t need to register or login to add a link.  I could have done a search for the word pymongo to check if the link already existed but the site will flag it and simply adding my star rating to the existing entry. 


**Online Notes**

Although I keep written notes when I’m studying at home, I want somewhere to jot down notes on my mobile when I’m on the commute or having a break at work. The language topic headings reflect Code Institute’s topics, making it easy to find my notes. I use the optional word search facility to pull notes covering more than 1 topic. Having to login means I know my notes are kept secure. I’m a dark mode fan and this is remembered on my mobile.


**Break Time**

When my brain is fried, motivation has dipped or its simply time for a coffee, I head to Qwerty’s distraction sidebar. The quote is randomly picked so chances are I haven’t seen this before. I check out today’s site of the day from the awwwards link. As I’m on the JavaScript milestone, I checkout the sample link for that language. I click on the Spotify link to start the playlist when I return to coding.



### Design


Qwerty's look and flow was designed for simplicity and ease of use. 


**Name**

Qwerty was chosen as it would be memorable for the target audience of coding students.


**Navigation**

The key driver of site design was navigation, allowing the user to find the desired location with as few clicks as possible.  The site was divided into two distinct sections, **notes** and **links**, highlighted by the pared back navbar home, notes, links and the tagline text save notes, share links. Users access either section by selecting a language from the section navbar dropdown.

As links are not associated with accounts, users selecting a links language are immediately routed to the read links page for their chosen language. From here users can access the add link page, or use the bespoke accordion or word search to find and edit existing links. With four levels, the links accordion allows for efficient filtering. Again focusing on efficiency, the word search searches all four levels simultaneously. 

Users that select a notes language are routed to the login page, if not already logged in, before being routed to the read notes page for their chosen language.  Following a consistent design, users can again access the add note page, or use the accordion and word search to find and edit existing notes. Users remain logged in until they select logout or end their session. New users can choose register directly from the notes dropdown or link from the login page. After registering, users are automatically logged in. The notes dropdown register option changes to logout once a user registers or logs in, following the mantra of only showing the user what they need, when they need it.


**Colours & Fonts**

Following on from simplified navigation, Qwerty has been designed with minimal graphics, fonts and colours. A simple pencil image, to reflect note taking, is used on the home page and repeated on the playlist. The main font *Cabin Condensed*, a very readable condensed font, was chosen to better display lists on mobile devices. In either normal or dark mode, the core colour scheme consists of a background, text and link colour. The stone and charcoal colours, taken from the pencil image, switch between background and text, depending on mode. The link colours, identifying everything clickable, were chosen for contrast and accessilibity. Flashed messages follow a green/red approach to notify or alert users. 

![Colours Image]( https://github.com/coderbeez/qwerty/blob/master/static/images/colours.png)


**Dark Mode**

Given dark mode is often discussed on Code Institute's Diploma Slack channel, it was incorporated as an option for users. A user's selection is saved in local storage so perference is remembered on return visits. 


**Preparation**

Microsoft Powerpoint was used to compile initial [planning documents](https://github.com/coderbeez/qwerty/blob/master/static/planning/planning.pdf) including Balsamiq wireframes, database collections and a pages flow diagram. During development several changes were made to the original design to simplify notes and distractions.



## Features


### Existing Features - *Components*


**Navbar**

A pared back navbar with a home button and two simple dropdowns, notes and links, highlights the two main site sections. Both dropdowns allow users to select a language passing it onto the relevant routes. The notes dropdown has an additional Register option if the user is not logged in and Logout if logged in. Apart from font size, the navbar remains the same on different devices.


**Image, Title, Tagline**

The text over a simple pencil image sets out the site's name, function (save notes, share links) and extent (HTML, CSS, JavaScript and Python).


**Dark Mode**

A slider, on the home page for mobile devices and sidebar on mediuma and large screens, allows users to switch between normal and dark mode. Local storage is used to keep track of users preference. CSS is used to style the slider while jQuery is used to check local storage for preferences, apply and remove styles.




**Distraction**

A distraction sidebar on medium and large screens, On mobile devices, visible under the pencil image on the home page.

*Quote*
A MongoDB quotes collection of coding related quotes is sampled and one displayed at the start of each site visit???

*Sample Links*
The MongoDB links collection is sampled and one displayed for each language at the start of each site visit??? Links that have been flagged as having a problem or that have added by a user but not checked by the administrator are not included in sampling.

*Inspiration*
Hard coded links to four site of the day web sites are included for design inspiration.

*Spotify*
A link to a Spotify playlist of upbeat songs with a strong Irish bias was generated for the site. An initial embedded Spotify playlist was removed as it resulted in problems with audio levels in headphones.


**Notes - Register Page**

New users access the Register page either by selecting Register from the notes dropdown, or by clicking the Register link on the Login page. In the forms.py file, WTForms is used to define the Register form's name, email, password, confirm password and submit fields. In HTML these form fields and field names are rendered using Jinga. Jinga if else loops are also used to display Flash Messages and apply Bootstrap classes, varying the formating and user feedback depending on input validation.  As email rather than name is used for login, users are free to use any name when registering but their email is checked for duplicates in app.py `mongo.db.users.find_one({"email": form.email.data})`. Flask-Bcrypt is used to hash users passwords `bcrypt.generate_password_hash(form.password.data).decode('utf-8')`. All other validation is specified using WTForms Validators. If a user is successfully registered, Flask-Login is used to automatically log the user in before being redirected to the home page. Once the user is logged in, the Register option is swapped for Logout in the notes dropdown using Jinga. Users are guided through the process of registering with Flash Messages.


**Notes - Login Page** 

On selecting a language from the notes dropdown, users not already logged in, are routed to the Login page using `login_manager.login_view = "login"`. A Flask-Login `@loginrequired` decorator on read, add, edit and delete routes ensures only logged in users access notes. The simple login form consists of an email and password field defined and validated using WTForms and rendered using Jinga. For new users, a link is provided to the Register page. Once users submit their email and password, the User class `get_user(email)` static method is used to retrieve the user document and Flask-Bcrypt to check the hashed password. If a user is successfully logged in, they are redirected to the notes page for the language they originally selected. Flask-Login `is_safe_url(next)` checks if the page redirected to is a Qwerty page and aborts if not. Once the user is logged in, the Register option is swapped for Logout in the notes dropdown using Jinga. Users are guided through the process of logging in with Flash Messages. Flask-Login manages the user until they select logout or end their session.


**Notes - Read/Delete Page**

Users access notes pages by selecting a language from the notes dropdown. If a user is logged in they go directly to their language notes page. A Flask-Login `@loginrequired` decorator ensures users not currently logged in, are first routed to the login page before being redirected to their relevant language notes page.

*Read*
Within the language notes page, notes are grouped by topic, sorted by name, and presented in a bespoke accordion. The MongoDB aggregate collection method is used to create a distinct list of user specific langauge topics. Closesly aligned to Codes Institute's lesson headings, these language topics form the first level in a three level accordion. Level two of the accordion reveals a list of sorted note names, whilst three reveals the contents, edit and delete buttons for an individual note.  The accordion, built using jQquery, uses a `slide(target)` function to check the current state of an accordion target, hiding a visible target and revealing a hidden target. On click functions, created for each accordion level, allow a button click to result in a target slide. Data attribute values associate a button to a target when the template is rendered.

PLACEHOLDER FOR VIDEO OF ACCORDION

Users can opt to view the full list or filter the accordion using a word search. The word search functionality is enabled by the search form created using WTForms and MongoDB's text index and $text operator. Firstly a text index is created `mongo.db.notes.create_index([("$**", "text")], language_override="en")` indexing all string fields in the notes collection. Then the `"$text": {"$search": form.tsearch.data}` text operator is added to both the aggregrate topics and the find notes methods filtering the accordion by the `tsearch` word. A clear button with link `href="{{ url_for('notes', language=language) }}` reloads the page for the language, clearing the word search. Flash Messages guide the user through the word search process.

*Delete*
To delete a note, users first click the delete note icon on level three of the accordion. Bootstrap collapse is then trriggered revealing the form submit button, confirm delete. Once confirm is clicked, the note id is passed to the deletenote route. As an added security measure, a MongoDB find_one_or_404 method is filtered by both the note and user ids `mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid), "user_id": ObjectId(current_user.id)})` ensuring the note belongs to the current user before the delete_one operation is performed.


*Edit*
To edit a note, users click the edit note icon on level three of the accordion which links to the edit note page for that note id using url_for.

*Add*
To add a note, users click the add note icon at the top of the page which links to the add note page for that language using url_for.


**Notes - Add Note Page** 
A Login_Manager `@login_required` decorator ensures access to this route is limited to logged in users. Users access the Add Note Page from a link on the language Notes Page, passing the language argument from Notes to Add Notes.  WTForms Note Form is used to define and validate the topic, name, content and submit fields. The select topic list displayed is language specific with a default `-select-` option.
``` document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
topics = document_language["topics"]
form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]
```
As well as the data from the form fields, a MongoDB insert_one method takes the language from language argument and the user id from `current_user.id`. Once a note is sucessfully added, the user is redirected to the language Notes page. Flash Messages guide the user through the add note process.
        


**Notes - Edit Page** 

A Login_Manager `@login_required` decorator ensures access to this route is limited to logged in users. Users access the Edit Note Page from a link on level three of the language Notes Page accordion.  Both the language and note id arguments are passed from Notes to Edit Notes pages. The Note Form created using WTForms and used to add a note is also used to edit a note. A get request fills the form fields with existing data for the note id. WTForm Validators verify data changes and valid changes are submitted to the notes collection using a MongoDB update_one method. As an added security measure, a MongoDB find_one_or_404 method is filtered by both the note and user ids `mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid), "user_id": ObjectId(current_user.id)})` ensuring the note belongs to the current user before the update_one operation is performed. Once sucessfully edited, the user is redirected to the language Notes page. Flash Messages guide the user through the edit note process.


**Links - Read/Edit Page** 

Users access links pages by selecting a language from the links dropdown. Links are not associated with a user and no login is required to access.

![Links Page Video]( https://github.com/coderbeez/qwerty/blob/master/static/readme/links.mp4)

*Read*
Within the language links page, links are grouped by topic and type, sorted by name, and presented in a bespoke accordion. The MongoDB aggregate collection method is used to create a distinct list of user specific langauge topics. Closesly aligned to Codes Institute's lesson headings, these language topics form the first level in a four level accordion. Level two of the accordion groups language topics by one of four types, i.e. instruct, practice, resource and other. The third accordion level reveals a list of sorted link names and average ratings, whilst the fourth reveals the description, total ratings to date, add rating and report problem buttons for an individual link.  Jinga is used to calculate this average rating `{{(link.ratings|sum)//(link.ratings|count)}}` based on the link document's array of rating integers. The accordion, also used for the Notes page, is built using jQquery. A `slide(target)` function checks the current state of an accordion target, hiding a visible target and revealing a hidden target. On click functions, created for each accordion level, allow a button click to slide a target. Data attribute values associate a button to a target when the template is rendered.

*Delete*
There is no facility for users to delete a link. Any deletions are performed by the administrator connecting directly to MongoDB.


*Edit*
Users can add edit a links document by adding a rating or reporting a problem for a specific link id. Star and tool icons are located on the fouth accordion level. Users click the relevant star icon to add a 1, 2, 3, 4 or 5 star rating or the tool icon to report a problem. As form submit buttons, these icons post to the ratelink or flaglink routes using url_for. A MongoDB find_one_or_404 method ensures the link id can be found before an update_one method is performed. JQuery is used to reformat icons once selected and a sleep method to delay submission allowing users to see the updated formatting. Once successfully submitted the language Links page is reloaded. An added rating is reflected in links average star ratings and ratings count. Flagged problems are not  show in the Flash messages guide the user through the edit process. 

*Add*
To add a note, users click the add link icon at the top of the page which links to the add link page for that language using url_for.

**Links - Add Page** 







### Existing Features - *Database Design*


As per Code Institute’s requirements MongoDb, a document based NoSQL database, was used for this project. 

1. **Languages Collection**

The Languages Collection was created to populate topic dropdowns for each language throughout the site. As topics are updated by Code Institute, rather than hard code lists per language this approach allows for efficient list management. Administrator completes all CRUD operations directly in MongoDd.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **language** | String | N/A | N/A | Admin |
| **topic** | Array Strings | N/A | N/A | Admin |


2. **Links Collection**

The Links Collection is a core data collection. Users can read all exisiting documents and create new documents. Their update options are limited to adding a star rating or flagging an issue with an existing document. Document deletion is limited to administrator. The Links Collection is shared amongst all users, hence the limited CRUD operations for users.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **language** | String | N/A | N/A | User *(nav dropdown)* |
| **topic** | String | Radio |Required | User |
| **url** | String | String | Required, URL, Unique| User |
| **link_name** | String | String | Required | User |
| **description** | String | Text Area | Optional | User |
| **ratings** | Array Integers | Integer | Required | User |
| **check** | Boolean | N/A | N/A | Auto *(default False)* / Admin |
| **flag** | Boolean | Button | N/A | Auto *(default False)* / User/ Admin |


3. **Notes Collection**

The Notes Collection is the second core collection. Users have the full range of CRUD operations for their own notes with no access to the notes of other users. Users must register and login for this section of the site. 

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **user_id** | ObjectId | N/A | N/A | User *(login)* |
| **language** | String | N/A | N/A | User *(nav dropdown)* |
| **topic** | String | Radio | Required | User |
| **note_name** | String | String | Required | User |
| **content** | String | Text Area | Required | User |


4. **Quotes Collection**

The Quotes Collectin is sampled in the Distraction section of the site. Read is the only CRUD operation available to users. The collection is managed by the administrator directly through MongoDb.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **quote** | String | N/A | N/A | Admin |
| **author** | String | N/A | N/A | Admin |


5. **Users Collection**

The Users Collection is used to faciliatate notes on this site. Users create a new account on register page and access existing account on login page. The remaining CRUD operations are managed by the administrator directly through MongoDb.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **user_name** | String | String |Required, Length 2-20 | User |
| **email** | String | String |Required, Email, Unique | User |
| **password** | String (hashed) | Password | Required, Length 6-10, Match Confirm | User |




### Future Features 


**Password Reset** Facility to reset password.

**Language** Addition of Django and milestone 4 topics. 



## Technologies & Programmes Used

**Languages**
- [HTML5](https://www.w3.org/)
- [CSS3](https://www.w3.org/)
- [JavaScript](http://www.ecma-international.org/)
- [Python](https://www.python.org/)

**Development Tools**
- [Visual Studio Code](https://code.visualstudio.com/) IDE used.
- [Git](https://git-scm.com/) Used to track changes in Visual Studio Code during development.
- [GitHub](https://github.com/) Used to host the version control system and website content before deployment to Heroku????.

**Hosting Platforms & Database**
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Cloud based database service used.
- [Heroku](https://www.heroku.com/) Cloud based hosting service used. 


**Frontend Resources**
- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap4](https://getbootstrap.com/) Used for responsive layout and styling.
- [jQuery](https://jquery.com/) Used for DOM manipulation enabling accordion dark-mode functionality.

**Backend Resources**
- [pip](https://pypi.org/project/pip/) Used to install Python modules.
- [Flask](https://palletsprojects.com/p/flask/) Web application framework used. 
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) Used to allow communication between Python and MongoDB.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) Used for hashing user passwords.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Used for user session management.
- [WTForms](https://jquery.com/) Used to define and validate forms???.
- [Jinja](https://palletsprojects.com/p/jinja/) Web template engine used. 


**Design Tools**
- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.
- [Microsoft Powerpoint](https://office.live.com/start/PowerPoint.aspx) Used to develop the initial webiste proposal.
- [Affinity Designer](https://affinity.serif.com/en-gb/) Used to edit images and identify hex colours for fonts and backgrounds.
- [Techsini](https://techsini.com/multi-mockup/index.php) Used to generate the README header image.



## Testing


### Validation


**HTML**

[W3C Validation Service](https://validator.w3.org/) Used to test the validity of HTML – no errors found.


**CSS**

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Used to test the validity of CSS – no errors found.

[Autoprefixer CSS](https://autoprefixer.github.io/) Used to ensure all relevant vendor prefixes included.


**JavaScript**

[JSHint](https://jshint.com/) Used to test the validity of JavaScript functions – no errors found.


**Python**
???


### Manual Testing

Throughout the development process Chrome was used to test for functionality and Chrome developer tools for layout and responsiveness on various screen sizes. Once deployed, the site was also tested on Edge, Firefox and Safari browers and on both android and iOS mobiles. 

After sign-off, structured manual testing of the site was carried out on various browsers and screens sizes. Detailed plans were followed to ensure code was thoroughly tested. The order and languages tested was varied to minic user paths and ensure UX user stories were covered.


**Distraction & User Management**

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| Site Load | P | P | P | P | P | P | P |
| **DISTRACTIONS** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *1* | *6* | *4* | *11* | *1* | *11* | *2* |
| Quote | P | P | P | P | P | P | P |
| Sample Links | P | P | P | P | P | P | P |
| Inspiration | P | P | P | P | P | P | P |
| Music | P | P | P | P | P | P | P |
| **REGISTER** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *2* | *4* | *6* | *1* | *10* | *1* | *3* |
| Nav – 4 + Register | P | P | P | P | P | P | P |
| Name - Validate| P | P | P | P | P | P | P |
| Email - Validate | P | P | P | P | P | P | P |
| Password - Validate | P | P | P | P | P | P | P |
| Confirm - Validate | P | P | P | P | P | P | P |
| Register - Home Page | P | P | P | P | P | P | P |
| Register - Message| P | P | P | P | P | P | P |
| Nav – 4 + Logout | P | P | P | P | P | P | P |
| **LOGIN** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *4* | *11* | *1* | *8* | *3* | *10* | *9* |
| *Test - Language* | *HTML* | *CSS* | *JS* | *Python*| *HTML* | *CSS* | *JS* |
| Register - Link | P | P | P | P | P | P | P |
| Email - Validate | P | P | P | P | P | P | P |
| Password - Validate | P | P | P | P | P | P | P |
| Login - Notes Page | P | P | P | P | P | P | P |
| Login - Message | P | P | P | P | P | P | P |
| Nav – 4 + Logout | P | P | P | P | P | P | P |
| **LOGOUT** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *3* | *10* | *5* | *7* | *9* | *6* | *8* |
| Logout - Home Page | P | P | P | P | P | P | P |
| Logout - Message | P | P | P | P | P | P | P |
| Nav – 4 + Register | P | P | P | P | P | P | P |

P - Passed
N/A - Not Applicable


**Notes**

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| **NOTES - READ** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *5* | *8* | *2* | *4* | *4* | *3* | *4* |
| *Test - Language* | *HTML* | *CSS* | *JS* | *Python*| *HTML* | *CSS* | *JS* |
| Accordion - List | P | P | P | P | P | P | P |
| Search Results – Message | P | P | P | P | P | P | P |
| Search Results – List | P | P | P | P | P | P | P |
| Search No Results – Message | P | P | P | P | P | P | P |
| Search Clear – Message | P | P | P | P | P | P | P |
| Search Clear – List | P | P | P | P | P | P | P |
| **NOTES - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *6* | *7* | *8* | *9* | *6* | *4* | *5* |
| *Test - Edit* | *Topic* | *Title* | *Content* | *All* | *Topic* | *Title* | *Content* |
| Message | P | P | P | P | P | P | P |
| Changed | P | P | P | P | P | P | P |
| **NOTES - DELETE** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *7* | *9* | *3* | *10* | *11* | *5* | *11* |
| Message | P | P | P | P | P | P | P |
| Deleted | P | P | P | P | P | P | P |
| **NOTES - CREATE** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *8* | *5* | *7* | *5* | *8* | *2* | *10*|
| Topic – List | P | P | P | P | P | P | P |
| Topic – Validate | P | P | P | P | P | P | P |
| Title – Validate | P | P | P | P | P | P | P |
| Content – Validate | P | P | P | P | P | P | P |
| Save – Message | P | P | P | P | P | P | P |
| Save – Saved | P | P | P | P | P | P | P |

P - Passed
N/A - Not Applicable


**Links**

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| **LINKS - READ** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *9* | *1* | *9* | *2* | *2* | *8* | *6* |
| *Test - Language* | *CSS* | *JS* | *Python* | *HTML*| *CSS* | *JS* | *Python* |
| Accordion - List | P | P | P | P | P | P | P |
| Search Results – Message | P | P | P | P | P | P | P |
| Search Results – List | P | P | P | P | P | P | P |
| Search No Results – Message | P | P | P | P | P | P | P |
| Search Clear – Message | P | P | P | P | P | P | P |
| Search Clear – List | P | P | P | P | P | P | P |
| **LINKS - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *10* | *2* | *10*  | *3* | *5* | *9* | *7* |
| Rate - Hover | P | P | P | P | P | P | P |
| Rate – Time Delay | P | P | P | P | P | P | P |
| Rate – Message | P | P | P | P | P | P | P |
| Rate – Average & Total | P | P | P | P | P | P | P |
| Flag - Hover | P | P | P | P | P | P | P |
| Flag – Time Delay | P | P | P | P | P | P | P |
| Flag – Message | P | P | P | P | P | P | P |
| Flag – MongoDB | P | P | P | P | P | P | P |
| **LINKS - ADD** | --- | --- | --- | --- | --- | --- | --- |
| *Test - Order* | *11* | *3* | *11* | *6* | *7* | *7* | *1* |
| Topic– List | P | P | P | P | P | P | P |
| Topic– List | P | P | P | P | P | P | P |
| Type – Validate | P | P | P | P | P | P | P |
| URL – Validate | P | P | P | P | P | P | P |
| Name – Validate | P | P | P | P | P | P | P |
| Description– Validate | P | P | P | P | P | P | P |
| Rate– Validate | P | P | P | P | P | P | P |
| Save– Message | P | P | P | P | P | P | P |
| Save– Saved | P | P | P | P | P | P | P |

P - Passed
N/A - Not Applicable


**JavaScript**

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
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
| *Test - Language* | *HTML* | *CSS* | *JS* | *Python* | *HTML* | *CSS* | *JS* |
| **NOTES - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - List | P | P | P | P | P | P | P |
| Accordion – Level 1 | P | P | P | P | P | P | P |
| Accordion – Level 2 | P | P | P | P | P | P | P |
| Accordion – Level 3 | P | P | P | P | P | P | P |
| Accordion – Visible Target | P | P | P | P | P | P | P |
| *Test - Language* | *CSS* | *JS* | *Python* | *HTML* | *CSS* | *JS* | *Python* |
| **LINKS - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - List | P | P | P | P | P | P | P |
| Accordion – Level 1 | P | P | P | P | P | P | P |
| Accordion – Level 2 | P | P | P | P | P | P | P |
| Accordion – Level 3 | P | P | P | P | P | P | P |
| Accordion – Visible Target | P | P | P | P | P | P | P |
| **LINKS - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| Rate - Hover | N/A | N/A | N/A | P | P | P | P |
| Rate – Click | P | P | P | P | P | P | P |
| Flag - Hover | N/A | N/A | N/A | P | P | P | P |
| Flag – Click | P | P | P | P | P | P | P |

P - Passed
N/A - Not Applicable



***11 12 13 14*** - Please see **Bug Log**



### Bug Log


1. **Touch Screen Keyboards** During development it quickly became apparent that relying on inbuilt keyboards on touch screen devices provided poor UX. Keypads were built into the website to avoid using device keyboards.


2. **iOS Tables** Initial keypad designs 


## Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via GitHub.

The following instructions to clone and deploy assume the user has:
- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- MongDB Atlas Account
- Heroku Account


### Clone in GitHub

The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).
1. Open the [Qwerty](https://github.com/coderbeez/qwerty) repository.
2. Click the **clone or download** button.
3. In the **clone with HTTPs** pop-up, click the **copy icon**.
4. Open **git bash**.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type **git clone** and paste the URL copied earlier.
7. Press **enter**. 


### Create MongoDB Atlas Database

1. On the [MongoDB](https://cloud.mongodb.com/user#/atlas/login) website log into your Atlas account.
2. Under **cluster/ collections** click **create database** and enter a **database name** and **collection name**.
3. Click **create collection** to add more collections as per the database design above.
4. Under **cluster/ overview** click **connect**.
5. Click **connect your application**.
6. Select **Python** as the **driver** and select the **version**.
7. Copy the connection string `mongodb+srv://root:<password>@mysecondcluster-xkuqo.azure.mongodb.net/test?retryWrites=true&w=majority`.


### IDE Development Setup

1. Add the `MONGO_URI` to your environment file for local deployment. Replace `<password>` with your **password** and `test` with your **database name**.
2. Add a `SECRET_KEY` to your environment file.
3. Use `pip install -r requirements.txt` to install requirements.


### Deploy to Heroku 

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click **new** and **create new app**.
3. Give your app a **name** (it must be unique), select a **region** and click **create app**.
4. Under **deployment method** click **GitHub**.
5. Under **connect to GitHub** select your **repository**, enter the **repo-name** and click **search**.
6. Click the **connect** button that appears under your repository and repo-name.
7. Under **settings/ config vars** click **reveal vars**.
8. Enter **IP** for key, **0.0.0.0** for value and click **add**.
10. Enter **MONGO_URI** for key, **your uri** for value and click **add**.
11. Enter **SECRET_KEY** for key, **your secret key** for value and click **add**.
12. Under **deploy/ manual deploy** click **deploy branch**.
13. Under **resources/ free dynos** click **edit** and **confirm**. 


## Credits


### Content

- Site concept and design by website developer.
- Language topics reflect Code Institute’s Diploma in Full Stack Web Development.
- Links collected by site developer during studies and from Code Institute's Diploma Slack channel.
- Quotes from [CodeWisdom](https://twitter.com/CodeWisdom), [DZone - Programming Quores](https://dzone.com/articles/best-programming-jokes-amp-quotes), [DZone - Software Developer Quotes](https://dzone.com/articles/more-inspirational-quotes-for-software-developers), [GoodReads](https://www.goodreads.com/quotes/tag/programming?page=1), [JournalDev](https://www.journaldev.com/240/my-25-favorite-programming-quotes-that-are-funny-too).



### Media

- Pencil image by Yoann Siloine from [Unsplash](https://unsplash.com/photos/dyaxQ-aoGWY).
- Spotify image adapted from [Spotify](https://www.spotify.com/ie/).


### Code

**HTML**
- Set textarea to display only from [Stack Overflow](https://stackoverflow.com/questions/12831092/textarea-without-input-functionality).

**CSS**
- Creating a switch in CSS from [W3Schools](https://www.w3schools.com/howto/howto_css_switch.asp).


**JavaScript**
- On page load event from [Stack Overflow](https://stackoverflow.com/questions/42541274/jquery-on-page-load-event-not-working).
- Check if an element is hidden from [Stack Overflow](https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery).
- Show hide elements by data attributes from [Stack Overflow](https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute).
- Get data attributes in jquery from [Code Project](https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery).
- Check and uncheck inputs or radios from [Learn jQuery](https://learn.jquery.com/using-jquery-core/faq/how-do-i-check-uncheck-a-checkbox-input-or-radio-button/).
- Define css hover in jquery from [Stack Overfow](https://stackoverflow.com/questions/21051440/how-to-define-the-css-hover-state-in-a-jquery-selector).
- Not class selector in jquery from [Stack Overfow](https://stackoverflow.com/questions/4614120/not-class-selector-in-jquery).
- Read value local storage on load from [Stack Overfow](https://stackoverflow.com/questions/50933011/read-value-of-localstorage-on-body-load-or-document-ready).
- Clear local storage from [Stack Overfow](https://stackoverflow.com/questions/10710674/how-to-remove-and-clear-all-localstorage-data).


**Python** 

*Database*
- [Maximilian Schwarzmüller - Udemy MongoDB The Complete Developer's Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850844?start=300#overview).
- [Flask-PyMongo Documentation](https://flask-pymongo.readthedocs.io/en/latest/).
- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/).
- [PyMongo Documentation](https://api.mongodb.com/python/current/).
- [Pretty Printed - YouTube Flask MongoDB Series](https://www.youtube.com/playlist?list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj).
- Text search from [Stack Overflow](https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search).
- Text search language override from [Stack Overflow](https://stackoverflow.com/questions/50071593/pymongo-language-override-unsupported-c-when-creating-index).

*Forms*
- [WTForms Documentation](https://wtforms.readthedocs.io/en/stable/).
- [Corey Schafer - YouTube Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=65&t=0s).
- [Pretty Printed - YouTube Flask WTForms Series](https://www.youtube.com/playlist?list=PLXmMXHVSvS-C_T5JWEDWIc9yEM3Hj52-1)
- Setting data attributes on WTForms field from [Stack Overfow](https://stackoverflow.com/questions/27779024/setting-data-attributes-on-a-wtforms-field).

*User Sessions*
- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/).
- [Corey Schafer - YouTube Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=65&t=0s).
- [Corey Schafer - YouTube Python Classes Series](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=41&t=0s).
- [Pretty Printed - YouTube Intro to Flask-Login](https://www.youtube.com/watch?v=2dEM-s3mRLE).
- [Running Codes - Blog PyMongo with Flask-Login](https://boh717.github.io/post/flask-login-and-mongodb).

*User Passwords*
- [Flask-Bcrypt Documentation](https://flask-bcrypt.readthedocs.io/en/latest/).
- [Corey Schafer - YouTube Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=65&t=0s).
- [Pretty Printed - YouTube Intro to Flask-Login](https://www.youtube.com/watch?v=2dEM-s3mRLE).

*Messages*
- [Flask Message Flashing Documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).
- [Corey Schafer - YouTube Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=65&t=0s).

*Templating*
- [Jinja Documentation](https://jinja.palletsprojects.com/en/2.10.x/).
- [Corey Schafer - YouTube Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=65&t=0s).
- Using url_for with static files from [Stack Overflow](https://stackoverflow.com/questions/16351826/link-to-flask-static-files-with-url-for).


### Acknowledgements

  - Many thanks to my mentor Ali Ashik and ***all*** on Slack who take the time to share useful links for their fellow students.

