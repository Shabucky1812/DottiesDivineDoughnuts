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
![First removing item screen](/assets/images/ddd-remove-item1.png)  

If the user instead wants to remove a menu item, after once again selecting which category their target item is in, they will be shown this similar screen. The program once again display the current options and their prices and requests an input from the user. Importantly, the user now has to type the full item name instead of using a quicker integer selection. This is valuable because it ensures the user is certain which item the are attempting to remove from the menu.  

![Second removing item screen](/assets/images/ddd-remove-item2.png)  

After inputting their desired item, the user is once again requested to confirm their decision.  

![Final removing item screen](/assets/images/ddd-remove-item3.png)  

Once the item to be deleted has been confirmed with the user, the application tells the user the item is being deleted and finally confirms the change upon completion. The user has then finished using this service and can return to the main menu or exit the program. Below is the newly updated prices worksheet.  

![Updated menu after deleted item](/assets/images/ddd-orders-update2.png)  

#### Editing an item:
![First item edit screen](/assets/images/ddd-edit-item1.png)  

The final service available to edit the menu is to edit an item's price. After selecting this option and again entering which category the target item is in, this screen will be presented to the user. It function exactly like the screen shown when selecting an item to remove.  

![Second item edit screen](/assets/images/ddd-edit-item2.png)  

The user's selection is confirmed.

![Third item edit screen](/assets/images/ddd-edit-item3.png)  

Next, the user is reminded of the item's current price and prompted to input the new price. This input is taken in pence like the price input used in the adding an item process.  

![Fourth item edit screen](/assets/images/ddd-edit-item4.png)  

A final confirmation displaying the item and new price is provided before the changes are made.  

![Final item edit screen](/assets/images/ddd-edit-item5.png)  

Finally, the changes are confirmed in the same style as the previous changes and the user is presented the service finished options once more. The freshly altered menu can be seen below.  

![Updated prices worksheet with freshly changed item price](/assets/images/ddd-prices-update2.png)  

### Viewing Analytics:
![First analytics screen](/assets/images/ddd-view-analytics1.png)  

The last available main menu option is the 'view analytics' service. Upon selecting this service, the program repeats to the user which service has been selected and than presents a small series of helpful analytics regarding recent sales. The first wave of analytics contains text that displays the most popular menu option for each category (size, filling, topping). This is valuable to the user as it can help Dottie know what stock to prepare more of and what stock might need a price change. For ease of use, the program waits for the user to press enter before displaying the next statement, this is helpful as it allows them to digest the information at their own pace.  

![Second analytics screen](/assets/images/ddd-view-analytics2.png)  

The next analytics shown is the number of doughnuts made and sold in the last 5 orders. This is valuable to the user because it gives Dottie a better idea of how much stock she has used and how many doughnuts she will have to prepare in the future.  

![Final analytics screen](/assets/images/ddd-view-analytics3.png)  

Lastly, the user is shown the total income of this business since it's creation. This is a less helpful statistic but it still provides value to Dottie by reminding her how far she has come! The program once again then displays the service finished screen.  

### Future Implementations:  
For the scope of this project, I am very happy with how the criteria listed in the user stories has been met. However, this application can be further developed in a number of ways:  

1. Firstly, a login system could be introduced. Currently, the user has access to every service immediately without any verification of who the user is. Since this application directly interacts with Dottie's menu and order history, it would be ideal if only Dottie and any future employee of the business had access to it. You may have noticed that the flowchart created for this project during planning actually contains a login system, this is because this feature was in my original scope for the project. However, I ultimately decided to leave it for a future version as the existing project content became a lot larger than I anticipated and it functions fine for now without one. The login system would take a username and a password and allow access to the application if the credentials were valid and deny entry otherwise. An additional service that allows a logged-in user to edit/add/remove valid accounts could also be paired with this feature.  

2. Another expansion I would like to see in this project's future would be an updated 'view analytics' service. The current service functions perfectly for the small scope of this business but as it grows, the small list of analytics shown now might become somewhat obselete. The limits of this expansion are far beyond my comprehension at the moment as data analysis is a large environment, saturated with possibility. One idea I would like to implement in this area would be a statistic that reveals the correlation between the menu options, something like: 'Most customers who purchase doughnuts with jam filling also request sugar topping'. This would be useful as it would reveal additional purchasing trends and could be used as a suggestion for creating special offers to entice more customers. 

## Technologies Used

- This application was created with the Python programming language.  
- This application was developed within [Gitpod](https://www.gitpod.io/).  
- The repository for this application was created using [GitHub](https://github.com/) and [Git](https://git-scm.com/) was used for version control.  
- The flowchart created during the planning of this application was created using [Lucidchart](https://www.lucidchart.com).
- The external spreadsheet accessed throughout this application was created using [Google Sheets](https://www.google.com/sheets/about/).
- The credentials used in this project to securely access the external sheet was generated using [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk).
- This application interacts with the external sheet using [Google Sheets API](https://developers.google.com/sheets/api)
- The follwing python libraries were used:
    - [gspread](https://docs.gspread.org/en/latest/): to read from/write to the external sheet.
    - [Google Auth](https://google-auth.readthedocs.io/en/master/): required to use credentials.
    - [statistics](https://docs.python.org/3/library/statistics.html): used to find modes of menu items.
    - [sys](https://docs.python.org/3/library/sys.html): used to exit the application when required.
- This application was deployed using [Heroku](https://id.heroku.com/login).

## Deployment
To clone this repository paste `git clone https://github.com/Shabucky1812/DottiesDivineDoughnuts.git` into the terminal of the editor you are using. Then follow the steps below to get everything up and running.  

Firstly, you must create a google sheet for your cloned application to interact with:  
- From this link: [Google Sheets](https://docs.google.com/spreadsheets/u/0/), create/sign-in to a personal (not-shared/business) google account.
- Press **Blank** to create a new spreadsheet.
- At the top-left of the screen, replace the _'Untitled Spreadsheet'_ placeholder text with the title: _'dotties_divine_doughnuts'_.
- At the bottom of the screen, rename the current worksheet _'Sheet1'_ to _'Prices'_.
- Create a new worksheet using the plus symbol to the left of the existing worksheet and rename the new sheet to _'Orders'_.
- Return to the _'Prices'_ worksheet and add the following values to the first row, from left to right: 
    - 'size'
    - 'Price(£)'
    - 'filling'
    - 'Price(£)'
    - 'topping'
    - 'Price(£)'  

- Your _'Prices'_ worksheet should now look like this:  
![Example Prices worksheet](/assets/images/ddd-example-prices-worksheet1.png)  

- I would recommend adding some sample menu data manually. Your menu options can be unique but the format must look like the example image below and importantly, all of the values you add must contain only alphabetical characters and no spaces!  
![Populated example prices worksheet](/assets/images/ddd-example-prices-worksheet2.png)  

- Next, select the _'Orders'_ worksheet and add the following values to the first row, from left to right:
    - 'Size'
    - 'Filling'
    - 'Topping'
    - 'Quantity'
    - 'Total Price(£)'  

- Your _'Orders'_ worksheet should now look like this:  
![Example orders worksheet](/assets/images/ddd-example-orders-worksheet.png)  

Next, you need to set up a couple API's to allow interaction between your code and your new spreadsheet:  
- Use this link to access the [Google Cloud Platform](https://console.cloud.google.com).
- From the project menu at the top of the screen, select **NEW PROJECT**.
- Enter a unique project name and the press **CREATE**.
- Select **Dashboard**.
- Open the navigation menu at the top-left of the screen then select **APIs and services** and then **Library**.
- Type _'Google Drive API'_ into the search bar, press enter, and then select **Google Drive API**.
- Click **ENABLE** and wait to be taken to a new screen.
- Select **CREATE CREDENTIALS** from the top-right of the screen.
- From the **Select an API** dropdown menu, select _'Google Drive API'_.
- Select the **Application data** radio button and then the **No, I'm not using them** radio button.
- Click **Next**.
- In the **Service account name** input, enter a service account name. This can be any value, I suggest _'dotties-divine-doughnuts'_.
- Select **CREATE AND CONTINUE**.
- From the **Select a role** dropdown, select **Basic** and then **Editor**.
- Select **CONTINUE** and then **DONE**
- Select the **CREDENTIALS** tab from the options in the middle of the screen.
- Under the __Service Accounts__ sub-heading, click on your newly created service account.
- Select the **KEYS** tab and from the **ADD KEY** dropdown, click **Create new key**.
- Select **JSON** and then click **CREATE**. A file containing API credentials will now be automatically downloaded to your device.
- Locate this file and copy it directly into your local clone of this application.
- Rename the file in the clone to: _'creds.json'_. This file contains sensitive data so make sure it is listed in the .gitignore file to prevent pushing it.
- From within the _'creds.json'_, copy the value for _'client_email'_.
- Return to your google sheet for this application and click **Share** at the top-right of the screen.
- Paste the copied value into the input provided, ensure _'Editor'_ is selected from the dropdown menu to the right, untick _'Notify people'_, and finally, click **Share**.
- Return to your project dashboard on the Google Cloud Platform and once again select **APIs and services** and then **Library** from the top-left navigation menu.
- Type _'Google Sheets API'_ into the search bar, press enter, and then select **Google Sheets API**.
- Finally, click **ENABLE**.

Lastly, deploy the application using [Heroku](https://id.heroku.com/login):
- Before the application can be deployed, you must make some changes to your local clone.
- Paste `pip3 install gspread google-auth` into the terminal to install the gspread and google-auth libraries into your development environment.
- Paste `pip3 freeze > requirements.txt` into the terminal so Heroku knows what dependencies the application uses.
- Commit and push these changes before deployment.
- Use this link to log-in/sign-up to [Heroku](https://id.heroku.com/login).
- From the Heroku dashboard, select the **New** dropdown from the top-right, and then click **Create new app**.
- Enter a name into the **App name** input, select your region from the **Region** dropdown, and then click **Create app**.
- From the tabs near the top of the screen, select **Settings** and scroll down to the **Config Vars** sub-heading.
- Enter _'CREDS'_ into the _'KEY'_ input and paste all the contents of your previously created _'creds.json'_ file into the _'VALUE'_ input.
- Click **Add**.
- Create another config var with the key: _'PORT'_, and the value: _'8000'_, then click **Add**.
- Scroll down to the **Buildpacks** sub-heading.
- Select **Add buildpack**, then select **python**, and finally select **Save changes**.
- Again select **Add buildpack**, then **nodejs**, and **Save changes** once more.
- Ensure the python buildpack comes first in the buildpack list. You can re-order the buildpacks if necessary.
- Now, scroll back up and select the **Deploy** tab.
- Under the **Deployment method** sub-heading, select **GitHub**.
- Search for the GitHub repo for your application and then click **Connect**.
- You can now deploy your application in two ways:
- Select **Enable Automatic Deploys** to automatically deploy your program. This means that whenever a change is pushed, Heroku will automatically update your live app.
- This project was manually deployed by selecting **Deploy Branch** under the **Manual Deploy** sub-heading. A manually deployed site will only update with new pushes when re-deployed next.
- Once Heroku has deployed your application, it will present you with a link to the live site.

## Testing  
Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits
### Contents  
- All of the code for this website was written by me, [Shaun Buck](https://github.com/Shabucky1812).
- Inspiration for manipulating single cell values using gspread was taken from [here](https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value).
- Additional information about dictionary usage was taken from [here](https://www.geeksforgeeks.org/python-dictionary-comprehension/).

### Acknowledgements  
I'll keep this one short:
- Huge thanks to Brain Macharia as always, thanks for all your support!
- Thanks to my gorgeous cat Phoenix, who is sat on my lap right now.
- Thank you for reading!
