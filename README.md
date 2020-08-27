# Harvalet

My website is a car valeting service where the user can make an account, sign in and securely purchase various levels of car valeting services each having their own features and price tags. My webpages all follow the same color scheme of orange/ whit and black which I think work very well together granting a clear a very readable experience. The user also has access to various social media links all directing to the relevent sites such as facebook and youtube in order to help the company to expand and gain new customers over time. 

My website has various ways to help the user find what they are looking for within the page if they already have an idea of what service they require. The user has the option to either user the clearly marked search bar at the top of the page to search for keywords in either the package name or descriptions and/or they can utilise the sort feature which allows the user to search the packages in order of either: Alphabetical order, Price or User ratings.


## UX

When designing my website I had decided that my target audience would be males between 20 and 50 years old. Whith this in mind i created a design that would grasp the attenion of the user and draw then in to have a browse of what the site has to offer. I used colors that you would typically see in a motor vehical themed website focusing on what colors you could assosiate with car cleaning such as black for tyres and polished black bodywork. 

When a user clicks on my site their goal would be to quickly but carefully search for car cleaning packages to purchase for whatever occation they may need it for in a safe environment. I believe my website has some of the perfect solutions for this by providing a low clutter home page clearly outlining the benefits of chosing this valeting service and displaying very short but detailed bulletpoints on what each package has to offer and a clearly marked price and they can pay online using a secure payment system.

## User Stories

As a shopper, I want to be able to search for packages by price in both ascending and descending order so that I can see what packages I have enough money for.

As a shopper, I want to be able to search for packages in alphabetical order in both ascending and descending order so that I can get a clearer view of the packages list.

As a shopper, I want to be able to search for packages based off of user reviews in both ascending and descending order so that I can see what other shoppers have viewed as being the best value for money.

As a shopper, I want to be able to search for a keyword related to what sort of package I want so that I can quickly find what packages are on offer for my specific needs.

As a shopper, I want to be able to add valeting packages to a basket where the price is totaled up so that I can clearly see how much money I am about to spend and what I have chosen.

As a shopper, I want to be sent email conformation when I purchase a package so I can keep records of what I have paid for.

As a user, I want to be able to create a profile where I can recall previous orders and also save personal details for future use so that I can save time in the future a purchase the same package as before.

As a user, I want to be able to follow the social media pages so I can keep up to date with new packages and package offers.

As a user, I want the website to be fully responsive so that I can view the website on both mobile and tablet formats as well as desktop.

As an admin, I want the ability to be able to manage existing packages and add them to the packages page so that I can correct any mistakes and change package descriptions.

As an admin, I want the ability to be able to create new packages to the website, so that I can draw in different types of customers with different needs.


## Features

### Existing features

* A sorting system which allows shoppers to sort the existing packages by price, rating and name in both ascending and descending aiding in readability and user accessibility.

* A search bar allows users to search for keywords making it easier for experienced shopper to quickly find what they are looking for.

* A basket sysetm the allows users to store packages in one area until they are ready to pay.

* A secure payment system allowing users to make payments for their chosen packages.

* An email system which automatically ends out confirmtion emails upon ordering a package.

* An account area when users can make and use an account where they can track pervious orders and save banking information for future use if neccessary.

* An admin section where a super user can make changes to the websites package lists by completing a form made in the django administration page.

### Future feature implementations

* The first feature i would like to add is a chat section where any user can join with an account and start chatting and interacting with other people on the page. This would prove useful to first of all increase customer interaction and to also help users who are stuck or unsure about a certain section of the website.

* The second feature i would like to add is the ability to allow a user to make specific reviews and comments about a chosen package which can then be viewed by others and sorted in the same way as the packages on the page. This could also make in impact on the customer rating section located within teach package card.

* The third feature i would like to add is giving the user the ability to upload a befor and after image to some sort of gallery page which can also be interacted with by all other users such as commenting and likes.


## Technologies Used

* [Bootstrap]
  * I used the bootstrap library to utilise their styling componnt such buttons and the grid system to lay my page out responsively.
  
* [MySQL]
  * I used MySQL as the websites main database for storing my package information.

* [Python] 
  * I used the python language to construct all of the apps used in my project.
  
* [Django]
  * I used Django as a base to create all of my individual apps allowing me to utilise them in the future as chunks rather than one massive app.
 
* [JavaScript] 
  * I used JavaScript to create a document ready function for the page buttons.

* [CSS]
  * I used CSS to style my website with things such as color and font-size.

* [HTML]
  * I used HTML as my base coding language throughout the page.

* [Googlefonts]
  * I used google fonts throughout the project to improve the look of my site https://fonts.google.com/.

* [Stripe]
  * I used Stripe to create a secure checkout system allowing the user to make secure purchases on my website https://stripe.com/docs/payments/checkout

* [Json]
  * I used Json to trasmit package data to and from the server allowing it to be stored and used on my website.
 

## Testing

Throughout the development process I was testing how my website was being effected by any alterations I made in my code such as positioning and sizes. I did this by running the website in a separate browser tab using 'python3 manage.py runserver and using the inspect function. Through this function I was consistently playing around with different sizes, colors and layouts as I could make any changes I wanted without effecting the actually code. This enabled me to pick up on silly mistakes I made like some elements not being responsive on the smallest resolutions. I was also able to pre plan what colors and sizes I wanted to implement without wasting any time on a gamble whether it would work or not. Using the inspect function also reduced the chance for errors because I was already able to see the end result before I added it to the real code. Also when i was testing the website myself I was constantly checking to make sure that all of my app.py functions were function correctly such as edit add and delete buttons.

The first test I conducted was making sure that allauth was functioning correctly allowing proper authentication systems. I tested this by running 'python3 manage.py runserver' in the terminal window and in the url bar adding 'account/login at the end redirecting me to the server login page. Here I signed in using my superuser credentials and I was correctly redirected to an email verification page.   
  
I also used a code validator website (https://validator.w3.org/) for both my CSS and HTML files throughout the development process. By using this website I was able to keep track of the code I was writing and any mistakes would be flagged up there and then which made rectifying them much easier as oppose to waiting until the end of my project then fixes every error I had made.

Another method of testing I used was sending my website out to other people. I sent the server port link out to a few of my family and friends and ask them to have a play around with the site including but not limited to the navigation features or forms I had. After they had a go with the site I then asked them to give me some feedback on what was good, what's was bad and what could be improved.

When testing my page button links it was as simple as clicking on the buttons and checkign to see if they went to the desired location or not and then checking for any errors in the inspect errors tab.

To test that my Stripe email confirmation system was working correctly all i had to do was place a test order on the website then check back on Gitpod and look at the terminal where it printed out the email template that i had pre-written and this worked successfully.

My website also adapts to different screen sizes and resolutions in a way that as the screen gets smaller the layout will change by shifting around the elements to hold a similar style while also being professional and functional. I have developed my website to be responsive as a whole in which I mean that as you switch resolutions to medium or small resolutions the whole page will stay very similar until you cross certain resolution checkpoints. For example, I have each of my recipe card data entries presented as a col 6 following the grid layout system featured on materialize. From what I have experience with other websites over the years and through the feedback I have been given this layout would work well with modern day internet styles. It makes each item easy to view and makes them all stand out due to them covering the entire width of the screen.

I have created a test account for you to user if you did want to access the /admin panel. The username is Test and the password is Milestone1.

## Testing a couple of user stories

* To find test if the social media buttons work, click on the icons located at the bottom of the page and see if they direct you to the relevent site.

* To test if the basket is working correctly try and add random packages to the basket and see if the correct packages are displayed on the basket page along with the correct prices.

* To test the sorting features navigate to the all packages text and click on each of the various dropdown sections and check to see if the packages have displayed in that desired order.

## Bugs and problems I ran into

* The first probelm I ran into was when I was preparing to loading my data to MySQL running the python3 manage.py loaddata command. I was repeadidly getting a DeserializationError in the terminal. After double checking my Json formatting I seeked help from the tutor team and we decided that it could have been that my SQL database was out of sync to the rest of the project. I then proceeded to delete all of my migrations.py files in the whole project and remigrate all of my SQL data using python3 manage.py makemigrations then python3 manage.py migrate to set it all up. After all of this I till could not run the loaddata command. We then looked at my project models.py nd found that I failed to include one of my Json fields. AFter fixing this everyhting worked correctly and I could move on to the next part of the projects developmetn.


## Deployment

* Deploying to github

  * My first step when deploying to github was creating my app.py file and getting the basic functionality in place so I could insure that my page connections were working smoothly. 
  
  * Then, in the terminal window I typed 'git add .' to add all of my intial files to the stagin area.
  
  * Then, also in the terminal window I typed 'git commit -m "Initial commit"' outlining what I had done between commits. 
  
  * Finally, I typed 'git push' which pushed my commits to github where it was stored ready for future commits.
  
* Deploying to heroku

  * My first step in deploying my website to Heroku was creating an account to host my project on the Heroku website.
  
  * Then, I needed to navigate to the 'new' button which then gave me the option to create a new app. When choosing the name for my app I attempted to make the name as close to the project theme as possible so I chose to name it 'Recipe-storages'
  
  * After creating a new app i was ready to deploy my initial commits to Heroku. I did this by navigating to the deploy page and clicking on the Github account linking button. I chose to use this method as oppose to using the Herkou CLI and pushing to the master branch every time. It just made everything simpler and more organised.
  
  * Once my Github and Heroku accounts were linked i needed to input the correct PORT and IP figures i used in my app.py file which were PORT:0,0,0,0 and IP:5000. To do this I went on the settings page on Heroku and revealed the config vars for my app. This is where i input my figures for the port and ip as well as my Mongodb URI and Name which was used to make sure my database would connect to the Heroku app. 

## Credits

Some unadaptable aspects of this project have come directly from the Boutique Ado example project such as settings.py in the project level folder names 'Harvalet'. I used this from the example because i wanted all of my settings to function correctly however I did change the names of the apps to fit my ideas. 
I have followed the course material through all of the parts I found particuarly trick to do myself such as the stripe payment and profiles sections purely for learning purposes as I am still very new to coding as a whole and in no way am I claiming to have written all of it by myself. 

All of the directories and files were adapted from the example mentioned above and I absolutely did not have any intention to copy the design and style of the example it was just the more backend parts I struggled with. I needed the extra support and validation from the videos for some aspects of the django framework due to not being 100% comfortable with the coding language.

Inspiration form this project came from my dad who has always wanted to have a professional car valeting service.

I must also metion that without the help of some of the tutors especially Tim my website would not be fucntion as it is now.

The information for the car packages used in my website were taken directly from [https://www.valetsonyourdrive.com/car-valeting/packages-pricing/] to get legitimate package descriptions and prices.


