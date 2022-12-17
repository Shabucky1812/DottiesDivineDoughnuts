# Dottie's Divine Doughnuts Testing
## Automated Testing  
All of the python wrote for this application passes through [this PEP8 Linter](https://pep8ci.herokuapp.com/) with no errors.

## Manual Testing 
### Functionality:
| Test Label | Test Action | Expected Outcome | Test Outcome |
|------------|-------------|------------------|--------------|
| Welcome Message displays correctly. | Reload live application. | Application should always display relevant welcome information upon initial load. | PASS |
| Multiple choice inputs should only accept valid inputs. | Try a range of valid and invalid inputs at various multiple choice inputs. | Program should only accept an integer that corresponds to options as well as 'exit' and 'main'. | PASS |
| Valid inputs should select correct option. | Enter valid inputs at various mulitple choice inputs. | Application should use selected information correctly (If input is '1', the application should use/run the option listed as '1'). | PASS |
| Logging order service should function correctly. | Attempt to use the 'logging a customer order' service. | Program should request a series of order details and then calculate the order price, and update the Google Sheet correctly. | PASS |
| Adding an item service should function correctly. | Attempt to use the 'Add an item to the menu' service. | Program should request new item name and price, receive final confirmation, and finally append to relevant column on the 'Prices' worksheet. | PASS |
| Deleting an item service should function correctly. | Attempt to use the 'Remove an item from the menu' service. | Program should request item category and name, confirm change, and finally delete the item from the 'Prices' worksheet. | PASS |
| Edit item price service should function correctly. | Attempt to use the 'Edit the price of an existing item' service. | Program should request item category, name, and new price, then confirm change before making relevant amendment on the 'Prices' worksheet. | PASS |
| View analytics service should function correctly. | Attempt to use the 'View analytics' service. | Program should display a series of analytics about recent order history. | PASS |
| Program should correctly handle what happens when a service is finished. | Finish using a service and see what happens. | Application should communicate that the service is finished to the user before presenting options to return to the main menu or exit the application. | PASS |
| Special 'exit' and 'main' inputs should function througout the application. | Test the special inputs at various input stages in the program. | Program should always return the user to the main menu if 'main' is entered, and exit the application if 'exit' is entered. | FAIL - Inputs used to display waves of analytics in the 'view analytics' process didn't react to these values. This bug is now solved. |

### Browser Compatibility:

## Bugs
### Solved Bugs:

### Known Bugs:

Return to [README](README.md)