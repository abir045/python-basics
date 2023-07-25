from random import choice

capital = "Topeka"

bird = "Western MadowLark"

flower = "sunflower"

song = "Home on the range"


def randomFunFact():

    funFacts = [

        "Kansas is well known for the Wizard of Oz movie.",
        "The World's largest easel is here.",
        "Kansas has over 800 caves.",
        "It has the geographical center of the lower 48 United States.",
        "Mount Sunflower is its highest point.",
        "Pizza Hut started in Kansas.",
        "Flint Hills has the most tallgrass prairie in the world."

    ]

    index = choice("0123")

    print(funFacts[int(index)])


# if __name__ == "__main__":
randomFunFact()
