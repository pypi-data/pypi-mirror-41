Deadline Docker submission™
==========================

Deadline Docker Submission allows for submission of docker jobs to the deadline 
render farm manager. Assumptions are that the docker daemon is of course installed on 
the workers, and that the daemon is actually running. This should also support any flavor of 
host operating system for clients/workers.


dds officially supports python 2.7 and up.


![image](https://www.3dv.com/resize/Shared/Images/Product/Thinkbox-Deadline-7/Deadline_Logo_250.jpg?bw=250&w=250&bh=250&h=250) ![image](https://www.docker.com/sites/default/files/social/docker_facebook_share.png)


Behold, the power of dds. This will run the canonical "docker hello-world example on 
any deadline worker in the "docker" pool :

``` {.sourceCode .python}
>>> from dds import DeadlineDockerSubmitter as dds
>>> return dds()('run hello-world', 'docker hello world job, 50)
0
```

[gitlab-project](https://gitlab.com/snowballvfx/dds)



Installation
------------

To install dds, simply use [pipenv](http://pipenv.org/) (or pip, of course):

``` {.sourceCode .bash}
$ pipenv install dds
```
