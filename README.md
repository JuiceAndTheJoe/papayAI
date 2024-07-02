# papayAI 🍊🌴

The newest addition to the AI frenzy taking over the world!

## ✨ YOU NEED AI IN YOUR LIFE ✨

Had enough of the sprinkle emoji✨ LITERALLY EVERYWHERE???

no you haven't :)

Now you can train your own AI**** to help you figure out (exactly?) what fruit you have in your hands

(**** decision tree)

## 💡 How it works

papayAI is a simple console-based python program that LEVERAGES [scikit-learn's "tree" module](https://scikit-learn.org/stable/modules/tree.html) to classificate objects given their physical characteristics.

Use the [IKEA Effect](https://en.wikipedia.org/wiki/IKEA_effect) to feel like a true Machine Learner! With papayaAI you can use training data (`features.txt` and `labels.txt`) to give your artificial friend an idea of what different fruits look like.

## ✍️ Data formatting

papayAI reads `features.txt` as a unique item per line, with three characteristcs (weight in grams, hairy or smooth and color) for each item. A "hairy" or "smooth" fruit is determined by a 0 or a 1 and numbers 7-9 represent brown, violet and green.

# Classifying process example:

1000 0 7
500 1 9

is then read by papayAI as:

weighs 1000g, is hairy and brown
weighs 500g, is smooth and green

and is classified as:

a VERY BIG kiwi!
a pretty small watermelon :)
