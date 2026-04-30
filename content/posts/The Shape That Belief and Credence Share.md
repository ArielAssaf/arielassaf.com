---
title: "The Shape That Belief and Credence Share"
date: 2026-03-26T00:00:00Z
draft: false
---

## The Wrong Frame

Epistemologists have been having a fight about belief.

On one side, you have the *belief-first* camp: the traditionalists. They say your mental life is built out of beliefs, discrete, binary commitments. You believe it's raining or you don't. You believe the earth is round or you don't. There's no 0.73 about it. Credences (degrees of confidence) are real enough, but they're secondary. They ride on top of belief, not the other way around.

And the traditionalists have strong arguments. Belief has a special relationship with action; trust seems to break rather than fade; the language of knowledge is binary. These aren't toy examples; they capture something real about how belief operates, and any account that can't explain them is incomplete.

On the other side, the *credence-first* camp, the Bayesians, says the binary picture is wrong despite its appeal. Nobody *just believes* anything. You hold propositions with varying degrees of confidence: you're nearly certain the earth is round, fairly confident your flight will be on time, and roughly 50-50 on whether it'll rain Tuesday. Belief, on this view, is a useful shorthand for "credence above some threshold," but the credences are doing the real work.

Then there are the dualists, who say both are real and irreducible. You have beliefs and credences, and neither reduces to the other. I will argue that the dualists are half right—both states are real—but they are wrong that they are irreducible. As the attractor geometry will show, belief and credence are simply two features of the exact same structure.

So what does the attractor epistemology from the last essay have to say about this? On my reading, it says the Bayesians got it almost right, and attractors support them. The mind works in degrees of confidence. The evidence for that, from neuroscience, from decision theory, from the simple phenomenology of uncertainty, is overwhelming, and I won't rehash it here. But the Bayesians have always known they face a challenge: explaining why belief *feels* binary. Because it does. When you believe your keys are on the counter, you don't experience a probability distribution. You experience certainty. And the traditionalist arguments about action, trust, and knowledge are real phenomena that demand an explanation, not a dismissal.

The standard Bayesian patch for this is the *Lockean thesis*: belief is just credence above some threshold. (It's the dominant credence-first reply; not every credence-first view goes this route, but the threshold story is the one that has set the agenda.) You "believe" P when your confidence crosses, say, 0.9 or 0.95 or wherever you want to draw the line. This works formally, but notice what it does. It takes a continuous system and imposes a sharp boundary on it, and as we'll see when we reach the lottery paradox, the boundary cuts badly. Sophisticated versions have tried to soften the cut. Interest-relative accounts let the threshold float with practical stakes; context-sensitive accounts replace the precise number with a thick region of confidence; some reject the geometry altogether and treat suspension of judgment as a distinct attitude rather than a middle zone. But every variant preserves the categorical layer. Belief remains a distinct kind of state, and somewhere in the transition from uncertainty to commitment, you cross into it. The boundary may shift, blur, or resist precise location, but it's still a boundary. It's the same structural move we've seen before: in the Sorites paradox, in the analysis of knowledge, in every case where philosophy tries to draw a clean line through a graded landscape. And in the previous chapter, we saw reasons to be suspicious of that move.

So here's the question I want to explore. The traditionalist argument has a particular shape: my experience of believing is binary, therefore the underlying state must be. The phenomenology drives the metaphysics. But that inference only goes through if the binary feeling can't be explained any other way. What if it can? What if continuous credences can produce binary-*feeling* belief without anyone having to stipulate where the line is?

I think they can.

---

## Valleys and Marbles

The previous chapter built a picture of concepts as attractor valleys: stable patterns a neural network falls into and stays in. What matters here is one feature of that geometry: **a system can be continuous in its structure while producing behavior that looks discrete.** The landscape is smooth. But the marble still ends up in one valley or another. From the outside, it looks like the system made a binary choice. From inside the geometry, the marble just rolled downhill.

An immediate objection: perhaps the neural dynamics are just the hardware, and the concept they implement could have a different structure entirely. The neurons *represent* belief; they don't determine what belief can be.

This is worth taking seriously, but the pattern from the previous chapter still matters: when science reveals the physical structure underlying a phenomenon, it doesn't replace the phenomenon, but it can constrain the viable accounts of it. Color science didn't change the experience of seeing red, but it did change what "redness" could mean.

I'm making a structurally similar claim here, scaled to the evidence available. The argument is not that neurons firing is the believing, full stop. It's that the geometry of neural dynamics should inform what belief can be, in the way that wavelengths informed what color can be. If neural dynamics merely represent belief, the brain could implement a binary switch without friction. But if the physical architecture constrains belief, then an attractor landscape fundamentally dictates how mental state transitions behave. If the geometry is attractor-shaped, then accounts of belief that assume a different geometry will generate friction. And that friction will show up as paradoxes. We'll see whether it does.

If this is what the brain is doing when it "believes" something, and I'll argue shortly that the evidence points that way, then the Bayesians were right about the continuous landscape and the belief-first camp was right about the phenomenology, and neither of them needs to be wrong. The feeling of binary commitment is what it's like to be at the bottom of a continuous valley. (I will explain exactly how a flat valley floor strips away the feeling of uncertainty in a later section, but first, we need to look at what the traditionalists get right.) No threshold required.

---

## What the Traditionalists Get Right (and What It Actually Shows)

I want to take the strongest traditionalist arguments for binary belief seriously, because I think they're pointing at real phenomena. The question is whether those phenomena require a binary *mechanism* or whether they're better explained as features of an attractor landscape.

### "Belief Commits You to Action"

The traditionalists observe, correctly, that belief has a special relationship to action. You don't partially flee a burning building or tentatively swerve to avoid a car. Action commits you: you do the thing or you don't. And so, the argument goes, the mental state that produces action must also be binary.

But notice what this argument actually shows. It shows that the *output* of the system is discrete. And that's exactly what attractor dynamics predict. The marble settles to a valley floor, and the floor triggers an action. The discreteness is real at the level of behavior. What doesn't follow is that the *process* leading to the action was discrete. And here we have good evidence it wasn't.

When neuroscientists want to watch a decision happen in real time, they use a beautifully simple setup. A monkey watches a screen full of dots. Most dots jitter randomly, but a small percentage drift consistently in one direction (say, left). The monkey's job is to figure out which way the signal is pointing and report it with an eye movement. Meanwhile, electrodes record neurons in an area called LIP, which helps plan where to look next.

Here's what the recordings show. The neurons don't sit quiet and then suddenly fire. They ramp up slowly, like water filling a basin. The firing rate of neurons favoring the correct direction climbs over hundreds of milliseconds while the rate for the wrong direction stays flat or drifts down. When the climbing signal hits a threshold, a graded ridge in the landscape rather than a sharp line stipulated in advance, the monkey flicks its eyes. More coherent dots produce a steeper ramp and a faster decision. Noisier dots produce a shallower ramp and a slower one.[^c2-drift]

The decision looks instantaneous, a sudden flick of the gaze. But the process that produced it was a long, continuous accumulation. Each moment of sensory input nudged the firing rate a little higher or a little lower, like a marble being gently pushed up a slope, until it crested the ridge and dropped into a valley. The commitment was the last thing that happened, not the first.

This pattern, often modeled as drift diffusion, is one of the most replicated findings in decision neuroscience. And it doesn't stop at perception.[^c2-drift]

Now, a traditionalist might reasonably object: "That's perception, not belief. Nobody disputes that perceptual processing involves continuous accumulation. But belief is a different kind of thing. It has propositional content. It's the kind of state that can be true or false, that enters into logical relationships with other beliefs. You've shown me neurons ramping in a sensory area, and I never claimed sensory processing was binary."

That's a fair objection, and it deserves a serious answer. Begin with the biologist's reply: as far as neurons are concerned, the perception/belief dichotomy doesn't carve anything. The mechanism is the same in both cases: accumulate evidence, ramp toward a threshold, settle into a committed state. The difference between perceiving that the dots are moving left and judging that the bridge is safe is a difference of inputs and timescale, not of architecture.

And the empirical evidence backs that up. The same accumulation-to-threshold dynamics have been observed in prefrontal cortex during abstract tasks such as rule application, category learning, and analogical reasoning. The architecture doesn't seem to be limited to perception. It appears to be how the brain arrives at committed states generally, including states with propositional content. If you want to argue that belief is a fundamentally different kind of state from perception, you need to find a point in the neural machinery where the continuous process stops and something categorically new begins. Nobody has found one.

What I'd suggest, tentatively, is that the traditionalist is describing the valley floor and mistaking it for the whole landscape. The commitment is real. The binary feeling is real. But it's the *result* of a continuous process settling into an attractor, not evidence of a binary mechanism underneath.

### "Trust Breaks, It Doesn't Fade"

Here's a traditionalist argument I find genuinely compelling. Think about betrayal. When you discover a close friend has been lying to you, your trust doesn't decrease by 0.15 on some internal scale. It *breaks*. One moment you trusted them, the next you don't. The phenomenology is violently discrete. And it seems to require binary mental states: Trust = 1, then Trust = 0.

But the empirical literature on trust tells us things that the binary model can't accommodate. The empirical picture is clear: trust transitions are path-dependent and asymmetric. There's a well-documented phenomenon called *betrayal aversion*: people treat a loss differently when it comes from a person who could have honored their trust than when the same loss comes from an impersonal lottery. Same odds, same stakes, different experience. The social character of the violation matters, which means the *path* into distrust matters, not just the destination.[^c2-trust]

And once you're there, getting back is harder than falling in was. Negative experiences erode trust more powerfully than positive experiences restore it, and the gap is wider for social risk than for impersonal risk. The path back also depends on the kind of break: if someone failed at a task, an apology helps; if someone lied to you, an apology can actually make things worse, because the inference about character is different.[^c2-trust]

If trust were a binary switch, none of this should be the case. Flipping a bit off and flipping it back on are the same operation, and it shouldn't matter who flipped it or how. On the attractor model, the path-dependence and the asymmetry fall out naturally: the distrust valley can be deeper than the trust valley, with steeper walls, and how you entered it shapes what it takes to climb out. The landscape isn't obligated to be fair.

These results sit more comfortably in an attractor-style model than in a symmetric binary switch. The specific predictions are ones the binary model doesn't make: that the social character of the violation matters, that the asymmetry is structural, that repair depends on the shape of the break.

### "You Can't Half-Know Something"

There's a third traditionalist argument, and it operates on different ground: the knowledge norm. It says that certain epistemic practices *require* binary standards. You either know enough to assert, or you hedge. And the binariness isn't presented as something we discovered about the mind; it's presented as something our practices need. This is a normative claim, and the standard objection to mixing neuroscience with normative epistemology is Hume's: you can't derive an ought from an is. Our senses, our empirical data, our science, can only describe the world. They cannot conclude what the world should be. The next chapter will make that point more directly for moral judgment; here I only need the narrower version.

I agree with that. The shape of the brain doesn't tell us how we ought to reason, any more than the shape of our limbs tells us where we ought to walk. But I want to suggest that something subtler is happening here, and that recognizing it doesn't violate the gap.

Epistemic norms aren't free-floating. They're norms *about* something: concepts like knowledge, belief, assertion. Those concepts are the primitives the norms manipulate. A norm that says "you should only assert what you know" assumes there's a fact of the matter about what knowing is. And if the concept of knowing has a specific structure (attractor-shaped, graded, history-dependent), then norms that assume a different structure don't become immoral or logically invalid. They become *misapplied*.

It's the difference between a grammar book that's internally consistent and a grammar book that's correct for the language people actually speak. Both can be self-consistent. Only one of them is doing what a grammar book is supposed to do. And no one would call the second grammar book more "normative" just because it stipulates more rigid rules; we'd say it's wrong about its subject matter. Norms can be internally valid while still being about the wrong thing.

This is what I think the neuroscience is showing us. Not that epistemic norms should be jettisoned, but that some of them are calibrated for primitives that don't exist in the way the norms imagine. The norm itself isn't the problem. The mismatch between the norm and the structure it's meant to govern is.

Consider: you *can* stipulate that "tall" has a sharp cutoff at 183 centimeters. Nothing stops you. The stipulation is internally coherent. But the concept will fight you at every edge case, because the underlying structure isn't cooperating. And I think that's what we see in epistemology.

Take the lottery paradox, which is worth lingering on, because it's a main counterargument the traditionalists use against the Bayesian position. If belief really is just credence above some threshold, they argue, then the following should be straightforward. You hold a ticket in a million-ticket lottery. Do you believe your ticket will lose? Of course; the odds are overwhelming. And the same is true for every other ticket. So you believe ticket #1 will lose, and ticket #2 will lose, and so on, for every ticket in the draw. But you don't believe *all* the tickets will lose. You know someone will win. Each belief is individually reasonable, but they can't all be true at once.

That's what happens when you treat belief as binary and then try to combine beliefs logically (the formal version of this problem is called *closure under conjunction*). The binary framework says each belief is either on or off, and if they're all on, their conjunction should be too. But the concept won't cooperate, because your confidence in each individual ticket losing, very high but not absolute, doesn't survive being multiplied across a million tickets.

The preface paradox is the same problem from a different angle. An author writes a book and believes every claim in it. That's why she wrote them. But she also knows, from experience and humility, that the book probably contains at least one error. She believes each claim and disbelieves their conjunction. On the binary model, that's a contradiction. On the attractor model, it's perfectly natural: each claim can sit stably at the bottom of its own valley without all of them being jointly stable (the formal term is *individual stability without joint stability*).

Note the pattern: the persistent, decades-old puzzles in epistemology cluster exactly where binary norms meet graded structure. That's suggestive. It's at least worth asking whether the puzzles are artifacts of the formalism rather than deep features of the subject matter.

One further observation bears directly on whether binary knowledge norms are necessary for good epistemic practice, or whether they're a philosophical habit that the best practitioners have already outgrown.

If you push working physicists on their most confident assertions (the speed of light, the second law of thermodynamics, the age of the universe), they will all, without exception, tell you they don't *know* these things in a binary sense. They haven't been proved the way a mathematical theorem is proved. Rather, these physicists are convinced beyond a certain number of nines: 99.99% confident, perhaps 99.9999%. They're open, in principle, to the possibility of being wrong. They simply consider it unproductive to dwell on it. That's not binary knowledge. That's a very deep valley: a marble sitting so firmly at the bottom that only a seismic perturbation could dislodge it. And yet the slopes are still there. The valley still has a shape. The physicist knows this and isn't troubled by it.

The point is this: the most epistemically successful practitioners in human history already operate on credences, not binary knowledge. They commit to action, publishing papers, building colliders, sending spacecraft, based on degrees of confidence, and they do it more effectively than any binary framework would allow. The coexistence of action and credence isn't a philosophical compromise. It's how the best knowledge-production in the world actually works. Nobody thinks physicists are being irrational when they act on 99.9999% confidence without claiming certainty. If anything, their practice is more epistemically sophisticated than the binary idealization: it tracks the actual structure of their confidence, including its limits.

The physics example supports the Bayesian picture directly: the most rigorous epistemic community on earth operates on credences, not binary commitments, and does so without losing decisiveness. But it also reveals something the standard Bayesian framework tends to leave implicit. At no point in the establishment of any of these results did the evidence cross a sharp line from "not known" to "known." The confidence deepened continuously. Publication conventions, sigma thresholds, and replication standards are practical agreements about when the valley is deep enough to act on, not discoveries that the valley has a ledge. If you go looking for the moment a result became known, you find only a gradient. That's the attractor picture: deep valleys, not sharp thresholds.

So the question isn't whether you *can* stipulate binary knowledge norms. You can. The question is whether you *should*, given that the primitives resist it, that the resulting framework generates persistent paradoxes, and that the most epistemically successful practitioners in human history operate without it.

---

## The Asymmetric Snap

Across these cases, the same pattern keeps returning: action looks discrete but the process producing it ramps continuously; trust breaks suddenly but the break is path-dependent and asymmetric; knowledge norms assume binary categories but generate paradoxes at exactly the seams where gradedness would predict them. In each case, the attractor framework accommodates features the binary model can't. But in each case, the evidence is indirect. We're inferring the landscape from the behavior. It would be nice to see the landscape directly. It turns out we can.

Take a picture of a dog and morph it, frame by frame, into a picture of a cat. Show the sequence to a subject while recording neurons in the inferior temporal cortex, the region that handles object recognition. What happens is striking. The neural population doesn't gradually slide from a "dog pattern" to a "cat pattern." It holds the dog pattern, then snaps to the cat pattern at some threshold. So far, the binary camp is nodding.[^c2-hysteresis]

But now run the sequence in reverse: cat morphing to dog. If the system were using binary categories with a fixed boundary, the snap should happen at the same frame in both directions. Dog becomes cat at frame 14 going forward; cat becomes dog at frame 14 going back.

It doesn't. The snap happens at a *different* frame depending on which direction you're coming from. If you started with the dog, you hold onto "dog" longer. If you started with the cat, you hold onto "cat" longer. This is called *hysteresis*, the same kind of history-sensitive settling introduced in the previous chapter's discussion of learned and innate valleys. It's a direct signature of attractor dynamics: the marble's momentum carries it further in whichever direction it's already rolling.

Why does this matter so much? Because hysteresis is *impossible* in a system with sharp, fixed boundaries. If "dog" and "cat" were boxes separated by a clean line, the line wouldn't move depending on where you started. The fact that it moves (that your current state changes where the boundary sits) means there is no fixed boundary. There's a landscape, and the marble is rolling through it.

This is the same structure we've been seeing, stripped to its essentials. The ramping neurons showed continuous process producing discrete-looking action. The trust literature showed path-dependence and asymmetry. Hysteresis shows both at once, in a system simple enough to measure precisely: the transition point depends on where you started, and on which direction you're traveling. The boundary isn't fixed. It's a feature of the landscape and the marble's trajectory through it.

This is where the distinction between representation and constraint becomes concrete. If the neural dynamics were merely *representing* a binary concept, the transition point could not shift depending on direction of approach. A binary concept has a fixed boundary; that's what makes it binary. Hysteresis means the boundary moves with your trajectory. And a moving boundary is not a boundary between boxes; it's a feature of a landscape. The dynamics here aren't merely implementing categorization. They're exposing the topology of what categorization actually is.

That doesn't prove higher-order belief states work the same way. But it does mean the burden falls on the traditionalist to explain why belief would be architecturally different from every other cognitive categorization system we've been able to measure. In the next chapter the same hysteresis signature also appears in a domain far removed from perception: moral judgment. That suggests the attractor architecture may be even more general than the epistemological debate requires.

---

## The Shape of the Valley

So far I've been arguing, or at least suggesting, that the attractor framework explains traditionalist observations better than the binary model. But I haven't said much about what happens inside the valley itself. And this is where, I think, something interesting comes into view.

The previous chapter argued that *concepts* are attractor states, valleys carved into a neural landscape by Hebbian learning. This chapter has been arguing that *beliefs* are too. The natural next question is whether they're the same kind of object or just architecturally similar. I think they're the same kind of object, and the most direct evidence comes from looking at what the population code actually contains.

Alexandre Pouget and collaborators have studied how populations of neurons encode information. The basic finding isn't new: the brain uses *population codes*, where the pattern of activity across hundreds or thousands of neurons represents a stimulus or concept. What Pouget's group showed is that these population codes don't just encode a best guess. They encode something that looks very much like an entire probability distribution.[^c2-pouget]

Here's what that means concretely. In the language of population coding, the peak of the response, the neurons firing most strongly, represents the brain's best estimate. In the landscape language, that corresponds to the valley floor where the marble settles. The *spread* of the response around that peak, how broad, how narrow, how symmetric, corresponds to the valley's shape: steep walls mean high confidence; broad shallow walls mean uncertainty.

If you're a Bayesian, this should sound familiar. The settled floor is something like belief: the state the system has committed to. The valley's shape is something like credence: the degree of confidence surrounding that commitment. And they're not two separate things. They're two features of a single representational structure, in the same way that a valley has both a floor and walls without those being different objects.

I find this suggestive. It doesn't prove that belief and credence are "the same thing" in any philosophically rigorous sense; the relationship between neural population codes and propositional attitudes is complicated, and I don't want to paper over that. But it does suggest that the brain isn't maintaining two separate ledgers, one for what it believes and one for how confident it is. It's maintaining one structure, the attractor state, that has both properties inherently. And that structure is the same kind of object that encoded concepts in the previous chapter. Concepts, beliefs, credences: the brain represents all of them with attractor-shaped states. The differences are differences of input and content, not of architecture.

There's a striking parallel in an unexpected place. When a large language model generates text, you see one token at a time, a single word, chosen and committed to. But underneath each output is a probability distribution over every possible token, and the token you see is just the peak. One structure, two descriptions: the peak is the "belief," the distribution around it is the "credence."LLMs aren't brains, and the analogy can be overextended. But this analogy breaks down if we imagine the marble as a distinct object rolling through the brain. There is no independent marble; the state of the network is the marble. The object and its trajectory are the same thing. Still, the architectural parallel is worth noticing: a system with entirely different hardware, trained by entirely different dynamics, converging on the same geometry of continuous internal distributions producing discrete-looking outputs. That suggests the structure may be a consequence of the learning problem itself, not a quirk of neurobiology. That's a question for a later chapter.

If that's right, then the dualist position (belief and credence are both real and irreducible) is half right. They're both real. But they're not irreducible to each other. They're *aspects* of the same thing, in the way a valley's floor and its walls are aspects of the same geometry.

---

## Why Belief Feels Binary

Let me come back to the phenomenology question, because I think it's where this chapter meets the previous one. Chapter 1 argued that geometry shapes how concepts feel from the inside. Belief is the same claim under more pressure.

I said earlier that the Bayesians' remaining problem is explaining why belief *feels* binary. The standard Bayesian answer, the Lockean thesis, draws a threshold. But a threshold is a line imposed on a continuum, and this project has been suspicious of those from the start.

The attractor framework offers a different explanation. At the bottom of a deep attractor basin, the landscape is flat. Move a little left, move a little right, and you're still at the bottom. Small perturbations produce no change in your state and therefore no change in your experience. The phenomenology of certainty, the feeling of simply *believing* something without qualification, is the experience of being at the floor of a deep valley where local exploration reveals no slope.

Move partway up the side and you feel it. The landscape tilts. This is the phenomenology of doubt: the uneasy sense that your position is unstable, that you could slide somewhere else.

And when you change your mind? That's a phase transition across a ridge. It feels sudden. It feels discrete. But the ridge was approached continuously; the marble climbed the slope of the old valley inch by inch before the transition happened. The sharpness is real (phase transitions *are* abrupt), but it emerges from a continuous substrate. The sharpness is a feature of the landscape, not evidence that the landscape is built out of discrete boxes.

This explains something that has always been awkward for the binary view: changing your mind can be fast or slow, easy or agonizing, complete or partial. If belief were a logical toggle, flipping it should always feel the same. It doesn't. Sometimes the valleys are close together with a low ridge, and changing your mind is easy, almost casual. Sometimes the valleys are far apart with a high ridge, and changing your mind is wrenching and slow. The topology of the attractor landscape predicts the phenomenology. The binary model has no story about why different belief-changes feel different. It just says the bit flipped.

---

## What the Shape Explains

I want to be honest about what I think this chapter does and doesn't show.

What it doesn't show: that binary epistemic norms are incoherent. They're not. You can build a perfectly consistent normative framework on binary belief, and many brilliant philosophers have.

What it does show, or what I hope it shows, is that the primitives those norms govern may not have the structure the norms assume. Every time we examine the physical system, we find continuous attractor dynamics producing behavior and phenomenology that *look* discrete. Hysteresis proves the boundaries aren't fixed. Population coding shows that "belief" and "credence" are features of a single structure. Drift-diffusion shows the process is continuous even when the outcome isn't. And attractor geometry explains why certainty *feels* the way it does without requiring a binary mechanism.

The Bayesians, I think, had most of this right. Credences are real, fundamental, and continuous. Where they reached for the Lockean threshold, a sharp line to explain binary-feeling belief, I think the attractor framework offers something better: a physical mechanism that produces the same phenomenology without the stipulated boundary. The line doesn't need to be drawn because the valley does the work.

That leaves a question I find genuinely open. If the primitives are attractor-shaped, and if binary norms applied to those primitives generate the persistent paradoxes that have defined epistemology for decades, at what point does the mismatch between the norms and the material they govern become a reason to revisit the norms? The traditionalist can hold the line: norms are norms, and they don't answer to neurons. But the paradoxes remain, and the attractor framework at least suggests an explanation for *why* they remain. That seems worth taking seriously.

I don't think it resolves the question. But I think it changes which side bears the burden.

That is where the next chapter goes: into moral judgment, where the pull of the valley is harder to ignore and the temptation to mistake that pull for truth is strongest.

[^c2-drift]: See Roitman and Shadlen, "Response of Neurons in the Lateral Intraparietal Area during a Combined Visual Discrimination Reaction Time Task," *Journal of Neuroscience* 22, no. 21 (2002); Gold and Shadlen, "The Neural Basis of Decision Making," *Annual Review of Neuroscience* 30 (2007).

[^c2-trust]: See Bohnet and Zeckhauser, "Trust, Risk and Betrayal," *Journal of Economic Behavior & Organization* 55, no. 4 (2004); Kim, Ferrin, Cooper, and Dirks, "Removing the Shadow of Suspicion," *Journal of Applied Psychology* 89, no. 1 (2004).

[^c2-hysteresis]: See Akrami, Liu, Treves, and Jagadeesh, "Converging Neuronal Activity in Inferior Temporal Cortex during the Classification of Morphed Stimuli," *Cerebral Cortex* 19, no. 4 (2009). For cat/dog category morphs recorded in IT and PFC, see McKee, Riesenhuber, Miller, and Freedman, "Task Dependence of Visual and Category Representations in Prefrontal and Inferior Temporal Cortices," *Journal of Neuroscience* 34, no. 48 (2014).

[^c2-pouget]: See Ma, Beck, Latham, and Pouget, "Bayesian Inference with Probabilistic Population Codes," *Nature Neuroscience* 9 (2006); Pouget, Beck, Ma, and Latham, "Probabilistic Brains," *Nature Neuroscience* 16 (2013).
