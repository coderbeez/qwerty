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


1. **Password Reset** Facility to reset password.

2. **Language** Addition of Django and milestone 4 topics. 



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
- [PyMongo](https://api.mongodb.com/python/current/) Used to allow communication between Python and MongoDB.
- [Flask](https://palletsprojects.com/p/flask/) Web application framework used. 
- [Jinja](https://palletsprojects.com/p/jinja/) Web template engine used. 
- [WTForms](https://jquery.com/) Used for form rendering and validation???.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) Used for hashing user passwords.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Used for user session management.


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



### Media

- Pencil image by Yoann Siloine from [Unsplash](https://unsplash.com/photos/dyaxQ-aoGWY).
- Spotify image adapted from [Spotify](https://www.spotify.com/ie/).
- Quotes from [CodeWisdom](https://twitter.com/CodeWisdom), [DZone - Programming Quores](https://dzone.com/articles/best-programming-jokes-amp-quotes), [DZone - Software Developer Quotes](https://dzone.com/articles/more-inspirational-quotes-for-software-developers),[GoodReads](https://www.goodreads.com/quotes/tag/programming?page=1), [JournalDev](https://www.journaldev.com/240/my-25-favorite-programming-quotes-that-are-funny-too).



### Code

**HTML**
- Set textarea to display only from [Stack Overflow](https://stackoverflow.com/questions/12831092/textarea-without-input-functionality).

**CSS**
- Creating a switch in CSS from [W3Schools](https://www.w3schools.com/howto/howto_css_switch.asp).


**JavaScript jQuery**
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
- [Running Code Blog](https://boh717.github.io/post/flask-login-and-mongodb).

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

  * Many thanks to my mentor Ali Ashik and ***all*** on Slack who take the time to share useful links for their fellow students.

