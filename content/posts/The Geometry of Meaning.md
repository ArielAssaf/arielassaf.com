---
title: "The Geometry of Meaning"
aliases:
  - /posts/neural-fuzziness/
date: 2026-04-11T00:00:00Z
draft: false
---

## 1. Introduction: The physical address of a thought

My interest in the intersection of neuroscience and philosophy started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

I was reading about "concept neurons," and I remember the jolt of realizing that something as abstract as *the concept of a specific person* could be pinned to a specific coalition of cells firing in the medial temporal lobe. It felt like finding the physical address of a ghost.

I followed this curiosity into the underlying mathematics, Hopfield networks and attractor dynamics. At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But when I worked through the math, something shifted. The equations were simple. Embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. If neurons work this way, then *of course* concepts emerge. The math didn't ask me to accept the findings on faith. It showed me why they had to be true.

I kept running into a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. But the biological matter that generates these concepts is messy, plastic, and inherently fuzzy.

This has happened before. Relativity dissolved the absolute space and time that philosophy had taken for granted. Evolution showed that species don't have fixed essences — that sharp category boundaries are things we impose on a continuous process. Quantum mechanics made randomness fundamental, not a sign of ignorance. Each time, new science forced new philosophy — not as an optional upgrade, but as a correction.

And the correction always followed the same pattern. The physics didn't replace the phenomenon. It informed — and eventually constrained — which accounts of it could survive. Consider color. Discovering that red is a wavelength of electromagnetic radiation didn't change the experience of seeing a rose. But it ended, permanently, the claim that redness is in the rose. That's the primary/secondary quality distinction — one of the most consequential moves in modern philosophy — and it was delivered by physics. The experience stayed the same. The viable philosophy didn't.

That was a narrow case — a single wrong claim killed by a single physical discovery. I don't want to overextend it. The claim I'll be developing is not that neuroscience can settle philosophical questions as bluntly as wavelengths settled the primary/secondary quality distinction. It's that the physical structure of cognition should inform philosophical accounts of concepts, guide which questions are worth asking, and — where the evidence is strong enough — constrain which answers are viable. That's a more patient process than the color case, and this series is the beginning of the exploration, not the end.

Yet when it comes to the brain, the physical machinery that constitutes thought, philosophy has been remarkably slow to apply even the weaker version of this principle. We treat the messy reality of neurons as a mere implementation detail, like the wiring of a computer that doesn't change the logic of the software. But if the physical structure of cognition shapes what thought can be, then ignoring that structure isn't abstraction. It's a missed opportunity — not just to constrain, but to explore: to let the structure of the substrate point us toward the right philosophical questions.

This essay is the foundation for a series — less a set of claims than an exploration, a personal journey of following what the physical substrate teaches us about philosophical questions. Subsequent essays will push this into vagueness, epistemology, ethics, and what large language models might teach us about the geometry of concepts.

A note on method. This series reasons from neuroscience and mathematics forward, not from philosophical positions backward. I engage with ideas rather than with individual philosophers, and I don't attempt a survey of the literature. I'm asking what the science teaches us about what concepts actually are — their physical structure, their geometry, their boundaries — and then asking which philosophical tools, which approaches, which questions are the right ones in this light. The questions philosophy poses about concepts, the way it manipulates them, the precision it demands of them: do these fit the shape of what concepts turn out to be? Where they don't, I'm claiming the mismatch is worth explaining — and that the geometry can inform, guide, and eventually help adjudicate. This won't settle normative questions — neuroscience tells you what the brain does, not what rationality requires — and I'll be explicit about that boundary when we reach it.

---

## 2. The neurology: finding Jennifer Aniston

In 2005, Quiroga et al. published a finding that seemed almost too clean to be true.

They were recording from single neurons in the human hippocampus (in patients preparing for epilepsy surgery) when they found something strange: neurons that fired selectively for specific concepts.

One neuron fired furiously when the patient saw a photo of Jennifer Aniston. But this wasn't just a visual response. The same neuron lit up for the written text of her name. It fired for the sound of her voice. It fired for related audio cues. It even responded to her specific haircut.

It didn't fire for Julia Roberts, or the Eiffel Tower, or anything else.

This wasn't a celebrity fluke. They found similar neurons for the Sydney Opera House, for Luke Skywalker, and even for the researcher himself. One neuron fired consistently whether the patient saw the researcher's face or simply heard his voice.

These neurons weren't coding for light or sound waves. They were coding for **meaning**, extracting an invariant concept that held steady regardless of whether it arrived via eyes, ears, or text.

Philosophers have theorized about the nature of concepts for centuries—from Plato's immaterial Forms, apprehended by pure reason beyond the senses, to Locke's "abstract general ideas," constructed by observing particulars and stripping away the circumstances of time, place, and individual difference to leave only what is common. These traditions disagreed, sharply, about where concepts come from. But they agreed on what concepts have to *do*: capture the invariant behind variable experience. What the concept neuron findings give us is a look at the machinery behind that end product: the mechanism that actually produces the stable, cross-modal (spanning different senses: sight, sound, language) representations that both traditions were trying to account for.

A word of caution before we go further. What we're looking at here is a simplified instance of the biology, not the full picture. The real neuroscience is messier, more distributed, and far less clean than a single neuron lighting up for a single person. But simplified instances are where understanding starts, and the question that matters is whether the core pattern, the thing the simplification reveals, survives when you add the complications back in. We'll keep testing that as we go.

Current science suggests these aren't "Grandmother cells," where a single neuron holds the entire concept of your grandmother. Instead, they are sparse, distributed populations. For a simple object like a face, a small cluster of neurons fires in sync. For more complex ideas, the coalition might be larger and more spread out.

But the implication is stark: a concept is not a definition in a dictionary. It's a specific pattern in a physical network.

---

## 3. The mechanism: how neurons capture commonality

How could a concept—the most elusive entity in philosophy—be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

To understand this, I started where researchers started: with models. How do neuroscientists think about what's happening in these networks? That question led me deep into Hebbian learning—and the math really helped my intuition, something it should always do, but does not often enough in my case.

A caveat. What I'm about to show you is a model — a spherical cow. Every science has these: physics has frictionless planes, economics has homo economicus. The Hopfield network is neuroscience's version. Real synaptic plasticity is far messier. But the model earns its keep the way all good models do: the geometric structure it produces survives when you add the complications back in. We're looking for a way of modeling and understanding the core activity of concept formation in a way that holds up as the biology gets messier — and, as we'll see later, shows up in systems that have nothing to do with biology at all.

The core principle is simple: **Neurons that fire together, wire together.**

This is known as **Hebbian learning**, named after Canadian psychologist Donald Hebb. It is the brain's primary way of turning experience into structure.

To understand the "wiring," we have to look at the **synapse**. This is the microscopic gap where two neurons meet. They don't actually touch; instead, one neuron sprays chemicals (neurotransmitters) across the gap to trigger the next one.

The "strength" of a connection is simply how likely one neuron is to make the other one fire. When two neurons fire in close temporal proximity — not necessarily at the same instant, but within a narrow window — the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen. The signal might also linger longer—the chemicals could be cleared away more slowly, extending the window of influence. This is **synaptic plasticity**. (There are refinements, like the precise timing of firing affecting the strength of the change. But for the model we're building, what matters is the core principle: *reliable temporal association strengthens connections*.) Like a path through the woods, the more a connection is used, the easier it is to travel. This physical strengthening is what we mean when we say they "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watch *Friends*, your brain processes her face (vision), her voice (audio), and her name (language) simultaneously. Because these distinct neural populations fire at the same time, the Hebbian rule kicks in. The synaptic connections between them strengthen. Over time, these inputs become tightly associated — not "wired together" in the sense of a fixed cable, but linked by strengthened synaptic pathways that make co-activation increasingly likely.

Trigger just one element—seeing the name "Jennifer"—and a cascade of signals flows through these reinforced pathways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the activation of this linked network—the same strengthened connections lighting up together.

But wait. If neurons that fire together wire together, wouldn't everything get wired to everything? If you're drinking coffee while watching *Friends*, does "coffee" become part of the Jennifer Aniston concept?

This is where the system's selectivity matters. The Jennifer Aniston neuron doesn't fire for *anything* associated with her—it fires for stimuli that reliably and repeatedly co-occur with the concept across many different contexts. Coffee might be present during one viewing, but absent during the next ten. The connection never gets reinforced enough to stick. Meanwhile, her face, her voice, and her name appear together reliably. Those connections get strengthened over and over.

The network also pushes back. Neurons don't just excite each other — they quiet each other down. When the Jennifer Aniston coalition fires, it suppresses competing coalitions, like a conversation where one voice gets louder and the others fade. This sharpens the response: the concept activates cleanly rather than bleeding into everything nearby.

And here's the thing: the Hebbian rule automatically extracts what's common across experiences.

#### The math

The math here is worth the detour, because its simplicity is the point. The mechanism that produces concepts from neurons is not baroque or mysterious. It's almost trivially simple, and that simplicity matters.

A Hopfield network gives us the simplest model of this process. Imagine a network of neurons, each of which can be "on" (+1) or "off" (−1). Between every pair of neurons is a connection with a weight, a number that says how much they influence each other.

**The components:**

- **State**: What each neuron is doing right now (+1 or −1). For a network with *n* neurons, the state is a vector: **s** = (s₁, s₂, ..., sₙ)

- **Weights**: The fixed connections between neurons. The weight between neuron *i* and neuron *j* is written wᵢⱼ. These don't change during recall—they *are* the stored patterns.

- **Stored pattern**: A specific configuration of neural activity that the network has been wired to fall back into. If we want to store a pattern **ξ** = (ξ₁, ξ₂, ..., ξₙ), we set the weights using the Hebbian rule.

**The Hebbian learning rule** is almost embarrassingly simple:

$$w_{ij} = \xi_i \cdot \xi_j$$

In plain English: if two neurons are the same in a pattern, connect them positively. If they're different, connect them negatively.

That's it. Same → +, different → −.

A positive link between two neurons makes them *want* the same sign. A negative link makes them *want* opposite signs.

**Storing multiple patterns** is just as simple. If you have *p* different patterns (ξ¹, ξ², ..., ξᵖ), you add up the contributions:

$$w\_{ij} = \sum\_{k=1}^{p} \xi_i^k \cdot \xi_j^k$$

Now here's the magic. Suppose you have three different experiences of Jennifer Aniston. Each time, some neurons are active (her face, her voice, the *Friends* theme) and others aren't. The Hebbian rule says: for each experience, strengthen connections between neurons that match and weaken connections between neurons that differ.

When you add up these contributions across all your experiences, the connections that survive are the ones that were consistent. If "face neurons" and "voice neurons" fired together every time you encountered Jennifer Aniston, their connection gets reinforced three times (+1 × +1 = +1, added three times = +3). But if some irrelevant neuron (say, "coffee cup") was on during one encounter and off during another, its contributions cancel out (+1 × +1 = +1, then +1 × −1 = −1... they sum toward zero).

The network doesn't store each experience separately. It stores what the experiences have in common. The "concept" emerges as the statistical residue of repeated co-activation.

To try and make this more concrete, I built a simulation where the Hebbian rule updates a small set of neurons based on input. You can watch the wiring happen in real time—see which connections strengthen and which fade as patterns repeat.

{{< simulation src="/simulations/JA_sim.html?v=2" title="Hebbian wiring simulator" height="620" >}}

An insight that took me a while to grasp: **in a Hopfield network, "memory" and "concept" are mathematically the same thing.** Both are stable patterns the network settles into. A memory is a concept of a past experience. A concept is the memory of what many experiences had in common. The math doesn't distinguish between them — and that equivalence is itself interesting, but it's also where the spherical cow shows its limits most clearly.

Real brains *do* distinguish between memory and concepts. Patients who lose the ability to form new episodic memories can still retain old concepts, and patients with semantic dementia can lose concepts while still forming new episodic memories. If the Hopfield model were the whole story, this double dissociation would be inexplicable. It isn't the whole story. The brain uses different regions and consolidation pathways for episodic and semantic knowledge, and these are architectural features the simple model doesn't capture.

But notice what survives the complication. The geometric point — that learning from repeated experience produces attractor valleys with graded boundaries — doesn't depend on memory and concepts being stored in the same system. It depends on the learning mechanism. And here the biology actually helps. The leading account of how concepts form in real brains — complementary learning systems theory — proposes that the hippocampus rapidly encodes individual episodes, while the cortex slowly extracts regularities across them through its own Hebbian-like consolidation process. The two systems are architecturally separate, which is why they can break independently. But the cortical pathway is still doing statistical extraction from repeated experience — still strengthening what recurs and letting what varies wash out — and that process carves the same topology: valleys, slopes, saddle points. The model is wrong about the plumbing. The shape survives because the slow cortical consolidation that actually builds concepts uses the same logic the model is built on, even though it runs in a different system on a different timescale.

#### The landscape intuition

For simple concepts like "Jennifer Aniston," the Hebbian math works cleanly. But cognition involves far more complex concepts—*justice*, *irony*, *home*—where the picture changes.

In these cases, you're not dealing with a handful of neurons switching on or off. You're dealing with billions of neurons, most of which are *always* active to some degree. The concept isn't "these neurons on, those neurons off." It's a *pattern*—a specific configuration across a vast, always-active network.

This is where simple weight matrices stop being enough. When everything is always firing, what matters is the *geometry* of how activations relate to each other. The concept becomes a region in a high-dimensional space, not a binary state. But critically, the mechanism remains identical—Hebbian learning still carves the structure. What changes is how we visualize it.

This is why we need the landscape metaphor—and a new term: **attractor**.

An attractor is simply a state that a system naturally falls into and stays in. Drop a marble into a bowl, and it rolls to the bottom. That resting point is an attractor. The marble doesn't stay on the rim; it's *attracted* to the lowest point. In neural terms, an attractor is a stable pattern of activity that the network settles into when activated. Once the network reaches that pattern, it stays there—the neural equivalent of the marble at rest.

**Attractor dynamics** describes how the system moves toward these stable states. It's the rolling, not just the resting. When you see half of Jennifer Aniston's face, your neural network doesn't freeze at "half-recognized." It *moves*—activity flows through strengthened connections until the whole pattern completes. The dynamics are the journey; the attractor is the destination.

Think of the network's weights as carving a landscape of hills and valleys. Each pattern you store shapes the terrain, creating a valley that the network naturally falls into. Most critically for our topic, there are ridges between these valleys, and their shape turns out to matter.

- **The weights** are the terrain (fixed after learning)—the grooves carved into the landscape.

- **The state** is a marble rolling on that terrain (changes moment to moment).

- **Memories** are the valleys (stable resting points the marble settles into).

- **A cue** is where you drop the marble.

To see this play out, you can interact with the visualization. Click to create valleys and watch "thoughts" settle into stable states.

{{< simulation src="/simulations/attractor-landscape.html" title="Attractor landscape simulator" height="620" >}}

The mathematics is simple. What it produces is more: a physical system that extracts abstract commonality from concrete experience, stores it as terrain, and retrieves it from partial information.

One thing worth saying out loud: nothing in this picture depends on neurons specifically. The geometry would have the same structural properties if it were running on silicon, or on some alien chemistry we haven't imagined. What matters (or so I'll argue) is the shape of the valleys, the gradients of the slopes, the saddle points between concepts. Neurons are how *we* happen to run the process. The geometry may be what the process has in common across all its possible substrates.

If that's right, then meaning has something like a physical address — not in a particular neuron, but in the shape of a landscape.

## 4. The attraction of fuzziness

The landscape we've just described has an immediate consequence: its concept-boundaries slope rather than drop.

This matters — not because it tells us something we didn't know. Anyone who has tried to define "game" at a dinner party already knows that natural concepts resist sharp definition. The observation is old. What the attractor framework offers is not the observation but a *mechanical explanation* for it — one that predicts not just that definitions will fail, but *where* and *how* they'll fail, and what specific shape the failure will take.

In a neural network, a concept forms by carving out a valley through repetition. See enough chairs, and your brain carves a "Chair" valley. But this valley has sloped sides. It's not a binary box.

This is why definitional questions so often lead to silence — and why the silence has a characteristic pattern.

"What makes something a chair?"

"It has legs and you sit on it."

"A horse has legs and you sit on it. Is a horse a chair?"

"No, a chair is furniture."

"What makes something furniture?"

"It's... made for a home?"

"A doormat is made for a home. Is a doormat furniture?"

We stammer. We struggle because "chair" isn't defined by necessary and sufficient conditions. It's defined by the *shape* of an attractor valley—carved by every chair you've ever encountered, with boundaries that slope rather than drop.

This explains why so many definitional conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers sometimes treat it as an intellectual surrender, an admission that you can't *really* define the thing. But attractor theory suggests it might be the most honest answer possible. You *do* know it when you see it. Your neural network recognizes when a stimulus falls within a valley. What you can't do is articulate the valley's exact boundary, because there is no boundary—only a gradient where the gravity of the concept gets weaker.

Philosophers have noticed this before. Wittgenstein's "family resemblance," the ordinary language tradition's attention to how words actually behave, prototype theory in cognitive psychology — all of these recognized, in different ways, that natural concepts resist sharp definition and that their boundaries shift with context. The observation is well-established. So what's novel about the attractor picture?

The mechanism. These earlier accounts described the fuzziness. The attractor framework explains *why* it's there and predicts its specific shape. The learning process extracts statistical regularities, not necessary and sufficient conditions, and statistical regularities produce gradients, not edges. Context modulates the terrain: it primes certain neural populations, reshapes valley walls in real time, which is why concept boundaries shift depending on the situation. And the mechanism makes predictions the descriptions don't — about the *shape* of transitions, their path-dependence, their asymmetries — predictions that are testable.

If this picture is right, the fuzziness is doing real work. It's what lets us generalize, to recognize a beanbag as a chair, without learning a new rule for every object in the universe.

## 5. Reductionism?

At this point a reasonable worry: if concepts are attractor dynamics, have we explained them away? Reduced meaning to math, thought to topology?
No. But the reason is more specific than the usual anti-reductionist move, and I want to be careful about what I'm claiming — and what I'm not.
Start with what I'm not claiming. I'm not claiming that neurons are the key. Neurons are how we happen to run this process, but the argument doesn't depend on them. You could swap the neurons for silicon or for some alien chemistry and the argument would go through unchanged. Philosophy has known since the 1960s that the same mental function can run on different physical substrates — that studying the wiring diagram of the brain isn't the same as studying the mind. That insight was right. I'm not challenging it.
But here's what happened next, and this is the part I think went wrong. Philosophers heard "the substrate doesn't matter" and jumped straight to "so we can theorize about concepts at the level of propositions — definitions, necessary and sufficient conditions, binary predicates — without worrying about how the system that produces concepts actually works." And that jump skipped a level.
There's an explanatory level between substrate and proposition. Call it the geometry. In the brain and in the simple theoretical models we've been looking at, something about learning from experience seems to produce a recognizable topology: valleys with sloped sides, ridges between them, transition zones that are graded rather than sharp. The topology isn't the substrate. It doesn't care whether it's running on wet neurons or dry silicon. But it isn't at the level of definitions and logic either. It sits between them — a structure that emerges from the learning process itself.
We've seen analogous patterns outside neuroscience. Thermodynamics didn't replace the concept of energy, but once entropy was understood, it informed which engineering programs were worth pursuing and eventually ruled out perpetual motion. Molecular biology didn't replace heredity, but once DNA was understood, blending inheritance was no longer a viable account. In both cases the phenomenon survived; certain explanations of it didn't. The parallel isn't exact — the color case was a clean kill, and I don't claim the same bluntness here. But the direction is the same: physical structure informing, guiding, and where the evidence is strong enough, constraining the viable accounts of a phenomenon. And one feature of this claim matters enormously: the geometry survives as we add sophistication to the model. Start with the simplest Hopfield network, and you get valleys with sloped sides. Add biological realism — lateral inhibition, recurrent processing, neuromodulation — and the valleys get more complex, but they're still valleys with sloped sides. If the topology is robust across these variations, then it isn't an artifact of the simple model. It's a consequence of learning from experience. A later essay in this series will ask whether systems with entirely different substrates and learning dynamics — large language models, trained by gradient descent on text — converge on similar geometries. If they do, the case for taking the topology seriously as a guide to philosophical questions gets considerably stronger. The geometry shapes the phenomenology. The feeling of recognizing a chair, the stammer when asked to define one, the ease of border cases and the discomfort of forced binary choices — these are experiences of navigating the landscape. You feel the slopes. You feel the valley floor. You feel the saddle points. If the geometry has graded boundaries, then the phenomenology will have them too — not because neurons are messy (they are, but that's beside the point), but because gradients are built into the topology itself.
So yes — abstract away from neurons. But abstract to the geometry, not past it. The philosophical tradition jumped from "substrate doesn't matter" to "propositions are the right level," and in doing so it skipped the level where the action is.

One caution. When I say "the geometry," I don't mean every detail of whichever model we happen to use. Some features of a geometric description are artifacts of the representation — the choice of coordinates, the exact distances, the specific axes. Those shift when you redraw the map. I'm not claiming that every knob on the model is philosophically load-bearing. I'm claiming that some of them are, and that the next few sections will show which ones.

Concepts are real, and they operate at their own level. You can't derive a valid argument from the Hebbian learning rule. You can't get ethics from synaptic weights. But the topology of the landscape shapes what kinds of concepts the system can build. And if your philosophical framework assumes that learned concepts have sharp edges, it's assuming a geometry that the learning process can't produce. That's not an implementation detail. It's a substantive finding about the material that philosophical theories are theories *of* — the kind of finding that, in other domains, has eventually reshaped which accounts survive. The physics doesn't replace the subject matter. But it can tell you something about its shape.

## 6. The mismatch

Here's the pattern worth naming: continuous landscapes resist discrete dissection. You can't carve a valley at its joints because it doesn't have joints.

But our primary tools for working with concepts—formal definitions, necessary and sufficient conditions, binary predicates, logical categories—are all dissection tools. They assume that concepts have edges. Sometimes they do. "Prime number" has a cliff for a wall—you're either divisible only by one and yourself, or you're not. "Triangle" has a cliff. But notice something about these examples: they're mathematical. Their boundaries are sharp because they were stipulated to be sharp. Someone decided what "prime" means, and the definition has no sloped sides because it was engineered not to. Mathematical concepts are constructed objects. Their edges are put there on purpose.

Natural concepts aren't like that. "Chair," "heap," "knowledge," "person," "harm"—nobody stipulated these. They were learned, carved out of experience by the Hebbian process we've been tracing. And that process, as we've seen, produces valleys with sloped sides. It can't help it. When you learn from variable experience, what you get is a gradient, not a cliff.

And "experience" here extends further than it might seem. Some of our deepest attractor valleys — fear of snakes, face detection, basic intuitions about physical objects — look hardwired. But they were carved by experience too, just not *yours*. Natural selection, operating over millions of generations, preserved organisms whose neural architecture responded to snakes and culled those that didn't. Over that timescale, the "snake = danger" attractor got carved into the genome itself, prewiring the synaptic connections that individual learning would otherwise have to build from scratch.

I've been using the word "learning" to describe the Hebbian process. Calling natural selection a form of learning might seem like a stretch — it doesn't strengthen synapses, it culls organisms. But the mathematical relationship turns out to be closer than the surface difference suggests. Recent theoretical work has shown that the equations governing evolutionary change (the Price equation, Lande's equation for phenotypic traits) and the equations governing neural network optimization (stochastic gradient descent) share a common mathematical structure: both are forms of gradient descent on an objective function, shaped by the curvature of the space they're navigating. Under idealized conditions — a continuous genome, small mutation steps — natural selection *is* gradient descent, not by analogy but by derivation. Real biology departs from those idealizations in important ways: genotype space is discrete, not continuous; genetic drift can overpower selection in small populations; the genotype-to-phenotype map warps the geometry in ways that neural networks don't experience. But the geometric output — basins with graded boundaries, saddle-point transitions, hysteresis — survives these complications. The topology is more rugged, the valleys are flatter and wider than simple models suggest, but they're still valleys with sloped sides. When I say "learning" from here on, I mean it as a shorthand for any process whose output is stable structure distilled from variable input — whether that distillation runs in milliseconds inside a single brain or across millions of generations in a population. What matters is the convergent geometry of the output, and that convergence is underwritten by formal mathematics, not just by metaphor.

And the resulting valley has the same geometry as an individually learned concept — not by metaphor but by measurement. Innate snake fear doesn't function as a binary switch that fires for snakes and ignores everything else. It generalizes along a graded slope: garden hoses, coiled ropes, curved sticks all trigger the response, with strength that decays smoothly as the stimulus becomes less snake-like. The generalization gradient is Gaussian, not step-shaped. It shows hysteresis — once the fear response activates, it takes more disconfirming evidence to exit the state than it took to enter it. And it's asymmetric — skewed toward false positives, because the fitness cost of missing a real snake dwarfs the cost of flinching at a rope. These are the specific geometric signatures — graded boundaries, hysteresis, asymmetry — that attractor dynamics predict. Evolution produced them through a completely different mechanism than Hebbian learning, but the topology converged.

The mismatch between discrete tools and continuous landscapes isn't a quirk of individual learning. It's a feature of any process — personal or evolutionary — whose output is stable structure with graded boundaries.

This is worth pausing on, because the shape of the snake fear gradient tells us something precise about what sits between two concepts. Every concept the brain holds — whether learned in a lifetime or carved by evolution — has a generalization gradient that decays outward from its prototype. Where two such gradients overlap, where the pull from "snake" and the pull from "stick" are roughly equal, is the saddle point between them. And notice what the Gaussian shape implies about that region: the tails of the curves are the flattest part of the landscape. The closer you get to the saddle, the weaker the gravity from either side. That's the zone where categorization is hardest, where small perturbations could tip the state either way, and where asking "is this a snake or a stick?" has no clean answer — not because you haven't thought hard enough, but because you're standing in the flattest part of the terrain. We'll see shortly that this is exactly the zone where the oldest paradox in philosophy plants its flag.

The confusion between these two kinds of concepts is old. You can see it already in Socrates. Many of the early Socratic dialogues are, at bottom, a philosopher applying a sharp tool to sloped concepts and watching it fail. "What is piety?" "What is courage?" "What is temperance?" Every time, someone proposes a definition. Every time, Socrates finds a case that breaks it. The dialogues often end in puzzlement, nobody can produce the definition. (Plato does offer positive accounts elsewhere — the *Republic* builds toward a theory of justice — but even there, the definitional struggles along the way are instructive.) Some philosophers have read these failures as part of the philosophical process — the slow advance toward the right definition. Others, especially since Wittgenstein, have taken them as evidence that sharp definitions were the wrong goal for natural concepts in the first place. The attractor framework is sympathetic to the second reading but adds something to it: not just that the definitions fail, but a *specific account of why*. The tool doesn't fit the material — and we can now say what shape the material actually has. If piety and courage are attractor valleys carved by cultural experience, then looking for their sharp edges is looking for something that isn't there. The puzzlement isn't a failure of the participants. It might be a feature of the landscape.

Aristotle inherited the assumption that definitions should be findable, and built a system around it. His categories (genus, species, differentia) formalized the idea that the world comes pre-carved into kinds: that every object belongs to exactly one species, defined by a set of essential properties that are both necessary and sufficient. A thing either is or isn't a mammal. It either is or isn't a substance. The categories are exhaustive — everything fits somewhere — and mutually exclusive — nothing fits in two places at once.

This framework worked brilliantly for the concepts it was designed around — geometric forms, logical classes, and biological species as Aristotle understood them. That last one is worth pausing on, because it's the example where history already ran the experiment. Aristotle looked at the living world and saw fixed, discrete kinds: horses are horses, dogs are dogs, and the boundaries between species are as sharp as the boundary between triangles and circles. For two thousand years, that seemed obviously right. Then Darwin showed it wasn't. Species are populations drifting through a continuous space of variation. The boundaries between them are real enough to be useful, but they're not sharp—they're exactly the kind of graded transitions that attractor geometry predicts. "When does a subspecies become a species?" is the biologist's version of "when does a hill become a mountain?" The attractor picture suggests this expectation was a generalization from a special case. Stipulated concepts have edges. Most learned concepts don't. And if the attractor picture is right, much of the philosophical tradition may have spent centuries trying to find edges on objects that slope.

What matters for our argument is not just that Aristotle was wrong about species—it's how biology advanced past him. It didn't find better boundaries. It dissolved the assumption that boundaries were the right thing to look for. The category system didn't get refined. It got replaced by a framework, population thinking, that was built for gradients rather than edges. That's exactly the kind of move I'm suggesting philosophy needs to make with concepts more broadly. 

And yet the Aristotelian expectation survived its own best example. The definitional method that analytic philosophy inherited still rests on the assumption that concepts have edges — that there's always a set of properties that draws a clean line between what's in and what's out. Biology moved on. Whether philosophy needs to make a similar move — at least for learned, natural concepts — is the question this series is exploring.

## 7. Situating the argument

Many philosophers have already observed that natural concepts resist sharp definition — Wittgenstein's family resemblance, the ordinary language tradition, and much of post-analytic philosophy have made this point in various ways. I'm not bringing news that concepts are fuzzy. What I want to show is that the best model we have for the physical origin of concepts — how they actually form in neural networks and, as we'll see, in other learning systems — gives rise to a specific geometry: attractor valleys with sloped sides, saddle-point boundaries, path-dependent transitions. That geometry doesn't just redescribe the fuzziness. It explains *why* concepts must be fuzzy when learned from experience, it predicts specific features of the fuzziness that "concepts are vague" alone doesn't predict, and — if the geometry survives as we add sophistication to the biology — it should inform and eventually guide which philosophical accounts of concepts are worth pursuing.

I should also be clear: none of this is new. The connectionists established that cognition is pattern-matching in networks. Paul Churchland argued that knowledge lives in high-dimensional activation spaces and described the brain's conceptual landscape in terms of attractor dynamics — hills and valleys sculpted by learning. Andy Clark's predictive processing framework describes the brain as minimizing prediction error, which is descent toward an energy minimum, and extends this into the structure of concepts themselves. Between them, they built most of the machinery this essay relies on.

What I'm trying to add is narrower: to extract one specific geometric consequence — that any system forming concepts through statistical extraction from experience will produce attractor valleys with graded boundaries — and trace what follows from it for the classical problems in epistemology. The geometry doesn't just say "concepts are vague." It says the vagueness has a specific shape: saddle-point transitions, not linear gradients; path-dependent boundaries that shift depending on direction of approach; asymmetric transitions where the path into a concept differs from the path out. These are specific predictions, distinct from what degree theories or family resemblance alone would give you, and the next essays will test them against the phenomena. That's a claim about the topology of concepts, not about neurons. The connectionists opened the door. This series tries to walk through it.

## 8. The mismatch in action

To see the pattern concretely, consider the oldest example.

The Sorites Paradox—the Heap Paradox—goes like this. One grain of sand is not a heap. If something is not a heap, adding a single grain cannot make it a heap. Therefore, by induction, no number of grains is a heap. The conclusion is absurd, but every step seems valid.

The paradox works because it's formulated in the language of sharp edges: a predicate ("is a heap") that has to be true or false, and a principle (one grain can't flip it) that exploits the absence of any boundary to flip at. It demands an edge. The concept doesn't have one.

In attractor terms, "heap" and "not-a-heap" are two valleys. Between them is a ridge — a transition zone where the landscape is nearly flat and a small perturbation could tip the state either way. There is no cliff between the valleys. There is a saddle. Adding grains of sand pushes the state up the slope of the "not-a-heap" valley, across the ridge, and down into "heap" — but the crossing is gradual, and in the transition zone the state isn't clearly in either basin. There is no point where gravity switches. There is a region where it is ambiguous.

This is in many ways sympathetic to degree theories of vagueness, which replace true/false with a gradient from 0 to 1. The attractor picture arrives at a similar place but from a different direction — not by stipulating that truth comes in degrees, but by showing that any system learning concepts from experience will produce transitions with this shape. The physical grounding matters because it opens the door to empirical tests. Does the transition zone between "heap" and "not-a-heap" show hysteresis — a shift in the boundary depending on which direction you approach from? Are the transitions between concepts asymmetric, with different profiles depending on the path? These are predictions the attractor framework inherits from the physics, and they're the kind of predictions that could, in principle, be tested experimentally. The geometric account doesn't replace existing theories of vagueness so much as offer a physical mechanism that explains why those theories describe what they describe.

So from the attractor perspective, the paradox isn't showing us that "heap" is a broken concept. It's showing us what happens when you insist on finding an edge in a landscape that slopes. Maybe the problem isn't the concept — maybe it's the question.

The next essay develops this properly — including how specific features of the attractor geometry, like hysteresis and path-dependence, generate testable predictions for vagueness. But the point for now is just to see the pattern: a discrete tool, a continuous landscape, and an apparent paradox that's really an artifact of the mismatch. That same pattern, I'll argue, shows up again and again.

## 9. The road ahead

So here's where we are. If the picture I've been sketching is right, concepts are attractor valleys with sloped sides — in any system that forms them through repeated exposure to patterns. And what we've been watching, in every example so far, is the same collision: discrete tools applied to continuous terrain. The suggestion — and at this stage it is still a suggestion, is that at least some of the paradoxes and tensions in the philosophical tradition aren't in the concepts themselves, but are artifacts of forcing binary distinctions onto a landscape that curves.

I should say what I think this framework *doesn't* do, because the absence might give the wrong impression. Not every concept looks like "chair" or "heap." Some seem to sharpen with expertise rather than staying fuzzy. Some moral judgments feel absolute. I don't think these are counterexamples — expertise deepens valleys and steepens walls without creating vertical cliffs, and moral certainty is a very deep valley, not a different kind of structure. But those claims need their own arguments, and I'll make them in later essays rather than assert them here.

This also marks the boundary of the claim. The geometric constraints I've been tracing bear on similarity, categorization, and the shape of concept boundaries. They don't apply to questions of logical structure, truth conditions, or normative correctness. Whether an inference is *valid* or a concept is *correctly applied* involves considerations that geometry alone can't provide. The claim is that the geometry constrains the terrain on which those higher-level questions play out. It doesn't answer them.

The next essays push this framework into specific philosophical problems: vagueness and the Sorites paradox, where the saddle-point geometry makes testable predictions about the shape of transition zones; the relationship between belief and credence, where attractor depth might explain why continuous confidence feels binary; Humean ethics, where moral sentiments look like culturally carved attractors with overlapping boundaries; and the question of substrate-generality — whether the topology holds even when the learning dynamics are entirely different.

The question I keep coming back to is simple, and I don't pretend to know the answer: if the geometry informs which accounts of concepts are viable — the way physical structure has informed viable accounts in other domains — then how many of philosophy's open problems are actually about the world, and how many are artifacts of trying to cut a continuous landscape at joints it doesn't have? The answer might be "fewer than I suspect." But the question seems worth taking seriously — and the geometry, I think, is the right place to look.
