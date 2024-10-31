<<<<<<< HEAD
1.Install Anaconda3     install Anaconda3，generally it has been installed 

2. Create virtual enviroment. Establish the virtual environment lms for this project in conda

method:
	Window: Start menu->Anocanda3->Anaconda Prompt
	Anaconda Prompt input:	conda create --name lms python=3.12  （Do not exit this console for next ）  Do not close the terminal window, continue to use it

3.Switch to the environment：	Switch to the virtual environment lms
method：	
Anaconda Prompt input:	 conda activate lms

4.Install Django
method:
Anaconda Prompt input:	pip install django

5. download our github project  (Do not operate in the terminal window and create a local project)

6.  Goto the project folder.	Go to the project directory (again in the original terminal window, easy to locate requirements.txt)
method:  in Anaconda Prompt console
cd your_project_folder    ex:	cd \lms2024fall 
you will find requirements.txt
Anaconda Prompt input:	pip install -r requirments.txt

7. initial database  (Initialize the database)
Anaconda Prompt input:	python manage.py migrate

8.run server
Anaconda Prompt input:	python manage.py runserver

9.Open browser,url：  127.0.0.1：8000


10 pycharm virtual environment for this project:   （firstly select lms from the drop-down list,if there don't have it then add Interpreter->conda->existting environment）
open project folder.
file->setting->project (lms2024fall): Python interpreter->select lms  (not add interpreter,if cannot found lms,maybe add interpreter )

	
	


=======
1.Install Anaconda3     install Anaconda3，generally it has been installed 

2. Create virtual enviroment. Establish the virtual environment lms for this project in conda

method:
	Window: Start menu->Anocanda3->Anaconda Prompt
	Anaconda Prompt input:	conda create --name lms python=3.12  （Do not exit this console for next ）  Do not close the terminal window, continue to use it

3.Switch to the environment：	Switch to the virtual environment lms
method：	
Anaconda Prompt input:	 conda activate lms

4.Install Django
method:
Anaconda Prompt input:	pip install django

5. download our github project  (Do not operate in the terminal window and create a local project)

6.  Goto the project folder.	Go to the project directory (again in the original terminal window, easy to locate requirements.txt)
method:  in Anaconda Prompt console
cd your_project_folder    ex:	cd \lms2024fall 
you will find requirements.txt
Anaconda Prompt input:	pip install -r requirements.txt

7. initial database  (Initialize the database)
Anaconda Prompt input:	python manage.py migrate

8.run server
Anaconda Prompt input:	python manage.py runserver

9.Open browser,url：  127.0.0.1：8000


10 pycharm virtual environment for this project:   （firstly select lms from the drop-down list,if there don't have it then add Interpreter->conda->existting environment）
open project folder.
file->setting->project (lms2024fall): Python interpreter->select lms  (not add interpreter,if cannot found lms,maybe add interpreter )

	
	


>>>>>>> f6c04517317835c2f1953245134555604477976b
