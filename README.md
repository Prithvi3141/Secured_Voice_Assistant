# Secured_Voice_Assistant
Secure Voice Assistant is a secure voice assisted movie tickets booking application. 
  
  
This application makes use of 2 Raspberry Pis and hosts a dynamic web application: 
  
1)Access Pi - This pi is used to obtain access to the application by making use of MCS Face API  
2)Control Pi - The user gains control of this pi once the user gains access through the access pi and then he can makes use of the Voice UI developed using Google Voice API to navigate through the website and book tickets for his favorite movies.  
3)Book My Show Web Application has been hosted on a LAMP server in an Amazon EC2 Instance.
  
  
Our project makes use of 3 protocols.
  
1)MQTT-This protocol is used by the Control Pi to communicate with AWS IoT and the messages of the topic 'projectTopic' is forwarded by  
the rules engine to AWS Lambda which does some event handling such as sending a notification if user has logged in or booked tickets     
for a show.  
2)MQTT over Websockets - This protocol is used by the Access Pi to publish messages to the topic 'accessTopic' and control Pi which   
subscribed to the thsi topic receives messages to login or logout of this application.  
3)HTTP - This protocol is used for Face API provided by Microsoft Cognitive Services. To make use of the cloud based service provided    
by Face API requests are sent using HTTP protocol. Python Requests module has been used to send http requests. 
  
  
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
 

