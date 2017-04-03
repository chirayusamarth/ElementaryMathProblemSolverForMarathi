# ElementaryMathProblemSolverForMarathi
Elementary Math Problem Solver aims to solve single-variable addition and subtraction word problems given in Marathi.
The motivation behind this idea comes from the fact that designing algorithms to convert
word problems to equations is a long-standing challenge. Particularly for NLP, such problems are
interesting because the text is concise and the semantics reduces to simple equations. Math solver
has been implemented for languages like English (Wolframalpha) and Hindi but not for Marathi.
Having a system which solves math problems using NLP will be a giant leap for Marathi language.


Example:

रमा कडे 5 खेळणी आहेत. ती दुकानातून 4 अधिक खेळणी विकत घेते. आता तिच्या कडे किती खेळणी आहेत?
Rama kade 5 khelni aahet. Ti dukanatun 4 adhik khelni vikat ghete. Aata tichya kade kiti khelni aahet? 
Translation: Rama has 5 toys. She buys 4 more toys from a shop. How many toys does she have now?


Entity: खेळणी
Container: दुकान

Quantity: 5, 4

Equation: 5 + 4

Result: 9
