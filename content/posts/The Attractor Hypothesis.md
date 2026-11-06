---
title: "The Attractor Hypothesis"
date: 2026-05-06T13:00:00Z
draft: false
narration: /audio/essay-04-the-attractor-hypothesis.mp3
---

*Previous in the series: [The Slopes of Approval](/posts/the-slopes-of-approval/).*
*Next in the series: [The Opacity of the Obvious](/posts/the-opacity-of-the-obvious/).*

## Three Essays, One Shape

Three essays in, the same shape kept appearing.

The essay on concepts described valleys in a learned landscape: sloped sides, fuzzy edges, and the deepest valleys under the most typical cases, the prototypes. The essay on belief found the same shape under a different name. Confidence comes in degrees and still feels all-or-nothing once it settles; the point where you switch from one view to another moves depending on which side you come from; and how you got into a belief affects how easily you can leave it. The essay on moral sentiment found it again: approval and disapproval as valleys, and moral dilemmas sitting at the saddle points, the mountain passes where two valleys meet and pull equally, so that a small thing decides which way you go. Each time, a theory that wanted clean lines was pressing against ground that wouldn't hold them. If the ground really is the same, then the philosophy of concepts, the theory of knowledge and ethics each keep every distinction they had, and gain an explanation of something none of them could explain alone: why the same puzzle, tools built for sharp lines failing on sloped ground, keeps being rediscovered by people who don't read each other's journals.

I wasn't planning a unified framework when I started. The recurrence happened anyway. By the third essay, I was reaching for the same toolbox, and the tools kept fitting. The honest question is whether they fit because the terrain is really shaped the way they assume, or because I've fallen in love with a hammer and every problem has started to look like a nail.

There are two ways to read that. One is that it's an artifact of my method: a mind committed to thinking from the substrate forward (starting from what the learning system physically is and working out to the philosophy) will find attractor geometry wherever it looks. The other, which I haven't said out loud until now, is the ambitious one: mental life has a common geometry inherited from learning, and the philosophical categories I've been treating one at a time are variations on one shape.

I think the ambitious reading is right, tentatively, and it comes with a bill. There's a question the previous essays quietly stepped around: whether any of this reaches slow, deliberate, step-by-step reasoning, the kind you do with a pen in your hand. And there's a worry that has been growing the whole way through: what would it take to show any of this is wrong?

## Why the Recurrence Was Inevitable

The cheapest explanation is the first one: of course the same shape turns up, given where I started looking. And it's true that once you commit to reasoning from the substrate forward, your options narrow. You don't get to pick the format you like best and then work backwards to a brain that could run it. You get whatever a learning system can stably support, whatever it's made of, and you work from there. The material is swappable: neurons and synapses, silicon, some future technology or alien biology. What isn't swappable is that something has to *learn*, and learning is what narrows the range of patterns that can last. The narrowing comes from what a learner can hold, not from where the method chose to look.

By *dynamics*, here, I mean how the system changes over time. Some patterns die out. Some reinforce themselves. Some compete. Some settle into a state the system can return to and hold. Those settled states are the ones that matter.

Take the cortex. Its local wiring has three rough features, each doing one thing. Neurons excite each other in loops, so a pattern of activity can keep itself going (*recurrent excitation*). Active patterns suppress their competitors. And connections between neurons that fire together grow stronger, Hebbian learning again, so the patterns that recur wear deeper grooves. Each of these, on its own, is just a local rule about how neurons treat their neighbours. Put them together and something follows that isn't obvious. Some patterns across the whole system keep themselves going and others destroy themselves: a pattern that reinforces itself and suppresses its rivals will hold, and one that does neither falls apart within moments of forming. So the space of possible states stops being flat. It takes on a shape, regions the system slides into and regions it slides out of, and the shape is set by what the system has learned, because learning is what set the strengths of the connections in the first place. Like a physical landscape, it makes some positions easy to settle into and others impossible to hold. A filing cabinet keeps whatever you put in it; a system like this has places it tends to go.

Those places are attractors, the low points the system settles into. The valley around one is also called a basin; the two words name the same thing.

The shape isn't only an image. It turns up in the mathematics: in Hopfield networks, essay 1's simple model of memory in which stored patterns become valleys, and in more elaborate models of networks that feed back on themselves, including ones that run in continuous time.[^c4-cohen-grossberg] The details differ from model to model, but the same features keep appearing: places where the system comes to rest, edges that are graded rather than sharp, unstable points between valleys, and hysteresis.

That last is the route-dependence from essay 1, the boundary moving depending on which way you came. Move slowly from one state to another and the system can hold the old state past the point where a fresh system would switch. Belief feels like that. So does perception. So does moral sentiment.

So what a stable, learned pattern looks like in a learning system isn't something I get to choose. The mathematics suggests the answer strongly: it tends to look like a basin with sloped sides.

If that holds for concepts, it should hold for anything else a brain learns and holds. The brain doesn't care whether philosophers file what it holds as a concept, a belief, a degree of confidence or a sentiment. Those are our categories. At the level of the wiring, there's one recurring way of being stable, and it's shaped like an attractor.

That's why the recurrence across essays now feels close to inevitable. Concepts, belief and moral sentiment are three places where the same fact about learning shows itself, in areas philosophy has usually expected to look different.

That's the ambitious reading, at full strength. It's also the reading most likely to lead me into overreach.

---

## Stable Content Has a Common Geometry

What the three essays kept finding fits in one sentence. Whatever a mind holds steady, whether it's something represented, believed or felt, tends to show the same marks: graded edges, a dependence on history, and settled states that are harder or easier to leave. Call this the attractor hypothesis. Stated exactly: those marks are what attractor basins in a learned landscape look like, and they should turn up wherever a mind holds something steady, whatever philosophical category we put it in.

Graded edges mean there are better and worse cases rather than clean yes-or-no boundaries. A dependence on history, *path-dependence*, means the same input has different effects depending on what the system has already learned or recently been doing; hysteresis, from the first essay, is its sharpest form. And settled states differ in how much it would take to move you off them, which is what confidence came to mean in the essay on belief. Being hard to move isn't the same as being right.

The hypothesis is about **primitives**, the basic things a mind can hold steady, and not about the **operations** that combine them. "The dog chased the cat" is something you can hold: a settled state you can return to, recognize and use. That's a primitive in the sense meant here, even though it's obviously not simple. Now do something with it. Swap the roles to get "the cat chased the dog," or put it inside "if the dog chased the cat, the cat ran." Those are operations. They take a held pattern and transform it.

So the hypothesis says the holding is attractor-shaped. It says nothing yet about the transforming, and that gap is where the hardest objection lives.

It's a hypothesis, not something I take to be established: three essays of unexpected fit is suggestive, not a proof.[^c4-scope]

## A Version of This Has Been Tried

Something close to this was tried in the 1980s and didn't survive contact with criticism. Paul Churchland argued that knowing something looks less like storing a sentence and more like occupying a location in a vast space of possible patterns: a thought as a *vector*, a list of numbers fixing its position in such a space.[^c4-churchland] It ran into a wall.

The wall was a 1988 paper by Jerry Fodor and Zenon Pylyshyn, aimed at the whole research program of explaining thought with networks of simple interacting units instead of rules for manipulating symbols. They argued, with real force, that patterns of activity spread across such a network couldn't give thought the structure it obviously has: anyone who can think "John loves Mary" can also think "Mary loves John," because the thought is built from parts that can be rearranged.[^c4-fodor-pylyshyn] The arguments stuck, and "knowledge as geometry" became a position philosophers could wave at without taking seriously.

The objections haven't gone away. What has changed is the evidence they now have to answer: decades of empirical and mathematical work the original critique never faced, from modern models of attractor networks to systems that learn where words belong in a space just from reading text, the networks behind today's language models, and a much richer picture of working memory. That's what follows.

---

## What About Actually Working Something Out?

Concepts have fuzzy edges. Beliefs settle. Moral reactions are fast and visceral. These are exactly the cases pattern recognition handles well, and exactly the cases where a graded basin is what you'd expect. The framework I've been building handles them.

But some thinking doesn't look like pattern recognition at all. Carrying the 2 in long division. Tracing a proof one step at a time, holding each result before taking the next step. Checking whether an argument is valid by looking at its structure rather than by feeling whether it sits right. Psychologists call this kind of work *System 2*, in contrast to the fast, pattern-based judgments they call System 1, a distinction drawn by Keith Stanovich and Richard West and made famous by Daniel Kahneman.[^c4-dual-process] Everything the last three essays covered was System 1. Nothing in them touched System 2, and you don't add up a restaurant bill by feeling which total sits right.

If slow reasoning really is a different kind of thing, the hypothesis has a ceiling. Geometry might explain what a mind holds and still need something else, built from symbols and rules, for what the mind does with it, like turning it round or building an argument on it. That wouldn't touch the hypothesis itself, which is about what a mind holds. It would cap how far it reaches: the common shape of mental life would stop where deliberate thought begins.

Three objections stand in the way. The first is Fodor and Pylyshyn's; the other two press just as hard on any account that wants to reach deliberate thought.

**Compositionality.** Thoughts are built from parts, and the same parts can be rearranged into new thoughts, with each part keeping track of its role: who chased whom. Symbol systems get this for free. It isn't obvious that a geometry can.

**Necessity.** A valid inference isn't a tendency. If the premises really guarantee the conclusion, you can't consistently accept them and reject it. A landscape runs on similarity and "close enough." Necessity doesn't.

**Working memory.** Reasoning in several steps means holding each result while you take the next step, and feeding it forward. A simple Hopfield network settles and stays settled. It doesn't take a step, hold it, and take another.

These three don't threaten the same thing. Compositionality is about what the mind holds. If the geometry can't keep "the dog chased the cat" apart from "the cat chased the dog," with each animal in its own role, then the valleys are holding the wrong kind of thing, and the hypothesis fails at its core. Necessity and working memory are about what the mind does with what it holds: taking one exact step and then another, the way you carry the 2 and move on to the next column. Losing those wouldn't sink the hypothesis. It would cap it where deliberate thought begins.

## The Dog, the Cat, and Which One Did the Chasing


A thought like "the dog chased the cat" has parts, and the parts are arranged by a relation: one thing chasing another. *Compositionality* is the name for what happens when you keep the relation and swap the parts: same frame, new thought, and no limit on how many times you can do it. That's what makes thought productive. Once you have "X chased Y," you have "the dog chased the cat" and "the cat chased the dog" and a thousand others, because one machine is doing all of them and it doesn't care what you feed it.

And it nests. One composed thought can be slotted into another, "If the dog chased the cat, the cat ran," and that one into another again.

This is why the old symbolic picture looked so powerful. Define a relation once, as a frame with slots, and it treats whatever fills the slots the same way. Define *loves* once, and "John loves Mary," "Mary loves John," "prince loves princess" and "king loves queen" all come for free. The same operation produces all of them, and the part of the system that does the producing doesn't have to know anything about kings or princes.

Geometry is where the difficulty bites. If "the dog chased the cat" is a position in a space of many dimensions, then "the cat chased the dog" is a different position. "John loves Mary" is somewhere else. "King loves queen" is somewhere else again, and "prince loves princess" somewhere else still. Nothing about the geometry obviously says these positions are produced by one shared operation. Each pairing lands in its own region, and the space doesn't come with slots, which is what lets one symbolic definition handle every pairing at once.

The clean symbolic story overstates what people do, though, and the gap has always puzzled me. I'm often amazed at how much effort it takes us to take in the principles of an introductory logic class, at how unintuitive probabilities are, and at how many of us find mathematics hard. If the mind ran on a symbol engine that treats whatever fills the slots the same way, these would be the easy parts. They're among the hardest.

Try this before reading on. Below are four cards and a rule, and you can see only one side of each card. Pick the cards you'd need to turn over to find out whether the rule is broken. Start with the version marked *Abstract*, and leave the other one for a moment.

{{< simulation src="/simulations/four-card-problem.html" title="Four-card reasoning experiment" height="700" >}}

If you picked the E, or the E and the 4, you're in good company. When the psychologist Peter Wason set versions of this puzzle in the 1960s, fewer than one in ten people got it right, and that has held up in the decades since.[^c4-wason] The answer is the E and the 7. The E has to be checked, because an odd number on its back would break the rule. The 7 has to be checked too, because a vowel on its back would break the rule just as surely. The 4 can't break it whatever is on the other side, because the rule says nothing about what sits behind an even number.

Now switch to the version at the bar. Each card is a customer, with what they're drinking on one side and their age on the other, and the rule is that anyone drinking beer must be old enough. You probably didn't hesitate: the beer and the 16. When Richard Griggs and James Cox gave students a version like this, about three in four got it right.[^c4-griggs-cox] It's the same if-then shape as the letters and numbers, and the 16 is obvious in a way the 7 never was.

What didn't help is as telling as what did. A semester-long introductory logic course made little difference to how students did on the abstract version.[^c4-logic-course] What helped was the bar: Griggs and Cox's students had lived with that very rule. Nobody solves the bar version by running "if P then Q." They solve it with a valley carved by experience of exactly that situation, of who might be breaking the rule and how you'd catch them. Most of the time that's how we get around in the world, and it works very well.

But the abstract version can be solved. Some people get it on their own, and anyone can be walked through it: whatever P and Q stand for, the only cards that can break "if P then Q" are the P and the not-Q. That's compositionality at work: one frame applied to whatever fills it, letters and numbers as readily as beer and ages. We have it. It's slow and effortful, and we use it far less often than the symbolic picture assumes. That's the standard the geometry has to meet: not a perfect symbol engine, but a mind that can do the general thing with effort and mostly gets by on the particular.

And when we do the general thing, we keep the parts and their roles straight. "The dog chased the cat" and "the cat chased the dog" stay different thoughts, and that takes *structure*, not just pattern recognition. How does a landscape do that? The rearranging itself doesn't have to be a matter of settling into valleys. What the valleys hold only has to be something the rearranging can work on.

At the time of the 1988 critique, even that looked out of reach: it seemed clear that geometry couldn't carry this kind of structure at all. That assumption hasn't held up.

When systems began learning a list of numbers for each word, just by predicting words from the text around them, each word ended up with a place in a space, and words used in similar ways ended up near each other.

{{< simulation src="/simulations/embedding-relations.html" title="Embedding relations simulator" height="620" >}}

The surprise was in the directions. The step from "man" to "woman" turned out to be roughly the same as the step from "king" to "queen," so "king" minus "man" plus "woman" lands near "queen." The step from "France" to "Paris" works the same way for "Italy" and "Rome." Nobody put those relationships in. They emerged because the geometry was shaped by how the words are used, and together they look like an arithmetic of meaning.

This doesn't prove a sweeping theory of language. But it shows something the 1988 critique didn't anticipate. A direction in the space can stand for a relation. Distance can stand for similarity. Shifting a point can move it into a new role. None of that is yet grammar. All of it is more structure than the critics thought such networks could have.

Paul Smolensky saw this possibility in the 1990s and built it deliberately.[^c4-smolensky] Write down a role, "the one doing the loving," as one list of numbers, and a filler, "John," as another. There's a way of combining two such lists that keeps both, so that "John-as-lover" can afterwards be pulled apart again into its role and its filler. You don't need the mathematics to see what it buys: combine "John-as-lover" with "Mary-as-beloved" and you have a representation of the whole thought, with the parts still recoverable.

He showed that patterns of numbers spread across many units can carry structured information, the kind we used to think only symbols could hold. The kind of network dismissed in 1988 was mathematically capable of more than its critics allowed.

The networks behind today's language models make the in-principle objection harder still. They use what's called *attention*: each word in the input weighs how relevant every other word is to it. They keep track of words that depend on each other across long stretches of text, produce grammatical text in dozens of languages, follow sentences nested inside sentences, and write code whose brackets match. None of this is done by a hand-written symbol engine. It's done by attention over learned patterns of numbers.

So the in-principle objection, that patterns of numbers *cannot* carry thoughts built from rearrangeable parts, is much weaker now than it was in 1988.[^c4-composition-caveat]

For this hypothesis, that's enough. It's about what a mind holds, not about every operation that puts held things together. The rearranging doesn't have to happen by settling into valleys. It only has to be compatible with attractor-shaped primitives, and the evidence makes that plausible.

## What Makes a Conclusion Feel Forced

Take *modus ponens*, a basic valid step: from "if P then Q" and "P," conclude "Q." If it's raining, the street is wet; it's raining; the street is wet. That last step isn't a guess. It follows from the premises. And that is exactly the move a landscape looks least able to make. Logic is exact; attractors are not. A geometry might explain why "chair" has fuzzy edges, but a conclusion doesn't have fuzzy edges. It either follows or it doesn't.

The worry is right, and answering it means keeping two questions apart. The first is what makes a valid step valid, and logical necessity isn't just a very strong habit. A valid inference doesn't become valid because a nervous system is confident about it. The relation between premises and conclusion is what it is whether or not anything ever computes it, and no fact about basins touches that.

The second question is about whatever does the reasoning: what would a system have to look like in order to move *reliably* from premises to conclusion?

Here the geometry has an answer. Once the system is in a state representing the premises, the landscape pulls it toward the conclusion. Drop the state anywhere in the region that represents "P implies Q, and P is the case," and it rolls to the state representing Q, not because it has been told to, but because in that region there is nowhere else to settle. In a trained system, every alternative resting place would have been eroded by training.

And this is where the account earns something, because it predicts the failures too. If reliability came from a rule being applied, bad reasoning would be a rule misapplied, and nothing about the rule says which misapplications should be common. Yet the errors aren't scattered. People commit the *same* fallacies, affirming the consequent in particular: if it's raining, the street is wet; the street is wet; so it's raining. It looks a lot like modus ponens and is a short roll away in the landscape. It's also the 4 in the card puzzle: turning the 4 to test the rule is checking whether the street is wet to find out whether it rained. A geometry explains why valid moves feel forced, and why the invalid ones that feel forced tend to be the near neighbours of valid ones.


Picture the marble. The premises mark out a region of the landscape, the part that fits the starting assumptions. The conclusion is the only valley that region drains into. The walls of that valley are steep enough that no small nudge anywhere in the region pushes the marble somewhere else. That's what necessity looks like in geometric terms: a fact about the shape of the space, not about any particular path through it, about a region with only one place to end up.

What the steep walls model is the *grip* necessity has on a reasoning system: why, once the premises are in place, the conclusion is the only place the marble can roll.[^c4-necessity-scope]

Watched over time instead of seen as a shape, that roll from premises to conclusion is a path with steep walls on either side, a *trajectory*. Once you have one steep-walled trajectory, you can chain it with others. Step one delivers conclusion A. That becomes the input to step two, which delivers conclusion B. Step two's output feeds step three. Chain reliable steps like this and a system can build a proof or an argument over time. A mathematical proof is the extreme case: a series of steps, each one tightly constrained where it stands, threaded into a single path through the space of possible states.

---

## Where the Half-Finished Thought Sits

When a monkey is shown a cue and then asked to remember it for several seconds before responding, particular groups of neurons in its prefrontal cortex stay active through the whole delay, carrying the cue in their sustained firing.[^c4-working-memory] The activity doesn't fade back to baseline the way most responses in the cortex do. It persists, holding the information ready, until it's used or replaced. Patricia Goldman-Rakic's group documented this in the 1990s; Xiao-Jing Wang and others traced it to recurrent excitation, neurons in local circuits keeping each other firing. This sustained firing is the classic signature of working memory in the brain, and it's exactly what the simple settle-and-stop model lacked.

In landscape terms, what prefrontal cortex adds is *metastable* attractors: shallow dips rather than deep valleys, stable enough to hold a state long enough to act on, and easy enough to leave that signals from elsewhere can move it on when the next step is ready. It's still geometry. The state is still a position in the space of possible states. What's new is a way to hold a position for a while instead of racing to a final resting point. The marble can sit in a shallow dip.

Put the shallow dips together with the chained steps from the last section and the picture starts to handle reasoning in several steps. The brain takes a step, rolling down one of those steep paths. It holds the result in a shallow dip in prefrontal circuits. It uses that result as the input to the next step, which sets off a new path in another circuit. The whole computation is a directed walk through a sequence of states, with each held state as the place where an intermediate result sits while the next step runs.

Language models make this story harder to dismiss. *Chain-of-thought prompting* asks a model to write out its intermediate steps and then use them as context for what comes next.[^c4-chain-of-thought] On a word problem like "Roger has 5 tennis balls; he buys 2 cans with 3 balls in each; how many tennis balls does he have now?", a chain-of-thought response writes out something like "5 + (2 × 3) = 11" before answering. That visible scratchpad measurably improves performance on tasks that require holding intermediate results. Here what holds the result is the written text itself, read back in at each step, so it's closer to the pen and paper below than to sustained firing. The model takes a step, holds the result, and uses it for the next. None of this shows that language models reason the way brains do, or that what goes on inside them matches the cortex. It shows the weaker point that matters here: systems built from learned patterns of numbers can work step by step, which once looked like something only symbols could do.

So necessity and working memory turn out to be one problem at two scales. How does a graded system take a step that has to be exact, and then take another? One answer: steep-walled trajectories chained together, with metastable attractors holding each result. That doesn't settle how reasoning is actually built. It does show the geometry has a more serious answer than the 1988 critique allowed.

It also doesn't end at the skull. When a problem outruns what a language model can keep in its flowing text, the model doesn't push harder against its own capacity; it calls a tool. Run this code. Compute this expression. Query this database. The model writes the request, the tool returns the result, and the model carries the answer forward. Nothing inside it ever has to keep all the intermediate work in view at once.

Humans do the same thing, and always have. When I don't trust myself to hold a long division in my head, I reach for a pen. Pen and paper do the same job on a more reliable substrate. The brain holds the current step. The page holds the steps before it. The page does the work the metastable attractor was doing inside, only steadier and for longer. Mathematicians use blackboards. Accountants used ledgers before they used spreadsheets. The principle is the same each time: put down what working memory can't carry, and keep in mind only what the next step needs.

## The Hard Part the Geometry Can't Answer

One objection is left, and it asks what makes a brain state *mean* anything. It goes by the name semantic grounding.[^c4-levels] A state that reliably shows up when a dog is present hasn't yet been shown to mean *dog*. A system can enter a state every time a dog appears, and there's still a real question about what makes the state *about* the dog rather than merely caused by it.

This isn't a problem the geometry fails to solve. It's a problem nothing has solved. Brentano gave it its modern name in the 1870s, *intentionality*, the way a mental state points at something beyond itself, and philosophers have circled it ever since without converging.[^c4-intentionality] It's possible the question is badly put. It assumes you can cleanly separate the state doing the meaning, a pattern of activity in a brain, from what it means, and that assumption may not survive a close look.

A better picture of the brain doesn't, by itself, make this question go away. Knowing the shape of what a mind holds tells us the format it's held in. It doesn't tell us how the holding comes to be *about* anything. That's as far as reasoning up from the biology can reach. The question may need to be reformulated before any framework, geometric or otherwise, can claim to answer it. Until then, it stays open.

But if the geometry can't explain what makes a state *mean* anything, hasn't the whole project explained the furniture while leaving the house empty?

I want to give that its due, because it's the version I find hardest to shake. Here is the most I think can be said against it. Chemistry didn't wait on a theory of what life is before ruling out most of what a living thing could be made of. The geometry is the same kind of claim: it says what shapes a mind's contents can take *at all*, and limits of that kind have consequences even when the deepest question stays open. That's where the furniture image flatters the objection. Furniture can be carried out of a house without changing the house. The shapes a mind's contents can take don't come apart from those contents that way.

That's a real reply and it isn't a complete one. If aboutness turns out to require something the geometry has no room for, the framework will have described the format of thought while missing what made it thought. I don't know how to rule that out.

## Everything Has an Answer, Which Is the Problem

If you've been reading the last few sections with any suspicion, you should have it by now. Three hard problems, three answers, all in the same vocabulary. Compositionality? Word arithmetic and Smolensky's way of combining roles with fillers. Necessity? Steep-walled trajectories. Working memory? Metastable attractors. Semantic grounding was the one exception, and I didn't pretend otherwise.

But one admitted gap is a thin defence. A picture with an answer for everything is not obviously a picture of anything. If there's a geometric translation for any mental capacity I come across, then the framework isn't a real claim about the mind. It's a vocabulary I'm fluent enough in to translate anything into.

This is the falsifiability trap, and the hypothesis as stated is open to it. To make it a real claim, I'd need to name things the geometry *does not* allow: things a mind could turn out to do that would count against the geometry rather than wait to be translated into it. I don't have that list yet, only candidates: places where the framework probably forbids something, none worked out carefully enough to stake the framework on. Turning them into the list is the most important piece of work the hypothesis still owes.


Take the sharpest candidate. Wherever a mind most clearly holds something steady, the geometry says you should find graded effects: path-dependence, hysteresis above all, and settled states that differ in how much it would take to move you off them. So find a place where a mind unmistakably holds something steady, and look for those effects. If they vanish there, if a firmly held belief showed none of the path-dependence and none of the hold-past-the-switch that the geometry says a deep basin must have, the picture is in trouble. That's the shape a real test would take. It wouldn't show the geometry is the only account that predicts hysteresis: a thermostat, on at 18° and off at 20°, has it with two numbers and no terrain. What it tests is that the geometry can't avoid hysteresis, where a threshold has to have it added by hand. Three more press from other angles. Each, if it turned out true, would count against the hypothesis or against its reach into reasoning:

- **Something held steady in a format cut off from the activity that uses it.** The geometry says the shape of what's held and the process that holds it are the same fact. Find something the brain can retrieve whose format has nothing to do with how the brain settles, and that fails.
- **Rearrangement with no friction.** Symbols promise rearrangement that ignores context completely: the same operation, whatever fills the slots. Learned landscapes resist this; they carry traces of what has been combined with what. Show that human thought rearranges parts with no friction at all, and the landscape isn't doing the work.
- **Separate systems for working and long-term memory.** The account needs these to be the same terrain, with shallow dips for what you're holding right now and deeper valleys for what you've learned. Show they run on separate systems with no shared geometry, and the unified picture is gone.

These are real pressures, not yet sharp tests. So the hypothesis is interesting, the method is principled, and the evidence and mathematics of recent decades have weakened the original objections. It's also dangerously accommodating. Until what it forbids is sharper, it's closer to a way of looking than to a theory.

That's the right place for it at this stage.

---

## Where the Hypothesis Stands

The case for geometry has always been easier to make for the fast, intuitive parts of thinking. The case for the slow, deliberate parts has been harder, and that difficulty put real pressure on the previous essays: a sense that the move was being made too cheaply, with the hardest cases left for later.

This was the later. The geometry doesn't break on the slow cases. It has a more serious answer to each of the three objections than the original critique allowed, and what it forbids is still open. Slow thinking on sloped ground looks like the same kind of walk the previous essays were describing, held longer, stepped more deliberately, threaded through a route. The landscape may be more than a local tool. It may be the common shape of what the mind can hold.

That's the suggestion the hypothesis names. It's now visible enough to argue with.

[^c4-scope]: Besides primitives versus operations, the claim is narrowed in three further ways. **Stable contents.** Attractor geometry is the geometry of what persists; transient firing patterns that come and go may or may not have this structure, and the hypothesis takes no position there. **Shared geometry, not sameness of content.** Saying concepts and beliefs share an attractor-shaped structure no more collapses the distinction between them than calling lakes and ponds both depressions that hold water collapses that distinction. The categories survive; the hypothesis says they are variations within a single structural type. **A hypothesis, not a thesis.** Across three essays the framework did unexpectedly good work in domains philosophy treats as distinct. That is suggestive and it is not a proof. The right attitude toward it is serious attention plus willingness to be wrong.

[^c4-cohen-grossberg]: Cohen, M. A., & Grossberg, S. (1983). "Absolute stability of global pattern formation and parallel memory storage by competitive neural networks." *IEEE Transactions on Systems, Man, and Cybernetics*, 13(5), 815-826.

[^c4-churchland]: Churchland was reaching for something in this neighbourhood, and the relationship is genealogical, not identical. He tied the picture to something much harder to defend, *eliminative materialism*: the idea that a mature neuroscience might not explain belief and desire so much as replace them, the way chemistry replaced phlogiston. That extra weight helped sink his program, at least among philosophers. The version sketched here is a claim about the shape of what the substrate carries, and it leaves entirely open whether beliefs and desires are real at the level of persons. The objections aimed at his version had specific targets, and this version doesn't have all of them.

[^c4-levels]: A lighter objection asks about the essay's own standing. If beliefs are "really" attractor states, what is this essay's own claim? It's stated in the language of beliefs and reasons, the very level the geometric story seems to dissolve; say that beliefs aren't really beliefs and you appear to saw off the branch you're sitting on. But this version leaves open whether beliefs are real at the level of persons, and different levels of description can both be true. A chess game is wood pieces on a board, and a contest between two players, and a position with a forced win in three. None of those undoes the others. The level at which I say "I believe my keys are in the kitchen" sits above the level at which my brain implements that belief in dynamics that have no sentence-shape; it doesn't compete with it. The essay's claim can be evaluated as a claim because the level where claims live is still there.

[^c4-fodor-pylyshyn]: Fodor, J. A., & Pylyshyn, Z. W. (1988). "Connectionism and cognitive architecture: A critical analysis." *Cognition*, 28(1-2), 3-71.

[^c4-wason]: Wason, P. C. (1968). "Reasoning about a rule." *Quarterly Journal of Experimental Psychology*, 20(3), 273-281. Rates on the abstract version vary from study to study, but typically fewer than 10% of people choose the correct cards.

[^c4-griggs-cox]: Griggs, R. A., & Cox, J. R. (1982). "The elusive thematic-materials effect in Wason's selection task." *British Journal of Psychology*, 73(3), 407-420. Their rule was "If a person is drinking beer, then the person must be over 19 years of age," and the students were asked to imagine they were police officers checking a bar. About three-quarters chose correctly on the drinking-age version; on the abstract version, almost none did.

[^c4-logic-course]: Cheng, P. W., Holyoak, K. J., Nisbett, R. E., & Oliver, L. M. (1986). "Pragmatic versus syntactic approaches to training deductive reasoning." *Cognitive Psychology*, 18(3), 293-328. Students tested at the start and end of a semester-long introductory logic course showed little improvement.

[^c4-composition-caveat]: The narrower claim is what the argument needs. Current learned systems don't match every aspect of human compositional ability cleanly, and there are aspects of those systems nobody fully understands yet. What's gone is the *in-principle* barrier: the claim that a continuous representation simply couldn't carry structured combination at all.

[^c4-smolensky]: Smolensky, P. (1990). "Tensor product variable binding and the representation of symbolic structures in connectionist systems." *Artificial Intelligence*, 46(1-2), 159-216.

[^c4-necessity-scope]: The analogy has to stop somewhere. Steep basin walls don't explain away what philosophers have meant by *must* for centuries. A dynamical model of inference is an implementation-level analog of necessity, not a theory of logical truth itself. Whether that analog exhausts necessity, or only models the cognitive grip necessity has on us, is a separate question, and not one this framework has to settle.

[^c4-working-memory]: Goldman-Rakic, P. S. (1995). "Cellular basis of working memory." *Neuron*, 14(3), 477-485; Wang, X.-J. (2001). "Synaptic reverberation underlying mnemonic persistent activity." *Trends in Neurosciences*, 24(8), 455-463.

[^c4-chain-of-thought]: Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., & Zhou, D. (2022). "Chain-of-thought prompting elicits reasoning in large language models." *Advances in Neural Information Processing Systems*, 35.

[^c4-intentionality]: Brentano introduced the term in *Psychology from an Empirical Standpoint* (1874). Husserl framed another version of the problem; Quine, Putnam, Dretske, Millikan and many others have worked on it for the better part of a century without converging on an answer.

[^c4-dual-process]: Stanovich, K. E., & West, R. F. (2000). "Individual differences in reasoning: Implications for the rationality debate?" *Behavioral and Brain Sciences*, 23(5), 645-665, which introduced the System 1 / System 2 labels; Kahneman, D. (2011). *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, which adopted and popularised them.
