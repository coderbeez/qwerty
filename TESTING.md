# Testing

## Validation

### HTML

[W3C Validation Service](https://validator.w3.org/) Used to test the validity of HTML – no errors found.

### CSS

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Used to test the validity of CSS – no errors found.

[Autoprefixer CSS](https://autoprefixer.github.io/) Used to ensure all relevant vendor prefixes included.

### JavaScript

[JSHint](https://jshint.com/) Used to test the validity of JavaScript functions – no errors found.

## Manual Testing

Throughout the development process Chrome was used to test for functionality and Chrome developer tools for layout and responsiveness on various screen sizes. Once deployed, the site was also tested on Edge, Firefox and Safari browsers and on both android and iOS mobiles.

After sign-off, structured manual testing of the site was carried out on various browsers and screens sizes. A detailed plan was followed to ensure code was thoroughly tested.

### Distraction & User Management

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| Site Load | P | P | P | P | P | P | P |
| **DISTRACTIONS** | --- | --- | --- | --- | --- | --- | --- |
| Quote | P | P | P | P | P | P | P |
| Sample Links | P | P | P | P | P | P | P |
| Inspiration | P | P | P | P | P | P | P |
| Music | P | P | P | P | P | P | P |
| Reload - Resample | P | P | P | P | P | P | P |
| **REGISTER** | --- | --- | --- | --- | --- | --- | --- |
| Nav – 4 + Register | P | P | P | P | P | P | P |
| Name - Validate| P | P | P | P | P | P | P |
| Email - Validate | *4* | *4* | P | P | P | P | P |
| Password - Validate | P | P | P | P | P | P | P |
| Confirm - Validate | P | P | P | P | P | P | P |
| Register - Home Page | P | P | P | P | P | P | P |
| Register - Message| P | P | P | P | P | P | P |
| Nav – 4 + Logout | P | P | P | P | P | P | P |
| **LOGIN** | --- | --- | --- | --- | --- | --- | --- |
| Register - Link | P | P | P | P | P | P | P |
| Email - Validate | *4* | *4* | P | P | P | P | P |
| Password - Validate | P | P | P | P | P | P | P |
| Login - Notes Page | P | P | P | P | P | P | P |
| Login - Message | P | P | P | P | P | P | P |
| Nav – 4 + Logout | P | P | P | P | P | P | P |
| **LOGOUT** | --- | --- | --- | --- | --- | --- | --- |
| Logout - Home Page | P | P | P | P | P | P | P |
| Logout - Message | P | P | P | P | P | P | P |
| Nav – 4 + Register | P | P | P | P | P | P | P |

P - Passed

N/A - Not Applicable

*4* - Please See Bug Log

### Notes

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| **NOTES - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - List | P | P | P | P | P | P | P |
| Search Results – Message | P | P | P | P | P | P | P |
| Search Results – List | P | P | P | P | P | P | P |
| Search No Results – Message | P | P | P | P | P | P | P |
| Search Clear – Message | P | P | P | P | P | P | P |
| Search Clear – List | P | P | P | P | P | P | P |
| **NOTES - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| Message | P | P | P | P | P | P | P |
| Changed | P | P | P | P | P | P | P |
| **NOTES - DELETE** | --- | --- | --- | --- | --- | --- | --- |
| Confirm | P | P | P | P | P | P | P |
| Message | P | P | P | P | P | P | P |
| Deleted | P | P | P | P | P | P | P |
| **NOTES - CREATE** | --- | --- | --- | --- | --- | --- | --- |
| Topic - List | P | P | P | P | P | P | P |
| Topic - Validate | P | P | P | P | P | P | P |
| Title - Validate | P | P | P | P | P | P | P |
| Content - Validate | P | P | P | P | P | P | P |
| Save - Message | P | P | P | P | P | P | P |
| Save - Saved | P | P | P | P | P | P | P |

P - Passed

N/A - Not Applicable

### Links

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| **LINKS - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - List | P | P | P | P | P | P | P |
| Search Results - Message | P | P | P | P | P | P | P |
| Search Results - List | P | P | P | P | P | P | P |
| Search No Results - Message | P | P | P | P | P | P | P |
| Search Clear - Message | P | P | P | P | P | P | P |
| Search Clear - List | P | P | P | P | P | P | P |
| **LINKS - EDIT** | --- | --- | --- | --- | --- | --- | --- |
| Rate - Hover & Click  | P | P | P | P | P | P | P |
| Rate - Time Delay | P | P | P | P | P | P | P |
| Rate - Message | P | P | P | P | P | P | P |
| Rate - Average & Total | P | P | P | P | P | P | P |
| Flag - Hover & Click | P | P | P | P | P | P | P |
| Flag - Time Delay | P | P | P | P | P | P | P |
| Flag - Message | P | P | P | P | P | P | P |
| Flag - MongoDB | P | P | P | P | P | P | P |
| **LINKS - ADD** | --- | --- | --- | --- | --- | --- | --- |
| Topic - List | P | P | P | P | P | P | P |
| Topic - Validate | P | P | P | P | P | P | P |
| Type - Validate | P | P | P | P | P | P | P |
| URL - Validate | P | P | P | P | P | P | P |
| Name - Validate | P | P | P | P | P | P | P |
| Description - Validate | P | P | P | P | P | P | P |
| Rate - Validate | P | P | P | P | P | P | P |
| Save - Message | P | P | P | P | P | P | P |
| Save - Saved | P | P | P | P | P | P | P |

P - Passed

N/A - Not Applicable

### JavaScript Language

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| **DARK MODE ON** | --- | --- | --- | --- | --- | --- | --- |
| Switch | P | P | P | P | P | P | P |
| Local Storage | N/A | N/A | N/A | P | P | P | P |
| Background - Grey | P | P | P | P | P | P | P |
| Font - Stone | P | P | P | P | P | P | P |
| List Item Bdr - Grey | P | P | P | P | P | P | P |
| List Item Bkg - Transparent | P | P | P | P | P | P | P |
| Link - Orange | P | P | P | P | P | P | P |
| Link Hover - Stone | N/A | N/A | N/A | P | P | P | P |
| Button - Stone + Grey Font | P | P | P | P | P | P | P |
| Button Hover - Orange Font| N/A | N/A | N/A | P | P | P | P |
| Dark Mode - Revisit | P | P | P | P | P | P | P |
| **DARK MODE OFF** | --- | --- | --- | --- | --- | --- | --- |
| Local Storage | N/A | N/A | N/A | P | P | P | P |
| Background - Stone | P | P | P | P | P | P | P |
| Font - Grey | P | P | P | P | P | P | P |
| List Item Bdr - Shadow | P | P | P | P | P | P | P |
| List Item Bkg - White | P | P | P | P | P | P | P |
| Link - Red | P | P | P | P | P | P | P |
| Link Hover - Grey | N/A | N/A | N/A | P | P | P | P |
| Button - Grey + Stone Font | P | P | P | P | P | P | P |
| Button Hover - Grey Font| N/A | N/A | N/A | P | P | P | P |
| **NOTES - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - Level 1 | P | P | P | P | P | P | P |
| Accordion - Level 2 | P | P | P | P | P | P | P |
| Accordion - Level 3 | P | P | P | P | P | P | P |
| **LINKS - READ** | --- | --- | --- | --- | --- | --- | --- |
| Accordion - Level 1 | P | P | P | P | P | P | P |
| Accordion - Level 2 | P | P | P | P | P | P | P |
| Accordion - Level 3 | P | P | P | P | P | P | P |
| Accordion - Level 4 | P | P | P | P | P | P | P |
| **LINKS - EDIT & ADD** | --- | --- | --- | --- | --- | --- | --- |
| Star - Click | P | P | P | P | P | P | P |

P - Passed

N/A - Not Applicable

## Bug Log

1. **Heroku CSS Updates** During development it became apparent that CSS updates were not being reflected in Heroku deployments. The solution from Stack Overflow was to restart Heroku in the terminal `Heroku restart -a coderbeez-qwerty` .

2. **Https to Http** After deployment to Heroku, the initial https address changed to http when navigating through the site. The solution from Sean Murphy was to install the Flask extension Flask-SSLify which redirects requests to https.

3. **Sidebar Sampling** After a number of different approaches, it was decided to have the sidebar samples refresh global variables on home page load. This fitted best with users’ habit of not closing browsers, especially on mobile. The Heroku deployment though lost these global variables on timeout resulting in an error when the user tried to reopen a page other than home. The solution was to store the variables in the session cookie. In addition to refreshing on home page load, the sidebar samples now refresh if an `@app.before_request` determines they're not in the session cookie.

4. **Mobile Auto Capitalise** During testing it was noted that emails were being auto capitalised on mobile devices. As MongoDB is case sensitive, to ease email input, `autocapitalize="off"` was added to the email form fields in html.
