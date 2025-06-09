# F1_knowledge_base
A simple XML parser and GUI written in Python that shows data about Formula1 2022 season standings.
The GUI was actually created with Qt Designer and after that converted into .py file.
Also, there is F1_knowledge_base.pl that is a Prolog file, and it represents the start point of this project. 

![f1](https://user-images.githubusercontent.com/62925188/231102998-737809e9-d86c-473c-a967-40b85da45268.jpg)


![f1_2](https://user-images.githubusercontent.com/62925188/231103031-3eb82cd0-0438-4acc-a653-1d7cafed2745.jpg)


![f1_3](https://user-images.githubusercontent.com/62925188/231103051-8bbace37-21e5-4169-a294-3f618eef783f.jpg)

To install and run locally, run the following commands:
-create the environment
```conda env create -f environment.yaml```
-activate the environment
```conda activate pyqt_env```
-run the application (terminal/cmd)
```python guy.py```

To remove the virtual environment, run the following commands:
-deactivate the environment
```conda deactivate pyqt_env```
-remove the environment
```conda remove --name pyqt_env --all```