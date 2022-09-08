from Madlibs import Sa_Tagalog, Self_Intro, 한국말로_쓰는_매드립
import random

if __name__ == "__main__":
    m = random.choice([Sa_Tagalog, Self_Intro, 한국말로_쓰는_매드립])
    m.madlib()