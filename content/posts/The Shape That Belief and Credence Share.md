---
title: "The Shape That Belief and Credence Share"
date: 2026-03-26T00:00:00Z
draft: false
---

## The Wrong Frame

Epistemologists have been having a fight about belief.

On one side, you have the *belief-first* camp — the traditionalists. They say your mental life is built out of beliefs — discrete, binary commitments. You believe it's raining or you don't. You believe the earth is round or you don't. There's no 0.73 about it. Credences — degrees of confidence — are real enough, but they're secondary. They ride on top of belief, not the other way around.

And the traditionalists have strong arguments. Belief has a special relationship with action: when you believe the bridge is safe, you walk across it — you don't walk 0.73 of the way across. Trust is binary in practice: it doesn't fade by degrees, it *breaks*. Knowledge functions as a norm — it's what entitles you to assert things, act without hedging, hold others accountable. These aren't toy examples. They capture something real about how belief operates in our lives, and any account that can't explain them is incomplete.

On the other side, the *credence-first* camp — the Bayesians — says the binary picture is wrong despite its appeal. Nobody *just believes* anything. You hold propositions with varying degrees of confidence: you're nearly certain the earth is round, fairly confident your flight will be on time, and roughly 50-50 on whether it'll rain Tuesday. Belief, on this view, is a useful shorthand for "credence above some threshold" — but it's the credences doing the real work.

Then there are the dualists, who say both are real and irreducible. You have beliefs *and* credences, and neither reduces to the other.

So what does the attractor epistemology from the last essay have to say about this? To my reading, I think it says the Bayesians got it almost right, and attractors support them. The mind works in degrees of confidence. The evidence for that — from neuroscience, from decision theory, from the simple phenomenology of uncertainty — is overwhelming, and I won't rehash it here. But the Bayesians have always known they face a challenge: explaining why belief *feels* binary. Because it does. When you believe your keys are on the counter, you don't experience a probability distribution. You experience certainty. And the traditionalist arguments I listed above — action, trust, knowledge — are real phenomena that demand an explanation, not a dismissal.

The standard Bayesian patch for this is the *Lockean thesis*: belief is just credence above some threshold. You "believe" P when your confidence crosses, say, 0.9 or 0.95 or wherever you want to draw the line. This works formally, but notice what it does. It takes a continuous system and imposes a sharp boundary on it. Sophisticated versions have tried to soften the cut. Interest-relative accounts keep the binary distinction but let the threshold float with practical stakes — same credence, different contexts, different verdicts on whether you "believe." Context-sensitive accounts go further, arguing that your epistemic state is often not a precise number but a thick region of confidence, which makes the mapping to any sharp cutoff unstable. Some reject the threshold picture's geometry altogether — treating suspension of judgment not as the middle zone between belief and disbelief, but as a distinct attitude in its own right, which can't be recovered by partitioning a credence scale at two points. But even the most flexible variant preserves the categorical layer: belief remains a distinct kind of state, and somewhere in the transition from uncertainty to commitment, you cross into it. The boundary may shift, blur, or resist precise location — but it's still a boundary. It's the same structural move we've seen before — in the sorites paradox, in the concept of knowledge, in every case where philosophy tries to draw a clean line through a graded landscape. And in the previous essay, we saw reasons to be suspicious of that move.

So here's the question I want to explore: what if the Bayesians don't need the sharp threshold? What if there's a physical mechanism that explains why continuous credences produce binary-feeling belief — without anyone having to stipulate where the line is?

I think there is. And it's the same attractor framework we used in the last essay.

---

## Valleys and Marbles

The previous essay, [The Geometry of Meaning](/posts/the-geometry-of-meaning/), built a picture of concepts as attractor valleys in a landscape — stable states that a neural network falls into and stays in. The mechanism is Hebbian learning; the geometry it produces is valleys with sloped sides and ridges between them. The math and the intuition are there. What matters for this essay is a single feature of that geometry: **a system can be continuous in its structure while producing behavior that looks discrete.** The landscape is smooth everywhere. But the marble still ends up in one valley or another. It doesn't hover between them. From the outside, it looks like the system made a binary choice. From the perspective of the landscape, nothing binary happened. The marble just rolled downhill.

If this is what the brain is doing when it "believes" something — and I'll argue shortly that the evidence points that way — then the Bayesians were right about the continuous landscape and the belief-first camp was right about the phenomenology, and neither of them needs to be wrong. The feeling of binary commitment *is* what it's like to be at the bottom of a continuous valley. No threshold required.

---

## What the Traditionalists Get Right (and What It Actually Shows)

I want to take the strongest traditionalist arguments for binary belief seriously, because I think they're pointing at real phenomena. The question is whether those phenomena require a binary *mechanism* or whether they're better explained as features of an attractor landscape.

### "Belief Commits You to Action"

The traditionalists observe — correctly — that belief has a special relationship to action. When you believe the bridge is safe, you walk across it. You don't walk 0.73 of the way across. Action is binary: you either do the thing or you don't. And so, the argument goes, the mental state that produces action must also be binary.

But notice what this argument actually shows. It shows that the *output* of the system is discrete. And that's exactly what attractor dynamics predict. The marble settles to a valley floor, and the floor triggers an action. The discreteness is real — at the level of behavior. What doesn't follow is that the *process* leading to the action was discrete. And here we have good evidence it wasn't.

When neuroscientists want to watch a decision happen in real time, they use a beautifully simple setup. A monkey watches a screen full of dots. Most dots jitter randomly, but a small percentage drift consistently in one direction — say, left. The monkey's job is to figure out which way the signal is pointing and report it with an eye movement. Meanwhile, electrodes record neurons in an area called LIP, which helps plan where to look next.
Here's what the recordings show. The neurons don't sit quiet and then suddenly fire. They ramp up — slowly, steadily, like water filling a basin. The firing rate of neurons favoring the correct direction climbs over hundreds of milliseconds while the rate for the wrong direction stays flat or drifts down. When the climbing signal hits a threshold, the monkey flicks its eyes. More coherent dots (a clearer signal) produce a steeper ramp and a faster decision. Noisier dots produce a shallower ramp and a slower one.
The decision looks instantaneous — a sudden flick of the gaze. But the process that produced it was a long, continuous accumulation. Each moment of sensory input nudged the firing rate a little higher or a little lower, like a marble being gently pushed up a slope, until it crested the ridge and dropped into a valley. The commitment was the last thing that happened, not the first.
This pattern — dubbed the drift-diffusion model — is one of the most replicated findings in decision neuroscience. And it doesn't stop at perception. 

Now, a traditionalist might reasonably say: "Fine, the *perceptual* process is continuous, but the *belief* is what happens at the end — the committed state." And that's not a bad objection. But the same accumulation-to-threshold dynamics have been observed in prefrontal cortex during abstract tasks — rule application, category learning, analogical reasoning. The architecture doesn't seem to be limited to perception. It appears to be how the brain arrives at committed states generally, including states with propositional content. We first should note that the biologist would not accept the perception vs. belief distinction dichotomy. As far as neurons are concerned, the mechanism is the same: accumulate evidence, ramp toward a threshold, settle into a committed state. The difference between perceiving that the dots are moving left and judging that the bridge is safe is a difference of inputs and timescale, not of architecture. If you want to argue that belief is a fundamentally different kind of state from perception, you need to find a point in the neural machinery where the continuous process stops and something categorically new begins. Nobody has found one.

What I'd suggest — tentatively — is that the traditionalist is describing the valley floor and mistaking it for the whole landscape. The commitment is real. The binary feeling is real. But it's the *result* of a continuous process settling into an attractor, not evidence of a binary mechanism underneath.

### "Trust Breaks, It Doesn't Fade"

Here's a traditionalist argument I find genuinely compelling. Think about betrayal. When you discover a close friend has been lying to you, your trust doesn't decrease by 0.15 on some internal scale. It *breaks*. One moment you trusted them, the next you don't. The phenomenology is violently discrete. And it seems to require binary mental states: Trust = 1, then Trust = 0.

I think this is the strongest card the traditionalists hold. And I think the attractor framework actually explains it better than they do.

What you're describing, when trust "breaks," has the signature of a *phase transition* — the marble cresting a ridge between two valleys and dropping into a new basin. Phase transitions are genuinely abrupt. Water doesn't gradually become ice; it freezes. A magnet doesn't slowly become magnetized; it snaps into alignment past a critical temperature. These transitions are as sudden as anything in nature. But they emerge from continuous processes. Temperature is continuous. Molecular motion is continuous. The *transition* is sharp; the *system producing the transition* is not.

So the betrayal experience is real, and it really is sudden. But the suddenness is the phase transition, not evidence of a binary architecture underneath. And the attractor framework predicts something the binary model doesn't: that the *path to the transition* should be continuous. You should be able, in retrospect, to identify the accumulating doubts — the marble climbing the slope — even though the transition itself felt instantaneous. I suspect most people who've experienced betrayal recognize this. The snap was sudden. But the doubts were building.

There's a further prediction. If trust were a binary switch, regaining it should be symmetric — flip the bit back. But trust is famously *easier to break than to rebuild*. This asymmetry is unexplained on the binary model. On the attractor model, it falls out naturally: the "trust" valley and the "betrayal" valley don't have to be symmetric. The betrayal basin can be deeper, with steeper walls, making it harder to climb out of. The landscape isn't obligated to be fair.

### "You Can't Half-Know Something"

There's a third traditionalist argument, and it operates on different ground. The knowledge norm — defended by Williamson for assertion, by Hawthorne and Stanley for practical reasoning — says that certain epistemic practices *require* binary standards. You either know enough to assert, or you hedge. You either know enough to act on, or you don't. And the binariness isn't presented as something we discovered about the mind — it's presented as something our practices need. This is a normative claim, and the standard objection to mixing neuroscience with normative epistemology is the naturalistic fallacy — you can't derive an ought from an is.

I agree with that. But I want to suggest that something subtler is happening here. Epistemic norms aren't free-floating. They're norms *about* something — about concepts like knowledge, belief, assertion. Those concepts are the primitives the norms manipulate. And if those primitives have a specific structure — if they're attractor-shaped, graded, history-dependent — then norms that assume a different structure don't become immoral or logically invalid. They become *misapplied*. It's the difference between a type system that's internally consistent and a type system that's correct for the language it's supposed to govern.

Consider: you *can* stipulate that "tall" has a sharp cutoff at 183 centimeters. Nothing stops you. The stipulation is internally coherent. But the concept will fight you at every edge case, because the underlying structure isn't cooperating. And I think that's what we see in epistemology. The lottery paradox — you believe each ticket will lose, but don't believe they'll all lose — is what happens when you apply closure under conjunction to a concept that isn't binary. The preface paradox — you believe every claim in your book, but don't believe they're all true — is what happens when you apply consistency norms to attractor states that can be individually stable without being jointly stable. Even Gettier cases, where justified true belief passes the binary checklist but something still feels wrong, might be symptoms of the same mismatch: a binary framework failing to capture the topology of the actual concept.

I'm not claiming these paradoxes are *solved* by the attractor framework. That would be glib. But I want to flag a pattern: the persistent, decades-old puzzles in epistemology cluster exactly where binary norms meet graded structure. That's suggestive. It's at least worth asking whether the puzzles are artifacts of the formalism rather than deep features of the subject matter.

There's a further observation. If you push working physicists on their most confident assertions — the speed of light, the second law of thermodynamics, the age of the universe — they will all, without exception, tell you they don't *know* these things in a binary sense. They haven't been proved the way a mathematical theorem is proved. Rather, these physicists are convinced beyond a certain number of nines: 99.99% confident, perhaps 99.9999%. They're open, in principle, to the possibility of being wrong. They simply consider it unproductive to dwell on it. That's not binary knowledge. That's a very deep valley — a marble sitting so firmly at the bottom that no reasonable perturbation could dislodge it. And yet the slopes are still there. The valley still has a shape. The physicist knows this and isn't troubled by it.

Notice that the physicist's epistemic practice isn't deficient. Nobody thinks physicists are being irrational when they act on 99.9999% confidence without claiming certainty. If anything, their practice is more epistemically sophisticated than the binary idealization — it tracks the actual structure of their confidence, including its limits. The binary norm doesn't describe best epistemic practice. It describes a philosophical idealization that working knowers don't use and don't need.

So the question isn't whether you *can* stipulate binary knowledge norms. You can. The question is whether you *should*, given that the primitives resist it, that the resulting framework generates persistent paradoxes, and that the most epistemically successful practitioners in human history operate without it. That question deserves its own treatment, and I'll take it up in the next essay.

---

## The Asymmetric Snap

The trust asymmetry points to something the attractor framework predicts and the binary model can't accommodate. But to see it most cleanly, it helps to look at a simpler case — one where we can measure the boundaries precisely.

Take a picture of a dog and morph it, frame by frame, into a picture of a cat. Show the sequence to a subject while recording neurons in the inferior temporal cortex — the region that handles object recognition. What happens is striking. The neural population doesn't gradually slide from a "dog pattern" to a "cat pattern." It holds the dog pattern, then snaps to the cat pattern at some threshold. So far, the binary camp is nodding.

But now run the sequence in reverse — cat morphing to dog. If the system were using binary categories with a fixed boundary, the snap should happen at the same frame in both directions. Dog becomes cat at frame 14 going forward; cat becomes dog at frame 14 going back.

It doesn't. The snap happens at a *different* frame depending on which direction you're coming from. If you started with the dog, you hold onto "dog" longer. If you started with the cat, you hold onto "cat" longer. This is called *hysteresis*, and it's a direct signature of attractor dynamics — the marble's momentum carries it further in whichever direction it's already rolling.

Why does this matter so much? Because hysteresis is *impossible* in a system with fixed binary boundaries. If "dog" and "cat" were boxes separated by a clean line, the line wouldn't move depending on where you started. The fact that it moves — that your current state changes where the boundary sits — means there is no fixed boundary. There's a landscape, and the marble is rolling through it.

This is the same asymmetry we saw with trust, but stripped of all the emotional complexity. Even at the level of basic perceptual categories, the brain doesn't use fixed binary boundaries. It uses attractor dynamics with history-dependent transitions. That doesn't prove higher-order belief states work the same way. But it does mean the burden falls on the traditionalist to explain why belief would be architecturally different from every other cognitive categorization system we've been able to measure.

---

## The Shape of the Valley

So far I've been arguing — or at least suggesting — that the attractor framework explains traditionalist observations better than the binary model. But I haven't said much about what happens inside the valley itself. And this is where, I think, something genuinely interesting comes into view.

Alexandre Pouget and collaborators have studied how populations of neurons encode information. The basic finding isn't new: the brain uses *population codes*, where the pattern of activity across hundreds or thousands of neurons represents a stimulus or concept. What Pouget's group showed is that these population codes don't just encode a best guess. They encode something that looks very much like an entire probability distribution.

Here's what that means concretely. The peak of the population response — the neurons firing most strongly — represents the brain's best estimate. If you like, it's the marble's position on the landscape: the bottom of the valley it's currently sitting in. But the *shape* of the response around that peak — how broad, how narrow, how symmetric — represents the brain's confidence in that estimate. A sharp, narrow peak means high confidence. A broad, flat peak means uncertainty.

If you're a Bayesian, this should sound familiar. The peak is something like belief — the state the system has committed to. The shape is something like credence — the degree of confidence surrounding that commitment. And they're not two separate things. They're two features of a single representational structure, in the same way that a valley has both a floor and walls without those being different objects.

I find this suggestive. It doesn't prove that belief and credence are "the same thing" in any philosophically rigorous sense — the relationship between neural population codes and propositional attitudes is complicated, and I don't want to paper over that. But it does suggest that the brain isn't maintaining two separate ledgers, one for what it believes and one for how confident it is. It's maintaining one structure — the attractor state — that has both properties inherently.

There's a striking parallel in an unexpected place. When a large language model generates text, you see one token at a time — a single word, chosen and committed to. It looks like a sequence of discrete decisions. But underneath each output is a probability distribution over every possible token: "cat" at 0.72, "dog" at 0.15, "hat" at 0.04, and so on across the entire vocabulary. The token you see is the peak of that distribution — the "belief," if you like. The shape around it — how confident, how spread across alternatives — is the "credence." One structure, two descriptions. LLMs aren't brains, and I don't want to overextend the analogy. But the architectural parallel is worth noticing: a system with entirely different hardware, trained by entirely different dynamics, converges on the same geometry — continuous internal distributions producing discrete-looking outputs. If two systems with different substrates arrive at the same representational structure, that structure may be a consequence of the learning problem itself, not a quirk of neurobiology. That's a question worth its own treatment.

If that's right, then the dualist position (belief and credence are both real and irreducible) is half right. They're both real. But they're not irreducible to each other. They're *aspects* of the same thing — the way a valley's floor and its walls are aspects of the same geometry.

---

## Why Belief Feels Binary

Let me come back to the phenomenology question, because I think it's where everything connects.

I said earlier that the Bayesians' remaining problem is explaining why belief *feels* binary. The standard Bayesian answer — the Lockean thesis — draws a threshold. But a threshold is a line imposed on a continuum, and we've spent two essays being suspicious of those.

The attractor framework offers a different explanation. At the bottom of a deep attractor basin, the landscape is flat. Move a little left, move a little right — you're still at the bottom. Small perturbations produce no change in your state and therefore no change in your experience. The phenomenology of certainty — the feeling of simply *believing* something without qualification — is the experience of being at the floor of a deep valley where local exploration reveals no slope.

Move partway up the side and you feel it. The landscape tilts. This is the phenomenology of doubt — the uneasy sense that your position is unstable, that you could slide somewhere else.

And when you change your mind? That's a phase transition across a ridge. It feels sudden. It feels discrete. But the ridge was approached continuously; the marble climbed the slope of the old valley inch by inch before the transition happened. The sharpness is real — phase transitions *are* abrupt — but they emerge from a continuous substrate. They're a feature of the landscape, not evidence that the landscape is built out of discrete boxes.

This explains something that has always been awkward for the binary view: changing your mind can be fast or slow, easy or agonizing, complete or partial. If belief were a logical toggle, flipping it should always feel the same. It doesn't. Sometimes the valleys are close together with a low ridge — changing your mind is easy, almost casual. Sometimes the valleys are far apart with a high ridge — changing your mind is wrenching and slow. The topology of the attractor landscape predicts the phenomenology. The binary model has no story about why different belief-changes feel different. It just says the bit flipped.

---

## Where This Leaves Us

I want to be honest about what I think this essay does and doesn't show.

What it doesn't show: that binary epistemic norms are incoherent. They're not. You can build a perfectly consistent normative framework on binary belief, and many brilliant philosophers have.

What it does show — or what I hope it shows — is that the primitives those norms govern may not have the structure the norms assume. Every time we examine the physical system, we find continuous attractor dynamics producing behavior and phenomenology that *look* discrete. Hysteresis proves the boundaries aren't fixed. Population coding shows that "belief" and "credence" are features of a single structure. Drift-diffusion shows the process is continuous even when the outcome isn't. And attractor geometry explains why certainty *feels* the way it does without requiring a binary mechanism.

The Bayesians, I think, had most of this right. Credences are real, fundamental, and continuous. Where they reached for the Lockean threshold — a sharp line to explain binary-feeling belief — I think the attractor framework offers something better: a physical mechanism that produces the same phenomenology without the stipulated boundary. The line doesn't need to be drawn because the valley does the work.

That leaves a question I find genuinely open. If the primitives are attractor-shaped, and if binary norms applied to those primitives generate the persistent paradoxes that have defined epistemology for decades, at what point does the mismatch between the norms and the material they govern become a reason to revisit the norms? The traditionalist can hold the line: norms are norms, and they don't answer to neurons. But the paradoxes remain, and the attractor framework at least suggests an explanation for *why* they remain. That seems worth taking seriously.

I don't think it resolves the question. But I think it changes which side bears the burden.

That's what I want to explore in the next essay.
