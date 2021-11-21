# quizify-zothacks

Created for [ZotHacks 2021](https://devpost.com/software/quizify-6detoa), hosted by Hack @ UCI.

## How we got here.
We're almost through the year, which means we're almost going to receive Spotify's yearly gift, our Spotify Wrapped! Although this year's playlist isn't available just yet, **data is forever**! 

## What does this app do?
On the front end, you connect with Spotify and select the correct song that corresponds with the random lyric. Quizifiy communicates with the Spotify API that returns a user's top fifty songs within the past six months. The data is then stripped down to song and artist, and is passed to a Python library that communicates with the MusixMatch API. From there, information is randomly iterated and presented prettily. 

## Production
Please use the test account to run the app, attached as a text file (to the organizers only), as we were unable to request an app quota extension.

## Contributions
We got started with HACK @ UCI's Flask and JS, HTML and CSS workshop. Then, we split into front-end and backend groups. John Lorenzini and Lawrence coded on the front lines, implementing the smooth gradient landing page. On the backend, John Daniel and Anthony implemented the APIs.

## This wasn't easy, let us tell you.
John Daniel and Anthony struggled communicating with the Spotify API, with data being transferred back and forward. John and Lawrence struggled with small elements of design, and was setback with a small error regarding synced versions. Our mentor gave us all the help he could :)

## Accomplishments that we're proud of!
The ability to communicate with multiple APIs, program collaboration with GitHub and Replit, deployment with Heroku... and overall, getting work done!

## What we learned...
We learned that we're able to accomplish a lot together in a short amount of time. Using our basic programming experience allowed us to adapt and learn different languages and to understand different libraries. Reading documentation is a must!

## What's next?
Implementing a global scoreboard in a database like Firebase, better implementation of secret keys (don't steal our public and private keys, grr), and possible options for smaller and larger text sizes.
