---
title: "Neural Fuzziness, Concepts, and the Epistemology of Logic"
date: 2026-03-22T09:00:00Z
draft: false
---

# Neural Fuzziness, Concepts, and the Epistemology of Logic

## 1. Introduction: The Physical Address of a Thought

My interest in the intersection of neuroscience and philosophy started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

I was reading about "concept neurons"—and I remember the jolt of realizing that something as abstract as *the concept of a specific person* could be pinned to a specific coalition of cells firing in the medial temporal lobe. It felt like finding the physical address of a ghost.

I followed this curiosity into the underlying mathematics—Hopfield networks, attractor dynamics. At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But when I worked through the math, something shifted. The equations were simple—embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. If neurons work this way, then *of course* concepts emerge. The math didn't ask me to accept the findings on faith. It showed me why they had to be true.

This highlighted a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. But the biological matter that generates these concepts is messy, plastic, and inherently fuzzy.

History shows that when science changes our map of reality, philosophy shifts to match. When Copernicus moved the Earth, Kant re-centered philosophy on the human mind. When Darwin revealed the fluid ancestry of species, he forced a total rethink of ethics. Even the strange math of quantum mechanics forced us to abandon the idea of a clockwork universe for one of probability. We accept that new physical facts demand new metaphysical frameworks.

Yet, when it comes to the "wetware" of the brain, we seem to be holding out. We treat the messy reality of neurons as a mere implementation detail—like the wiring of a computer that doesn't change the logic of the software. But if our concepts are physically instantiated in this messy, fuzzy way, shouldn't that knowledge fundamentally change our philosophies of truth and logic?

This piece is my inquiry. I'll walk through the neuroscience, the mathematics, and then push toward application—because I wonder if philosophy has treated these findings as "implementation details" when they're actually the whole show EEE Instead of the whole show, I want to say something like it's foundational in a constructive sense, i.e. the fact that this is a foundation impacts, changes the philosophy. EEE.

---

## 2. The Neurology: Finding Jennifer Aniston

In 2005, Quiroga et al. made a discovery that sounded like science fiction.

They were recording from single neurons in the human hippocampus (in patients preparing for epilepsy surgery) when they found something strange: neurons that fired selectively for specific concepts.

One neuron fired furiously when the patient saw a photo of Jennifer Aniston. But this wasn't just a visual response. The same neuron lit up for the written text of her name. It fired for the sound of her voice. It fired for the *Friends* theme music. It even responded to her specific haircut.

It didn't fire for Julia Roberts, or the Eiffel Tower, or anything else.

This wasn't a celebrity fluke. They found similar neurons for the Sydney Opera House, for Luke Skywalker, and even for the researcher himself. One neuron fired consistently whether the patient saw the researcher's face or simply heard his voice.

These neurons weren't coding for light or sound waves. They were coding for **meaning**—extracting an invariant concept that held steady regardless of whether it arrived via eyes, ears, or text. It was a physical manifestation of what philosophers had theorized for centuries. For Plato, a "Form" was the perfect, immaterial essence of a thing (like the universal concept of a Chair) that the intellect apprehends by looking past imperfect, physical copies. Millennia later, John Locke argued that we construct "abstract general ideas" through a process of mental subtraction—observing multiple particular objects and stripping away the specific circumstances of time, place, and individual differences to leave only what is common. Here, in the hippocampus, was the biological machinery doing exactly what philosophy demanded—stripping away sensory particulars to isolate the universal.

Current science suggests these aren't "Grandmother cells"—where a single neuron holds the entire concept of your grandmother. Instead, they are sparse, distributed populations. For a simple object like a face, a small cluster of neurons fires in sync. For more complex ideas, the coalition might be larger and more spread out.

But the implication is stark: **A concept is not a definition in a dictionary. It's a specific pattern in a physical network.**

---

## 3. The Mechanism: How Neurons Capture Commonality

How could a concept—the most elusive entity in philosophy—be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

EEE Here I want to start with something other than the answer starts with. Rather I want to say in trying to understand this I started by seeing how researchers understood this, how they modeled it. And that's why I got to heavy in learning. EEE The answer starts with a simple principle: **Neurons that fire together, wire together.**

This is known as **Hebbian learning**, named after psychologist Donald Hebb. It is the brain’s primary way of turning experience into structure. 
To understand the "wiring," we have to look at the **synapse**. This is the microscopic gap where two neurons meet. They don't actually touch; instead, one neuron sprays chemicals (neurotransmitters) across the gap to trigger the next one. 

The "strength" of a connection is simply how likely one neuron is to make the other one fire. When two neurons fire at the same time, the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen EEE We should add here also that the signal may last longer, i.e. it could clean up the chemicals more slowly or have them last longer in other ways. EEE. This is **synaptic plasticity**. Like a path through the woods, the more a connection is used, the easier it is to travel. This physical strengthening is what we mean when we say they "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watch *Friends*, your brain processes her face (vision), her voice (audio), and her name (language) simultaneously. Because these distinct neural populations fire at the same time, the Hebbian rule kicks in. The synaptic connections between them strengthen. Over time, these inputs become physically linked.

Trigger just one element—seeing the name "Jennifer"—and a cascade of signals flows through these reinforced highways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the *resonance* of this Hebbian web. EEE I'm not sure I like the resonance of Habean web. We're introducing both the word resonance and web without really explaining it. I think we should replace this with something that's already familiar from our explanation. EEE

But here's what makes this profound: **the Hebbian rule automatically extracts what's common across experiences.** EEE So a couple of things. First of all, I don't want to say that this is what makes it profound. I say this is what I find profound. Because this seems to me to imply that the Hebbian rule automatically extracts, etc. But I think that before we say this, we need to explain a little bit more. We need to explain when it doesn't fire. because right now it seems to fire with anything related to Jennifer Aniston or to that concept. It seems to overfire based on our explanation so far. We need to explain when it doesn't as well. EEE

#### The Math (Feel free to skip this)

A key insight that took me a while to grasp: **in neural networks, "memory" and "concept" are the same thing.** Both are stable patterns the network settles into. A memory is a concept of a past experience. A concept is the memory of what many experiences had in common. The math doesn't distinguish between them—and that's the point.

A Hopfield network gives us the simplest model of this process. Imagine a network of neurons, each of which can be "on" (+1) or "off" (−1). Between every pair of neurons is a connection with a weight—a number that says how much they influence each other.

**The key components:**

- **State**: What each neuron is doing right now (+1 or −1). For a network with *n* neurons, the state is a vector: **s** = (s₁, s₂, ..., sₙ)

- **Weights**: The fixed connections between neurons. The weight between neuron *i* and neuron *j* is written wᵢⱼ. These don't change during recall—they *are* the stored patterns.

- **Stored pattern**: A specific configuration of neural activity that the network has been wired to fall back into. If we want to store a pattern **ξ** = (ξ₁, ξ₂, ..., ξₙ), we set the weights using the Hebbian rule.

**The Hebbian learning rule** is almost embarrassingly simple:

$$w_{ij} = \xi_i \cdot \xi_j$$

In plain English: **If two neurons are the same in a pattern, connect them positively. If they're different, connect them negatively.**

That's it. Same → +, different → −.

A positive link between two neurons makes them *want* the same sign. A negative link makes them *want* opposite signs.

**Storing multiple patterns** is just as simple. If you have *p* different patterns (ξ¹, ξ², ..., ξᵖ), you add up the contributions:

$$w\_{ij} = **\sum\_**{k=1}^{p} \xi_i^k \cdot \xi_j^k\$$

Now here's the magic. Suppose you have three different experiences of Jennifer Aniston. Each time, some neurons are active (her face, her voice, the *Friends* theme) and others aren't. The Hebbian rule says: for each experience, strengthen connections between neurons that match and weaken connections between neurons that differ.

When you add up these contributions across all your experiences, **the connections that survive are the ones that were consistent**. If "face neurons" and "voice neurons" fired together every time you encountered Jennifer Aniston, their connection gets reinforced three times (+1 × +1 = +1, added three times = +3). But if some irrelevant neuron (say, "coffee cup") was on during one encounter and off during another, its contributions cancel out (+1 × +1 = +1, then +1 × −1 = −1... they sum toward zero).

The network doesn't store each experience separately. It stores what the experiences have in common. The "concept" emerges as the statistical residue of repeated co-activation.

To make this concrete, here's a small simulation. Repeatedly train the same co-occurring features and watch their links strengthen under a simple Hebbian update rule.

{{< simulation src="/simulations/hebbian-wiring.html" title="Hebbian wiring simulator" height="620" >}}

#### The Landscape Intuition

For simple concepts like "Jennifer Aniston," the Hebbian math works cleanly. But cognition involves far more complex concepts—*justice*, *irony*, *home*—where the picture changes.

In these cases, you're not dealing with a handful of neurons switching on or off. You're dealing with billions of neurons, most of which are *always* active to some degree. The concept isn't "these neurons on, those neurons off." It's a *pattern*—a specific configuration across a vast, always-active network.

This is where simple weight matrices stop being enough. When everything is always firing, what matters is the *geometry* of how activations relate to each other. The concept becomes a region in a high-dimensional space, not a binary state. EEE but critically the mechanism remains identical. EEE

This is why we need the landscape metaphor—and a new term: **attractor**.

An attractor is simply a state that a system naturally falls into and stays in. Drop a marble into a bowl, and it rolls to the bottom. That resting point is an attractor. The marble doesn't stay on the rim; it's *attracted* to the lowest point. In neural terms, an attractor is a stable pattern of activity that the network settles into when activated. Once the network reaches that pattern, it stays there—the neural equivalent of the marble at rest.

**Attractor dynamics** describes how the system moves toward these stable states. It's the rolling, not just the resting. When you see half of Jennifer Aniston's face, your neural network doesn't freeze at "half-recognized." It *moves*—activity flows through strengthened connections until the whole pattern completes. The dynamics are the journey; the attractor is the destination.

Think of the network's weights as carving a landscape of hills and valleys. Each pattern you store shapes the terrain—creating a valley that the network naturally falls into. Most critically for our topic here, there are ridges between these valleys, and as we'll see their shape is very telling about some philosopihical questions. 

This is where simple weight matrices stop being enough. When everything is always firing, what matters is the *geometry* of how activations relate to each other. The concept becomes a region in a high-dimensional space, not a binary state.

This is why we need the landscape metaphor.

Think of the network's weights as carving a landscape of hills and valleys (basins in topology). Each pattern you store shapes the terrain—creating a valley that the network naturally falls into.

- **The weights** are the terrain (fixed after learning)—the grooves carved into the landscape.

- **The state** is a marble rolling on that terrain (changes moment to moment).

- **Memories** are the valleys (stable resting points the marble settles into).

- **A cue** is where you drop the marble.

{{< simulation src="/simulations/attractor-landscape.html" title="Attractor landscape simulator" height="620" >}}

The mathematics is simple. But what it produces is not: a physical system that automatically extracts abstract commonality from concrete experience, stores it as terrain, and retrieves it from partial information.

This is how meaning gets a physical address.

## 4. The Attraction of Fuzziness

Why does this matter for philosophy?

Because it might explain why we can never quite define our terms.

In a neural network, a concept forms by carving out a valley through repetition. See enough chairs, and your brain carves a "Chair" valley. But this valley has sloped sides. It's not a binary box.

This is why definitional questions so often lead to silence.

"What makes something a chair?"

"It has legs and you sit on it."

"A horse has legs and you sit on it. Is a horse a chair?"

"No, a chair is furniture."

"What makes something furniture?"

"It's... made for a home?"

"A doormat is made for a home. Is a doormat furniture?"

We stammer. We struggle because "chair" isn't defined by necessary and sufficient conditions. It's defined by the *shape* of an attractor valley—or at least, that's what this framework suggests.

This is why so many definitional conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers sometimes treat it as an intellectual surrender—an admission that you can't *really* define the thing. But attractor theory suggests it might be the most honest answer possible. You *do* know it when you see it. Your neural network recognizes when a stimulus falls within a valley. What you can't do is articulate the valley's exact boundary, because **there is no boundary—only a gradient where the gravity of the concept gets weaker.**

Wittgenstein noticed this too. His "family resemblance" concept—the idea that category members share overlapping similarities rather than a single defining feature—is a philosophical description of what attractor valleys produce. Games don't share one essential property. They share a web of partial overlaps, each reinforcing the same valley through different pathways.

If this picture is right, fuzziness isn't a bug. It's the feature that lets us generalize—to recognize a beanbag as a chair—without learning a new rule for every object in the universe.

---

## 5. From Concepts to Logic: A Defense

At this point, reductionist alarm bells ring.

If concepts are just balls rolling into valleys, what about logic? Are we just biological machines following gravity? Does truth exist?

I think this fear is circular.

Admitting that logic has a physical substrate doesn't destroy logic, just as admitting that heat is molecular motion doesn't stop water from boiling.

But there's a deeper problem. If concepts are fuzzy—if "chair" bleeds into "stool" at the edges—can we reliably manipulate them with logic? Classical logic assumes crisp boundaries. When we say "All A are B," we assume we know exactly what counts as A.

And there's a more troubling question still: where did our logical concepts come from? "And," "or," "not," "if-then"—these feel different from "chair" or "Jennifer Aniston." They don't seem to be abstractions from sensory experience. So what valleys do they occupy? Are they carved by the same Hebbian process, or do they arise from some different neural architecture entirely?

I don't have a confident answer here, but here's my working hypothesis: maybe logical operators aren't valleys at all. Maybe they're something more like *transitions between valleys*—the rules governing how the marble moves, not where it rests. "And" might be the operation of activating two valleys simultaneously. "Or" might be the state of being on a ridge between two valleys, ready to fall into either. "If-then" might describe a reliable pathway from one valley to another. This is speculative, but it would explain why logical concepts feel categorically different from object concepts—they're the dynamics of the landscape, not features of it.

What I find more compelling is thinking through the lens of **emergence**. A single molecule doesn't have a temperature. Temperature is a statistical property of millions of molecules. Similarly, a single neuron doesn't have "logic." Logic might be the macroscopic description of a well-formed energy landscape.

When we say an argument is "valid," perhaps we're saying that the neural transition from Premise A to Conclusion B is a frictionless slide down a steep, stable valley. When we say reasoning is "sound," perhaps we're saying the valleys correspond to something real in the world.

I find this plausible. But I'm not certain it's right.

---

## 6. Vagueness Revisited: Hills, Mountains, and Transitions

Now we can approach the Sorites Paradox—the Heap Paradox.

- 1 grain of sand is not a heap.

- 2 grains are not a heap.

- ...

- At what exact number does it become a heap?

Logic fails here because it demands a binary switch. Attractor theory might dissolve the problem—or at least reframe it.

Imagine two valleys side-by-side. One is "Non-Heap," the other is "Heap." Between them is a ridge—what topologists call a **saddle point**, a place where the landscape curves up in one direction and down in another. It's unstable: a marble perched there could roll either way.

As you add grains of sand, you're pushing the ball up the slope of the "Non-Heap" valley. There's no single point where it switches. There's a **transition zone**—the ridge—where the state is unstable. The neural network might flicker between the two concepts.

If this is right, the concept of "Heap" isn't broken. We're simply standing on the topological ridge between two attractors.

**Vagueness might not be a semantic mystery. It might be the feeling of a neural state traversing a saddle point.**

The same logic could apply to other classic puzzles:

- When does a hill become a mountain?

- When does a person become old?

- When does a collection of cells become a person?

I don't want to claim these puzzles are "solved." But I wonder if they're less mysterious when reframed this way. They might not be failures of language at all—just accurate descriptions of continuous landscapes being forced into discrete categories.

---

## 7. So What? Questions Worth Asking

If we take this seriously—that knowledge might be topology, not propositions—it opens questions I don't know how to answer. But they feel worth asking.

**Logic**

What would it mean to replace "justified true belief" with something like "stable attractor"? The standard philosophical definition of knowledge is a belief that is both true and justified. But if beliefs are valleys, what does "justified" mean? Perhaps it means the valley was carved by reliable processes—consistent experiences that track real patterns in the world. Or perhaps this whole translation is a category error. I'm not sure.

There's also the question of conviction. What makes us *feel* certain? Is certainty the depth of a valley? The steepness of its walls? I don't know, but I'd like to.

**Ethics**

**Ethics**:

We keep trying to build perfectly consistent ethical systems. They keep failing. Trolleys on a 'ridge'....

[Editor's Note: This is very brief. Consider spelling out the Trolley Problem explicitly as a topological ridge where conflicting moral attractor valleys (e.g., "do no harm" vs. "minimize overall death") meet.]

**Metaphysics**

What would a "self" look like if it were a valley? We experience ourselves as continuous, unified. But the landscape shifts over time—new experiences carve new grooves. Does the "self" attractor drift? Can it split? What happens when two valleys merge?

[Editor's Note: Needs a slight elaboration. If the self is a valley, what does it mean when the landscape shifts over time? (Also, fix typo: "vallyes")]

**Experimental Philosophy?**

Large Language Models are, in a meaningful sense, synthetic minds with their own energy landscapes. We can probe them, map their geometries, test their boundaries. Could this be a form of **experimental philosophy**? What do their attractor structures tell us about ours?

I don't have answers here. Just the sense that something interesting might be hiding in that direction.

---

## 8. Context and Novelty

To be clear: I'm not the first to suggest these connections. The groundwork was laid decades ago, and I've chosen not to engage directly with the philosophical literature here. I'd rather let the ideas stand on their own and see if they prompt useful thinking.

**The Connectionists** (1980s) argued that cognition is pattern-matching in neural networks, not symbol manipulation.

**Paul Churchland** (Neurosemantics) argued that knowledge is a high-dimensional vector space, not a set of propositions.

**Andy Clark** and the Predictive Processing camp describe the brain as minimizing "prediction error"—which is another way of describing finding the energy minimum.

Philosophy has largely treated these insights as "implementation details"—interesting facts about the brain that don't affect the *real* questions about truth, knowledge, and meaning.

I'm not certain this is wrong. But I wonder if it's backwards.

My goal isn't to claim discovery of the mechanism. It's to ask whether the mechanism matters more than we've assumed. What if the topology *is* the theory of knowledge? What if replacing the search for "Truth" with the study of "Stability" would help us make progress on puzzles that have stalled for centuries?
