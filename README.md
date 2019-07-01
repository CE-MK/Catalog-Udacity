# Item Catalog Project Number 4: Fullstack Developer Nanodegree
Create a restaurant menu app where users can add, edit, and delete restaurants and menu items in the restaurants.
## How to run the project
### Prerequisites
* Python 2.7 or later
* Vagrant
* VirtualBox

### Get started
1. Install VirtualBox
2. Download or clone repository [https://github.com/udacity/fullstack-nanodegree-vm]
3. Copy all of my files
4. Place all files in your vagrant/cataloge directory
5. Launch Vagrant
```
$ vagrant up
```
6. Login to Vagrant
```
$ vagrant ssh
```
7. Change directory to `/vagrant`
```
$ cd /vagrant
```
8. Initialize the database
```
$ python database_setup.py
```
9. Populate the database with some initial data
```
$ python menus.py
```
10. Launch application
```
$ python project.py
```
11. Open your browser and go to http://localhost:5000

### JSON endpoints
#### Returns JSON of all restaurants

```
/restaurants/JSON
```
#### Returns JSON of a specific menu item

```
/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON
```
#### Returns JSON of the menu

```
/restaurants/<int:restaurant_id>/menu/JSON
```
### Credits
Photo bought on Shutterstock Photo ID 1066763171 Photographer: Wasant [https://www.shutterstock.com/g/Wasant?sort=popular]
