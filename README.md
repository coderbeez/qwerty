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


![Header Image](https://github.com/coderbeez/trigg4tables/blob/master/assets/images/header.png)


**[Qwerty](https://coderbeez.github.io/trigg4tables/)** *, a website to assist coding students save notes and share links, developed for Code Institute Milestone 3: Data Centric Developement.*



## UX


Qwerty is a website developed to assist coding students studying HTML, CSS, JavaScript and Python languages under the Code Institute’s Diploma in Full Stack Wed Development, allowing students to save notes and share links.  

Qwerty has been designed to address some of the limitations of similar websites and apps:

1. **Notes** Students can register to save their own notes under . 

2. **Links** Practice that reflects homework where a single set of times tables is selected. 

3. **Distraction** Code . 

4. **Dark Mode**  . 



### User Stories


User stories for potential visitors to the website include:

1. **Find Link** 

I’m struggling with a topic and looking for some links for further study. Having viewed the link, I can go back and add my 5 star rating. If there’s any problem with the link, I can 


2. **Share Link**

I’ve come across a great YouTube video for PyMongo which I’d like to share with my fellow students. On Slack links can get lost unless they are pinned, so I open Qwerty, select Python under the links navbar and click add new link. I enter the details, selecting MongoDB for the topic, instruct fror type and giving it a 4 star rating.  Its easy and quick – I don’t need to register or login to add a link.  If the link was added by another student for this language, my rating is added and the system tells me where the link is located. 


3. **Online Notes**

Although I keep written notes when I’m studying at home, I want somewhere to jot down notes when I’m on the bus or having my lunch break at work. The language topic headings reflect the Code Institute’s topics, making it easy to find my notes just by heading. I use the optional word search facility to pull notes covering more than 1 topic. Having to login means I know my notes are kept secure. I’m a dark mode fan and this is remembered on my phone.


4. **Break Time**

With a fried brain and or a lull in motivation I head to Qwerty and go straight to the distraction sidebar. The quote is randomly picked so chances are I haven’t seen this before. I check out todays website of the day from the awwwards link – definitely my favourite awards site. As I’m on the JavaScript milestone I checkout the sample link for that language. I click on the Spotify link to start the playlist when I return to coding.



### Design


The look and feel of Qwerty was designed for simplicity and ease of use. 

1. **Simple** Given the target audience, the website was designed to be viewed primarily on a mobile phone.

2. **Navigation** As few steps as possible to get to notes and/ or link.

3. **Dark Mode** A very limited colour palette was used with colours taken from Trigg’s images or chosen to complement them. Equal amounts of blue and pink ensure a gender-neutral site. Red and green convey meaning.

4. **Preparation** Balsamiq was used to generate [wireframes](https://github.com/coderbeez/trigg4tables/blob/master/assets/wireframes/wireframes.pdf) for various device sizes. The [initial proposal](https://github.com/coderbeez/trigg4tables/blob/master/assets/wireframes/proposal.pdf) document was completed using Microsoft Powerpoint. Testing during development resulted in several changes to the original design with a move away from 



## Features


### Existing Features - *Components*


![Trig FlowChart](https://github.com/coderbeez/trigg4tables/blob/master/assets/images/features.png)
***Website Components***


1. **Trigg Images** Trigg character images from [VectorStock](https://www.vectorstock.com/royalty-free-vectors/vectors-by_Westamult) set the overall look of the website. jQuery is used to change the image source, alternating Trigg’s expressions and providing feedback for the child.

![Trig FlowChart](https://github.com/coderbeez/trigg4tables/blob/master/assets/wireframes/triggflow.png)
***Question & Answer Flowchart***


2. **Information Video** Although the website was designed to be as intuitive as possible, an instruction video was created using [Snagit](https://www.techsmith.com/screen-capture.html) with voiceover by an enthusiastic 12 year old. A dedicated YouTube channel was setup to host Trigg’s video. Given the target audience, this was deemed the most appropriate medium. Text instructions were also included for improved accessibility.


3. **Keypads** Touch screen keyboard functionality and positioning was a serious problem, so the initial design was amended to include website keypads. jQuery click and JavaScript concat methods are used to enter and retrieve values from HTML buttons, radio buttons and labels. CSS styles, including active, simulate key pressing and indicate selection.


4. **Timer** JavaScript setTimeout and clearTimeout methods are used to start the timer on go and stop on complete. Time taken to finish is shown on the report.


5. **Sound** JavaScript play methods are used to provide audio feedback when an answer is missing, correct, incorrect or all complete. Sound can be turned on or off at any stage by clicking the sound or mute icons. jQuery is used to toggle between icons, adding and removing Font Awesome classes.


6. **Restart** Using the JavaScript reload method, the website can be refreshed at any stage by clicking the x icon, taking the child back to the start.


7. **Feedback** jQuery hide, show, add and remove class methods are used to provide instructions and feedback.


8. **Progress** jQuery is used to set the attributes for a [Bootstrap](https://getbootstrap.com/docs/4.3/components/progress/) progress bar showing the child how they are progressing.


9. **Tables** Times tables lists are generated, randomised, marked as completed and highlighted as needing revision, using 3 JavaScript arrays: timesArray, todoArray and reviseArray.


10. **Report** [jCanvas](https://projects.calebevans.me/jcanvas/) is used to fill and format a HTML canvas element. This canvas acts as a detailed report showing the date, tables, time taken to complete and any sums that need to be revised. As canvas content is not accessible to screen readers, the report text is also shown in a paragraph element.


11. **Download** Clicking the download button converts the canvas report first to a blob and then to a png file which can be shared. JavaScript libraries [Canvas-toBlob.js](https://github.com/eligrey/canvas-toBlob.js) and [FileSaver.js](https://github.com/eligrey/FileSaver.js/) facilitate this.



### Existing Features - *Responsiveness*


This one page website was designed using a mobile first approach. In order to limit scrolling, the order, position and visibility of elements change depending on screen size. (1) CSS attributes and media queries, (2) Bootstrap grid system and display classes, and (3) jQuery hide and show methods are used to facilitate this responsiveness.


![Bootstrap Plan]( https://github.com/coderbeez/trigg4tables/blob/master/assets/wireframes/bootstrap.PNG)
***Bootstrap Column & Row Plan***


1. **Viewport Width** Using the [Bootstrap](https://getbootstrap.com/docs/4.3/layout/grid/) grid system, the percentage of viewport width used to display content varies from 100% on small and medium screens to 83% (10 Bootstrap columns) on large screens.

2. **Viewport Height** CSS percentage of viewport height classes are used to ensure site fills screen, regardless of screen size and limits scrolling.

3. **Element Width & Position** The [Bootstrap](https://getbootstrap.com/docs/4.3/layout/grid/) grid system is also used to change the width and position of elements on small, medium and large screens to better display content.

4. **Display** Using the CSS display property, [Bootstrap](https://getbootstrap.com/docs/4.3/utilities/display/) display classes and [jQuery]( https://api.jquery.com/show/) hide and show methods, elements, rows and columns appear and disappear on this single page website.

5. **Video** [Bootstrap](https://getbootstrap.com/docs/4.3/utilities/embed/#about) utility of embed-responsive is used to make the embedded iframe responsive.

6. **Margins & Padding** [Bootstrap](https://getbootstrap.com/docs/4.3/utilities/spacing/) spacing utilities are used to vary margins and padding by breakpoints.

7. **Font Size** Media queries are used to change font sizes depending on screen size.

8. **REM** REM sizes are used throughout the website to improve responsiveness.



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

8. [Visual Studio Code](https://code.visualstudio.com/) A source-code editor, Visual Studio Code was the IDE used.

9. [Git](https://git-scm.com/) A distributed version-control system for tracking changes in code during development, Git was used to track changes in Visual Studio Code.

10. [GitHub](https://github.com/) A web-based hosting service for version control using Git, GitHub was used to host the version control system and website content.

11. [HTML5](https://www.w3.org/) A document mark-up language, HTML was the language used.

12. [CSS3](https://www.w3.org/) A style sheet language, CSS was the style sheet used.

14. [Bootstrap4](https://getbootstrap.com/) A CSS framework directed at responsive, mobile-first front-end web development, Bootstrap was used primarily for layout and styling.

13. [JavaScript](http://www.ecma-international.org/) A high-level, interpreted programming language that conforms to the ECMAScript specification, Javascript was used to provide interactivity.

15. [jQuery](https://jquery.com/) A JavaScript library designed to manipulate HTML documents, JQuery was used here by Bootstrap, jCanvas and to manipulate the DOM.

15. [MongoAtlas](https://jquery.com/) A JavaScript library designed to manipulate HTML documents, JQuery was used here by Bootstrap, jCanvas and to manipulate the DOM.




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

Throughout the development process Chrome developer tools were used to test for responsiveness on various screen sizes. After deployment android and iOS mobiles were used to to test for functionality and layout, and Chrome, Edge and Firefox browsers to identify bugs.


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


2. **iOS Tables** Initial keypad designs relied on tables to position elements. Although no problem was encountered with android, tables did not render correctly on iOS. Keypads were redesigned using break elements and margins.


3. **iOS Radio Buttons** To limit selection to one item from a group, radio buttons were wrapped in label elements. Labels were then styled as buttons to provide a consistent look to keypads. Although no problem was encountered with android, radio buttons remained visible on iOS. The following CSS resolved the issue. 

```
input[type="radio"] {
  -webkit-appearance: none;
}

[type="radio"] {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
WHERE: https://www.sitepoint.com/replacing-radio-buttons-without-replacing-radio-buttons/
```


4. **Keyboard Verses Keypad** During initial testing children were using the device keyboard to input letters rather than numbers. Changing an input field to a label forced the use of the keypad, preventing device keyboard use. 


5. **Enter Reloading Site** During development it was noted that pressing the enter key on a desktop would reload the page sending the user back to the start. A prevent default method resolved the issue.

```
$(document).on("keypress", function(e) {
    if (e.which == 13) {
      event.preventDefault();
    }
  });
WHERE: https://stackoverflow.com/questions/8866053/stop-reloading-page-with-enter-key
```


6. **Loading Images** During initial testing on both android and iOS mobiles, Trigg images were slow to load. Changing png to svg files improved load times on android, however images were only displayed on iOS on second use. Preloading image sources in JS resolved this issue.


7. **Closing Video** Once the instruction video was embedded it became apparent that if clicked before the video had ended, the close button used to hide did not stop play. Adding the following code to the close button click method reset the video and stopped the audio.

```
$("iframe").attr("src", "https://www.youtube.com/embed/QnvT6_Fp1B4?rel=0");
WHERE: https://stackoverflow.com/questions/2128535/stop-a-youtube-video-with-jquery
```


8. **Playing Audio** During development sound clips were not always audible even though the play method was running correctly. Using the current time property in the play audio function, reset the audio clip back to the start giving consistent sound on each play. 

```
function playAudio(audio) {
    if (sound === true) {
      audio.play();
      audio.currentTime = 0;
    }
  }
WHERE: https://stackoverflow.com/questions/9563887/setting-html5-audio-position
```


9. **Firefox Audio** During development testing although all audio clips were mp3 files, in Firefox one clip would not load. Resaving the clip as a m4a file resolved this issue.


10. **Edge toBlob** During development testing the report would not download in Edge as the browser does not support the toBlob method. Using the [Canvas-toBlob.js](https://github.com/eligrey/canvas-toBlob.js) JS library resolved this issue.

![toBlob Compatiblity](https://github.com/coderbeez/trigg4tables/blob/master/assets/images/toblob.PNG)
***toBlob Compatibility [Mozilla]( https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob)***


11. **iOS Double Tap** When using the keypad for entering numbers e.g. 11, double tapping on the 1 key can cause an iPhone or iPad to zoom in. Although this action can be turned off in device settings, no fix has been found to apply to the website.


12. **Firefox Video** In Firefox, as you move the cursor over the YouTube video the following warning message appears in the console; “MouseEvent.mozPressure is deprecated. Use PointerEvent.pressure instead”. The video plays without an issue. 


13. **Firefox Audio** Rewinding audio elements by setting audio.currentTime results in an abort error message in the console in Firefox as noted in [Bugzilla]( https://bugzilla.mozilla.org/show_bug.cgi?id=1507193). This error does not affect website function.


14. **Safari Canvas-toBlob.js** [Stock Overflow]( https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob)
 revealed an error message on iOS was due to the sourceMap flag being set to false instead of true in the tsconfig.json file of [Canvas-toBlob.js](https://github.com/eligrey/canvas-toBlob.js). This does not affect functionality.


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

