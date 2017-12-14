# Secured_Voice_Assistant
Secure Voice Assistant is a secure voice assisted movie show booking application. 
This application makes use of 2 Raspberry Pis: 
1)Access Pi
2)Control Pi

Access to this application is obtained through facial recognition by making use of the cloud based service, Microsoft Cognitive Services
Face API. 
a)User gains access to this application by authenticating himself at the Access Pi through facial recognition by using of Face API.
b)Once the user authenticate himself, the Access Pi publishes a message ,containing the username, making use of MQTT over Websockets to AWS 
IoT, where in turn the message goes to Control Pi which has subscribed to the topic to which the Access Pi publishes.
c)Once the control pi receives the message containing the username, it login into the Movie booking Website.
d)Now that the user has logged in to the Voice Assisted Movie Booking Application, he can start using the control pi and it's voice ui to help him navigate through the application
e) The user now gives voice commands to the Control Pi to navigate through the movie show booking application and to ultimately book movie shows for his favorite movies.
The Voice UI keeps listening for the hotword "Google". It treats the rest of the phrase following the hotword as a command
Voice Commands Supported-  
1)Go Home - This command takes the user to to the homepage of this application.
2)Show Me Cities - This command retrieves the cities in which theatres are located.
3)Show Me favorite Theaters - This command give a list of your own customized Favorite Theaters list.
4)Show Me Booked Movie Shows - This command is used to list out your upcoming shows i.e. the shows you have booked tickets for.
5)Locate [Theater Name] - This command gives you the location of the theater on Google Maps.
6)Review of [Movie Name] - This command gives you the review for the given movie on Rotten Tomatoes.
7)Movies in [Theatre Name] - This command shows you the list of movies currently in the theatre [Theatre Name]
8)Book Tickets - This command is followed by a question which show. Then after responding with the show number it prompts the user for
number of tickets to be booked for the show.
9)Go To [Movie name] -  This command is used to view upcoming shows for the movie [Movie Name] in the selected theatre.
10)Theatres in [City Name] - This command lists out movie theatres in the city [City Name]
11)Add to Favorites - This command adds the selected theatre to your Favorites List.
12)Remove from Favorites - This command removes the selected theatre from your Favorites List.

Our project makes use of 3 protocols.
1)MQTT-This protocol is used by the Control Pi to communicate with AWS IoT and the messages of the topic 'projectTopic' is forwarded by the rules engine to AWS Lambda which does some event handling such as sending a notification if user has logged in or booked tickets for a show.
2)MQTT over Websockets - This protocol is used by the Access Pi to publish messages to the topic 'accessTopic' and control Pi which 
subscribed to the thsi topic receives messages to login or logout of this application.
3)HTTP - This protocol is used for Face API provided by Microsoft Cognitive Services. To make use of the cloud based service provided by Face API requests are sent using HTTP protocol. Python Requests module has been used to send http requests.

This secure voice assistant application provides voice assisted control of movie show booking website.
The dynamic website Book My Show has been hosted on a LAMP server in Amazon EC2
a)The dynamic website or web application has been built using PHP for server side scripting and MYQL for backend database querying. 
b)Pages are dynamically loaded by making use of PHP which queries the database and dynamically generates the content for the website.
The dynamic web application Book My Show employs a secure and resilient multi-tier architecture. 
This app is resilient to 
1)SQL Injection(SQLi).
2)Cross Site Scripting(XSS).
3)Session Hijacking.
4) Cross Site Request Forgery(CSRF).
5) Brute Force Password Attacks.
