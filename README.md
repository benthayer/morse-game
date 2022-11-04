Simple command line game to learn morse.

I built this game because I wanted to start by learning words rather than letters. I think my brain works better that way. Start small with a real example, then build up. It just takes too long going letter by letter.

How to play:
1) Install prerecs
2) `git clone https://github.com/benthayer/morse-game.git`
3) `cd morse-game`
4) `python main.py`


Prerecs:
- python 3.10
- `pip install simpleaudio`
- `pip install pycwgen`


How does the game work?

You wil play a series of rounds. Each round generates a sample and you have to guess what word it is. You can also play with sentences. Simply type in your guess and it'll tell you if you're right. There is a word bank.


Learning approach

At first you'll have no idea what any of the sounds mean, especially on day one. Some magic happens while you're sleeping and after a few days you'll be able to differentiate sounds, but it'll still be confusing. Eventually, it'll be second nature. Learning with this is faster than other methods because your brain learns to recognize all the sounds right away. Once you're an expert with the phrases provided, edit the code to add more phrases. It'll get easier and easier to understand and you'll be hearing words instead of dits and dahs in no time.

Limitations
- No longer phrases
- No numbers / special characters
- Limited vocabulary (but still has every letter)

```
Example:
Available Words
----------------
Articles: ['the', 'her', 'its', 'their', 'my']
Adjectives: ['brown', 'small', 'big', 'quick', 'jynxed']
Nouns: ['frog', 'bag', 'plane', 'zebra', 'video']

Example Sentences
------------------
my quick video
the small video
their big zebra
its brown zebra
its quick frog
the jynxed video

Please select mode:
 1) Sentence Mode
 2) Article Mode
 3) Adjective Mode
 4) Noun Mode

Selection: 1

How many rounds would you like to play?
Selection: 3

Playing 3 rounds of Sentence Mode

Round 1/3:
---------
Score: 0%

Playing sample...

Type solution. If you don't know a word, type ? instead of the word
Your guess: their small zebra

Your guess    :  their small zebra
Actual answer :  the small zebra
Score: 2/3


Round 2/3:
---------
Score: 33%

Playing sample...

Type solution. If you don't know a word, type ? instead of the word
Your guess: the brown bag

Your guess    :  the brown bag
Actual answer :  the jynxed video
Score: 1/3


Round 3/3:
---------
Score: 33%

Playing sample...

Type solution. If you don't know a word, type ? instead of the word
Your guess: ? jynxed frog

Your guess    :  ? jynxed frog
Actual answer :  my jynxed plane
Score: 1/3


Final Score: 44%
```
