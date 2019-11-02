# Is this on fire?

This image recognition tool will detect if an object is on fire or not.

## Contributing

Steps for pushing local changes to github:

To clone repository to your local drive:

`git clone https://github.com/thomashopkins32/HackRPIF2019.git`

Make your desired changes

`git add .`

to stage changes for local commit

`git commit -m "(message)"`

to commit locally

`git push origin master`

to push changes to the master branch on github.

To pull changes from github

`git pull origin master`

## Example Data File
```
cats_and_dogs_filtered
|__ train
    |______ cats: [cat.0.jpg, cat.1.jpg, cat.2.jpg ....]
    |______ dogs: [dog.0.jpg, dog.1.jpg, dog.2.jpg ...]
|__ validation
    |______ cats: [cat.2000.jpg, cat.2001.jpg, cat.2002.jpg ....]
    |______ dogs: [dog.2000.jpg, dog.2001.jpg, dog.2002.jpg ...]
```
