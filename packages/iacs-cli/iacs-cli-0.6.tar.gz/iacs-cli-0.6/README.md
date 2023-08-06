
# hiacs-cli

#### Tool for organizing and creating Harvard IACS Course Materials

Based on conversations that I had with Pavlos and Rahul, I am proposing to create a command line tool for creation, organization, and management of Harvard IACS course content and website.  Leveraging **[Pelican](https://github.com/getpelican/pelican)**, a static site generator powered by Python, **hiacs-cli** will enable course instructor to quickly build course materials and translate the materials into website for students and the public.

Some of the challenges faced by IACS course instructor include:

1. Creating course materials often in Jupyter notebook, R markdown document, or Powerpoint slides.  Unfortunately, course instructors are expected to upload these materials on to a website that must be maintained separately from course content.  That means instructors must be versed in HTML, CSS, and sometimes Javascript as well as website deployment.  Ideally, course instructor should focus 100% of his or her effort in course content development and delegate website development to someone else.  

2. Every IACS course instructor organizes the course project in his or her project organizational structure.  This makes navigating course materials challenging for a new course instructor who takes over the curriculum.  Moreover, because of the lack of convention in how the course content is presented online, students also face difficulty of quickly finding materials on topic of their curiosity.  Ideally, IACS course website should follow a consistent *look-and-feel*, and searching for learning contents should be intuitive and easy.  

3. Course instructor should be able to quickly leverage existing content from the previous iteration of the course instead of starting the course project from scratch.  Moreover, if course materials are organized following the same convention, it will be easier for course instructors to pull materials from other courses and integrate them into another course.  For instance, if CS109 Data Science must borrow concepts from AM207 Monte Carlo Methods, CS109 instructor can copy the material - provided that CS109 course instructor has been proper credited - and present the material with small modifications and no concern for HTML and CSS.

To address these challenges, I am proposing to build **hiacs-cli** a command line tool in Python.  Here are some of its promised benefits for IACS course instructors:

* *No more HTML, CSS, or Javascript* - Course instructor should not be dedicating hours building a website to share the course content.  Focus should be on developing contents in Python, R, etc.  However, **hiacs-cli** will provide enough flexibility for course instructors to modify the website using custom CSS files.  

* *Minimal knowledge of Git and Github* - After a Git repository and Github remote repository are setup, course instructor should never have to touch git functionality again.  Unless, the instructor find a need to perform sophisticated version control functions, he or she will never have to touch Git again.  If instructor chooses to do so, **hiacs-cli** is flexible to accommodate manual git functions.  

* *Same convention across all courses* - Courses will be organized following the same convention across all IACS courses.  While this takes away flexibility from individual course instructors who may want to implement their own project structure, the benefit of maintaining a strict project convention will be rewarding for all instructors as well as students.    

---

## Workflow

Here I outline five simple steps (sixth, for style customization) that a course instructor will follow to setup and build content for a course.

##### 1. Create a new course

In a directory of your choice, you initiate a project (i.e. course) by entering the following command in the terminal:
> $ hiacs-cli create <course name>


This command creates `<course name>` directory and populates the directory with a *Pelican* configuration file and two sub-directories, `content` and `docs`, as shown below:

<img src="img/project_start.png" width=500 />


##### 2. Editing content

In the `content` directory, course instructor can add course materials by directly editing Jupyter notebooks.

<img src="img/editing_document.png" width=500 />

It is advised that course content contains some *key words* (e.g. "Gaussian Process", "Stochastic Gradient Descent") relevant to the topics covered in the material.  In the notebook, course instructor is advised to include them by selecting `Edit Notebook Metadata` from `Edit` in the control panel.

<img src="img/edit_metadata1.png" width=500 />

You can include information such as *title*, *author*, and *key words*.

<img src="img/edit_metadata2.png" width=500 />


Alternatively, course instructor can directly create and edit course content in a markdown document for materials such as course schedule and syllabus.  

<img src="img/edit_markdown.png" width=500 />


##### 3. Publishing

After the content has been edited, course instructor enters the following command in the project root directory:
> $ hiacs-cli publish


This command exports all jupyter notebooks and markdown documents in the `content` directory and converts them into static html files in the `docs` directory.  It is not advised to modify files in the `docs` directory directory as this command will remove and repopulate the html static files in this directory.  



##### 4. Preview content

Before uploading the content online via Github, course instructor can view the web site by entering the following command the project root directory:
> $ hiacs-cli launch


Open up a browser and go to https://localhost:8000/, and instructor will see the home page of the course and he or she can navigate the website like its online version on Github pages.

<img src="img/home.png" width=500 />


##### 5. Uploading to Github

Once the course materials are ready to be published online, initialize a git repository in the project root directory and link the repository to a remote Github repository by following these steps *only once*:
> $ git init

> $ git add .

> $ git commit -m "first commit"

> $ git remote add <github repo>


After the git repo has been initialized and connected to a remote github repository, course instructor can simply enter the following command every time they want to commit and upload the project files to github and publish contents on the course website:
> $ hiacs upload


Because **hiacs-cli** abstracts away most of git functionality, there is no need to do a separate git commands for the commits, unless the course instructor needs to do sophisticated version control.  

##### 6. Customizing style

Although **hiacs-cli** comes with a standard [Bootstrap 4](http://getbootstrap.com/) template, course instructor are free to make modifications to their website's *look-and-feel* by including a CSS file inside a `css` directory in the project root directory.   

<img src="img/editing_theme.png" width=500 />

---

## Project Organization

**hiac-cli** will follow a course content organization similar to that found in 2017 and 2018 AM207.

<img src="img/project_folder.png" width=750 />

Inside the `content` directory, course instructors are advised to organize the course materials by dividing them into the following structure:

* index.md - This contains materials to be presented in the home page of the course website, which include course logistics, instructor bio, etc.  
* Lectures
* Labs (i.e. Sections)
* Homeworks
* Notebooks - This folder contains miscellaneous notebooks that are neither in Lectures, Labs, or Homeworks; for instance, Exams, Final Projects, etc.  
* Pages - This documents contains the syllabus and course schedule documents, and whatever important material to be displayed at the top of the navigation menu on the website.
* Data - This folder contains data to be shared by notebooks across notebooks throughout the course.  
* Images - Similar to Data, this folder contains images shared throughout materials in the course.

Course instructor can experiment with organizational structure that meets their own needs but are encouraged to maintain some degree of consistency.  

---


## Course Website

**hiac-cli** comes with a standard website template that is powered by Bootstrap4.  Static website is automatically generated when the course is published without the need to touch HTML and CSS.  For instance, **hiac-cli** automatically includes documents in `content/pages` directory to populate the navigation bar with links to those documents.  Here is the basic look of a typical IACS course website:    

###### Website Outline
* Home Page

* Syllabus

* Schedule

* Materials

* Topic Pages

###### Home Page

<img src="img/home.png" width=500 />

###### Syllabus

<img src="img/syllabus.png" width=500 />

###### Schedule

<img src="img/schedule.png" width=500 />


###### Materials

Materials page will be automatically generated based on the materials found in `content` directory.  It will organize the materials in chronological order; however, students will also be able to access materials based on key words (e.g. Bayes Theorem, MCMC, etc.).

<img src="img/materials.png" width=500 />

---

## Installation & Setup

**hiac-cli** is available via PyPI.

> $ pip install hiacs


##### Dependencies
* Pelican >= 3.7.0
* Pelican-ipynb

### Command Line Arguments

* `create`
 Initializes a course project and populates the directory with Pelican configuration file.
> $ hiacs-cli create <course_name>


* `publish`
Converts markdown, ipython notebook, and R markdown files in the `content` directory into static html files in the `docs` folder.
> $ hiacs-cli publish


* `launch`
Launches Python server to view course website before it is uploaded remotely.
> $ hiacs-cli launch


* `upload`
Uploads course content to a Github repository.
> $ hiacs-cli upload


* `copy`
Copies an existing course project to create a new project.
> $ hiacs-cli copy <existing_course> <new_course>
