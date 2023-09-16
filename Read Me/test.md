# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Validation](#validation)
    - [PEP8](#pep8)
    - [CSS](#css)
    - [HTML](#html)
    - [Lighthouse](#lighthouse)
  - [Test Of All Features](#test-of-all-features)
    - [Links](#links)
    - [Different Types Of Headers](#different-types-of-headers)
    - [Security](#security)


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

| App| Feature |Result |
| ------ | ------ | ------ |
| Accounts | Log In | Works as expected |
| Accounts | Log Out | Works as expected |
| Accounts | Sign Up | Works as expected |
| Accounts | Log in | Works as expected |
| Events | Create Event | Works as expected |
| Events | Edit Event | Works as expected |
| Events | Delete Event | Works as expected |
| Profile | Edit Profile | Works as expected |
| Payment | Make A Payment | Works as expected |
| Payment | Download A Ticket | Works as expected |
| Venues | Create Venue | Works as expected |
| Venues | Edit Venue | Works as expected |
| Venues | Delete Venue | Works as expected |
| Contact | Contact Us | Works as expected |


### Links

| Type| Page |Result |
| ------ | ------ | ------ |
| External | Linkedin | Works as expected |
| External | Facebook | Works as expected |
| External | Twitter/X | Works as expected |
| External | Instagram | Works as expected |
| Navigation | Home | Works as expected |
| Navigation | Events | Works as expected |
| Navigation | Bag | Works as expected |
| Navigation | Subscribe | Works as expected |
| Navigation | Venues | Works as expected |
| Navigation | Contact Us | Works as expected |
| Navigation | Profile | Works as expected |
| Navigation | New Event | Works as expected |
| Navigation | New Venue | Works as expected |

### Different Types Of Headers 

| Account| Result | Image |
| ------ | ------ | ------ |
| Superuser | Works as expected | (<a href="pictures/header_super.png">Image</a>) |
| Signed In | Works as expected | (<a href="pictures/header_login.png">Image</a>) |
| Signed Out | Works as expected | (<a href="pictures/header_logout.png">Image</a>) |

### Security
> You can't use CRUD functionality when you are signed out.
> When you write something that is not a correct url you get redirected to a 404 page

| Test | Action | Result |
| ------ | ------ | ------ |
| Create Event | Redirected to sign in page | Works as expected |
| Create Venue | Redirected to sign in page | Works as expected |
| Edit Event | Redirected to sign in page | Works as expected |
| Edit Venue | Redirected to sign in page | Works as expected |
| Delete Event | Redirected to sign in page | Works as expected |
| Delete Venue | Redirected to sign in page | Works as expected |
| Incorrect Url | Redirected to 404 page | Works as expected |

