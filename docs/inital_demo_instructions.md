# Initial Demo Instructions

The instructions below will guide you to setting up the initial demo of our project. Each entity will run in a separate terminal window. Later, this will be an automated system and possibly run virtually, but for now, this demonstrates how the parts will connect with one another.

## Part 1
The first step is cloning the four repos (that are actually our forks). It's important to note that each of these clones will end up having the same name `capstone2021`, so I suggest making four directories: **Riley**, **John**, **Juan**, **Kylie**. In each of those, clone the appropriate repositories. 

1. Clone [Riley's repo](https://github.com/rileyalankirk/capstone2021),
2. Clone [John's repo](https://github.com/lapatchak97/capstone2021),
3. Clone [Juan's repo](https://github.com/Juan-gbp/capstone2021),
4. Clone [Kylie's repo](https://github.com/kylienorwood/capstone2021),

all in their respective directories. 

## Part 2
### Redis Database
I recommend closing all the terminal windows you have open now, and starting from scratch. Open a new terminal window and start a redis server by executing`redis-server`. 

**NOTE**: In *each* repository you will need to run the setup steps: create a virtual environment, activate the virtual environment, and run `pip install -e .`. **Make sure you do these three tasks in the repositories** (see below for when exactly to compelte these tasks). 

### Work Server
1. Open a second terminal window and navigate to the **Riley** directory. Execute`cd capstone2021`, complete the *Note* steps, and then enter the appropriate branch: `git checkout work_server`. 
2. Navigate to the location of the appropriate file: `cd src/c21server/work_server`. 
3. Run the file: `python3 work_server.py`. 
4. If you get any `ModuleNotFound` errors, `pip install` whatever module is missing (this is probably just a result of not having the updated setup.cfg file, which *should not* cause problems when everything is merged).

### Work Generator
1. Open a third terminal window and navigate to the **John** directory. Execute `cd capstone2021`, complete the *Note* steps, and then enter the appropriate branch: `git checkout work_gen`. 
2. Navigate to the location of the appropriate file: `cd src/c21server/work_gen`. 
3. Run the file: `python3 basic_work_gen.py`. 
4. Follow the same process as above if any modules are not imported. 

### Client
1. Open a fourth terminal window and navigate to the **Juan** directory. Execute `cd capstone2021`, complete the *Note* steps, and then enter the appropriate branch: `git checkout client`. 
2. Navigate to the location of the appropriate file: `cd src/c21client`.
3. Run the file: `python3 client.py`. 
4. Follow the same process as above if any modules are not imported. 

### Dashboard
1. Open a fifth (and final) terminal window and navigate to the **Kylie** directory.  Execute `cd capstone2021`, complete the *Note* steps, and then enter the appropriate branch: `git checkout dashboard_documentation` (not the most accurate name here anymore).
2. Navigate to the location of the appropriate file: `cd src/c21server/dashboard`.
3. Run the file: `python3 dashboard_server.py`. 
4. You should see: `* Running on http://[IP_ADDRESS]:5000/ (Press CTRL+C to quit)`.
5. Paste `[IP_ADDRESS]:5000` in your browser. 
6. We have two endpoints - `data` and `dashboard`. You will most likely have an error when just pasting the original address in your browser. Decide which endpoint you'd like to view and paste either `[IP_ADDRESS]:5000/data` or `[IP_ADDRESS]:5000/dashboard`. 

Periodically refresh and see the updates on the dashboard! 

## Part 3
To shutdown, simply *control C* in each terminal window. 

