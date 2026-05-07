---
title: "The Attractor Hypothesis"
date: 2026-05-06T13:00:00Z
draft: false
---

*This essay follows [The Slopes of Approval](/posts/the-slopes-of-approval/).*

## What the Pattern Is

Three chapters in, the same shape kept appearing. The chapter on concepts described basins of attraction in a learned representational landscape: sloped sides, fuzzy edges, deeper for prototypes. The chapter on belief recovered the same geometry under a different label. Continuous credences that feel categorical when the system settles. Hysteresis around interpretive switches. Paths into a state mattering for how easily you can leave it. The chapter on moral sentiment did it again. Approval and disapproval as basins. Dilemmas as saddle points where two basins compete. The systematizing impulse of normative theory pushing against terrain that won't hold neat partitions.

I wasn't planning a unified framework when I started. The recurrence happened. By the third chapter, the same toolbox was being reached for, and the tools kept fitting, and the honest question is whether they fit because the material is really shaped the way the tools assume, or because I've fallen in love with a hammer and every problem has started to look like a nail.

There are three readings of what's happening. It could be an artifact of method: a commitment to thinking from the substrate forward might find attractor geometry whatever it's pointed at. It could be a real feature of the material: stable mental content really has this shape, and the chapters are showing the same fact from different angles. Or it could be the beginning of a wider claim, one I haven't stated out loud yet, that mental life has a common geometry inherited from the substrate, and the philosophical categories I've been treating one at a time are variations within a single structural type.

My tentative answer is the third. The hypothesis has to be stated carefully, with real limits, with one objection the previous chapters quietly avoided taken seriously, and with the falsifiability worry that's been growing the whole time flagged early.

## Why the Method Predicts the Recurrence

In the first chapter I committed to substrate-forward reasoning, and that commitment has consequences. By *substrate*, I mean the physical and computational machinery any mental content has to be carried by: neurons, synapses, learning rules, circuits, or some future techonology or alien biology. Any substrate will accomodate mechanisms, a the patterns of activity,. Substrate-forward reasoning starts there and only then asks what such patterns can do for concepts, beliefs, sentiments, and reasons.

Once that choice is made, the space of available models narrows. You don't get to pick your favorite representational format and then reverse-engineer a neural implementation for it. You get whatever the they can stably support, and you work from there.

By *dynamics*, here, I mean how the system changes over time. Some patterns die out. Some reinforce themselves. Some compete. Some settle into a state the system can return to and hold. Those settled states are the ones that matter.

A nervous system with recurrent excitation, lateral inhibition, and a Hebbian-style learning rule (the coarse architecture of cortical microcircuitry) develops what mathematicians call an energy landscape. Recurrent excitation lets a pattern reinforce itself. Lateral inhibition makes competing patterns suppress one another. Hebbian learning deepens the patterns that recur. Put those together and the system stops being a passive store. It becomes terrain with easier and harder states to fall into.

An *attractor* is one of those easy-to-fall-into states. An *attractor basin* is the surrounding region that pulls toward that state. If the picture is a landscape, the attractor is the valley floor and the basin is the sloped region around it.

This is true in the formal mathematics, from Hopfield networks through more elaborate recurrent models to modern continuous-time network theory.[^c4-cohen-grossberg] The details differ across models. The broad shape recurs: learned recurrent systems develop stable regions, graded boundaries, unstable transition points, and hysteresis on approach.

That last term is worth a beat. *Hysteresis* means where you end up depends on where you came from. Move slowly from one state to another and the system can hold the old state past the point where a fresh system would switch. Belief feels like that. So does perception. So does moral sentiment.

So when I ask, "what does a stable learned representation look like in this substrate?", the answer isn't just something I'm choosing. It's something the math suggests strongly. A stable learned representation tends to look like an attractor basin with sloped sides.

If that holds for concepts, it should hold for whatever else the substrate carries as a learned representation. The system doesn't care whether we philosophers classify the content as a concept, a belief, a credence, or a sentiment. Those are our categories. At the level of learned recurrent dynamics, the recurring form of stability is attractor-shaped.

This is why the recurrence across chapters now feels close to inevitable. The chapters on concepts, belief, and sentiment aren't three independent applications of a shared metaphor. They're three visible consequences of one substrate-level commitment, playing out in domains philosophy has often expected to look different.

That's the charitable reading. It's also the reading most likely to lead me into overreach.

---

## The Hypothesis, Stated

*The Attractor Hypothesis, tentative form:* the stable contents of mind, what is represented, what is believed, what is felt toward, share a common geometry imposed by the substrate. That geometry is the geometry of attractor basins in a learned landscape. Its characteristic signatures should appear wherever persistent mental content appears, regardless of the philosophical category we assign to that content.

Those signatures are worth naming plainly. *Gradedness* means there are better and worse cases, not clean yes-or-no boundaries. *Hysteresis* means the path into a state affects how easily you leave it. *Path-dependence* means history matters: the same input has different effects depending on what the system has already learned or recently activated. *Depth-as-confidence* means a deeper basin behaves like stronger commitment, though not necessarily like greater truth.

Four things about this claim narrow what's being said.

First, the claim is about *primitives*. By that I mean the basic things the mind can hold in a stable way. Concepts, beliefs, and sentiments are not simple in ordinary life. The point is that, at the level of implementation, there has to be some pattern the system can return to and use. Operations that compose, transform, or reason over those patterns are a separate question, and the rest of this chapter has to do its work there, because that's where the hardest counterargument lives.

Second, the claim is about *stable* contents. Attractor geometry is the geometry of what persists. Transient firing patterns that come and go may or may not have this structure. The hypothesis takes no position there.

Third, the claim is about *shared geometry*, not sameness of content. Saying that concepts and beliefs share an attractor-shaped structure no more collapses the distinction between them than saying lakes and ponds are both depressions that hold water collapses the distinction between lakes and ponds. The categories survive. The hypothesis says they're variations within a single structural type.

Fourth, what's being offered is a hypothesis, not a thesis I take to have been established. Across three chapters the framework did unexpectedly good work in domains philosophy treats as distinct. That's suggestive. It isn't a proof. The hypothesis is what the suggestion is *of*, and the right attitude toward it is serious attention plus willingness to be wrong.

## A Version of This Has Been Tried

Something close to this hypothesis was attempted in the 1980s and didn't survive contact with criticism.

Paul Churchland argued, beginning around then, that knowledge is best understood as a position in a high-dimensional vector space rather than a set of propositions. In plain language: knowing something looks less like storing a sentence and more like occupying a location in a vast space of possible patterns. He framed this as part of a broader program, *neurosemantics*, and tied it to the more controversial claim of *eliminative materialism*, the view that some everyday mental categories may be replaced rather than preserved by mature neuroscience.

The vector-space picture was close to what I'm sketching here. And it ran into a wall.

The wall came in the form of objections to *connectionism*, the research program that tried to explain cognition with networks of simple interacting units rather than classical symbol manipulation. Fodor and Pylyshyn's 1988 paper argued, with considerable force, that continuous distributed representations couldn't deliver the structural features thought obviously has.[^c4-fodor-pylyshyn] The arguments stuck. Combined with eliminativism's harder-to-defend claims, the program lost momentum, and "knowledge as geometry" became a position philosophers could wave at without taking seriously.


The version sketched here isn't old connectionism with a new label. It differs from Churchland's program in at least two ways. It doesn't depend on eliminative materialism. The claim is about the geometry of what the substrate carries, not about whether beliefs and desires are real at the level of personhood. And it has access to decades of empirical and mathematical work the original critique didn't have to answer: modern attractor models, learned vector embeddings, transformer architectures, a much richer picture of working memory.

The relationship is genealogical, not identical. Churchland was reaching for something in this neighborhood. The objections aimed at his version had specific targets, and the version sketched here doesn't have all those targets. The objections themselves haven't gone away, though. They've been waiting for someone to look at them again with newer evidence and a more bounded claim. That's what follows.

---

## The Objection the Easy Cases Hid

Concepts have fuzzy edges. Beliefs settle. Moral reactions are fast and visceral. These are exactly the cases pattern recognition handles well, and exactly the cases where a graded basin is what you'd expect. The framework I've been building handles them.

But there's a class of mental phenomena where pattern recognition seems clearly insufficient. Carrying the 2 in long division. Tracing a proof one step at a time, holding the intermediate result before applying the next operation. Checking whether an argument is valid by inspecting its structure rather than by feeling whether it sits right. Kahneman and Tversky called this kind of work *System 2*, in contrast to the fast pattern-based judgments they called System 1. The framework is comfortable with System 1. The objection is that it fails on System 2.

If that's right, the wider hypothesis has a ceiling. Geometry might cover the primitives but require a different kind of machinery, symbolic and rule-governed, for the operations that combine them.

The objection comes in several strands. The three with real teeth are these.

**Compositionality.** Thought has productive, systematic structure. If you can think "John loves Mary," you can think "Mary loves John." Symbolic systems get this kind of role-sensitive recombination for free. It isn't obvious that a geometry can produce that.

**Necessity.** A valid inference isn't a tendency. If the premises really entail the conclusion, the conclusion *must* follow. Attractors operate on similarity and "close enough." Critics argue this can't deliver necessity.

**Working memory and serial processing.** Multi-step reasoning requires holding intermediate results across time and feeding them forward. A simple Hopfield network settles and stays settled. It doesn't take a step, hold it, and take another.

Two further strands, about self-refutation and semantic grounding, get separate treatment later. The first dissolves once levels of description are kept distinct. The second is older than this framework and won't be settled by it. The three above are where the action is, and where the wider hypothesis is most exposed. They were the objections that ended Churchland's program.

## Compositionality in the Geometry

A *proposition* is a structured claim, like "the dog chased the cat," that says one thing of another in a particular way. Propositions have parts, and the parts are arranged according to a relation. *Compositionality* is the observation that the same relation can be filled with different parts to produce different propositions, and that this kind of recombination is what makes thought productive. Once you have "X chased Y," you have "the dog chased the cat" and "the cat chased the dog" and a thousand others, because the relation is one mechanism reused across an open-ended set of fillers.

The mechanism is recursive too. The output of one composition can be slotted in as the input of another. "If the dog chased the cat, the cat ran." Once the relation is in hand, it can be nested inside itself.

This is why the classical symbolic picture looked so powerful. A relation defined as a slot-and-filler structure handles every filler the same way. Define *loves* once, and "John loves Mary," "Mary loves John," "prince loves princess," and "king loves queen" all come for free. The same mechanism produces all of them, and the part of the system that does the producing doesn't have to know anything about kings or princes.

Geometry is where the difficulty bites. If "the dog chased the cat" is a position in a high-dimensional space, then "the cat chased the dog" is a different position. "John loves Mary" is somewhere else. "King loves queen" is somewhere else again, and "prince loves princess" somewhere else still. Nothing about the geometry obviously says these positions are produced by a shared mechanism. Each filler-pair lands in its own region, and the space doesn't come pre-equipped with the kind of slot that lets one operation handle every binding the way a symbolic predicate does.

Two things complicate the clean symbolic story before any reply gets started. First, human compositionality is real but not frictionless. We don't always read structure cleanly. "The mother lifted the child" and "The child lifted the mother" are structurally clear, but the more familiar version pulls on comprehension. People can misread who did what, or answer from plausibility rather than from syntax. Second, garden-path sentences show the same fragility across time. "While Anna dressed the baby played in the crib" trips many readers the first time through, with "the baby" first read as the thing Anna dressed and only later repaired. The wrong role assignment can linger after correction.[^c4-compositional-limits] So before asking whether the geometric framework can deliver compositionality, it's worth noticing that what humans actually deliver is partial, context-sensitive, and prone to characteristic failures.

At the time of the original critique, it seemed clear that geometry couldn't carry this kind of structure at all. Something interesting has happened to that assumption.

When word embeddings came into wide use (vectors learned from raw text by predicting context), they developed arithmetic properties that look like semantic algebra. A *vector*, here, is just a list of numbers placing a word in a space of relations. Words used in similar ways end up near each other. Some relations become directions in the space.

The famous example is "king" minus "man" plus "woman," which lands near "queen." Another is "Paris" minus "France" plus "Italy," which lands near "Rome." The relationships weren't stipulated. They emerged because the geometry was shaped by patterns of use.

{{< simulation src="/simulations/embedding-relations.html" title="Embedding relations simulator" height="620" >}}

This doesn't prove a sweeping theory of language. But it shows something the original critique didn't anticipate. Direction in space can encode a relation. Distance can encode similarity. A transformation can move a vector into a new role or relational position. None of that is yet syntax. All of it is more structure than critics of distributed representation assumed was available.

Paul Smolensky saw this possibility in the 1990s and built it explicitly.[^c4-smolensky] His tensor product representations encode role-filler bindings directly into vector arithmetic. You don't need the math for the point. The role "lover" can be represented one way, the filler "John" another way, and the combined pattern can represent "John-as-lover." Combine that with "Mary-as-beloved" and you get a representation of the whole proposition. The parts can then be recovered by mathematical operations.

The point isn't that Smolensky solved cognition. The narrower point is what matters here: continuous distributed representations can carry structured information of the kind classical symbol systems were supposed to monopolize. The architecture dismissed in 1988 was mathematically capable of more than its critics allowed.

Modern transformer architectures make the in-principle objection even harder to sustain. Transformers (the architecture behind contemporary language models) use *attention*, a mechanism that lets each position in the input weigh the relevance of every other position. They handle long-range dependencies, produce grammatical text in dozens of languages, track nested syntactic structure across many words, and generate code that respects bracket-matching rules. None of this is done by a hand-written symbol engine. It's done by attention over learned vector representations.

The hedge matters. Compositionality isn't solved by saying "vectors carry more structure than we thought." There are aspects of human compositional ability that current systems don't match cleanly, and aspects of current systems that nobody fully understands. The narrower claim is what survives: the in-principle objection, that continuous representations *cannot* carry structured combinatorial relations, is much weaker now than it was in 1988.

For the hypothesis being defended here, that's enough. The hypothesis is about what the substrate holds, not about every mechanism that composes what is held. Compositionality doesn't have to be an attractor phenomenon for the wider claim to survive. It only has to be compatible with attractor-shaped primitives. The evidence makes that compatibility plausible.

## Necessity as a Topological Feature

Take modus ponens. If "all mammals are warm-blooded" and "whales are mammals," then "whales are warm-blooded" isn't a guess. It follows from the premises. The critic's claim is that attractor dynamics, which are graded and similarity-based, are too soft to deliver a move like that. Logic is exact. Attractors are not. So a geometric framework can explain category fuzziness but not deductive necessity.



The right response has to be careful about levels. At the philosophical level, logical necessity isn't a very strong habit. A valid inference doesn't become valid because a nervous system is confident about it. The relation between premises and conclusion is what it is whether anything ever computes it. But at the implementation level, a different question is available: what would a system have to look like in order to move reliably from premises to conclusion?

Here the geometric picture has an answer. A trained inference can be modeled as a trajectory whose basin covers the relevant premise-region. In less compressed form: once the system is in a state representing the premises, the landscape pulls it toward the conclusion. Drop the state anywhere in the region defined by "P implies Q, and P is asserted," and it rolls to the configuration where Q is asserted, because no competing state is dynamically stable in that region.

The marble picture is concrete. The premise-region is the part of the landscape compatible with the starting assumptions. The conclusion is the only valley that part of the landscape drains into. The walls of that valley are steep enough that no small perturbation in the relevant region pushes the marble somewhere else. That's what necessity looks like in geometric terms: a topological fact about a region where one trajectory dominates all competitors.

The analogy has to stop somewhere. Steep basin walls don't explain away what philosophers have meant by *must* for centuries. A dynamical model of inference is not a theory of logical truth. The narrower claim is that the framework can support an implementation-level analog of necessity. Whether that analog exhausts necessity, or only models the cognitive grip necessity has on us, is a separate question that doesn't need to be settled here.

Once you have one steep-walled trajectory, you can chain it with others. Step one delivers conclusion A. That state becomes input to step two, which delivers conclusion B. Step two's output feeds step three. Chaining locally reliable transitions gives the system a way to construct a proof or argument across time. Mathematical proof is the limit case: a sequence of transitions, each step locally constrained, threaded into a path through state space.

That brings us to working memory.

---

## Working Memory as the Holding Surface

When a monkey is shown a cue and then asked to remember it for several seconds before responding, specific populations of neurons in its prefrontal cortex stay active across the entire delay period, encoding the cue in their sustained firing.[^c4-working-memory] The activity doesn't decay back to baseline the way most cortical responses do. It persists, holding the information online, until it's used or replaced. Goldman-Rakic's group documented this in the 1990s; Wang and others traced it to recurrent excitation in cortical microcircuits. *Persistent activity* is the neural correlate of working memory, and it's exactly the architectural feature the simple settle-and-stop model didn't have.


In attractor terms, prefrontal cortex implements *metastable* attractors: stable enough to hold a state across time, shallow enough to be displaced by control signals when the next operation is ready. The dynamics are still geometric. The state is still a position in high-dimensional space. What's added is an architecture for *holding* a position rather than racing to a final resting point. The marble can pause on a plateau.

Combine the metastable architecture with the chaining argument from the previous section and the picture starts to handle multi-step reasoning. The brain takes a step, settling into a constrained inference. It holds the result, using metastable activity in prefrontal circuits. It uses that result as input to the next step, producing a new trajectory in another circuit. The whole computation is a directed walk through a sequence of states, with active maintenance providing the holding surface where intermediate results sit while the next operation runs.

Modern learned vector systems make this story even harder to dismiss. *Chain-of-thought prompting* asks a large language model to produce visible intermediate steps and then use those steps as context for what comes next.[^c4-chain-of-thought] On a math word problem like "Roger has 5 tennis balls; he buys 2 cans with 3 balls in each; how many tennis balls does he have now?", a chain-of-thought response writes out something like "5 + (2 × 3) = 11" before answering. That visible scratchpad measurably improves performance on tasks that require holding intermediate state. None of this shows that LLMs reason the way brains do. It also doesn't show that their internal dynamics literally match cortical dynamics. It shows the weaker point that matters here: learned vector systems can support stepwise behavior that once looked like the exclusive territory of symbols.

So the strongest two objections, necessity and working memory, turn out to be the same problem at different scales. What does it look like for a graded geometric system to take a step that has to be exact, and then take another? One available answer: steep-walled trajectories chained together, with metastable attractors providing the holding surface. That doesn't settle the architecture of reasoning. It does show the geometric framework has a more serious answer than the original critique allowed.

The framework also doesn't end at the skull. When the problem outruns what a language model can keep in flowing text, modern systems don't push harder against their internal capacity; they call a tool. Run this code. Compute this expression. Query this database. The model writes the request, the tool returns the result, and the model carries the answer forward. The internal state never has to keep all the intermediate work present at once.

Humans do the same thing, and have always done it. When I don't trust myself to hold a long division in working memory, I reach for a pen. The pen-and-paper version isn't a different kind of reasoning. It's the same architecture extended onto a more reliable substrate. The brain holds the current step. The page holds the prior steps. The page does the work the metastable attractor was doing inside, only steadier and for longer. Mathematicians use blackboards. Programmers use REPLs. Accountants used ledgers before they used spreadsheets. The principle is the same in each case: offload what working memory can't carry, and keep in mind only what the next step needs.

This isn't a defeat of the geometric framework. It's a sketch of how the framework scales. Short reasoning chains are handled by the internal dynamics directly. Longer chains externalize intermediate state to a more durable substrate, the way models use tools and the way we use paper.

## Levels and the Hard Remainder

A reader might worry that any account claiming "beliefs are really just attractor states" saws off the branch it sits on. If beliefs aren't really beliefs, what is the chapter's claim, and how could it be true?

The worry has force only if the geometric story is meant to replace the language of beliefs and reasons rather than sit beneath it. It isn't. Different levels of description can be true at the same time, and a description at one level doesn't cancel a description at another. A chess game can be wood pieces on a board, a contest between two players, and a position with a forced win in three. None of those descriptions undoes the others. The level at which I say "I believe my keys are in the kitchen" sits above, not against, the level at which my brain implements that belief in dynamics that don't themselves have sentence-shape. The chapter's claim can be evaluated as a claim because we still have the level where claims live.

That move resolves the lighter version of the worry. The heavier version is something else.

Semantic grounding is the harder remainder. Mere covariation between input and attractor doesn't by itself constitute meaning. A system reliably enters state S when object O is present, and there is still a real question about what makes S *about* O rather than merely caused by O. This is not a problem the geometric framework fails to solve. It's a problem nothing has solved. Brentano framed a version of it. Husserl framed another. Quine, Putnam, Dretske, Millikan, and many others have circled it for the better part of a century without converging. There's a real possibility the question is poorly formulated, that the clean separation between representational vehicle and represented content it presupposes won't survive close inspection.

What I want to say plainly is that a better picture of the substrate doesn't, by itself, dissolve this question. Knowing more about the geometry of stable mental states tells us about the format of what mind carries. It doesn't tell us how that carrying works in the strong intentional sense. That isn't a gap the geometric framework owes a fix for. It's the limit of what substrate-forward reasoning can address from below. The question may need to be reformulated before any framework, geometric or otherwise, can claim to answer it. Until then, the honest move is to leave it visible.


## The Worry I Haven't Answered

Notice what just happened across the last several sections. For almost every objection the framework had a geometric reply ready. Compositionality? Vector arithmetic and role-filler binding. Necessity? Steep-walled trajectories. Working memory? Metastable attractors. Self-refutation? Levels of description. Semantic grounding was the exception, and the framework didn't pretend otherwise.

But that's a thin exception. A theory that absorbs every objection except one acknowledged-as-open question risks predicting nothing in the domain it does cover. If there's a geometric translation for any cognitive capacity I encounter, then the framework isn't a substantive claim about cognition. It's a vocabulary I'm fluent enough in to translate any phenomenon into.

This is the falsifiability trap, and the hypothesis as stated is open to it. To make it substantive, I'd need to identify cognitive phenomena the geometry *does not* allow. Capacities whose existence would count against the framework rather than waiting to be retranslated. I don't have that list yet. It's the most important piece of work the hypothesis still owes, and it belongs visible rather than papered over.

What can be said tentatively is that the framework probably forbids something. It would be evidence against the hypothesis if stable mental content turned out to be stored in a format insulated from the dynamics that use it. It would be evidence against if human thought showed the kind of frictionless, fully context-independent recombination classical symbols promise but learned landscapes resist. It would be evidence against if working memory and long-term memory operated on architecturally separate substrates with no shared geometry. And it would be evidence against if the graded effects the framework predicts (hysteresis, path-dependence, depth-as-confidence) disappeared exactly where stable content was most clearly present.

These are real pressures. They aren't yet sharp tests. None has been worked out carefully enough that the framework could be staked on it failing. So: the hypothesis is interesting, the method is principled, and the empirical and formal work of recent decades has weakened the original objections. The hypothesis is also dangerously accommodating. Until what it forbids is sharpened, it sits closer to a frame than to a theory.

That's the right place for it at this stage, and it belongs sitting there in plain view.

---

## Where the Hypothesis Stands

Stable mental contents (concepts, beliefs, credences, sentiments, the trained inferences underlying deduction) share a common geometry imposed by the substrate, and that geometry is the geometry of attractor basins in a learned landscape. The signatures are gradedness, hysteresis, path-dependence, and depth-as-confidence. The claim is about *primitives* and about *stable* content. It is a claim about *shared geometry*, not sameness of content. It is a hypothesis, not an established thesis.

Three things make it worth taking seriously now.

First, the geometry isn't a metaphor I happen to like. It falls out of the kind of machinery the brain seems to use. Recurrent excitation, lateral inhibition, and Hebbian-style learning produce attractor landscapes; that's a mathematical fact, not a stylistic preference. When attractors keep showing up in domains philosophy treats as different, the recurrence has a substrate-level reason.

Second, the geometry pulls together things that otherwise look unrelated. It explains why concepts resist strict definitions, why belief can feel settled while still admitting degrees, why credence has slopes, why moral approval can grip us before argument shows up, and why deliberate reasoning seems to require held states and chained transitions.

Third, the geometry gives the project a risky question to keep working on. If attractor-like structure is really the common shape of stable mental content, its signatures should appear across domains, and we should be able to say what would count against the claim. Sharpening that, turning the framework into a theory by identifying what it forbids, is what the hypothesis still owes.

The case for geometry has always been easier to make for the fast, intuitive parts of cognition. The case for the slow, deliberate parts has been harder, and that hardness was real pressure across the previous chapters: a sense that the move was being made too cheaply, with the most demanding cases left for later.

This was the later. The geometry doesn't break here. It opens up, bounded and hedged, with the falsifiability question still open. Slow thinking on sloped ground turns out to be the same kind of walk the previous chapters were describing, held longer, stepped more deliberately, threaded through a route. The landscape may be more than a local tool. It may be the common shape of what the mind can hold.

That's the suggestion the hypothesis names. It's now visible enough to argue with.

[^c4-cohen-grossberg]: Cohen, M. A., & Grossberg, S. (1983). "Absolute stability of global pattern formation and parallel memory storage by competitive neural networks." *IEEE Transactions on Systems, Man, and Cybernetics*, 13(5), 815-826.

[^c4-fodor-pylyshyn]: Fodor, J. A., & Pylyshyn, Z. W. (1988). "Connectionism and cognitive architecture: A critical analysis." *Cognition*, 28(1-2), 3-71.

[^c4-compositional-limits]: Ferreira, F., Bailey, K. G. D., & Ferraro, V. (2002). "Good-enough representations in language comprehension." *Current Directions in Psychological Science*, 11(1), 11-15; Christianson, K., Hollingworth, A., Halliwell, J. F., & Ferreira, F. (2001). "Thematic roles assigned along the garden path linger." *Cognitive Psychology*, 42(4), 368-407.

[^c4-smolensky]: Smolensky, P. (1990). "Tensor product variable binding and the representation of symbolic structures in connectionist systems." *Artificial Intelligence*, 46(1-2), 159-216.

[^c4-working-memory]: Goldman-Rakic, P. S. (1995). "Cellular basis of working memory." *Neuron*, 14(3), 477-485; Wang, X.-J. (2001). "Synaptic reverberation underlying mnemonic persistent activity." *Trends in Neurosciences*, 24(8), 455-463.

[^c4-chain-of-thought]: Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., & Zhou, D. (2022). "Chain-of-thought prompting elicits reasoning in large language models." *Advances in Neural Information Processing Systems*, 35.
