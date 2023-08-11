# Live Events

[Here is the livelink](https://live-events-9e71b07dd75e.herokuapp.com/)

Welcome to our event site, where unforgettable experiences await! Whether you're looking for a night of live music, a thrilling sports match, an immersive theater performance, or something in between, we've got you covered. Our site offers a wide variety of events to suit every taste and budget, all in one convenient location. Plus, purchasing tickets is easy and hassle-free, so you can spend less time planning and more time enjoying the excitement of the event. Join us in creating unforgettable memories at the hottest events around we can't wait to see you there!

## Features

- Register an account for the site to login and logout
- Upload your event to the site
- Edit and update your event
- Delete your event
- Buy tickets to events
- Create a profile
- Create, edit and delete a venue
- Contact the site for questions and ideas

## models

I have created 6 models for this project. This is Events and looks like this
| | |
| ------ | ------ |
| user | ForeignKey |
| name | CharField |
| description | CharField |
| price | DecimalField |
| location | CharField |
| date | DateField |
| time | TimeField |
| image | ResizedImagedField |

This is Order and looks like this
| | |
| ------ | ------ |
| order_number | Charfield |
| full_name | CharField
| email | EmailField |
| phone_number | CharField |
| date_now | DateTimeField |
| order_total | DecimalField |

This is OrderItem and looks like this
| | |
| ------ | ------ |
| order | ForeignKey |
| event | ForeignKey
| quantity | IntegerField |
| lineitem_total | DecimalField |

This is Profile and looks like this
| | |
| ------ | ------ |
| user | ForeignKey |
| image | ResizedImageField |
| about | CharField |
| real_name | CharField |

This is Venues and looks like this
| | |
| ------ | ------ |
| user | ForeignKey |
| address | CharField |
| phone_number | CharField |
| home_page | URLField |
| social_media | URLField |
| city | CharField |
| country | CountryField |
| name | CharField |
| image | ResizedImagedField |

This is Contact and looks like this
| | |
| ------ | ------ |
| name | CharField |
| image | EmailField |
| phone_number | CharField |
| Subject | TextField |

Here is an image of the ERD Relationship that I created in DrawSQL

<details>
  <summary>Entity Relationship Diagram</summary>
  <img src="pictures/drawSQL.png" alt="Image description">
</details>

## User Stories

These are the user stories I developed at the start of the project, prioritizing their implementation using the Moscow method.

| Userstories                                                                                                          | Moscow      |
| -------------------------------------------------------------------------------------------------------------------- | ----------- |
| As a site user, I can register an account so that I can have a personal account                                      | Must Have   |
| As a site user, I can login and logout so that I can access my personal information                                  | Must Have   |
| As a Site User I can have a personalized profile so that I can view my orders                                        | Could Have  |
| As a shopper I can view a list of events so that I can select one to purchase tickets to                             | Must Have   |
| As a shopper I can view Individual Eventdetails so that i can identify the details , time and the price of the event | Must Have   |
| As a shopper I can view the total of my purchase so that I can avoid to spend too much money                         | Must Have   |
| As a shopper I can view items in my bag so that I can see all the items I am going to purchase                       | Must Have   |
| As a Shopper I can adjust the quantity in my bag so that I can make changes before I purchase                        | Should Have |
| As a shopper I can easily enter my payment information so that I can checkout quickly                                | Must Have   |
| As a shopper I can search for an event so that I can find a specific event that interests me                         | Should Have |
| As an admin, I can add an event so that new events will be added to the page                                         | Must Have   |
| As an admin, I can edit an event so that I can update the details of the event                                       | Must Have   |
| As an admin, I can delete an event so that I can remove events that are fully booked                                 | Must Have   |
| As an admin I can create a profile so I can see my uploaded events                                                   | Should Have |
| As a user I can search for an event so I can discover new, upcoming events                                           | Could Have  |
| As an admin, I can edit my profile so I can make changes to it                                                       | Should Have |
| As a buyer I can download my order so I can save it on my computer                                                   | Must Have   |
| As a shopper I can view a list of events so that I can see where the events are held | Must Have |
| As an admin, I can add a venue so that new venues will be added to the page | Must Have |
| As an admin, I can edit a venue so that I can update the details of the venue | Must Have |
| As an admin, I can delete a venue so that I can remove venues that are closed | Must Have |
| As a site user, I can contact the page so that I can share my ideas and questions to the site | Must Have |


I used Trello during my development because I am used to work on that platform from earlier jobs and projects.

<details>
  <summary>Kanban on Trello</summary>
  <img src="pictures/trello2.png" alt="Image description">
</details>

## Sizes

- Small: 320x480
- Medium: 768x1024
- Large: 1280x802
- X-large: 1600x992

### Home

<details>
  <summary>Small</summary>
  <img src="pictures/home_small_1.png" alt="Image description">
  <img src="pictures/home_small_2.png" alt="Image description">
  <img src="pictures/home_small_3.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/home_medium.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/home_large.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/home_xlarge.png" alt="Image description">
</details>

### Events

<details>
  <summary>Small</summary>
  <img src="pictures/events_small_1.png" alt="Image description">
  <img src="pictures/events_small_2.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/events_medium_1.png" alt="Image description">
  <img src="pictures/events_medium_2.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/events_large_1.png" alt="Image description">
  <img src="pictures/events_large_2.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/events_xlarge_1.png" alt="Image description">
  <img src="pictures/events_xlarge_2.png" alt="Image description">
</details>

### Venues

<details>
  <summary>Small</summary>
  <img src="pictures/venues_small_1.png" alt="Image description">
  <img src="pictures/venues_small_2.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/ven_med.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/venues_large.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/venues_xlarge.png" alt="Image description">

</details>

### Bag 

<details>
  <summary>Small</summary>
  <img src="pictures/bag_small1.png" alt="Image description">
  <img src="pictures/bag_small2.png" alt="Image description">
  <img src="pictures/bag_small3.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/bag_medium1.png" alt="Image description">
  <img src="pictures/bag_medium2.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/bag_large.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/bag_xlarge.png" alt="Image description">

### Empty Bag

<details>
  <summary>Small</summary>
  <img src="pictures/bag_empty_small.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/bag_empty_medium.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/bag_empty_large.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/bag_empty_xlarge.png" alt="Image description">

###  Gallery

<details>
  <summary>Small</summary>
  <img src="pictures/gallery_small1.png" alt="Image description">
  <img src="pictures/gallery_small2.png" alt="Image description">
</details>

<details>
  <summary>Medium</summary>
  <img src="pictures/gallery_medium1.png" alt="Image description">
  <img src="pictures/gallery_medium2.png" alt="Image description">
</details>

<details>
  <summary>Large</summary>
  <img src="pictures/gallery_large1.png" alt="Image description">
  <img src="pictures/gallery_large2.png" alt="Image description">
</details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/gallery_xlarge1.png" alt="Image description">
  <img src="pictures/gallery_xlarge2.png" alt="Image description">

### Subscribe

<details>
  <summary>Small</summary>
  <img src="pictures/subscribe_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/subscribe_medium.png" alt="Image description">
  </details>


  <details>
  <summary>Large</summary>
  <img src="pictures/subscribe_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/subscribe_xlarge.png" alt="Image description">
  </details>

### Login

<details>
  <summary>Small</summary>
  <img src="pictures/login_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/login_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/login_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/login_xlarge.png" alt="Image description">
  </details>

### Logout

<details>
  <summary>Small</summary>
  <img src="pictures/signout_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/signout_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/signout_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/signout_xlarge.png" alt="Image description">
  </details>

### Signup

<details>
  <summary>Small</summary>
  <img src="pictures/signup_small1.png" alt="Image description">
    <img src="pictures/signup_small2z.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/signup_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/signup_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/signup_xlarge.png" alt="Image description">
  </details>
  
### Profile

<details>
  <summary>Small</summary>
  <img src="pictures/profile_small_1.png" alt="Image description">
    <img src="pictures/profile_small_2.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/profile_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/profile_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/profile_xlarge.png" alt="Image description">
  </details>

  ### Create Event

<details>
  <summary>Small</summary>
  <img src="pictures/create_event_small1.png" alt="Image description">
    <img src="pictures/create_event_small2z.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/create_event_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/create_event_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/create_event_xlarge.png" alt="Image description">
  </details>

### Create Venue

<details>
  <summary>Small</summary>
  <img src="pictures/create_venue_small1.png" alt="Image description">
    <img src="pictures/create_venue_small2z.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/create_venue_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/create_venue_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/create_venue_xlarge.png" alt="Image description">
  </details>
  
### Edit Event

<details>
  <summary>Small</summary>
  <img src="pictures/edit_event_small1.png" alt="Image description">
    <img src="pictures/edit_event_small2.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/edit_event_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/edit_event_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/edit_event_xlarge.png" alt="Image description">
  </details>

### Edit Venue


<details>
  <summary>Small</summary>
  <img src="pictures/edit_venue_small1.png" alt="Image description">
    <img src="pictures/edit_venue_small2.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/edit_venue_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/edit_venue_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/edit_venue_xlarge.png" alt="Image description">
  </details>
  
### Delete Event

<details>
  <summary>Small</summary>
  <img src="pictures/delete_event_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/delete_event_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/delete_event_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/delete_event_xlarge.png" alt="Image description">
  </details>

### Delete Venue

<details>
  <summary>Small</summary>
  <img src="pictures/delete_venue_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/delete_venue_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/delete_venue_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/delete_venue_xlarge.png" alt="Image description">
  </details>

### Event Detail

<details>
  <summary>Small</summary>
  <img src="pictures/event_detail_small1.png" alt="Image description">
  <img src="pictures/event_detail_small2.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/event_detail_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/event_detail_large_1.png" alt="Image description">
    <img src="pictures/event_detail_large2.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
 <img src="pictures/event_detail_xlarge1.png" alt="Image description">
  <img src="pictures/event_detail_xlarge2.png" alt="Image description">
  </details>

### Venue Detail

<details>
  <summary>Small</summary>
  <img src="pictures/venue_detail_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/venue_detail_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/venue_detail_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/venue_detail_xlarge.png" alt="Image description">
  </details>

  ### Checkout

<details>
  <summary>Small</summary>
  <img src="pictures/checkout_small1.png" alt="Image description">
  <img src="pictures/checkout_small2.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/checkout_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/checkout_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/checkout_xlarge.png" alt="Image description">
  </details>

  ### Checkout Success

<details>
  <summary>Small</summary>
  <img src="pictures/success_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/success_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/success_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/success_xlarge.png" alt="Image description">
  </details>

  ### 404

<details>
  <summary>Small</summary>
  <img src="pictures/404_small.png" alt="Image description">
  </details>

  <details>
  <summary>Medium</summary>
  <img src="pictures/404_medium.png" alt="Image description">
  </details>

  <details>
  <summary>Large</summary>
  <img src="pictures/404_large.png" alt="Image description">
  </details>

<details>
  <summary>Xlarge</summary>
  <img src="pictures/404_xlarge.png" alt="Image description">
  </details>

## Design

- I have chosen to have a footer and a header available all the time because it is important for the visitor to be able to navigate easy all the time. I have chosen words on the header to easy describe what the links do and go to so the user easy can understand and icons for my socialmedia because the icons are well known and designed well.  
- For my homepage I have chosen to use images to describe what the page are for and I think the images are beautiful and fits well on my page. 
- The event/venue/bag pages uses card attributes for the items because it packages the information well and makes the layout easy to follow on both small and large screen sizes. 
- I have a minmal approach on my site because I want only the keywords and the information to be easy to see and understand. 
- My color is light blue/turqouise because I want to have a light visual on my site because that is what I like myself and I wanted to have a background that I personally have not seen before to make the page stand out compared to others.
- I chose a font that is easy to read, with a friendly and inviting shape, ensuring clarity and creating a visually appealing experience for visitors
  
## SEO

The purpose of my site is to provide small businesses with an easy way to publish their events and reach their target audience. To generate ideas and gauge the search volume and competition of keywords related to events, I used Google Autosearch and Wordtracker. After researching and analyzing the results, I selected the keywords that were most relevant to my site's purpose.

<details>
  <summary>Google</summary>
  <img src="pictures/google1.png" alt="Image description">
  <img src="pictures/google2.png" alt="Image description">
</details>

<details>
  <summary>Wordtracker</summary>
  <img src="pictures/cheap.png" alt="Image description">
  <img src="pictures/family.png" alt="Image description">
</details>

I decided to use these keywords beacuse they gave me good results and are related to what I want to contribute with on this site.

- Community events Events near me
- Nightlife events Family event
- Upcoming events
- Where to see local bands
- Find tickets for karaoke events
- Get tickets for local bar events
- Cheap event tickets online
- Community events and ticket sales
- local family events near me
- cheap easy event ticket online
- activities and events that parents and kids can enjoy together

This is how I implemented some of these keywords on my site.

<details>
<summary>Keywords</summary>
  <img src="pictures/homeseo2.png" alt="Image description">
  <img src="pictures/description.png" alt="Image description">
</details>

It's important to note that since the content on my site will vary depending on the events being showcased, SEO is an ongoing and continuous effort that requires responsiveness to adapting content to match what users are searching for.

### Marketing
I creates three different avatars so I could learn to know some of my target auddiences and approach them in a good way

#### Avatar 1 Young Professional/Student

  - Location: Lives in a small city
  - Age: 18-25
  - Career: Studies/Young Professional
  - Family: None
  - Motivation to buy: Wants to have fun times with friends
  - Buying concerns: Limited budget, needs to save money for events
- Media: Social Media, YouTube
- Approach: For this avatar, organic social media marketing would be effective. Focus on creating engaging content such as short videos and images showcasing your events. Advertise the event well in advance and offer packages like early bird tickets to incentivize early purchases. Utilize platforms like Facebook, Instagram, and YouTube to reach this audience.

#### Avatar 2 Wife with 2 kids
- Lives in a medium-sized city
- Age: 35-40
- Career: Teacher
- Family: Parents to kids who are 7-12 years old
- Motivation to buy: Wants to spend time and activities with their family
- Buying concerns: Limited budget due to family and household expenses
- Media: Instagram, News sites, Clothes sites, Facebook, Television
- Approach: Display marketing banners on relevant websites such as news sites and clothes sites, with a clear call to action. Target parents with engaging visuals and messaging that highlights the family-friendly nature of our events. Utilize platforms like Instagram, Facebook, and television advertising to reach this audience.

#### Avatar 3 Music Enthusiast
- Location: Lives in a large city
- Age: 55-60
- Career: Scrum Master in a tech company
- Family: Wife and adult kids
- Motivation to buy: Interested in music and has a collection of vinyl records
- Buying concerns: Picky about choices, seeks the best experiences
- Media: Facebook, News sites, Television
- Approach: Paid search marketing would be effective for this avatar. Create targeted ads that appear on platforms like Facebook and news sites, focusing on the music aspect of our events. Highlight unique experiences and the quality of the performances. Consider partnering with local record stores or music blogs to reach this audience.


### Facebook Page

<details>
  <summary>Facebook</summary>
  <img src="pictures/facebook1.png" alt="Image description">
  <img src="pictures/facebook2.png" alt="Image description">
  <img src="pictures/facebook3.png" alt="Image description">
</details>

### Subscribe

<details>
  <summary>Subscribe</summary>
  <img src="pictures/subscribe1.png" alt="Image description">
  <img src="pictures/subscribe2.png" alt="Image description">
</details>

I've included links to social media profiles such as Instagram, LinkedIn, and Twitter in the footer of my website. As many of the creators associated with the events I promote use social media as a means of self-promotion, I believe this addition contributes to the content, purpose, and marketing of my site.

## Validation

> PEP8 Validation Service was used to check the code for PEP8 requirements.
> All the code passes with no errors or warnings.

### Home

<details>
  <summary>urls.py</summary>
  <img src="pictures/homeurls.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/homeviews.png" alt="Image description">
</details>

### Events

<details>
  <summary>urls.py</summary>
  <img src="pictures/eventurls.png" alt="Image description">
</details>

<details>
  <summary>admin.py</summary>
  <img src="pictures/eventadmin.png" alt="Image description">
</details>

<details>
  <summary>forms.py</summary>
  <img src="pictures/eventforms.png" alt="Image description">
</details>

<details>
  <summary>models.py</summary>
  <img src="pictures/eventmodels.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/eventviews.png" alt="Image description">
</details>

### Bag

<details>
  <summary>urls.py</summary>
  <img src="pictures/bagurls.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/bagview.png" alt="Image description">
</details>

<details>
  <summary>context.py</summary>
  <img src="pictures/bagcontext.png" alt="Image description">
</details>

### Checkout

<details>
  <summary>urls.py</summary>
  <img src="pictures/checkouturls.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/checkoutviews.png" alt="Image description">
</details>

<details>
  <summary>models.py</summary>
  <img src="pictures/checkoutmodels.png" alt="Image description">
</details>

<details>
  <summary>forms.py</summary>
  <img src="pictures/checkoutforms.png" alt="Image description">
</details>

<details>
  <summary>admin.py</summary>
  <img src="pictures/checkoutadmin.png" alt="Image description">
</details>

<details>
  <summary>signals.py</summary>
  <img src="pictures/signals.png" alt="Image description">
</details>

### Profiles

<details>
  <summary>urls.py</summary>
  <img src="pictures/profilesurl.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/profilesview.png" alt="Image description">
</details>

<details>
  <summary>models.py</summary>
  <img src="pictures/profilemodels.png" alt="Image description">
</details>

<details>
  <summary>forms.py</summary>
  <img src="pictures/profileforms.png" alt="Image description">
</details>

<details>
  <summary>admin.py</summary>
  <img src="pictures/profileadmin.png" alt="Image description">
</details>

### Venues

<details>
  <summary>urls.py</summary>
  <img src="pictures/ven_url.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/ven_views.png" alt="Image description">
</details>

<details>
  <summary>models.py</summary>
  <img src="pictures/ven_model.png" alt="Image description">
</details>

<details>
  <summary>forms.py</summary>
  <img src="pictures/ven_form.png" alt="Image description">
</details>

### Contact

<details>
  <summary>urls.py</summary>
  <img src="pictures/con_url.png" alt="Image description">
</details>

<details>
  <summary>views.py</summary>
  <img src="pictures/con_views.png" alt="Image description">
</details>

<details>
  <summary>models.py</summary>
  <img src="pictures/con_model.png" alt="Image description">
</details>

<details>
  <summary>forms.py</summary>
  <img src="pictures/con_form.png" alt="Image description">
</details>

## Test

### Accounts

<details>
  <summary>Signup</summary>
  <img src="pictures/signup1.png" alt="Image description">
  <img src="pictures/signup2.png" alt="Image description">
</details>

<details>
  <summary>Login</summary>
  <img src="pictures/login1.png" alt="Image description">
  <img src="pictures/login2.png" alt="Image description">
</details>

<details>
  <summary>Sign Out</summary>
  <img src="pictures/signout.png" alt="Image description">
</details>

### Events

<details>
  <summary>Create Event</summary>
  <img src="pictures/create1.png" alt="Image description">
  <img src="pictures/create2.png" alt="Image description">
</details>

<details>
  <summary>Edit Event</summary>
  <img src="pictures/edit1.png" alt="Image description">
  <img src="pictures/edit2.png" alt="Image description">
</details>

<details>
  <summary>Delete Event</summary>
  <img src="pictures/delete1.png" alt="Image description">
  <img src="pictures/delete2.png" alt="Image description">
</details>

### Profile

<details>
  <summary>Edit Profile</summary>
  <img src="pictures/editp1.png" alt="Image description">
  <img src="pictures/editp2.png" alt="Image description">
  <img src="pictures/editp3.png" alt="Image description">
</details>

### Payment

<details>
  <summary>Payment</summary>
  <img src="pictures/pay1.png" alt="Image description">
  <img src="pictures/pay2.png" alt="Image description">
  <img src="pictures/pay3.png" alt="Image description">
  <img src="pictures/pay4.png" alt="Image description">
</details>

<details>
  <summary>Download</summary>
  <img src="pictures/download.png" alt="Image description">
</details>

### Venues

<details>
  <summary>Create</summary>
  <img src="pictures/create_venue.png" alt="Image description">
  <img src="pictures/create_venue_2.png" alt="Image description">
</details>

<details>
  <summary>Edit</summary>
  <img src="pictures/edit_venue.png" alt="Image description">
  <img src="pictures/edit_venue_2.png" alt="Image description">
  <img src="pictures/edit_venue_3.png" alt="Image description">
</details>

<details>
  <summary>Delete</summary>
  <img src="pictures/delete_venue_1.png" alt="Image description">
  <img src="pictures/delete_venue_2.png" alt="Image description">
  <img src="pictures/delete-venue_3.png" alt="Image description">
</details>

### Contact Form

<details>
  <summary>Contact us</summary>
  <img src="pictures/contact_1.png" alt="Image description">
  <img src="pictures/contact_2.png" alt="Image description">
</details>

### External links


<details>
  <summary>Linkedin</summary>
  <img src="pictures/linkedin_1.png" alt="Image description">
  <img src="pictures/linkedin_2.png" alt="Image description">
</details>


<details>
  <summary>Instagram</summary>
  <img src="pictures/instagram_1.png" alt="Image description">
  <img src="pictures/instagram_2.png" alt="Image description">
</details>

<details>
  <summary>Twitter/X</summary>
  <img src="pictures/twitter_1.png" alt="Image description">
  <img src="pictures/twitter_2.png" alt="Image description">
</details>


<details>
  <summary>Facebook</summary>
  <img src="pictures/facebook_1.png" alt="Image description">
  <img src="pictures/facebook_2.png" alt="Image description">
</details>

### Navigation links

<details>
  <summary>Home</summary>
  <img src="pictures/home_1.png" alt="Image description">
  <img src="pictures/home_2.png" alt="Image description">
</details>

<details>
  <summary>Events</summary>
  <img src="pictures/events_1.png" alt="Image description">
  <img src="pictures/events_2.png" alt="Image description">
</details>

<details>
  <summary>Bag</summary>
  <img src="pictures/bag_1.png" alt="Image description">
  <img src="pictures/bag_2.png" alt="Image description">
  <img src="pictures/bag_3.png" alt="Image description">
</details>

<details>
  <summary>Subscribe</summary>
  <img src="pictures/subscribe_1.png" alt="Image description">
  <img src="pictures/subscribe_2.png" alt="Image description">
</details>

<details>
  <summary>Venues</summary>
  <img src="pictures/venues_1.png" alt="Image description">
  <img src="pictures/venues_2.png" alt="Image description">
</details>

<details>
  <summary>Contact Us</summary>
  <img src="pictures/contact_us_1.png" alt="Image description">
  <img src="pictures/contact_us_2.png" alt="Image description">
</details>

<details>
  <summary>Profile</summary>
  <img src="pictures/profile_1.png" alt="Image description">
  <img src="pictures/profile_2.png" alt="Image description">
</details>

<details>
  <summary>New Event</summary>
  <img src="pictures/new_event_1.png" alt="Image description">
  <img src="pictures/new_event_2.png" alt="Image description">
</details>

<details>
  <summary>New venue</summary>
  <img src="pictures/new_venue_1.png" alt="Image description">
  <img src="pictures/new_venue_2.png" alt="Image description">
</details>

### Header

<details>
  <summary>Header when you are a superuser</summary>
  <img src="pictures/header_super.png" alt="Image description">
</details>

<details>
  <summary>Header when you are logged in</summary>
  <img src="pictures/header_login.png" alt="Image description">
</details>

<details>
  <summary>Header when you are logged out</summary>
  <img src="pictures/header_logout.png" alt="Image description">
</details>

### Security

<details>
  <summary>When you are logged out and try to go to the create page for events and venues</summary>
  <img src="pictures/try_event_1.png" alt="Image description">
  <img src="pictures/try_event_2.png" alt="Image description">
  <img src="pictures/try_venue_1.png" alt="Image description">
  <img src="pictures/try_venue_2.png" alt="Image description">
</details>

<details>
  <summary>When you are logged out and try to go to the edit page for events and venues</summary>
  <img src="pictures/try_edit_event_1.png" alt="Image description">
  <img src="pictures/try_edit_event_2.png" alt="Image description">
  <img src="pictures/try_edit_venue_1.png" alt="Image description">
  <img src="pictures/try_edit_venue_2.png" alt="Image description">
</details>


<details>
  <summary>When you are logged out and try to go to the delete page for events and venues</summary>
  <img src="pictures/try_delete_event_1.png" alt="Image description">
  <img src="pictures/try_delete_event_2.png" alt="Image description">
  <img src="pictures/try_delete_venue_1.png" alt="Image description">
  <img src="pictures/try_delete_venue_2.png" alt="Image description">
</details>

<details>
  <summary>When you are write something that is not a correct url you get redirected to a 404 page</summary>
  <img src="pictures/404.png" alt="Image description">

</details>

## Validation 2

> Lighthouse to check quality and performance of the page.

<details>
  <summary>Lighthouse</summary>
  <img src="pictures/ligthouseh.png" alt="Image description">
  <img src="pictures/lighthousee.png" alt="Image description">
  <img src="pictures/lighthouseed.png" alt="Image description">
  <img src="pictures/lighthousec.png" alt="Image description">
  <img src="pictures/lighthousep.png" alt="Image description">
</details>

> Html Validator was used to check the code for html.
> All the code passes with no errors or warnings except for 2 warnings.
> The type attribute is not neccessary in a script tag
> An alt tag is missing when you choose a flag because of django countries

<details>
  <summary>home</summary>
  <img src="pictures/home-html.png" alt="Image description">
</details>

<details>
  <summary>Events</summary>
  <img src="pictures/events-html.png" alt="Image description">
</details>

<details>
  <summary>Create Event</summary>
  <img src="pictures/add-event-html.png" alt="Image description">
</details>

<details>
  <summary>Edit Event</summary>
  <img src="pictures/edit-event-html.png" alt="Image description">
</details>

<details>
  <summary>Delete Event</summary>
  <img src="pictures/delete-event-html.png" alt="Image description">
</details>

<details>
  <summary>Event Detail</summary>
  <img src="pictures/event-detail-html.png" alt="Image description">
</details>

<details>
  <summary>Venues</summary>
  <img src="pictures/venue-html.png" alt="Image description">
</details>

<details>
  <summary>Create Venue</summary>
  <img src="pictures/add-venue-html.png" alt="Image description">
</details>

<details>
  <summary>Edit Venue</summary>
  <img src="pictures/edit-venue-html.png" alt="Image description">
</details>

<details>
  <summary>Delete Venue</summary>
  <img src="pictures/delete-venue-html.png" alt="Image description">
</details>

<details>
  <summary>Venue Detail</summary>
  <img src="pictures/venue-detail-html.png" alt="Image description">
</details>

<details>
  <summary>Bag</summary>
  <img src="pictures/bag-html.png" alt="Image description">
</details>

<details>
  <summary>Subscribe</summary>
  <img src="pictures/subscribe-html.png" alt="Image description">
</details>

<details>
  <summary>Contact Us</summary>
  <img src="pictures/contact-us-html.png" alt="Image description">
</details>

<details>
  <summary>Profile</summary>
  <img src="pictures/profile-html.png" alt="Image description">
</details>

<details>
  <summary>Login</summary>
  <img src="pictures/login-html.png" alt="Image description">
</details>

<details>
  <summary>Logout</summary>
  <img src="pictures/logout-html.png" alt="Image description">
</details>

<details>
  <summary>Sign Up</summary>
  <img src="pictures/signup-html.png" alt="Image description">
</details>

<details>
  <summary>Gallery</summary>
  <img src="pictures/galleryhtml.png" alt="Image description">
</details>

<details>
  <summary>checkout</summary>
  <img src="pictures/checkouthtml.png" alt="Image description">
</details>

<details>
  <summary>404</summary>
  <img src="pictures/404-html.png" alt="Image description">
</details>

> Css validator was used to check the code for my css.
> All the code passes with no errors or warnings.

<details>
  <summary>CSS</summary>
  <img src="pictures/css.png" alt="Image description">
</details>

## Tech

I used these libraries, frameworks and databases for this project

- Cloudinary
- GitHub
- Django AllAuth
- Pillow
- Psycopg2
- PostgreSQL
- Stripe
- Django: receiver
- Django: ResizedImageField
- Django: CountryField
- crispy_forms
- Django: User
- Django: post_save
- Heroku
- Code anywhere

## Features to make in The Future

- Save the users bought tickets to their profile
- A list of the pages profiles
- Categorys to the events
- A list of common venues
- A contactpage to contact the profiles
- Email the order and tickets to the buyers

## Deployment

- I have the repository for the page on github.com
- I set up all my secret keys in my env.py and put my env.py in my .gitignore to keep them hidden
- My secret keys include django_secretKey, database_url and cloudinary_url
- set up my debug in my env.py so that debug is true during production and false when it is live
- I freezed all my requirements before I added, commited and pushed everything on Github
- created an app on Heroku called Live Events
- Configured my Config vars on Heroku which includes Database_url, Cloudinary_url, Secret_key, Stripe_pk, Stripe_sk and a port of 8000
- Set up disablecollectstaic for my first Deployment
- Connect Heroku to my repository on github
- Deployed my project manually

## Credits

> Here are some walkthroughs and videos that inspired and helped me with this project.

- [Django Recipe sharing](https://www.youtube.com/watch?v=LsU79aY79UA&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=15)
- [Boutique Ado](https://www.youtube.com/watch?v=3gQazh-EIzY&embeds_referring_euri=https%3A%2F%2Flearn.codeinstitute.net%2F&embeds_referring_origin=https%3A%2F%2Flearn.codeinstitute.net&source_ve_path=NzY3NTg&feature=emb_yt_watermark)

> Here for the css and images

- [Bootstrap for the css](https://getbootstrap.com)
- [Pexels for the images](https://www.pexels.com/)
- [Google font for the fonts](https://fonts.google.com/)
- [Font Awesome for the icons](https://fontawesome.com/)
- [For my favicon](https://favicon.io/favicon-converter/)
