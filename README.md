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
### Google Sheet:
![Prices worksheet of external spreadsheet](/assets/images/ddd-prices.png)  
Above is the 'Prices' worksheet of the external [Google Sheet](https://www.google.com/sheets/about/) the application interacts with.  

![Orders worksheet of external spreadsheet](/assets/images/ddd-orders.png)  
Above is the 'Orders' worksheet of the external [Google Sheet](https://www.google.com/sheets/about/) the application interacts with.  

### Welcome Message:  
![Welcome message of Dottie's Divine Doughnuts application.](/assets/images/ddd-welcome.png)  
After initially loading the application, the user is greeted with the above welcome message. The welcome message introduces the user to the application, communicates important information, and prompts the user to choose from a selection of services. This welcome is valuable to the user because it introduces the consistent and user-friendly style of the application, and lets the user know important information regarding exiting the application and returning to this very selection menu.

### Logging a customer order:
![First logging order screen](/assets/images/ddd-log1.png)  
This is the next message that will be presented to the user should they select option 1 - 'Log Current Customer Order' from the main menu. The program re-iterates the user's choice to them to confirm the service they are now using and then presents the first category options to select from. It is worth noting now that every user input is validated before being used further in the code. For the exact snippet of code above, If the user attempts to submit a non-integer value they will be presented with a quick message to remind them that their input should be an integer and if their input is an integer but does not correlate to one of the options to choose from then they will be shown a different message prompting them to choose from the selection above. After both of these cases, the user is allowed to try again. This style of validation is present for every user input required throughout the application but I won't continue to detail them like this to avoid repeating myself.  

![Second logging order screen](/assets/images/ddd-log2.png)  
After successfully making a size selection, the program will present a quick confirmation message followed by the next category options. This selection is identical in style to the previous selection to maintain consistent design for the user.  

![Third logging order screen](/assets/images/ddd-log3.png)  
Once more, after making a successful filling selection the user is presented with a small confirmation message and the last category options. I would also like to mention here that all three of the above selection messages fully adapt to the current state of the menu. For example, if the user was to add a new size to the menu after logging this order, then the next time an order is logged, the new size will be presented and selectable at the size selection screen.  

![Fourth logging order screen](/assets/images/ddd-log4.png)  
This time, after successfully selecting a topping, the user is presented with a slightly different screen. The program confirms the topping selected and requests a quantity between 1 and 8. If the user attempts to input a quantity outside of these boundaries, the input will be rejected and a new one within these confines will be requested once more.  

![Fifth logging order screen](/assets/images/ddd-log5.png)  
Finally, after selecting an acceptable quantity, the program presents the user with the complete order details. If the user is unhappy with these details for any reason (they may have made a mistake/customer changes mind last minute) then they have the option to retry which will take them back to the start of the order logging process. If they are happy with these details then they enter '1' and continue with the process.  

![Sixth logging order screen](/assets/images/ddd-log6.png)  
Once the user has confirmed their order details, they will be presented with the above screen. Firstly, the program tells the user it is calculating the total order price, before presenting the calculated price back to the user. It is important that the program communicates this process because it involves reading from the external spreadsheet and mathematical calculations which are both actions that can take time for python to achieve. This can create a small delay which would be frustrating for the user if they did not understand why it was occuring, the small message lets the user know that a small delay is expected and that nothing is wrong if one occurs. After printing the total price, the program then tells the user that is updating (and eventually has updated) the orders worksheet before finishing the service and asking what the user would like to do next. The user may either return to the main menu or exit the application. Below you can see that the order has been fully appended to the orders worksheet.  

![Updated orders worksheet](/assets/images/ddd-orders-update.png)  

The logging an order service is valuable to the user because it allows them to easily track a customer's order and have the price calculated and orders worksheet updated automatically. The UI throughout this service is consistent and simple to use which reduces user error and elicits a positive response upon use.  

### Editing the menu:
![Process selection for editing the menu](/assets/images/ddd-edit-menu.png)  

If the user instead selects option 2 - 'Edit menu' from the main menu then they will be presented with the above screen. The application now provides the user with additional options regarding the edit they would like to make. This is valuable to the user as it seperates their tasks into smaller, more manageable processes and provides clarification about the task they are currently working on.  

![Category selection screen](/assets/images/ddd-edit-menu2.png)  

Whatever selection the user makes, the user is first prompted to select which order option the item they would like to add to/remove from/edit an item from. This is important as it ensures the menu remains structured correctly after changes are made.  

#### Adding an item:
![First adding item screen](/assets/images/ddd-add-item1.png)  

In this example the user has chosen to add an item to the sizes category. The program responds by printing all of the current menu options for the relevant category, alongside the matching prices, and it then request the user's new item. This input is validated to ensure it consists of only alphabetical characters and, importantly, that the new item does not already exist. This is necessary because duplicate options would create a number of bugs when running the other application services.  

![Second adding item screen](/assets/images/ddd-add-item2.png)  

Once they have inputted a new item, the user will be prompted to input the item's price. The program receives this input in pence to remove the potential user error surrounding inputting a value with a '.' followed by 2 decimal places. This is intended to make validation of this value easier and to prevent having to translate specific formatting rules to the user. To fully ensure this input is simple for the user, the application provides an example input.  

![Third adding item screen](/assets/images/ddd-add-item3.png)  

Next, the program prints the new menu data to the user and requests confirmation that everything is correct. This is valuable because it prevents frustration should the user have made a mistake entering any information. If the user enters '2' then they are taken back to enter the new item data again.  

![Final adding item screen](/assets/images/ddd-add-item4.png)  

Once the user is happy with their new data and has confirmed this with the application, the program will update the menu and explain this to the user before presenting the same service finished text as before. Below you can see how the menu has been updated with our new size!  

![Updated menu with new addition](/assets/images/ddd-prices-update.png)

#### Removing an item:


## Technologies Used
- The flowchart created during the planning of this application was created using [Lucidchart](https://www.lucidchart.com).

## Deployment

## Testing  
Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits
### Contents  
- All of the code for this website was written by me, [Shaun Buck](https://github.com/Shabucky1812).

### Acknowledgements  
