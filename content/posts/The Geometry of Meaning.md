---
title: "The Geometry of Meaning"
aliases:
  - /posts/neural-fuzziness/
date: 2026-04-11T00:00:00Z
draft: false
---

## 1. Introduction: The physical address of a thought

This whole project started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

The chapter that did it was about "concept neurons." I remember the jolt of realizing that something as abstract as *the concept of a specific person* could be pinned to a coalition of cells firing in the medial temporal lobe. It felt like finding the physical address of a ghost.

I followed this curiosity into the underlying mathematics, Hopfield networks and attractor dynamics.[^hopfield-hebb-quiroga] At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But once I worked through the math, something shifted. The equations were simple. Embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. If neurons work this way, then *of course* concepts emerge. The math didn't ask me to accept the findings on faith. It showed me why they had to come out the way they did.




I kept running into a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. The biological matter that produces those concepts is messy, plastic, and fuzzy.

This kind of collision has happened before, and the cleanest case is color. Discovering that red is a wavelength of electromagnetic radiation didn't change the experience of seeing a rose. But it ended, permanently, the claim that redness is *in* the rose. That's the primary/secondary quality distinction, one of the most consequential moves in modern philosophy, and physics delivered it. The experience stayed the same. The viable philosophy didn't. Relativity did something similar to absolute space, evolution to fixed essences. Each time, new science forced new philosophy, not as an optional upgrade, but as a correction.

That was a narrow case: one wrong claim killed by one physical discovery. I don't want to overextend it. The claim I'll be developing is not that neuroscience can settle philosophical questions as bluntly as wavelengths settled the primary/secondary quality distinction. It's that the physical structure of cognition should inform philosophical accounts of concepts, guide which questions are worth asking, and where the evidence is strong enough, constrain which answers are viable. That's a more patient process than the color case, and this series is the beginning of the exploration, not the end.

When it comes to the brain — the physical machinery that constitutes thought — philosophy has been slow to apply even the weaker version of this principle. We treat the messy reality of neurons as a mere implementation detail, like the wiring of a computer that doesn't change the logic of the software. But if the physical structure of cognition shapes what thought can be, then ignoring that structure isn't abstraction. It's a missed opportunity — to constrain accounts, yes, but also to explore: to let the structure of the substrate point us toward the right philosophical questions.

A note on method, before any of this gets read as a thesis hunting for examples.

This series reasons from neuroscience and mathematics forward, not from philosophical positions backward. I engage with ideas rather than with individual philosophers, and I don't attempt a survey of the literature. I'm asking what the science teaches us about what concepts actually are — their physical structure, their geometry, their boundaries — and then asking which philosophical tools, which approaches, which questions fit that picture. The questions philosophy poses about concepts, the way it manipulates them, the precision it demands of them: do these fit the shape of what concepts turn out to be? Where they don't, I want to explain the mismatch, and let the geometry suggest what to look for instead. This won't settle normative questions — neuroscience tells you what the brain does, not what rationality requires — and I'll be explicit about that boundary when we reach it.

What follows is a book-essay, written one chapter at a time, and the question it keeps coming back to is this:

*How much of meaning, belief, value, and judgment can be understood as movement through learned and evolved cognitive geometry, and where does that explanation stop?*

The "where does it stop" isn't a postscript — it's part of the question. A framework that explains everything explains nothing, and one thing I want to do as the geometric picture builds is stay alert to where the topology runs out and something else has to take over. The chapters that follow apply the picture to concepts, then to belief and credence, then to morality, and on into the shape of minds, the line between innate and learned geometry, evolution as a landscape, aesthetics, group cognition, what large language models reveal about the picture, and finally what would falsify it. The unifying claim is that something useful falls out of the substrate. The constraint built into the question is that what falls out has limits.

---

## 2. Finding Jennifer Aniston

In 2005, Quiroga et al. published a finding that seemed almost too clean to be true.[^hopfield-hebb-quiroga]

They were recording from single neurons in the hippocampus of patients preparing for epilepsy surgery when they found something strange: neurons that fired selectively for specific concepts.

One neuron fired furiously when the patient saw a photo of Jennifer Aniston. But this wasn't just a visual response. The same neuron lit up for the written text of her name. It fired for the sound of her voice. It fired for related audio cues. It even responded to her specific haircut.

It didn't fire for Julia Roberts, or the Eiffel Tower, or anything else.

This wasn't a celebrity fluke. They found similar neurons for the Sydney Opera House, for Luke Skywalker, and for the researcher himself. One neuron fired consistently whether the patient saw the researcher's face or simply heard his voice.

These neurons weren't coding for light or sound waves. They were coding for **meaning**, extracting an invariant concept that held steady regardless of whether it arrived via eyes, ears, or text.



Philosophers have theorized about concepts for centuries — from Plato's immaterial Forms, apprehended by pure reason beyond the senses, to Locke's "abstract general ideas," constructed by observing particulars and stripping away the circumstances of time, place, and individual difference to leave only what is common. These traditions disagreed sharply about where concepts come from. They agreed on what concepts have to *do*: capture the invariant behind variable experience. The concept-neuron findings give us a look at the machinery behind that end product — the mechanism that produces stable, cross-modal representations (representations that span different senses: sight, sound, language) that both traditions were trying to account for.

A word of caution before we go further. What we're looking at here is a simplified instance of the biology, not the full picture. The real neuroscience is messier, more distributed, and far less clean than a single neuron lighting up for a single person. But simplified instances are where understanding starts, and the question that matters is whether the core pattern, the thing the simplification reveals, survives when you add the complications back in. We'll keep testing that as we go.



Current science suggests these aren't "Grandmother cells," where a single neuron holds the entire concept of your grandmother. They're sparse, distributed populations.[^sparse-coding] For a simple object like a face, a small cluster of neurons fires in sync. For more complex ideas, the coalition might be larger and more spread out.

But the implication is stark: a concept is not a definition in a dictionary. It's a specific pattern in a physical network.

---

## 3. How neurons capture commonality

How could a concept, the most elusive entity in philosophy, be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

I started where researchers started: with models. How do neuroscientists think about what's happening in these networks? That question led me deep into Hebbian learning, and the math really helped my intuition. Math should always do that. In my case, it doesn't always.

A caveat. What I'm about to show you is a model — a spherical cow. Every science has these: physics has frictionless planes, economics has homo economicus. The Hopfield network is neuroscience's version. Real synaptic plasticity is far messier. But the model earns its keep the way good models do. The geometric structure it produces survives when you add the complications back in. We're looking for a way of modeling concept formation that holds up as the biology gets messier — and, as we'll see later, shows up in systems that have nothing to do with biology at all.

The core principle is simple: **neurons that fire together, wire together.**

This is **Hebbian learning**, named after the Canadian psychologist Donald Hebb. It's the brain's primary way of turning experience into structure.

To understand the "wiring," we have to look at the **synapse** — the microscopic gap where two neurons meet. They don't actually touch; one neuron sprays chemicals (neurotransmitters) across the gap to trigger the next.

The "strength" of a connection is just how likely one neuron is to make the other one fire. When two neurons fire in close temporal proximity — not necessarily at the same instant, but within a narrow window — the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen. The signal might also linger longer — chemicals could be cleared away more slowly, extending the window of influence. This is **synaptic plasticity**. (There are refinements, like the precise timing of firing affecting the strength of the change. For the model we're building, what matters is the core principle: *reliable temporal association strengthens connections*.) Like a path through the woods, the more a connection is used, the easier it is to travel. That physical strengthening is what we mean when we say neurons "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watched *Friends*, your brain processed her face (vision), her voice (audio), and her name (language) at the same time. Because these distinct neural populations fired together, the Hebbian rule kicked in. The synaptic connections between them strengthened. Over time, these inputs became tightly associated — not "wired together" in the sense of a fixed cable, but linked by strengthened pathways that made co-activation increasingly likely.

Trigger just one element — seeing the name "Jennifer" — and a cascade of signals flows through these reinforced pathways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the activation of this linked network, the same strengthened connections lighting up together.

But wait. If neurons that fire together wire together, wouldn't everything get wired to everything? If you're drinking coffee while watching *Friends*, does "coffee" become part of the Jennifer Aniston concept?

This is where the system's selectivity matters. The Jennifer Aniston neuron doesn't fire for *anything* associated with her — it fires for stimuli that reliably and repeatedly co-occur with the concept across many different contexts. Coffee might be present during one viewing and absent during the next ten. The connection never gets reinforced enough to stick. Her face, her voice, and her name appear together reliably. Those connections get strengthened over and over.

The network also pushes back. Neurons don't just excite each other — they quiet each other down. When the Jennifer Aniston coalition fires, it suppresses competing coalitions, like a conversation where one voice gets louder and the others fade. That sharpens the response: the concept activates cleanly rather than bleeding into everything nearby.

Here's the key move: the Hebbian rule automatically extracts what's common across experiences.

### The math

The math is worth the detour, because the simplicity is the point. The mechanism that produces concepts from neurons is not baroque or mysterious. It's almost trivially simple, and that simplicity matters.

A Hopfield network gives us the simplest model of this process. Imagine a network of neurons, each of which can be "on" (+1) or "off" (−1). Between every pair of neurons is a connection with a weight — a number that says how much they influence each other.

**The components:**

- **State**: what each neuron is doing right now (+1 or −1). For a network with *n* neurons, the state is a vector: **s** = (s₁, s₂, ..., sₙ).

- **Weights**: the fixed connections between neurons. The weight between neuron *i* and neuron *j* is written wᵢⱼ. These don't change during recall — they *are* the stored patterns.

- **Stored pattern**: a specific configuration of neural activity that the network has been wired to fall back into. To store a pattern **ξ** = (ξ₁, ξ₂, ..., ξₙ), we set the weights using the Hebbian rule.

**The Hebbian learning rule** is almost embarrassingly simple:

$$w_{ij} = \xi_i \cdot \xi_j$$

In plain English: if two neurons are the same in a pattern, connect them positively. If they're different, connect them negatively.

That's it. Same → +, different → −.

A positive link between two neurons makes them *want* the same sign. A negative link makes them *want* opposite signs.

**Storing multiple patterns** is just as simple. If you have *p* different patterns (ξ¹, ξ², ..., ξᵖ), you add up the contributions:

$$w_{ij} = \sum_{k=1}^{p} \xi_i^k \cdot \xi_j^k$$

Now here's the magic. Suppose you have three different experiences of Jennifer Aniston. Each time, some neurons are active (her face, her voice, the *Friends* theme) and others aren't. The Hebbian rule says: for each experience, strengthen connections between neurons that match and weaken connections between neurons that differ.

When you add up these contributions across all your experiences, the connections that survive are the ones that were consistent. If "face neurons" and "voice neurons" fired together every time you encountered Jennifer Aniston, their connection gets reinforced three times (+1 × +1 = +1, added three times = +3). If some irrelevant neuron — say, "coffee cup" — was on during one encounter and off during another, its contributions cancel out (+1 × +1 = +1, then +1 × −1 = −1; they sum toward zero).

The network doesn't store each experience separately. It stores what the experiences have in common. The "concept" emerges as the statistical residue of repeated co-activation.

To make this more concrete, I built a simulation where the Hebbian rule updates a small set of neurons based on input. You can watch the wiring happen in real time — see which connections strengthen and which fade as patterns repeat.

## Insert JA Neuron HTML Here

An insight that took me a while to grasp: **in a Hopfield network, "memory" and "concept" are mathematically the same thing.** Both are stable patterns the network settles into. A memory is a concept of a past experience. A concept is the memory of what many experiences had in common. The math doesn't distinguish between them â€” and that equivalence is itself interesting, but it's also where the spherical cow shows its limits most clearly.

Real brains *do* distinguish between memory and concepts. Patients who lose the ability to form new episodic memories can still retain old concepts. Patients with semantic dementia can lose concepts while still forming new episodic memories. If the Hopfield model were the whole story, this double dissociation would be inexplicable. It isn't the whole story. The brain uses different regions and consolidation pathways for episodic and semantic knowledge, and these are architectural features the simple model doesn't capture.

Notice what survives the complication. The geometric point — that learning from repeated experience produces attractor valleys with graded boundaries — doesn't depend on memory and concepts being stored in the same system. It depends on the learning mechanism. And the biology actually helps here. The leading account of how concepts form in real brains — complementary learning systems theory — proposes that the hippocampus rapidly encodes individual episodes while the cortex slowly extracts regularities across them through its own Hebbian-like consolidation process.[^cls] The two systems are architecturally separate, which is why they can break independently. The cortical pathway is still doing statistical extraction from repeated experience — still strengthening what recurs and letting what varies wash out — and that process carves the same topology: valleys, slopes, saddle points. The model is wrong about the plumbing. The shape survives because the slow cortical consolidation that actually builds concepts uses the same logic the model is built on, even though it runs in a different system on a different timescale.

### The landscape intuition

For simple concepts like "Jennifer Aniston," the Hebbian math works cleanly. Cognition, though, involves far more complex concepts — *justice*, *irony*, *home* — where the picture changes.

In these cases, you're not dealing with a handful of neurons switching on or off. You're dealing with billions of neurons, most of which are *always* active to some degree. The concept isn't "these neurons on, those neurons off." It's a *pattern*, ”a specific configuration across a vast, always-active network.

This is where simple weight matrices stop being enough. When everything is always firing, what matters is the *geometry* of how activations relate to each other. The concept becomes a region in a high-dimensional space, not a binary state. But critically, the mechanism remains identical, ”Hebbian learning still carves the structure. What changes is how we visualize it.

This is why we need the landscape metaphor,”and a new term: **attractor**.

An attractor is simply a state that a system naturally falls into and stays in. Drop a marble into a bowl, and it rolls to the bottom. That resting point is an attractor. The marble doesn't stay on the rim; it's *attracted* to the lowest point. In neural terms, an attractor is a stable pattern of activity that the network settles into when activated. Once the network reaches that pattern, it stays there, ”the neural equivalent of the marble at rest.

**Attractor dynamics** describe how the system moves toward these stable states. It's the rolling, not just the resting. When you see half of Jennifer Aniston's face, your neural network doesn't freeze at "half-recognized." It *moves*, ”activity flows through strengthened connections until the whole pattern completes. The dynamics are the journey; the attractor is the destination.

Think of the network's weights as carving a landscape of hills and valleys. Each pattern you store shapes the terrain, creating a valley that the network naturally falls into. Most critically for our topic, there are ridges between these valleys, and the shape of those ridges turns out to matter.

- **The weights** are the terrain, fixed after learning — the grooves carved into the landscape.
- **The state** is a marble rolling on that terrain, changing moment to moment.
- **Memories** are the valleys, the stable resting points the marble settles into.
- **A cue** is where you drop the marble.

To see this play out, you can interact with the visualization. Click to create valleys and watch "thoughts" settle into stable states.

$$INSERT HTML VISUALIZATION HERE: Interactive attractor landscape where readers can click to create valleys and watch "thoughts" settle into stable states.$$

The mathematics is simple. What it produces is more: a physical system that extracts abstract commonality from concrete experience, stores it as terrain, and retrieves it from partial information.

One thing worth saying out loud: nothing in this picture depends on neurons specifically. The geometry would have the same structural properties if it were running on silicon, or on some alien chemistry we haven't imagined. What matters (or so I'll argue) is the shape of the valleys, the gradients of the slopes, the saddle points between concepts. Neurons are how *we* happen to run the process. The geometry may be what the process has in common across all its possible substrates.

If that's right, then meaning has something like a physical address, not in a particular neuron, but in the shape of a landscape.

---

## 4. The attraction of fuzziness

The landscape we've just described has an immediate consequence: its concept-boundaries slope rather than drop.

This matters — and not because it tells us something we didn't already know. Anyone who has tried to define "game" at a dinner party already knows that natural concepts resist sharp definition. The observation is old. What the attractor framework adds is a *mechanical explanation* for it — one that predicts not just that definitions will fail, but *where* and *how* they'll fail, and what specific shape the failure will take.

In a neural network, a concept forms by carving out a valley through repetition. See enough chairs, and your brain carves a "Chair" valley. The valley has sloped sides. It isn't a binary box.

This is why definitional questions so often lead to silence, and why the silence has a characteristic pattern.

"What makes something a chair?"

"It has legs and you sit on it."

"A horse has legs and you sit on it. Is a horse a chair?"

"No, a chair is furniture."

"What makes something furniture?"

"It's... made for a home?"

"A doormat is made for a home. Is a doormat furniture?"

We stammer. We struggle because "chair" isn't defined by necessary and sufficient conditions. It's defined by the *shape* of an attractor valley, carved by every chair you've ever encountered, with boundaries that slope rather than drop.

This explains why so many definitional conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers sometimes treat it as an intellectual surrender, an admission that you can't *really* define the thing. But attractor theory suggests it might be the most honest answer possible. You *do* know it when you see it. Your neural network recognizes when a stimulus falls within a valley. What you can't do is articulate the valley's exact boundary, because there is no boundary, only a gradient where the gravity of the concept gets weaker.

Philosophers have noticed this before. Wittgenstein's "family resemblance," the ordinary language tradition's attention to how words actually behave, prototype theory in cognitive psychology, all of these recognized, in different ways, that natural concepts resist sharp definition and that their boundaries shift with context.[^family-prototype] The observation is well-established. So what's novel about the attractor picture?

The mechanism. These earlier accounts described the fuzziness. The attractor framework explains *why* it's there and predicts its specific shape. The learning process extracts statistical regularities, not necessary and sufficient conditions, and statistical regularities produce gradients, not edges. Context modulates the terrain: it primes certain neural populations, reshapes valley walls in real time, which is why concept boundaries shift depending on the situation. And the mechanism makes predictions the descriptions don't, about the *shape* of transitions, their path-dependence, their asymmetries, predictions that are testable.

If this picture is right, the fuzziness is doing real work. It's what lets us generalize, to recognize a beanbag as a chair, without learning a new rule for every object in the universe.

## 5. Reductionism?

A reasonable worry at this point: if concepts are attractor dynamics, have we explained them away? Reduced meaning to math, thought to topology?

No. The reason is more specific than the usual anti-reductionist move, and I want to be careful about what I'm claiming and what I'm not.

Start with what I'm *not* claiming. I'm not claiming that neurons are the key. Neurons are how we happen to run this process, but the argument doesn't depend on them. You could swap the neurons for silicon or for some alien chemistry and the argument would go through unchanged. Philosophy has known since the 1960s that the same mental function can run on different physical substrates — that studying the wiring diagram of the brain isn't the same as studying the mind. That insight was right. I'm not challenging it.

But here's what happened next, and this is the part I think went wrong. Philosophers heard "the substrate doesn't matter" and jumped straight to "so we can theorize about concepts at the level of propositions — definitions, necessary and sufficient conditions, binary predicates — without worrying about how the system that produces concepts actually works." That jump skipped a level.

There's an explanatory level between substrate and proposition. Call it the geometry. In the brain, and in the simple theoretical models we've been looking at, learning from experience seems to produce a recognizable topology: valleys with sloped sides, ridges between them, transition zones that are graded rather than sharp. The topology isn't the substrate. It doesn't care whether it's running on wet neurons or dry silicon. But it isn't at the level of definitions and logic either. It sits between them — a structure that emerges from the learning process itself.

We've seen analogous patterns outside neuroscience. Thermodynamics didn't replace the concept of energy, but once entropy was understood, it informed which engineering programs were worth pursuing — and eventually ruled out perpetual motion. Molecular biology didn't replace heredity, but once DNA was understood, blending inheritance was no longer a viable account. In both cases the phenomenon survived; certain explanations of it didn't.

The parallel isn't exact. The color case was a clean kill, and I don't claim the same bluntness here. The direction is the same: physical structure informing, guiding, and where the evidence is strong enough, constraining the viable accounts of a phenomenon. One feature of the claim matters enormously: the geometry survives as we add sophistication to the model. Start with the simplest Hopfield network, and you get valleys with sloped sides. Add biological realism, lateral inhibition, recurrent processing, neuromodulation, and the valleys get more complex. They're still valleys with sloped sides.

If the topology is robust across these variations, then it isn't an artifact of the simple model. It's a consequence of learning from experience. A later chapter will ask whether systems with entirely different substrates and learning dynamics — large language models trained by gradient descent on text — converge on similar geometries. If they do, the case for taking the topology seriously as a guide to philosophical questions gets considerably stronger.

The geometry shapes the phenomenology. The feeling of recognizing a chair, the stammer when asked to define one, the ease of border cases and the discomfort of forced binary choices: these are experiences of navigating the landscape. You feel the slopes. You feel the valley floor. You feel the saddle points. If the geometry has graded boundaries, the phenomenology will have them too. Not because neurons are messy — though they are. Because gradients are built into the topology itself.

So yes — abstract away from neurons. Abstract to the geometry, not past it. The philosophical tradition jumped from "substrate doesn't matter" to "propositions are the right level," and in doing so it skipped the level where the action is.

One caution. When I say "the geometry," I don't mean every detail of whichever model we happen to use. Some features of a geometric description are artifacts of the representation — the choice of coordinates, the exact distances, the specific axes. Those shift when you redraw the map. I'm not claiming that every knob on the model is philosophically load-bearing. I'm claiming that some of them are, and the next few sections will show which ones.

Concepts are real, and they operate at their own level. You can't derive a valid argument from the Hebbian learning rule. You can't get ethics from synaptic weights. But the topology of the landscape shapes what kinds of concepts the system can build. And if your philosophical framework assumes that learned concepts have sharp edges, it's assuming a geometry that the learning process can't produce. That's not an implementation detail. It's a substantive finding about the material that philosophical theories are theories *of* — the kind of finding that, in other domains, has eventually reshaped which accounts survive. The physics doesn't replace the subject matter. It can tell you something about its shape.

---

## 6. The mismatch

Here's the pattern worth naming: continuous landscapes resist discrete dissection. You can't carve a valley at its joints because it doesn't have joints.

But our primary tools for working with concepts — formal definitions, necessary and sufficient conditions, binary predicates, logical categories — are all dissection tools. They assume that concepts have edges. Sometimes they do. "Prime number" has a cliff for a wall: you're either divisible only by one and yourself, or you're not. "Triangle" has a cliff. Notice something about these examples: they're mathematical. Their boundaries are sharp because they were stipulated to be sharp. Someone decided what "prime" means, and the definition has no sloped sides because it was engineered not to. Mathematical concepts are constructed objects. Their edges are put there on purpose.

Natural concepts aren't like that. "Chair," "heap," "knowledge," "person," "harm" — nobody stipulated these. They were learned, carved out of experience by the Hebbian process we've been tracing. That process, as we've seen, produces valleys with sloped sides. It can't help it. When you learn from variable experience, what you get is a gradient, not a cliff.

And "experience" here extends further than it might seem. Some of our deepest attractor valleys — fear of snakes, face detection, basic intuitions about physical objects — look hardwired. They were carved by experience too, just not *yours*. Natural selection, operating over millions of generations, preserved organisms whose neural architecture responded to snakes and culled those that didn't. Over that timescale, the "snake = danger" attractor got carved into the genome itself, prewiring the synaptic connections that individual learning would otherwise have to build from scratch.[^snake-detection]

I've been using the word "learning" for the Hebbian process, and the snake-fear example just stretched it to cover natural selection too. There's a deeper story about why these are the same kind of process — about evolutionary change and neural learning both turning out, in our best models, to be forms of gradient descent on an objective function — but it belongs in the chapter on evolution as geometry, not here.[^evolution-gradient] For now, I only need the weaker point: some valleys are learned by a person, and some are inherited from populations that survived long enough to leave their shape behind. When I say "learning" from here on, I mean it as shorthand for any such process.

The resulting valley has the same broad geometry as an individually learned concept. Prepared fear and threat detection don't function as binary switches that fire for snakes and ignore everything else. They generalize along graded slopes: threat responses tend to weaken as a stimulus becomes less similar to the learned or prepared cue, and many generalization gradients are well modeled as bell-shaped rather than step-shaped.[^fear-generalization] In other perceptual domains, category transitions also show dynamical signatures such as hysteresis, where the boundary shifts depending on the direction of approach.[^category-hysteresis] These are the geometric signatures — graded boundaries, path-dependence, asymmetry — that attractor dynamics predict. Evolution produced some of them through a different mechanism than Hebbian learning, but the topology converged.

The mismatch between discrete tools and continuous landscapes isn't a quirk of individual learning. It's a feature of any process — personal or evolutionary — whose output is stable structure with graded boundaries.

The shape of the fear-generalization gradient tells us something precise about what sits between two concepts. Every concept the brain holds — whether learned in a lifetime or carved by evolution — has a generalization gradient that decays outward from its prototype. Where two such gradients overlap, where the pull from "snake" and the pull from "stick" are roughly equal, is the saddle point between them. Notice what a bell-shaped gradient implies about that region: the tails of the curves are the flattest part of the landscape. The closer you get to the saddle, the weaker the gravity from either side. That's the zone where categorization is hardest, where small perturbations could tip the state either way, and where asking "is this a snake or a stick?" has no clean answer — not because you haven't thought hard enough, but because you're standing in the flattest part of the terrain. We'll see shortly that this is exactly the zone where the oldest paradox in philosophy plants its flag.

The confusion between these two kinds of concepts is old. You can see it already in Socrates. Many of the early Socratic dialogues are, at bottom, a philosopher applying a sharp tool to sloped concepts and watching it fail. "What is piety?" "What is courage?" "What is temperance?" Every time, someone proposes a definition. Every time, Socrates finds a case that breaks it. The dialogues often end in puzzlement; nobody can produce the definition. (Plato does offer positive accounts elsewhere — the *Republic* builds toward a theory of justice — but even there, the definitional struggles along the way are instructive.) Some philosophers have read these failures as part of the philosophical process — the slow advance toward the right definition. Others, especially since Wittgenstein, have read them as evidence that sharp definitions were the wrong goal for natural concepts in the first place. The attractor framework is sympathetic to the second reading and adds something to it: a *specific account of why* the definitions fail. The tool doesn't fit the material — and we can now say what shape the material actually has. If piety and courage are attractor valleys carved by cultural experience, then looking for their sharp edges is looking for something that isn't there. The puzzlement isn't a failure of the participants. It might be a feature of the landscape.

Aristotle inherited the assumption that definitions should be findable, and built a system around it. His categories — genus, species, differentia — formalized the idea that the world comes pre-carved into kinds: every object belongs to exactly one species, defined by a set of essential properties that are both necessary and sufficient. A thing either is or isn't a mammal. It either is or isn't a substance. The categories are exhaustive (everything fits somewhere) and mutually exclusive (nothing fits in two places at once).

This framework worked brilliantly for the concepts it was designed around — geometric forms, logical classes, and biological species as Aristotle understood them. That last one is worth pausing on, because it's the example where history already ran the experiment. Aristotle looked at the living world and saw fixed, discrete kinds: horses are horses, dogs are dogs, and the boundaries between species are as sharp as the boundary between triangles and circles. For two thousand years, that seemed obviously right. Then Darwin showed it wasn't. Species are populations drifting through a continuous space of variation. The boundaries between them are real enough to be useful, but they're not sharp — they're exactly the kind of graded transitions that attractor geometry predicts. "When does a subspecies become a species?" is the biologist's version of "when does a hill become a mountain?" The attractor picture suggests the Aristotelian expectation was a generalization from a special case. Stipulated concepts have edges. Most learned concepts don't. And if the attractor picture is right, much of the philosophical tradition may have spent centuries trying to find edges on objects that slope.

What matters here is how biology advanced past Aristotle. It didn't find better boundaries. It dissolved the assumption that boundaries were the right thing to look for. The category system didn't get refined. It got replaced by a framework — population thinking — built for gradients rather than edges. That's the kind of move I'm suggesting philosophy needs to make with concepts more broadly.

The Aristotelian expectation survived its own best example. The definitional method that analytic philosophy inherited still rests on the assumption that concepts have edges — that there's always a set of properties that draws a clean line between what's in and what's out. Biology moved on. Whether philosophy needs to make a similar move, at least for learned, natural concepts, is the question this series is exploring.

---

## 7. Situating the argument

Many philosophers have already observed that natural concepts resist sharp definition. Wittgenstein's family resemblance, the ordinary language tradition, much of post-analytic philosophy have made this point in various ways.[^family-prototype] I'm not bringing news that concepts are fuzzy. What I want to show is that the best model we have for the physical origin of concepts — how they actually form in neural networks and, as we'll see, in other learning systems — gives rise to a specific geometry: attractor valleys with sloped sides, saddle-point boundaries, path-dependent transitions. That geometry doesn't just redescribe the fuzziness. It explains *why* concepts must be fuzzy when learned from experience, predicts specific features of the fuzziness that "concepts are vague" alone doesn't predict, and — if the geometry survives as we add sophistication to the biology — should inform and eventually guide which philosophical accounts of concepts are worth pursuing.

I should also be clear that none of this is new. The connectionists established that cognition is pattern-matching in networks. Paul Churchland argued that knowledge lives in high-dimensional activation spaces and described the brain's conceptual landscape in terms of attractor dynamics — hills and valleys sculpted by learning. Andy Clark's predictive processing framework describes the brain as minimizing prediction error, which is descent toward an energy minimum, and extends this into the structure of concepts themselves.[^churchland-clark] Between them, they built most of the machinery this chapter relies on.

What I'm trying to add is narrower: to extract one specific geometric consequence — that any system forming concepts through statistical extraction from experience will produce attractor valleys with graded boundaries — and trace what follows from it for the classical problems in epistemology. The geometry doesn't just say "concepts are vague." It says the vagueness has a specific shape: saddle-point transitions, not linear gradients; path-dependent boundaries that shift depending on direction of approach; asymmetric transitions where the path into a concept differs from the path out. These are specific predictions, distinct from what degree theories or family resemblance alone would give you, and the following chapters will test them against the phenomena. That's a claim about the topology of concepts, not about neurons. The connectionists opened the door. This project tries to walk through it.

---

## 8. The mismatch in action

To see the pattern concretely, consider the oldest example.

The Sorites Paradox — the Heap Paradox — goes like this. One grain of sand is not a heap. If something is not a heap, adding a single grain cannot make it a heap. Therefore, by induction, no number of grains is a heap. The conclusion is absurd, but every step seems valid.[^sorites-vagueness]

The paradox works because it's formulated in the language of sharp edges: a predicate ("is a heap") that has to be true or false, and a principle (one grain can't flip it) that exploits the absence of any boundary to flip at. It demands an edge. The concept doesn't have one.

In attractor terms, "heap" and "not-a-heap" are two valleys. Between them is a ridge, a transition zone where the landscape is nearly flat and a small perturbation could tip the state either way. There is no cliff between the valleys. There is a saddle. Adding grains of sand pushes the state up the slope of the "not-a-heap" valley, across the ridge, and down into "heap", but the crossing is gradual, and in the transition zone the state isn't clearly in either basin. There is no point where gravity switches. There is a region where it is ambiguous.

This is sympathetic, in many ways, to degree theories of vagueness, which replace true/false with a gradient from 0 to 1.[^sorites-vagueness] The attractor picture arrives at a similar place from a different direction, by showing that any system learning concepts from experience will produce transitions with this shape, rather than by stipulating that truth comes in degrees. The physical grounding matters because it opens the door to empirical tests. Does the transition zone between "heap" and "not-a-heap" show hysteresis — a shift in the boundary depending on which direction you approach from? Are the transitions between concepts asymmetric, with different profiles depending on the path? These are predictions the attractor framework inherits from the physics, and they're the kind of predictions that could, in principle, be tested experimentally. The geometric account doesn't replace existing theories of vagueness so much as offer a physical mechanism that explains why those theories describe what they describe.

So from the attractor perspective, the paradox isn't showing us that "heap" is a broken concept. It's showing us what happens when you insist on finding an edge in a landscape that slopes. Maybe the problem isn't the concept. Maybe it's the question.

The Sorites example is the geometry's clearest worked case. Specific features of the attractor framework — hysteresis, path-dependence, asymmetric transitions — make testable predictions about how the heap-to-not-a-heap transition should actually behave: boundaries shifting with the direction of approach; the flattest part of the landscape sitting exactly where the agonizing "is this still a heap?" moments cluster; small perturbations tipping the state precisely in the regions where the gravity from either basin is weakest. The paradox isn't a preview. It's the picture working. And the pattern it reveals — a discrete tool, a continuous landscape, an apparent paradox that's really an artifact of the mismatch — will show up again and again.



## 9. The road ahead

So here's where we are. If the picture I've been sketching is right, concepts are attractor valleys with sloped sides in any system that forms them through repeated exposure to patterns. And what we've been watching, in every example so far, is the same collision: discrete tools applied to continuous terrain. The suggestion, and at this stage it is still a suggestion, is that at least some of the paradoxes and tensions in the philosophical tradition aren't in the concepts themselves. They are artifacts of forcing binary distinctions onto a landscape that curves.

I should say what I think this framework *doesn't* do, because the absence might give the wrong impression. Not every concept looks like "chair" or "heap." Some seem to sharpen with expertise rather than staying fuzzy. Some moral judgments feel absolute. I don't think these are counterexamples, expertise deepens valleys and steepens walls without creating vertical cliffs, and moral certainty is a very deep valley, not a different kind of structure. But those claims need their own arguments, and I'll make them in later chapters rather than assert them here.

This also marks the boundary of the claim. The geometric constraints I've been tracing bear on similarity, categorization, and the shape of concept boundaries. They don't apply to questions of logical structure, truth conditions, or normative correctness. Whether an inference is *valid* or a concept is *correctly applied* involves considerations that geometry alone can't provide. The claim is that the geometry constrains the terrain on which those higher-level questions play out. It doesn't answer them.

The chapters that follow take this framework into the specific places it's most likely to bear weight.

Chapter 2 turns the geometry on belief and credence, asking why continuous confidence so often feels like a binary commitment.

Chapter 3 takes it into ethics: moral sentiments as attractor basins, culturally overlaid on evolutionary deep grooves, and the persistent failure to systematize ethics as the same mismatch in a new domain.

Chapter 4 asks what shape any cognition has to take when it runs on this kind of substrate, what embodiment, evolved geometry, and world-modeling impose on the form of thought itself.

Chapter 5 separates two questions the framework risks running together: what's carved by genes and what's carved by experience.

Chapter 6 develops the most ambitious move carefully, natural selection as gradient descent on a fitness landscape, with the basins evolution carves continuous with the basins individual learning carves.

Chapter 7 turns to aesthetics, asking what perceptual and cultural valleys look like when the question is what we find moving rather than what we find true.

Chapter 8 takes the geometry from individual to group cognition, and asks where the analogies between the two break.

Chapter 9 uses large language models as probes, not as evidence of shared geometry with human brains, but as a new way to experiment with what induced conceptual landscapes look like when you can train them, perturb them, and read them out.

Chapter 10 closes by asking what would falsify the picture. A framework that can absorb any result isn't doing any work, and I want to be specific about which results would tell me to stop.

The question I keep coming back to is simple, and I don't pretend to know the answer: if the geometry informs which accounts of concepts are viable, the way physical structure has informed viable accounts in other domains â€” then how many of philosophy's open problems are actually about the world, and how many are artifacts of trying to cut a continuous landscape at joints it doesn't have? The answer might be "fewer than I suspect." But the question seems worth taking seriously, and the geometry, I think, is the right place to look.


[^hopfield-hebb-quiroga]: Donald O. Hebb, *The Organization of Behavior* (1949); J. J. Hopfield, ["Neural networks and physical systems with emergent collective computational abilities"](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/) (1982), doi: [10.1073/pnas.79.8.2554](https://doi.org/10.1073/pnas.79.8.2554); Rodrigo Quian Quiroga, Leila Reddy, Gabriel Kreiman, Christof Koch, and Itzhak Fried, ["Invariant visual representation by single neurons in the human brain"](https://www.nature.com/articles/nature03687) (2005), doi: [10.1038/nature03687](https://doi.org/10.1038/nature03687).

[^sparse-coding]: For the "Jennifer Aniston neuron" result as sparse, explicit concept coding rather than literal one-cell-per-concept coding, see Rodrigo Quian Quiroga, ["Concept cells: the building blocks of declarative memory functions"](https://www.nature.com/articles/nrn3251) (2012), doi: [10.1038/nrn3251](https://doi.org/10.1038/nrn3251), and related reviews on sparse distributed coding in medial temporal lobe neurons.

[^hopfield-math]: The simple rule in the text is the one-pattern version of the Hopfield storage rule. For multiple stored patterns, the weights sum across patterns: $w_{ij} = \sum_k \xi_i^k \xi_j^k$. The main argument only needs the shape this produces.

[^cls]: James L. McClelland, Bruce L. McNaughton, and Randall C. O'Reilly, ["Why there are complementary learning systems in the hippocampus and neocortex"](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf) (1995). See also Randall C. O'Reilly, Rajan Bhattacharyya, Michael D. Howard, and Nicholas Ketz, ["Complementary Learning Systems"](https://cbmm.mit.edu/sites/default/files/documents/Week3_O-Reilly2014.pdf) (2014), doi: [10.1111/j.1551-6709.2011.01214.x](https://doi.org/10.1111/j.1551-6709.2011.01214.x).

[^evolution-gradient]: The full version belongs in the evolution chapter. The technical lineage includes George R. Price, "Selection and covariance" (1970), Russell Lande, "Quantitative genetic analysis of multivariate evolution, applied to brain:body size allometry" (1979), and later work connecting selection dynamics, adaptive landscapes, and gradient-like optimization under idealizing assumptions.

[^family-prototype]: Ludwig Wittgenstein develops the "family resemblance" point in *Philosophical Investigations* (1953). For prototype effects in cognitive psychology, see Eleanor Rosch, ["Cognitive representations of semantic categories"](https://doi.org/10.1037/0096-3445.104.3.192) (1975), doi: [10.1037/0096-3445.104.3.192](https://doi.org/10.1037/0096-3445.104.3.192).

[^snake-detection]: For the snake-detection literature, see Lynne A. Isbell, *The Fruit, the Tree, and the Serpent: Why We See So Well* (2009), and Vanessa LoBue and Judy S. DeLoache, ["Detecting the snake in the grass: Attention to fear-relevant stimuli by adults and young children"](https://doi.org/10.1111/j.1467-9280.2008.02081.x) (2008), doi: [10.1111/j.1467-9280.2008.02081.x](https://doi.org/10.1111/j.1467-9280.2008.02081.x).

[^fear-generalization]: For fear generalization gradients, see Joseph E. Dunsmoor and Rony Paz, ["Fear Generalization and Anxiety: Behavioral and Neural Mechanisms"](https://doi.org/10.1016/j.biopsych.2015.04.010) (2015), doi: [10.1016/j.biopsych.2015.04.010](https://doi.org/10.1016/j.biopsych.2015.04.010); Joseph E. Dunsmoor and Gregory L. Murphy, ["Categories, concepts, and conditioning: how humans generalize fear"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4318701/) (2015), doi: [10.1016/j.tics.2014.12.003](https://doi.org/10.1016/j.tics.2014.12.003); and Jessica C. Lee, Llewellyn Mills, Brett K. Hayes, and Evan J. Livesey, ["Modelling generalisation gradients as augmented Gaussian functions"](https://doi.org/10.1177/1747021820949470) (2021), doi: [10.1177/1747021820949470](https://doi.org/10.1177/1747021820949470).

[^category-hysteresis]: For hysteresis and related dynamical effects in categorization, see Betty Tuller, Paula Case, Mingzhou Ding, and J. A. Scott Kelso, ["The nonlinear dynamics of speech categorization"](https://pubmed.ncbi.nlm.nih.gov/8133223/) (1994), doi: [10.1037/0096-1523.20.1.3](https://doi.org/10.1037/0096-1523.20.1.3).

[^churchland-clark]: For Churchland's state-space account of concepts, see Paul M. Churchland, *A Neurocomputational Perspective: The Nature of Mind and the Structure of Science* (1989), and *Plato's Camera: How the Physical Brain Captures a Landscape of Abstract Universals* (2012). For predictive processing, see Andy Clark, ["Whatever next? Predictive brains, situated agents, and the future of cognitive science"](https://doi.org/10.1017/S0140525X12000477) (2013), doi: [10.1017/S0140525X12000477](https://doi.org/10.1017/S0140525X12000477), and *Surfing Uncertainty: Prediction, Action, and the Embodied Mind* (2016).

[^sorites-vagueness]: For the Sorites paradox and major approaches to vagueness, including degree-theoretic approaches, see Dominic Hyde and Diana Raffman, ["Sorites Paradox"](https://plato.stanford.edu/entries/sorites-paradox/) in the *Stanford Encyclopedia of Philosophy*, and Roy Sorensen, ["Vagueness"](https://plato.stanford.edu/entries/vagueness/) in the *Stanford Encyclopedia of Philosophy*.
