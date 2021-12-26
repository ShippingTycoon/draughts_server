# MSc Summer Project - Integrating Draughts with Software Applications through Computer Vision  

With the popularity of physical board games’ digital counterparts ever increasing, there is a danger of
the physical game’s unique benefits being left behind. As the setting of a physical board game promotes
social skills in a way digital games struggle to imitate, the question is asked as to whether the physical
game can harness the advantages of the digital setting without compromising on it’s inherent benefits.


This project sought to answer this question by developing a mobile application integrating the physical
and digital environments of draughts. This was achieved by employing computer vision techniques to
capture the state of a board and manipulate this data to provide value to the user through a generated
move suggestion represented graphically.  

Implementation of this application was achieved through the following:
- An open source object detection model was trained to recognise the required elements of a draughts
board to capture game state
- A program was developed to improve the object detection model’s performance through evaluating and parsing results 
- A program was developed to translate the elements returned from the object detection model into a game state 
- An open source game AI was integrated to take game state as input and output a suggested move
- A web application encapsulating object detection, game state translation and game AI for remote communication via REST API call was hosted 
- A native mobile application was developed for image capture, image upload and move suggestion representation
- A testing pipeline was developed and executed to assess application functionality and value to the user 

The application prototype implemented in this project is designed for over-the-board draughts players
who would like to experience features unique to a digital environment without leaving the physical game.
Evaluation was conducted through 2 categories:
1. Core application performance, broken down into components, assessing the efficacy with which the
application provides a move suggestion from image input.
2. Value of the application’s feature set to over-the-board draughts players, conducted through mod-
erated in person user tests.

The findings of this evaluation showed that through a combination of software development and the
integration of open-source tools, a suitable move suggestion system from image input on a mobile device
can be created. However, the feature set is not evaluated to provide value to the physical game at this
stage and future development is planned to implement features more aligned with the needs of draughts
players. Specifically, user-informed evaluation found that a move suggestion system was not particularly
useful for the purposes of learning, and a feature set focused on basic game education has been outlined
for future development.

The key contributions of this project are the development of the mobile draughts application and the
labelled image dataset. This application and the accompanying documentation serve as evidence of a
successful method to obtain and represent game state in an understandable and manipulable format.
From here, software implementations can be made in relation to the game of draughts in a manner
similar to a purely digital environment. The publicly available dataset can be used by other developers
in the computer vision community to further the development of models and techniques to recognise
board games. The dataset can be found at https://universe.roboflow.com/harry-field-qemqy/draughts-board-fm9sx.

