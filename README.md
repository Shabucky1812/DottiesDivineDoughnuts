# Dottie's Divine Doughnuts
Dottie's Divine Doughnuts is a command line application designed to automate common tasks for the owner of a doughnut retailer, Dottie. The application should make logging customer orders more efficient, allow Dottie to edit the menu in various ways, and reveal recent purchasing trends. In order to accomplish these goals, the application should interact with an external google sheet that contains Dottie's current menu, and order history.

[Live App](https://dottiesdivinedoughnuts.herokuapp.com/)
## Contents
- [UX](#ux)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Deployment](#deployment)  
- [Testing](#testing)  
- [Credits](#credits)  

## UX
### User Stories:
As the business owner and sole employee (Dottie), I want to be able to:
1. Log a customer order and have the total order price calculated for me.
2. Store customer order history in an external spreadsheet.
3. Add options to the menu.
4. Remove options from the menu.
5. Edit existing option prices.
6. View some trends in recent purchases.

Additionally, any user of this application should find the UI accessibile and easy to navigate, and be able to exit the application or return to the main menu at any time.

### Flowchart:
![Features Flowchart for Dottie's Divine Doughnuts](/assets/images/ddd-flowchart.png)  
Above is the Flowchart for this application, created using [Lucidchart](https://www.lucidchart.com).

As this application features no front-end design, I decided to not create a visual wireframe. I instead created a flowchart which details the potential pathways a user of this application may follow and explains the steps the code will have to take for the application to function as intended.
## Features
### Welcome Message:  
![Welcome message of Dottie's Divine Doughnuts application.](/assets/images/ddd-welcome.png)  
After initially loading the application, the user is greeted with the above welcome message. The welcome message introduces the user to the application, communicates important information, and prompts the user to choose from a selection of services. This welcome is valuable to the user because it introduces the consistent and user-friendly style of the application, and lets the user know important information regarding exiting the application and returning to this very selection menu.

### Logging a customer order:
![First logging order screen](/assets/images/ddd-log1.png)  
This is the next message that will be presented to the user should they select option 1 - 'Log Current Customer Order' from the main menu. The program re-iterates the user's choice to them to confirm the service they are now using and then presents the first category options to select from. It is worth noting now that every user input is validated before being used further in the code. For the exact snippet of code above, If the user attempts to submit a non-integer value they will be presented with a quick message to remind them that their input should be an integer and if their input is an integer but does not correlate to one of the options to choose from then they will be shown a different message prompting them to choose from the selection above. After both of these cases, the user is allowed to try again. This style of validation is present for every user input required throughout the application but I won't continue to detail them like this to avoid repeating myself.

## Technologies Used
- The flowchart created during the planning of this application was created using [Lucidchart](https://www.lucidchart.com).

## Deployment

## Testing  
Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits
### Contents  
- All of the code for this website was written by me, [Shaun Buck](https://github.com/Shabucky1812).

### Acknowledgements  
