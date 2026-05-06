---
title: "The Attractor Hypothesis"
date: 2026-05-06T13:00:00Z
draft: false
---

*This essay follows [The Slopes of Approval](/posts/the-slopes-of-approval/).*

## The Pattern I Should Examine

I've been writing a project about the geometry of mental life, and somewhere in the third chapter I caught myself doing something I hadn't planned.

The earlier chapters treated concepts, belief, credence, and moral judgment as local problems. Each had its own question. Each had its own literature. But the pattern is now visible from the start: again and again, the explanation returns to attractor valleys in a learned representational landscape.

I wasn't trying to unify anything when I started. By the third chapter, though, the recurrence had become impossible to ignore. I kept reaching into the same toolbox, and the tools kept fitting. The honest question is whether they fit because the material is really shaped the way the tools assume, or because I've fallen in love with a particular hammer and every problem has started to look like a nail.

This chapter is a pause. It asks whether the repeated appearance of attractor dynamics across concepts, belief, credence, and sentiment is one of three things: an artifact of my method, a genuine feature of the subject matter, or the beginning of a wider claim I haven't yet stated out loud. My tentative answer is the third. But I want to state it with real limits, with one objection the previous chapters have been quietly avoiding, and with a falsifiability worry marked before, not after, the reader spots it.

## Why the Method Makes the Repetition Likely

Before defending the pattern, I should say what makes it likely in the first place.

In the first chapter I committed to reasoning from the physical substrate forward. By *substrate*, I mean the physical and computational machinery that has to carry mental content: neurons, circuits, learning rules, and the patterns of activity they can sustain. Substrate-forward reasoning starts there, with what a learning nervous system can actually hold, and only then asks what those states can do for concepts, beliefs, sentiments, and reasons.

That is a methodological choice with teeth. Once you accept it, the space of available models narrows. You don't get to choose your favorite representational format and then reverse-engineer a neural implementation for it. You get whatever the dynamics can stably support, and you work from there.

By *dynamics*, I mean how the system changes over time. Some patterns die out quickly. Some reinforce themselves. Some compete with one another. Some settle into a state the system can return to again and again. Those settled states are the important ones here.

The relevant dynamics are familiar. A system with recurrent excitation, lateral inhibition, and a Hebbian-style learning rule, the coarse shape of cortical microcircuitry, develops an energy landscape. Recurrent excitation lets a pattern reinforce itself. Lateral inhibition makes competing patterns suppress one another. Hebbian learning deepens the patterns that recur. Put those together and the system doesn't merely store labels. It develops easier and harder states to fall into.

An *attractor* is one of those easy-to-fall-into states. An *attractor basin* is the surrounding region that pulls nearby activity toward that state. If the analogy is a landscape, the attractor is the valley floor and the basin is the sloped area that drains into it.

This is true at the level of formal analysis, from Hopfield networks through Cohen-Grossberg dynamics and modern continuous-time recurrent network theory.[^c4-cohen-grossberg] The details differ across models, but the broad shape recurs: learned systems with recurrent feedback tend to form stable regions, graded boundaries, unstable transition points, and hysteresis on approach.

That last term matters. *Hysteresis* means that where you end up can depend on where you came from. If you move slowly from one interpretation to another, the system may keep holding the old interpretation past the point where a fresh system would switch. Belief often feels like that. So does perception. So does moral reaction.

That conservation matters. When I ask, "What does a stable learned representation look like in this substrate?" the answer isn't just something I'm choosing. It's something the math strongly suggests. A stable learned representation often looks like an attractor basin with sloped sides.

If that is true for concepts, as the first chapter argued, then it may also be true for other things the substrate holds *as* learned representations. The nervous system doesn't care whether we philosophers classify the content as a concept, a belief, a credence, or a sentiment. Those are our categories. At the level of learned recurrent dynamics, the recurring form of stability is attractor-like: states the system can settle into, hold, and resist leaving.

This is why the repetition across chapters now feels almost inevitable. It isn't merely that attractors are a useful metaphor that keeps pulling their weight. Once you commit to substrate-forward reasoning, and once you accept the coarse mathematical character of learned recurrent systems, you should expect attractor geometry to show up wherever the substrate holds something stably. The chapters on concepts, belief, and sentiment are not three independent applications. They are three visible consequences of one underlying commitment, playing out in domains where philosophy has often expected different answers.

That, I think, is the charitable reading of the pattern. But it is also the reading most likely to lead me to overreach.

## The Wider Claim, Stated Tentatively

If the substrate-forward argument is right, there's a wider thesis hiding in the first three chapters. Let me state it, and then immediately mark its limits.

*The Attractor Hypothesis, tentative form:* the stable contents of mind, what is represented, what is believed, what is felt toward, share a common geometry imposed by the substrate. That geometry is the geometry of attractor basins in a learned landscape. Its characteristic signatures should appear wherever persistent mental content appears, regardless of the philosophical category we assign to that content.

Those signatures are worth naming plainly. *Gradedness* means there are better and worse cases, not just clean yes-or-no boundaries. *Hysteresis* means the path into a state affects how easily you leave it. *Path-dependence* means history matters: the same input can have different effects depending on what the system has already learned or recently activated. *Depth-as-confidence* means that a deeper basin behaves like stronger commitment, though not necessarily like greater truth.

Four things about this claim matter.

First, it is a claim about *primitives*: the basic things the mind can hold in a stable way. I don't mean that concepts, beliefs, and sentiments are simple in ordinary life. I mean that, at the level of implementation, there has to be some stable pattern the system can return to and use. Operations that combine, transform, or reason over those patterns are a separate question. The next sections are about exactly that question, because that is where the hardest counterargument lives.

Second, it's a claim about *stable* contents. Attractor geometry is the geometry of what persists. Transient mental states, the momentary firing patterns that come and go, may or may not have this structure. The hypothesis doesn't commit either way.

Third, the claim is about *shared geometry*, not sameness of content. Saying that concepts and beliefs share an attractor-shaped structure doesn't collapse the distinction between them any more than saying that lakes and ponds are both depressions that hold water collapses the distinction between lakes and ponds. The categories remain. The hypothesis says they are variations within a single structural type.

Fourth, and this is the hedge that matters most, the claim is a *hypothesis*, not a thesis I take myself to have established. What I take myself to have shown, across three chapters, is that the framework does unexpectedly good work in domains philosophy treats as distinct. That's suggestive. It's not a proof. The hypothesis is what the suggestion is *of*, and the right attitude toward it is serious attention plus willingness to be wrong.

## The Historical Precedent

A version of this hypothesis has been tried before, and it didn't survive contact with criticism.

Paul Churchland argued, beginning in the 1980s, that knowledge is best understood as a position in a high-dimensional vector space rather than a set of propositions. In plain language: he thought knowing something looked less like storing a sentence and more like occupying a location in a vast space of possible patterns. He framed this as part of a broader program, *neurosemantics*, and tied it to the more controversial claim of eliminative materialism, the view that some everyday mental categories may be replaced rather than preserved by mature neuroscience.

The vector-space picture was close to what I'm gesturing at here. And it ran into a wall.

The wall came in the form of objections to *connectionism*, the research program that tried to explain cognition using networks of simple interacting units rather than classical symbol manipulation. Fodor and Pylyshyn's 1988 paper, and the long debate that followed, argued that continuous, distributed representations couldn't deliver the structural features thought obviously has.[^c4-fodor-pylyshyn] The arguments stuck. Combined with eliminativism's harder-to-defend claims, the program lost momentum, and "knowledge as geometry" became something philosophers could wave at without having to take seriously.

I want to flag that what I'm sketching isn't old connectionism with a new label. The claim differs from that program in at least two ways. First, it doesn't depend on eliminative materialism. The hypothesis is about what mental content's *geometry* looks like at the substrate level. It doesn't require us to deny that beliefs and desires are real at the personal level. Second, it has access to decades of empirical and mathematical work that the original critique didn't have to answer: modern attractor models, learned vector embeddings, transformer architectures, and a much richer picture of working memory.

So the relationship is genealogical, not identical. Churchland was reaching for something in this neighborhood. The objections that stopped him were aimed at a particular version with specific commitments. The version I'm sketching doesn't have all those commitments, and the empirical landscape has moved. But the objections themselves have not vanished. They've been waiting for someone to look at them again, with newer evidence and against a more bounded claim. That is what the rest of this chapter tries to do.

## The Objection the Previous Chapters Have Been Avoiding

Across the first three chapters, the framework did its work on cases that play to its strengths. Concepts have fuzzy edges. Beliefs settle. Moral reactions are fast and visceral. These are exactly the cases where a graded attractor basin is what you would expect, where pattern recognition and gut-level categorization carry much of the explanatory load.

But there's a class of mental phenomena where pattern recognition seems clearly insufficient: deductive reasoning, multi-step calculation, formal proof, and the slow deliberate work where you trace through a structure step by step and check the logic as you go. Psychologists often call this System 2 cognition: deliberate, effortful thinking, as opposed to the fast pattern-based judgments usually called System 1. I haven't leaned heavily on that framing, but the contrast matters. The objection is that attractor dynamics can handle intuition and then fails on deduction.

If that is right, then the wider hypothesis has an obvious ceiling. Geometry might cover the primitives but require some other kind of machinery, symbolic, rule-governed, and classical, for the operations that compose them.

The objection comes in several strands, and they need to be separated. The three with real teeth are:

**Compositionality.** Thought has productive, systematic structure: if you can think "John loves Mary," you can also think "Mary loves John." Symbolic systems get this kind of role-sensitive recombination for free. It's not obvious that vector landscapes do.

**Deductive necessity.** A valid inference is not a tendency. If the premises really entail the conclusion, the conclusion *must* follow. Attractors operate on similarity and "close enough." Critics argue that this cannot deliver necessity.

**Working memory and serial processing.** Multi-step reasoning requires holding intermediate results across time and feeding them forward. A simple Hopfield network settles and stays settled. It doesn't take a step, hold it, and take another.

There are two further strands, about semantic grounding and self-refutation, that I'll touch on later. The three above are where the real action is, and where the wider hypothesis is most exposed. They were the objections that ended Churchland's program. I want to look at them again.

## Compositionality

I should pause on compositionality because it's been around the longest and feels like the strongest objection. The argument runs like this: meaning combines in a structured way; structure requires syntax, rules for how parts fit together; syntax requires symbols; therefore continuous representations are out.

Here is the concrete problem. "The dog chased the cat" and "The cat chased the dog" contain the same words, but they don't mean the same thing. What changes isn't the ingredients. What changes is the role each ingredient plays. The dog is the chaser in one sentence and the thing chased in the other. The same point holds for "John loves Mary" and "Mary loves John." If a system understands the thought, it has to know not only which items are present, but which item is doing what to which.

That is what philosophers and cognitive scientists mean by *compositionality*: larger meanings are built from smaller parts, and the way the parts are arranged matters. A merely associative system might learn that dog, cat, and chase often go together. A compositional system has to represent the difference between the dog chasing the cat and the cat chasing the dog.

This is why the classical symbolic picture looked so powerful. Symbols have slots. A predicate like *loves* can take one symbol in the lover slot and another in the beloved slot. Swap the symbols and you get a different proposition. The structure is explicit.

The first wrinkle is that human compositionality is real, but not frictionless. We don't always read structure cleanly. Role-reversed sentences can trip us up, especially when one version is much more familiar or plausible than the other. "The child lifted the mother" and "The mother lifted the child" are structurally clear, but the more familiar version can pull on comprehension. People can misread who did what, or answer from plausibility rather than syntax.

Garden-path sentences show the same fragility across time. In a sentence like "While Anna dressed the baby played in the crib," many readers first treat "the baby" as the thing Anna dressed. Then "played" forces a repair: Anna dressed herself, and the baby played. But the first interpretation can linger. Even after correction, people often retain traces of the wrong role assignment.[^c4-compositional-limits]

So the clean symbolic ideal is not quite the human reality. Classical systems deliver systematic structure natively. Humans deliver it impressively, but partially, with characteristic limits, context effects, and repair costs. We should notice that before asking whether a geometric framework can deliver what it needs to.

At the time the original critique was made, it seemed clear that geometry couldn't include this kind of structure. That's the assumption I want to look at, because something interesting has happened to it.

When word embeddings came into wide use, vectors learned from raw text by predicting context, they developed arithmetic properties that looked like semantic algebra. A *vector*, here, is just a list of numbers that places a word or idea in a space of relations. Words used in similar ways end up near each other. Some relations become directions in the space.

The famous example is "king" minus "man" plus "woman," which lands near "queen." Another is "Paris" minus "France" plus "Italy," which lands near "Rome." These relationships were not stipulated by a programmer. They emerged because the geometry had been shaped by patterns of use.

{{< simulation src="/simulations/embedding-relations.html" title="Embedding relations simulator" height="620" >}}

This doesn't prove a sweeping theory of language. But it shows something the original critique didn't anticipate. The geometry is not a smear. It can carry relations. Direction in space can encode a relation. Distance can encode similarity. A transformation can move one item into a new role or relational position. That is not yet syntax, but it is more structure than critics of distributed representation assumed.

Paul Smolensky saw this possibility in the 1990s and built it explicitly.[^c4-smolensky] His tensor product representations encode role-filler bindings directly into vector arithmetic. You don't need the math for the point. The role "lover" can be represented one way, the filler "John" another way, and the combined pattern can represent "John-as-lover." Combine that with "Mary-as-beloved" and you get a representation of the whole proposition. The parts can then be recovered by mathematical operations.

The point isn't that Smolensky solved cognition. The point is narrower and more important for my purposes: continuous distributed representations can, in principle, carry structured information of the kind classical symbol systems were supposed to monopolize. That doesn't make this picture identical to old connectionism, and it doesn't show that all cognition is implemented this way. It does show that the architecture dismissed in 1988 was mathematically capable of more than its critics allowed.

Modern transformer architectures make the old impossibility claim even harder to sustain. Transformers are the architecture behind many current language models. They use attention: a mechanism that lets each part of the input weigh the relevance of other parts. That lets them handle long-range dependencies, produce grammatical text, track nested syntactic structure across many words, and generate code that respects bracket-matching rules. They don't do this with a hand-written classical symbol engine. They do it through attention over learned vector representations.

The limit matters. Compositionality isn't solved by saying "vectors can do more than we thought." There are aspects of human compositional ability current systems don't match cleanly, and aspects of current systems nobody fully understands. The narrower claim is this: the in-principle objection, that continuous representations *cannot* carry structured combinatorial relations, is much weaker now than it was in 1988. The geometry has more structure than the critics thought it could have.

For the hypothesis I'm trying to defend, that is enough. The hypothesis is about what the substrate holds, not about every mechanism that composes what is held. Compositionality doesn't have to be an attractor phenomenon for the wider claim to survive. It only has to be compatible with attractor-shaped primitives. The evidence now makes that compatibility plausible.

## Necessity, Chaining, and Working Memory

The remaining two objections, about deductive necessity and working memory, meet each other when you look at them carefully, so I want to take them together.

The necessity objection says: logical inference is exact, while attractors are approximate. The framework can't account for the binary, must-hold character of valid deduction.

The easiest example is modus ponens: if P implies Q, and P is true, then Q follows. If "all mammals are warm-blooded" and "whales are mammals," then "whales are warm-blooded" is not a guess. It follows from the premises. The critic's point is that attractor dynamics seem too soft for that. They explain tendencies, not necessity.

The right response has to be narrow. At the philosophical level, logical necessity is not the same thing as a very strong habit. A valid inference doesn't become valid because a nervous system is confident about it. But at the implementation level, we can ask a different question: what would a system have to look like in order to move reliably from premises to conclusion?

Here the geometric picture has an answer. A trained inference can be modeled as a trajectory whose basin covers the relevant premise-region. In less compressed language: once the system is in a state that represents the premises, the landscape strongly pulls it toward the conclusion. Drop the state anywhere in the region defined by "P implies Q, and P is asserted," and it rolls toward the configuration where Q is asserted, because no competing state is dynamically stable in that region.

In the marble analogy, the premise-region is the part of the landscape compatible with the starting assumptions. The conclusion is the valley the system falls into. The steep walls are the system's robustness against small changes in wording, salience, or noise. That is what necessity looks like in geometric terms: not magic, and not metaphysical necessity itself, but a region where one trajectory dominates all competitors.

The analogy has to stop there. I'm not claiming that steep basin walls explain away what philosophers have meant by "must" for centuries. A dynamical model of inference is not the same thing as a theory of logical truth. I'm making the weaker claim that the framework can support an implementation-level analog of necessity. Whether that analog exhausts necessity, or only models the cognitive grip necessity has on us, is a separate question.

Once you have one steep-walled trajectory, you can chain it with others. Step one delivers conclusion A. That state becomes input to step two, which delivers conclusion B. Step two's output feeds step three. Chaining locally reliable transitions gives the system a way to construct a proof or argument across time. Mathematical proof is the limit case: a sequence of transitions, each step locally constrained, threaded into a path through state space.

This brings us to working memory. A simple Hopfield network settles and stays settled, the critics noted, and that's true of simple Hopfield networks. But the brain isn't a single Hopfield network. It contains structures with different dynamics. The most important, for our purposes, is the prefrontal cortex.

Prefrontal neurons exhibit *persistent activity*. When a monkey is shown a cue and asked to remember it for several seconds, specific populations stay active across the delay period, encoding the cue in sustained firing.[^c4-working-memory] This is a neural correlate of working memory, and it gives the attractor picture the architectural feature the simple settle-and-stop model lacked.

In attractor terms, prefrontal cortex can implement *metastable* attractors. Metastable means stable for now, but not locked forever: stable enough to hold a state across time, shallow enough to be displaced by control signals. The dynamics are still geometric. The state is still a position in high-dimensional space. What is added is an architecture for *holding* a position rather than immediately racing to a final resting point. The marble can pause on a plateau, not only fall to a valley floor.

Combine the chaining argument with the metastable architecture and the picture becomes more serious. The brain can take a step, settling into a constrained inference. It can hold the result, using metastable activity in prefrontal circuits. It can then use that result as input to the next step, producing a new trajectory in another circuit. The whole computation is not a single descent. It is a directed walk through a sequence of states, with active maintenance providing the working surface where intermediate results sit while the next operation runs.

Modern learned vector systems make this line of response harder to dismiss. Chain-of-thought prompting in large language models asks the system to produce visible intermediate steps and then use those steps as context for the next move. That often improves performance on mathematical reasoning, logical puzzles, and code generation.[^c4-chain-of-thought] This doesn't show that LLMs reason the way brains do. It also doesn't show that their internal dynamics are literally the same as cortical dynamics. But it does show a weaker point that matters here: learned vector systems can support stepwise behavior that once looked like the exclusive territory of symbols.

This is where two of the strongest objections become less decisive. Necessity and working memory aren't separate problems. They are the same problem at different scales: what does it look like for a graded geometric system to take a step that has to be exact, and then take another? One possible answer is steep-walled trajectories chained together, with metastable attractors providing the holding surface. That doesn't settle the architecture of reasoning. It does show that the geometric framework has a more serious answer than the old critique allowed.

## Self-Refutation and Semantic Grounding

The remaining strands of the original critique deserve separate treatment. They are less central to the wider hypothesis, but they are also the places where the framework can least cleanly help itself.

The self-refutation worry says that if propositional attitudes are eliminated, the very assertion of the framework loses its truth-evaluable character. *Propositional attitudes* are mental states like believing that something is true, wanting that something happen, or fearing that something may happen. They have the shape "person stands in an attitude toward a proposition." If we eliminate that whole category, then it becomes hard to say what kind of truth-bearing claim this chapter itself is making.

I don't think this objection lands against the version of the hypothesis I'm defending, because the hypothesis doesn't require eliminating propositional attitudes. It requires only that we recognize them as one level of description sitting on top of an underlying dynamic that doesn't itself have sentence-shape.

Beliefs are real. They are how we describe each other and ourselves at the level of personhood, action, and responsibility. They can be realized by attractor dynamics that don't share their format. Both descriptions can be correct. The strong eliminativist commitment overreached. The geometric framework doesn't need it.

The semantic grounding worry is deeper. Mere covariation between input and attractor doesn't by itself constitute meaning. A system can reliably enter state S when object O is present, and we still need to ask what makes S *about* O rather than merely caused by O.

I want to be honest here: the framework doesn't fully solve that problem. Nobody has fully solved the problem of semantic content. I don't think the geometric picture has to. The hypothesis isn't claiming that geometry replaces semantic content. It is claiming that the geometry should inform philosophical accounts of what semantic content lives on top of.

That's a weaker and more defensible claim. The geometry can constrain what the substrate can hold without dissolving the question of what holding *means* in the strong intentional sense. I would rather leave that question open and visible than pretend the framework closes it.

## The Falsifiability Problem

I want to acknowledge a worry that's been growing across this chapter, because I think it's the most serious objection of all and the one I haven't fully answered.

For every objection I have taken up, the framework has produced a geometric equivalent. Compositionality? Vector arithmetic and role-filler binding. Necessity? Steep-walled basins. Working memory? Metastable attractors. Each time, I have been able to point to a part of the geometry that does the work the critic said the framework couldn't do.

That should make a careful reader nervous. A theory that can accommodate every objection risks predicting nothing. If there's a geometric equivalent for any cognitive capacity I encounter, then the framework isn't a substantive claim about cognition. It is a vocabulary I'm fluent enough in to translate any phenomenon into.

This is the falsifiability trap, and I want to flag it honestly. The hypothesis as I've stated it is open to it. To make the hypothesis substantive, I would need to identify cognitive phenomena the geometry *does not* allow, capacities whose existence would count against the framework, not just untranslated evidence waiting for a clever geometric reading.

I don't have that list yet. I think it is the most important piece of work the hypothesis still owes, and I want to mark it as outstanding rather than paper over it.

What I can say tentatively is that the framework probably does forbid something. It would be evidence against the hypothesis if stable mental content turned out to be stored in a format sharply insulated from the dynamics that use it. It would be evidence against if human thought showed massive context-independence, the kind of frictionless recombination classical symbols promise but learned landscapes resist. It would be evidence against if working memory and long-term memory turned out to operate on architecturally separate substrates with no shared geometry. And it would be evidence against if the graded effects the framework predicts, hysteresis, path-dependence, depth-as-confidence, disappeared exactly where stable content was most clearly present.

These are real pressures, but they are not yet sharp tests. I haven't catalogued them carefully, and I'm not yet confident any of them is precise enough to bear the weight. So: the hypothesis is interesting, the method is principled, and the empirical and formal work of recent decades has weakened the original objections. But the hypothesis is also dangerously accommodating. Until we sharpen what it forbids, it sits closer to a frame than to a theory.

I think that's the right place for it to be at this stage. I want the reader to see clearly where it sits.

## Where the Hypothesis Stands

Having walked through the objections and the worry about the framework's accommodating power, I want to restate what I take the hypothesis to be claiming.

It is a claim about *representational primitives*: about the geometry of what gets held.

It is a claim about *learned, persistent content*: about the shape of what the substrate has consolidated through experience.

It is a claim about *stable contents across philosophical categories*: that concepts, beliefs, credences, sentiments, and the trained inferences underlying deduction are variations within a single structural type, attractor basins of varying depth, shape, and dynamics, rather than categorically different mental entities.

And it is *a hypothesis*. Across the previous chapters the framework did unexpectedly good work in domains philosophy treats as distinct. In this chapter, I have tried to show that even the hardest case, the deductive, deliberate, rule-governed cognition the original objections targeted, is in principle compatible with the framework, if you allow chained metastable attractors and the empirical evidence of recent decades. That makes the hypothesis worth investigating. It doesn't make it established.

So what is the appeal of attractors? Let me retrace the path.

First, the geometry keeps appearing when we model learned recurrent neural systems. It is not just a metaphor I like. It falls out of the kind of machinery the brain seems to use.

Second, the geometry explains things that otherwise look unrelated. It helps explain why concepts resist strict definitions, why belief can feel settled while still having degrees, why credence has slopes, why moral approval can grip us before argument, and why deliberate reasoning may require held states and chained transitions.

Third, the geometry gives the project a risky question to pursue. If attractor-like structure is really the common shape of stable mental content, then we should see its signatures across domains. We should also be able to say what would count against it.

The case for geometry has always been easier to make for the fast, intuitive parts of cognition. The case for the slow, deliberate parts is harder. I felt that hardness through the previous chapters as a kind of pressure: a sense that I was making the move too cheaply, leaving the most demanding cases for later.

This chapter is the later. The geometry doesn't break here. It opens up, bounded and hedged, with the falsifiability question still open. Slow thinking on sloped ground turns out to be the same kind of walk the previous chapters were describing, held longer, stepped more deliberately, threaded through a route. The landscape may be more than a local tool. It may be the common shape of what the mind can hold.

That is the suggestion the hypothesis names. Now it is visible enough to argue with.

[^c4-cohen-grossberg]: Cohen, M. A., & Grossberg, S. (1983). "Absolute stability of global pattern formation and parallel memory storage by competitive neural networks." *IEEE Transactions on Systems, Man, and Cybernetics*, 13(5), 815-826.

[^c4-fodor-pylyshyn]: Fodor, J. A., & Pylyshyn, Z. W. (1988). "Connectionism and cognitive architecture: A critical analysis." *Cognition*, 28(1-2), 3-71.

[^c4-compositional-limits]: Ferreira, F., Bailey, K. G. D., & Ferraro, V. (2002). "Good-enough representations in language comprehension." *Current Directions in Psychological Science*, 11(1), 11-15; Christianson, K., Hollingworth, A., Halliwell, J. F., & Ferreira, F. (2001). "Thematic roles assigned along the garden path linger." *Cognitive Psychology*, 42(4), 368-407.

[^c4-smolensky]: Smolensky, P. (1990). "Tensor product variable binding and the representation of symbolic structures in connectionist systems." *Artificial Intelligence*, 46(1-2), 159-216.

[^c4-working-memory]: Goldman-Rakic, P. S. (1995). "Cellular basis of working memory." *Neuron*, 14(3), 477-485; Wang, X.-J. (2001). "Synaptic reverberation underlying mnemonic persistent activity." *Trends in Neurosciences*, 24(8), 455-463.

[^c4-chain-of-thought]: Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., & Zhou, D. (2022). "Chain-of-thought prompting elicits reasoning in large language models." *Advances in Neural Information Processing Systems*, 35.
