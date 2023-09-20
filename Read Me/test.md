# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Validation](#validation)
    - [PEP8](#pep8)
    - [CSS](#css)
    - [HTML](#html)
    - [Lighthouse](#lighthouse)
  - [Test Of All Features](#test-of-all-features)
  - [Security](#security)
  - [Links](#links)
  - [Different Types Of Headers](#different-types-of-headers)
  - [Sizes](#sizes)
  - [Marketing \& SEO](#marketing--seo)


## Validation

### PEP8
> PEP8 Validation Service was used to check the code for PEP8 requirements.
> All the code passes with no errors or warnings.

| App| File |Result | Image
| ------ | ------ | ------ | ------ |
| Home | urls.py | Works as expected | (<a href="pictures/homeurls.png">Image</a>)
| Home | views.py | Works as expected | (<a href="pictures/homeviews.png">Image</a>)
| Events | urls.py | Works as expected | (<a href="pictures/eventurls.png">Image</a>)
| Events | views.py | Works as expected | (<a href="pictures/eventviews.png">Image</a>)
| Events | admin.py | Works as expected | (<a href="pictures/eventadmin.png">Image</a>)
| Events | forms.py | Works as expected | (<a href="pictures/eventforms.png">Image</a>)
| Events | models.py | Works as expected | (<a href="pictures/eventmodels.png">Image</a>)
| Bag | urls.py | Works as expected | (<a href="pictures/bagurls.png">Image</a>)
| Bag | views.py | Works as expected | (<a href="pictures/bagview.png">Image</a>)
| Bag | context.py | Works as expected | (<a href="pictures/bagcontext.png">Image</a>)
| Checkout | urls.py | Works as expected | (<a href="pictures/checkouturls.png">Image</a>)
| Checkout | views.py | Works as expected | (<a href="pictures/checkoutviews.png">Image</a>)
| Checkout |forms.py | Works as expected | (<a href="pictures/checkoutforms.png">Image</a>)
| Checkout |admin.py | Works as expected | (<a href="pictures/checkoutadmin.png">Image</a>)
| Checkout |signals.py | Works as expected | (<a href="pictures/signals.png">Image</a>)
| Checkout |models.py | Works as expected | (<a href="pictures/checkoutmodels.png">Image</a>)
| Profiles |urls.py | Works as expected | (<a href="pictures/profilesurl.png">Image</a>)
| Profiles |views.py | Works as expected | (<a href="pictures/profilesview.png">Image</a>)
| Profiles |admin.py | Works as expected | (<a href="pictures/profileadmin.png">Image</a>)
| Profiles |forms.py | Works as expected | (<a href="pictures/profileform.png">Image</a>)
| Profiles |models.py | Works as expected | (<a href="pictures/profilemodels.png">Image</a>)
| Venues |urls.py | Works as expected | (<a href="pictures/ven_url.png">Image</a>)
| Venues |views.py | Works as expected | (<a href="pictures/ven_views.png">Image</a>)
| Venues |forms.py | Works as expected | (<a href="pictures/ven_form.png">Image</a>)
| Venues |models.py | Works as expected | (<a href="pictures/ven_model.png">Image</a>)
| Contact |urls.py | Works as expected | (<a href="pictures/con_url.png">Image</a>)
| Contact |views.py | Works as expected | (<a href="pictures/con_views.png">Image</a>)
| Contact |forms.py | Works as expected | (<a href="pictures/con_form.png">Image</a>)
| Contact |models.py | Works as expected | (<a href="pictures/con_model.png">Image</a>)

### CSS
> Css validator was used to check the code for my css.
> All the code passes with no errors or warnings.

| Validation| Result | Image |
| ------ | ------ | ------ |
| CSS | Works as expected | (<a href="pictures/css.png">Image</a>)  |

### HTML
> Html Validator was used to check the code for html.
> All the code passes with no errors or warnings except for 2 warnings.
> The type attribute is not neccessary in a script tag
> An alt tag is missing when you choose a flag because of django countries

| App| Page |Result | Image
| ------ | ------ | ------ | ------ |
| Home | Home | Works as expected | (<a href="pictures/home-html.png">Image</a>)
| Home | Subscribe | Works as expected | (<a href="pictures/subscribe-html.png">Image</a>)
| Home | Gallery | Works as expected | (<a href="pictures/galleryhtml.png">Image</a>)
| Home | 404 | Works as expected | (<a href="pictures/404-html.png">Image</a>)
| Events | Events | Works as expected | (<a href="pictures/events-html.png">Image</a>)
| Events | Create Event | Works as expected | (<a href="pictures/add-event-html.png">Image</a>)
| Events | Edit Event | Works as expected | (<a href="pictures/edit-event-html.png">Image</a>)
| Events | Delete Event | Works as expected | (<a href="pictures/delete-event-html.png">Image</a>)
| Events | Event Detail | Works as expected | (<a href="pictures/event-detail-html.png">Image</a>)
| Venues | Venues | Works as expected | (<a href="pictures/venue-html.png">Image</a>)
| Venues | Create Venue | Works as expected | (<a href="pictures/add-venue-html.png.png">Image</a>)
| Venues | Edit Venue | Works as expected | (<a href="pictures/edit-venue-html.png">Image</a>)
| Venues | Delete Venue | Works as expected | (<a href="pictures/delete-venue-html.png">Image</a>)
| Events | Venue Detail | Works as expected | (<a href="pictures/venue-detail-html.png">Image</a>)
| Bag | Bag | Works as expected | (<a href="pictures/bag-html.png">Image</a>)
| Contact | Contact Us | Works as expected | (<a href="pictures/contact-us-html.png">Image</a>)
| Profiles | Profile | Works as expected | (<a href="pictures/profile-html.png">Image</a>)
| Accounts | Login | Works as expected | (<a href="pictures/login-html.png">Image</a>)
| Accounts | Logout | Works as expected | (<a href="pictures/logout-html.png">Image</a>)
| Accounts | Sign Up | Works as expected | (<a href="pictures/signup-html.png">Image</a>)
| Checkout | Checkout | Works as expected | (<a href="pictures/checkouthtml.png">Image</a>)

### Lighthouse 

| Test| Result |Image |
| ------ | ------ | ------ |
| Test 1 | Works as expected | (<a href="pictures/ligthouseh.png">Image</a>)
| Test 2 | Works as expected | (<a href="pictures/ligthousee.png">Image</a>)
| Test 3 | Works as expected | (<a href="pictures/ligthouseed.png">Image</a>)
| Test 4 | Works as expected | (<a href="pictures/ligthousec.png">Image</a>)
| Test 5 | Works as expected | (<a href="pictures/ligthousep.png">Image</a>)

## Test Of All Features

| App| Feature | Action | Expectations | Result |
| ------ | ------ | ------ | ------ | ------ |
| Accounts | Log In | User enters login credentials | User gets signed in and redirected to the homepage | Works as expected |
| Accounts | Log Out | User press the logout button | User gets signed out and redirected to the homepage |Works as expected |
| Accounts | Sign Up | User signs up and creates a user | User gets signed in, gets a profile and redirected to the homepage| Works as expected |
| Events | Create Event | User press create button and fills in the form | A new event will be created and added to the eventlist | Works as expected |
| Events | Edit Event | User press Edit button and fills in the form | The event will be edited and appears on the eventlist | Works as expected |
| Events | Delete Event | User press delete button | The event will be deleted | Works as expected |
| Profile | Edit Profile | User press Edit button and fills in the form | The Profile will be edited and appears on the profile page | Works as expected |
| Payment | Make A Payment | User enthers their payment info and presses pay | A payment will be transferred | Works as expected |
| Payment | Download A Ticket | User press Download button| A ticket will be downloaded | Works as expected |
| Venues | Create Venue | User press create button and fills in the form | A new venue will be created and added to the venuelist | Works as expected |
| Venues | Edit Venue | User press Edit button and fills in the form | The venue will be edited and appears on the venuelist | Works as expected |
| Venues | Delete Venue | User press delete button | The venue will be deleted | Works as expected |
| Contact | Contact Us | User fills in the form and press contact button | A message will appear form the user on admin page | Works as expected |

## Security
> You can't use CRUD functionality when you are signed out.
> When you write something that is not a correct url you get redirected to a 404 page

| Test | Try |Action | Result |
| ------ | ------ | ------ | ------ |
| Create Event | Not a superuser tries to create an event via url | Redirected to sign in page | Works as expected |
| Create Venue | Not a superuser tries to create a venue via url | Redirected to sign in page | Works as expected |
| Edit Event | Not a superuser tries to edit an event or edit another users event via url | Redirected to sign in page | Works as expected |
| Edit Venue | Not a superuser tries to edit a venue or edit another users venue via url | Redirected to sign in page | Works as expected |
| Delete Event | Not a superuser tries to delete an event or delete another users event via url | Works as expected |
| Delete Venue | Not a superuser tries to delete a venue or delete another users venue via url | Redirected to sign in page | Works as expected |
| Incorrect Url | A user tries to write an incorrect url |Redirected to 404 page | Works as expected |
## Links

| Type| Page | Expectations | Result |
| ------ | ------ | ------ | ------ |
| External | Linkedin | Gets redirected to Linkedin | Works as expected |
| External | Facebook | Gets redirected to Facebook | Works as expected |
| External | Twitter/X | Gets redirected to Twitter/X |Works as expected |
| External | Instagram | Gets redirected to Instagram | Works as expected |
| Navigation | Home | Gets redirected to Homepage | Works as expected |
| Navigation | Events | Gets redirected to Eventspage | Works as expected |
| Navigation | Bag | Gets redirected to Bagpage | Works as expected |
| Navigation | Subscribe | Gets redirected to Subscribepage | Works as expected |
| Navigation | Venues | Gets redirected to Venuespage | Works as expected |
| Navigation | Contact Us | Gets redirected to Contactpage | Works as expected |
| Navigation | Profile | Gets redirected to Profilepage | Works as expected |
| Navigation | New Event | Gets redirected to Create Event page| Works as expected |
| Navigation | New Venue| Gets redirected to Create Venue page | Works as expected |

## Different Types Of Headers 

| Account| Expectations |Result | Image |
| ------ | ------ | ------ | ------ |
| Signed Out | Gives the user events, bag, subscribe, venues and login links | Works as expected | (<a href="pictures/header_logout.png">Image</a>) |
| Signed In | Same links as a signed out user with the adition of a contact and account link | Works as expected | (<a href="pictures/header_login.png">Image</a>) |
| Superuser | Same links as a signed in user with the adition of a create link | Works as expected | (<a href="pictures/header_super.png">Image</a>) |





## Sizes 
[See Sizes Here](sizes.md)

## Marketing & SEO
[See Marketing Here](marketing.md)

[Back to Top](#table-of-contents)
