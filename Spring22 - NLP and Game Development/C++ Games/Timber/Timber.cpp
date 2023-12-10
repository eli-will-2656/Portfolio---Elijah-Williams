// Timber.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

// Including the contents of this header file into our code before compilation
// During preprocessing

// So the include directories tell the compiler / preprocessor which directories to search for header files that we include in our program
#include <SFML\Graphics.hpp>

// Here we include the string stream module to help us manipulate and print out string literals
#include <sstream>

// Here we import the entire namespace dictionary from sf into the
// global scope of our program

using namespace sf;

// Function declaration
void updateBranches(int seed);
const int NUM_BRANCHES = 6;
Sprite branches[NUM_BRANCHES];

// Where is the player/branch? (Left, Right, None)
enum class side { LEFT, RIGHT, NONE };
side branchPositions[NUM_BRANCHES];

int main()
{
    VideoMode vm(1920, 1080);

    RenderWindow window(vm, "Timber!!!", Style::Fullscreen);

    // Set up background ///////////////////////
    Texture textureBackground;

    // Load a graphic into the texture
    textureBackground.loadFromFile("graphics/background.png");

    // Create a sprite
    Sprite spriteBackground;
        
    // Attatch a texture to the SPrite
    spriteBackground.setTexture(textureBackground);

    // Set the spriteBackground to cover screen
    spriteBackground.setPosition(0, 0);

    // Set up Tree /////////////////////////////
    Texture textureTree;
    textureTree.loadFromFile("graphics/tree.png");

    // Creating a sprite to load to window each game loop
    Sprite spriteTree;
    spriteTree.setTexture(textureTree);
    spriteTree.setPosition(810, 0);

    // Prepare the Bee /////////////////////////
    Texture textureBee;
    textureBee.loadFromFile("graphics/bee.png");

    Sprite spriteBee;
    spriteBee.setTexture(textureBee);
    spriteBee.setPosition(0, 800);

    // Adding movement
    bool beeActive(false);
    float beeSpeed(0.0f);

    // Placing the three Clouds //////////////////
    Texture textureCloud;
    textureCloud.loadFromFile("graphics/cloud.png");

    // Creating three sprites from a single texture
    Sprite spriteCloud1;
    spriteCloud1.setTexture(textureCloud);
    Sprite spriteCloud2;
    spriteCloud2.setTexture(textureCloud);
    Sprite spriteCloud3;
    spriteCloud3.setTexture(textureCloud);

    // Setting at different heights
    spriteCloud1.setPosition(0, 0);
    spriteCloud2.setPosition(0, 250);
    spriteCloud3.setPosition(0, 500);

    // Are clouds on the screen?
    bool cloud1Active = false;
    bool cloud2Active = false;
    bool cloud3Active = false;

    float cloud1Speed = 0.0f;
    float cloud2Speed = 0.0f;
    float cloud3Speed = 0.0f;

    // Create a clock object to control for frame rate
    Clock clock;

    // Creating a timebar
    RectangleShape timeBar;
    float timeBarStartWidth = 400;
    float timeBarHeight = 80;
    timeBar.setSize(Vector2f(timeBarStartWidth, timeBarHeight));
    timeBar.setFillColor(Color::Red);
    timeBar.setPosition((1920 / 2) - (timeBarStartWidth / 2), 980);
    Time gameTimeTotal;
    float timeRemaining = 6.0f;
    float timeBarWidthPerSecond = timeBarStartWidth / timeRemaining;

    // Start the game in paused mode
    bool paused = true;

    int score = 0;

    sf::Text messageText;
    sf::Text scoreText;

    // Loading in font
    // We need to choose a font
    sf::Font font;
    font.loadFromFile("fonts/KOMIKAP_.ttf");

    // Set the font to our message
    messageText.setFont(font);
    scoreText.setFont(font);

    // Assign the actual message
    messageText.setString("Press Enter to start!");
    scoreText.setString("Score = 0");

    // Make it really big
    messageText.setCharacterSize(75);
    scoreText.setCharacterSize(100);

    // Choose a color
    messageText.setFillColor(Color::White);
    scoreText.setFillColor(Color::White);

    // Position the text
    FloatRect textRect = messageText.getLocalBounds();

    messageText.setOrigin(textRect.left +
        textRect.width / 2.0f,
        textRect.top +
        textRect.height / 2.0f);

    messageText.setPosition(1920 / 2.0f, 1080 / 2.0f);

    scoreText.setPosition(20, 20);

    // Loading in the branch texture //////////////
    Texture textureBranch;
    textureBranch.loadFromFile("graphics/branch.png");
     
    // Creating Sprites from the branch textures
    for (int i(0); i < NUM_BRANCHES; ++i) {
        branches[i].setTexture(textureBranch);
        branches[i].setPosition(-2000, -2000);
        branches[i].setOrigin(220, 20);
    }


    // Creating the game loop
    while (window.isOpen())
    {
        // C-style comment
        /*
        ****************************
        
        Handle the players input 

        ****************************
        */
        if
            (Keyboard::isKeyPressed(Keyboard::Escape))
        {
            window.close();
        }
        // Start the game if Enter is pressed

        if
            (Keyboard::isKeyPressed(Keyboard::Return)) {
            paused = false;
            // Reset the time and the score

            score = 0;

            timeRemaining = 6;
        }

 

        /*
        ****************************************
        Update the screen

        ****************************************
        */

        if (!paused) {
            // Measure time (storing in delta time variable)
            Time dt = clock.restart();  // restart method returns time elapsed on clock since last restart

            // Update timebar
            timeRemaining -= dt.asSeconds();
            timeBar.setSize(Vector2f(timeBarWidthPerSecond *

                timeRemaining, timeBarHeight));

            if (timeRemaining <= 0.0f) {



                // Pause the game

                paused = true;

                // Change the message shown to the player

                messageText.setString("Out of time!!");

                //Reposition the text based on its new size

                FloatRect textRect = messageText.getLocalBounds();

                messageText.setOrigin(textRect.left +

                    textRect.width / 2.0f,

                    textRect.top +

                    textRect.height / 2.0f);

                messageText.setPosition(1920 / 2.0f, 1080 / 2.0f);

            }



            // Setting up the Bee at a place and speed
            if (!beeActive) {
                srand((int)(time(0)));

                beeSpeed = (rand() % 200) + 200;

                // Seeding the RNG with different number
                srand((int)time(0) * 10);

                float height = (rand() % 500) + 500;

                spriteBee.setPosition(2000, height);

                beeActive = true;
            }

            else {
                spriteBee.setPosition(
                    spriteBee.getPosition().x - beeSpeed * dt.asSeconds(),
                    spriteBee.getPosition().y
                );
                if (spriteBee.getPosition().x <= -100) {
                    beeActive = false;
                }
            }

            Sprite clouds[3] = { spriteCloud1, spriteCloud2, spriteCloud3 };
            bool cloudsActive[3] = { cloud1Active, cloud2Active, cloud3Active };
            float cloudsSpeed[3] = { cloud1Speed, cloud2Speed, cloud3Speed };
        
            
            // Set up the cloud if not active (initialize posiiton and speed)
            if (!cloud1Active) {

                // Give cloud1 a speed
                srand((int)time(0) * 10);  // Make sure to get a diffrent seed for each of the clouds

                // Generate random number for cloud spped
                cloud1Speed = (rand() % 50) + 50;

                // Set cloud1 to random height
                srand((int)time(0) * 10);
                int height = rand() % 200;

                // Set the position of cloud on the left hand side
                spriteCloud1.setPosition(-200, height);

                // Set cloud1 variable to be acrive
                cloud1Active = true;
            }

            // If the cloud is active
            else {
                spriteCloud1.setPosition(
                    spriteCloud1.getPosition().x + dt.asSeconds() * cloud1Speed,
                    spriteCloud1.getPosition().y
                );

                // if cloud goes offscreen
                if (spriteCloud1.getPosition().x > 1920) {
                    cloud1Active = false;
                }
            }

            if (!cloud2Active) {

                // Give cloud2 a speed
                srand((int)time(0) * 20);  // Make sure to get a diffrent seed for each of the clouds

                // Generate random number for cloud spped
                cloud2Speed = (rand() % 200) + 50;

                // Set cloud1 to random height
                srand((int)time(0) * 20);
                int height = rand() % 200 + 150;

                // Set the position of cloud on the left hand side
                spriteCloud2.setPosition(-200, height);

                // Set cloud variable to be acrive
                cloud2Active = true;
            }

            // If the cloud is active
            else {
                spriteCloud2.setPosition(
                    spriteCloud2.getPosition().x + dt.asSeconds() * cloud2Speed,
                    spriteCloud2.getPosition().y
                );

                // if cloud goes offscreen
                if (spriteCloud2.getPosition().x > 1920) {
                    cloud2Active = false;
                }
            }
            if (!cloud3Active) {

                // Give cloud3 a speed
                srand((int)time(0) * 30);  // Make sure to get a diffrent seed for each of the clouds

                // Generate random number for cloud spped
                cloud3Speed = (rand() % 150) + 50;

                // Set cloud1 to random height
                srand((int)time(0) * 30);
                int height = rand() % 200 + 400;

                // Set the position of cloud on the left hand side
                spriteCloud3.setPosition(-200, height);

                // Set cloud1 variable to be acrive
                cloud3Active = true;
            }

            // If the cloud3 is active
            else {
                spriteCloud3.setPosition(
                    spriteCloud3.getPosition().x + dt.asSeconds() * cloud3Speed,
                    spriteCloud3.getPosition().y
                );

                // if cloud goes offscreen
                if (spriteCloud3.getPosition().x > 1920) {
                    cloud3Active = false;
                }
            }

            // Update the score text
            std::stringstream ss;
            ss << "Score = " << score;
            scoreText.setString(ss.str());

            //update the branch sprites

            for (int i = 0; i < NUM_BRANCHES; ++i) {
                float height = i * 150;
                if (branchPositions[i] == side::LEFT) {
                    // Then we want to set the position
                    branches[i].setPosition(610, height);
                    // And flip the branch around
                    branches[i].setRotation(180);
                }
                else if (branchPositions[i] == side::RIGHT) {
                    branches[i].setPosition(1330, height);
                    // Set the rotation to normal
                    branches[i].setRotation(0);
                }
                else {
                    // Hide the branch
                    branches[i].setPosition(3000, height);
                }

            }


        } // End of (if !paused) code block


        

        /*

        ****************************************

        Draw the scene

        ****************************************

        */
        // Clear everything from the last frame
        window.clear();

        // Draw our game scene here
        window.draw(spriteBackground);

        // Draw clouds
        window.draw(spriteCloud1);
        window.draw(spriteCloud2);
        window.draw(spriteCloud3);

        // Drawing the branches to the window
        for (int i(0); i < NUM_BRANCHES; ++i) {
            window.draw(branches[i]);
        }

        // Draw tree
        window.draw(spriteTree);


        // Draw bee
        window.draw(spriteBee);

        // Draw text objects

        // Draw the timebar

        window.draw(timeBar);

        // Draw the score
        window.draw(scoreText);


        if (paused)
        {
            // Draw our message
            window.draw(messageText);
        }


        window.display();
    }

    return 0;
}


void updateBranches(int seed) {
    // Move all the branches down one place

    // LOGIC: 
    // for branches 0 - 4, set the branch posiitons equal to the one above it,
    // for branch[5], pick a random integer between 0, 1, if 0 on left, if 1 pickr ight
    for (int i(NUM_BRANCHES - 1); i > 0; --i) {
        branchPositions[i] = branchPositions[i - 1];

    }
    // Spawning a new branch position
    srand((int)time(0) + seed); // seed the RNG using time
    int r = (rand() % 5);

    // Creating cases in which 2 / 5 times a branch appears
    switch (r) {
    case(0):
        branchPositions[0] = side::LEFT;
        break;
    case(1):
        branchPositions[0] = side::RIGHT;
        break;
    default:
        branchPositions[0] = side::NONE;
        break;
    }

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
