# CalApp

## Once your command line is open, enter these commands:
python --version <br/>
pip --version

## Next, you’ll need to install Flask. At the command line, type
pip install flask

# Run the project
### Clone the repo git clone https://github.com/ilma-sheriff/CalApp.git
* cd CalApp/api
* python api.py

* Show the last 10 calculations descending from most recent to oldest: http://0.0.0.0:5000/currentevents
* Perform calculations, for example: 
  * For addition, http://0.0.0.0:5000/compute?user_name=%27userA%27&operation=10%2b10  
  * For multiplication, http://0.0.0.0:5000/compute?user_name=%27userB%27&operation=10*10 
