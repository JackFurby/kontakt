# kontakt

In this repo I will be make a helper script for the word game Kontakt.

## How to play the game

For reference here are the rules for the game itself. This game also goes by the name Contact which mostly has the same rules. The game below is a modified version of some rules for contact which can be found here: [https://www.quora.com/How-do-you-play-the-word-game-Contact](https://www.quora.com/How-do-you-play-the-word-game-Contact).

Kontakt requires at least 3 people to play and there is no upper limit.

The game runs in rounds. For each round, one person will be the word-master and everyone else will be guessers. There is no rule about who is the word master but circulating the role is recommended.

The word-master thinks of a noun (cannot be a proper noun) and gives the guessers the first letter. The longer the noun the better as it generally means longer rounds.

The guessers will then try to guess the word the word-master came up with. They will do this by describing a word they think might have been selected to everyone in such a way the other guessers might know it, but the word master might not know it. If two guessers think they have the same word they say "kontakt" and count down from 10 before saying their respective words at the same time. If they match, the word master will give them the next letter (this repeats until the word the word-master came up with is correctly guessed / when there are no more letters to give). During the countdown or while the guessers are describing the word, if the word-master says the word the guesser is describing, then the guessers need to think of a new possible word.

Guessers have to describe words that start with the same letters provided by the word master (in the same order provided).

### An example

`To give credit, this is the same example used in the Contact linked above.`
1. The word-master comes up with the word "apple". They say the word starts with the letter "a". The guessers try to think of words that also start with the letter "a".
2. One of the guessers thinks of the word "apathy" and gives the group a clue, say "This is a symptom of depression".
3. If the word-master can come up with a word that fits the clue, say "apathy" or "anhedonia," they say "It's not apathy" or "It's not anhedonia," and the guessers have to think of another clue.
4. If the word-master cannot think of a word, but one of the other guessers can, the other guesser says "kontakt" and the guessers say the word together after counting down from 10. If they both say the same word, the word-master has to give them the next letter (in this case "p"). If they say different words, then the guessers have to think of another clue. Any two guessers can have a matching word e.g. if three guessers say a word at the end of the countdown, but only two of them match, then the word master still has to provide the next letter.

The guessers will then need to think of and describe a new possible word, but this time starting with "ap" (repeat steps 2-4).

A few house rules:

* The word-masters word must be a dictionary word, and it shouldn't be a word the group is unlikely to know.
* The guessers can use any words they want, including phrases and proper nouns to describe the word they think the word-master has thought of. Like with the word-masters word though, it should be a word everyone will know and described in such a way everyone has a chance of knowing it (obscure is good, but don't describe a word with a reference only two or more of the guessers would ever know). It's best if they're clues that the word-master is expected to know, but doesn't for some reason.

## Kontakt helper script

For the noun list I am using a copy for [http://www.desiquintans.com/nounlist](http://www.desiquintans.com/nounlist) which is a list of aproximatly 6000 popular nouns.

### Options

```
=== Kontakt word game help ===

\q					-	Exit Kontakt helpers
isNoun			-	Returns Yes if a given word is a noun
whatsNext		-	Returns the top 5 word prefixes when given a shorter prefix
```
