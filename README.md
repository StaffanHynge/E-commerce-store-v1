# Live Events

#### Share your Events with others

[Here is the livelink]()
Welcome to our event site, where unforgettable experiences await! Whether you're looking for a night of live music, a thrilling sports match, an immersive theater performance, or something in between, we've got you covered. Our site offers a wide variety of events to suit every taste and budget, all in one convenient location. Plus, purchasing tickets is easy and hassle-free, so you can spend less time planning and more time enjoying the excitement of the event. Join us in creating unforgettable memories at the hottest events around – we can't wait to see you there!

## Features

- Register a account for the site to login and logout
- Upload your event to the site
- Edit and update your event
- Delete your event
- Buy tickets to events
- Create a profile

## models

I have created 4 models for this project. This is Events and looks like this
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

## User Stories

Here are the user stories I created in the beginning of the project. I have used the moscow method to prioritize what to do first and to know what can be implemented in the future.

| Userstories                                                                                                          | Moscow      | Test |
| -------------------------------------------------------------------------------------------------------------------- | ----------- | ---- |
| As a site user, I can register an account so that I can have a personal account                                      | Must Have   | Yes  |
| As a site user, I can login and logout so that I can access my personal information                                  | Must Have   | Yes  |
| As a Site User I can have a personalized profile so that I can view my orders                                        | Could Have  | Yes  |
| As a shopper I can view a list of events so that I can select one to purchase tickets to                             | Must Have   | Yes  |
| As a shopper I can view Individual Eventdetails so that i can identify the details , time and the price of the event | Must Have   | Yes  |
| As a shopper I can view the total of my purchase so that I can avoid to spend to much money                          | Must Have   |
| As a shopper I can view items in my bag so that I can see all the items I am going to purchase                       | Must Have   |
| As a Shopper I can adjust the quantity in my bag so that I can make changes before I purchase                        | Must Have   |
| As a shopper I can easily enter my payment information so that I can checkout quickly                                | Must Have   |
| As a shopper I can search for an event so that I can find a specific event that interests me                         | Should Have |
| As an admin, I can add an event so that new events will be added to the page                                         | Must Have   |
| As an admin, I can edit an event so that I can update the details of the event                                       | Must Have   |
| As an admin, I can delete an event so that I can remove events that are fully booked                                 | Must Have   |

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
