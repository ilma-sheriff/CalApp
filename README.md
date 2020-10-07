# CalApp

## Once your command line is open, enter these commands:
python --version
pip --version

## Next, you’ll need to install Flask. At the command line, type
pip install flask

### You can directly git clone https://github.com/ilma-sheriff/CalApp.git

# Run the project
* Home - Show the most recent event logs: http://0.0.0.0:5000/
* Show most recent 10 event logs: http://0.0.0.0:5000/currentevents
* Show all event logs: http://0.0.0.0:5000/allevents
* Perform calculation
  For example: http://0.0.0.0:5000/compute?user_name=%27userA%27&operation=10%2b10
  http://0.0.0.0:5000/compute?user_name=%27userB%27&operation=10*10
