# Neural Fuzziness, Concepts, and the Epistemology of Logic

## 1. Introduction: The Physical Address of a Thought

My interest in the intersection of neuroscience and philosophy started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

I was reading about "concept neurons"—and I remember the jolt of realizing that something as abstract as *the concept of a specific person* could be pinned to a specific coalition of cells firing in the medial temporal lobe. It felt like finding the physical address of a ghost.

I followed this curiosity into the underlying mathematics—Hopfield networks, attractor dynamics. At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But when I worked through the math, something shifted. The equations were simple—embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. If neurons work this way, then *of course* concepts emerge. The math didn't ask me to accept the findings on faith. It showed me why they had to be true.

This highlighted a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. But the biological matter that generates these concepts is messy, plastic, and inherently fuzzy.

Science has a history of pulling the rug out from under philosophy. Relativity dissolved the absolute space and time that Newton had taken for granted. Evolutionary biology undermined the idea that species have fixed essences, showing that sharp category boundaries are human impositions on a continuous process. Quantum mechanics introduced irreducible randomness into the foundations of physics, upending two centuries of confidence that the universe was deterministic. In each case, new physical facts forced new conceptual frameworks—not as optional upgrades, but as corrections to philosophies that had been built on physics that turned out to be wrong.

Yet when it comes to the "wetware" of the brain—the physical machinery (substrate) that actually produces thought—philosophy has been remarkably slow to absorb the implications. We treat the messy reality of neurons as a mere implementation detail—like the wiring of a computer that doesn't change the logic of the software. But if our concepts are physically instantiated in this messy, fuzzy way, shouldn't that change our philosophies of truth and logic?

This piece is my inquiry. I'll walk through the neuroscience, the mathematics, and then push toward application—because the nature of a substrate shapes and constrains what can be built on it, and I suspect philosophy has been ignoring this particular substrate for too long.

---

## 2. The Neurology: Finding Jennifer Aniston

In 2005, Quiroga et al. made a discovery that sounded like science fiction.

They were recording from single neurons in the human hippocampus (in patients preparing for epilepsy surgery) when they found something strange: neurons that fired selectively for specific concepts.

One neuron fired furiously when the patient saw a photo of Jennifer Aniston. But this wasn't just a visual response. The same neuron lit up for the written text of her name. It fired for the sound of her voice. It fired for the *Friends* theme music. It even responded to her specific haircut.

It didn't fire for Julia Roberts, or the Eiffel Tower, or anything else.

This wasn't a celebrity fluke. They found similar neurons for the Sydney Opera House, for Luke Skywalker, and even for the researcher himself. One neuron fired consistently whether the patient saw the researcher's face or simply heard his voice.

These neurons weren't coding for light or sound waves. They were coding for **meaning**—extracting an invariant concept that held steady regardless of whether it arrived via eyes, ears, or text.

Philosophers have theorized about the nature of concepts for centuries—from Plato's immaterial Forms, apprehended by pure reason beyond the senses, to Locke's "abstract general ideas," constructed by observing particulars and stripping away the circumstances of time, place, and individual difference to leave only what is common. These traditions disagreed—sharply—about where concepts come from. But they agreed on what concepts have to *do*: capture the invariant behind variable experience. What the concept neuron findings give us is a look at the machinery behind that end product—the mechanism that actually produces the stable, cross-modal representations that both traditions were trying to account for.

Current science suggests these aren't "Grandmother cells"—where a single neuron holds the entire concept of your grandmother. Instead, they are sparse, distributed populations. For a simple object like a face, a small cluster of neurons fires in sync. For more complex ideas, the coalition might be larger and more spread out.

But the implication is stark: a concept is not a definition in a dictionary. It's a specific pattern in a physical network.

---

## 3. The Mechanism: How Neurons Capture Commonality

How could a concept—the most elusive entity in philosophy—be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

To understand this, I started where researchers started: with models. How do neuroscientists think about what's happening in these networks? That question led me deep into Hebbian learning—and the math really helped my intuition, something it should always do but not often enough for me.

The core principle is simple: **Neurons that fire together, wire together.**

This is known as **Hebbian learning**, named after psychologist Donald Hebb. It is the brain's primary way of turning experience into structure.

To understand the "wiring," we have to look at the **synapse**. This is the microscopic gap where two neurons meet. They don't actually touch; instead, one neuron sprays chemicals (neurotransmitters) across the gap to trigger the next one.

The "strength" of a connection is simply how likely one neuron is to make the other one fire. When two neurons fire at the same time, the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen. The signal might also linger longer—the chemicals could be cleared away more slowly, extending the window of influence. This is **synaptic plasticity**. Like a path through the woods, the more a connection is used, the easier it is to travel. This physical strengthening is what we mean when we say they "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watch *Friends*, your brain processes her face (vision), her voice (audio), and her name (language) simultaneously. Because these distinct neural populations fire at the same time, the Hebbian rule kicks in. The synaptic connections between them strengthen. Over time, these inputs become physically linked.

Trigger just one element—seeing the name "Jennifer"—and a cascade of signals flows through these reinforced pathways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the activation of this linked network—the same strengthened connections lighting up together.

But wait. If neurons that fire together wire together, wouldn't everything get wired to everything? If you're drinking coffee while watching *Friends*, does "coffee" become part of the Jennifer Aniston concept?

This is where the system's selectivity matters. The Jennifer Aniston neuron doesn't fire for *anything* associated with her—it fires for stimuli that reliably and repeatedly co-occur with the concept across many different contexts. Coffee might be present during one viewing, but absent during the next ten. The connection never gets reinforced enough to stick. Meanwhile, her face, her voice, and her name appear together every single time. Those connections get strengthened over and over.

The network is also actively inhibitory. Neurons don't just excite each other—they suppress each other. When the Jennifer Aniston coalition fires, it actively inhibits competing coalitions. This sharpens the response: the concept activates cleanly rather than bleeding into everything nearby.

Here's what makes this profound: the Hebbian rule automatically extracts what's common across experiences.

#### The Math

The math here is worth the detour, because its simplicity is the point. The mechanism that produces concepts from neurons is not baroque or mysterious. It's almost trivially simple—and that simplicity is itself philosophically significant.

A key insight that took me a while to grasp: **in a Hopfield network, "memory" and "concept" are mathematically the same thing.** Both are stable patterns the network settles into. A memory is a concept of a past experience. A concept is the memory of what many experiences had in common. The math doesn't distinguish between them—and that equivalence is itself interesting, even though real brains turn out to be messier. (Patients who lose the ability to form new memories can still retain old concepts, and vice versa—so the biology clearly has more moving parts than the model.)

A Hopfield network gives us the simplest model of this process. Imagine a network of neurons, each of which can be "on" (+1) or "off" (−1). Between every pair of neurons is a connection with a weight—a number that says how much they influence each other.

**The key components:**

- **State**: What each neuron is doing right now (+1 or −1). For a network with *n* neurons, the state is a vector: **s** = (s₁, s₂, ..., sₙ)

- **Weights**: The fixed connections between neurons. The weight between neuron *i* and neuron *j* is written wᵢⱼ. These don't change during recall—they *are* the stored patterns.

- **Stored pattern**: A specific configuration of neural activity that the network has been wired to fall back into. If we want to store a pattern **ξ** = (ξ₁, ξ₂, ..., ξₙ), we set the weights using the Hebbian rule.

**The Hebbian learning rule** is almost embarrassingly simple:

$$w_{ij} = \xi_i \cdot \xi_j$$

In plain English: if two neurons are the same in a pattern, connect them positively. If they're different, connect them negatively.

That's it. Same → +, different → −.

A positive link between two neurons makes them *want* the same sign. A negative link makes them *want* opposite signs.

**Storing multiple patterns** is just as simple. If you have *p* different patterns (ξ¹, ξ², ..., ξᵖ), you add up the contributions:

$$w_{ij} = \sum_{k=1}^{p} \xi_i^k \cdot \xi_j^k$$

Now here's the magic. Suppose you have three different experiences of Jennifer Aniston. Each time, some neurons are active (her face, her voice, the *Friends* theme) and others aren't. The Hebbian rule says: for each experience, strengthen connections between neurons that match and weaken connections between neurons that differ.

When you add up these contributions across all your experiences, the connections that survive are the ones that were consistent. If "face neurons" and "voice neurons" fired together every time you encountered Jennifer Aniston, their connection gets reinforced three times (+1 × +1 = +1, added three times = +3). But if some irrelevant neuron (say, "coffee cup") was on during one encounter and off during another, its contributions cancel out (+1 × +1 = +1, then +1 × −1 = −1... they sum toward zero).

The network doesn't store each experience separately. It stores what the experiences have in common. The "concept" emerges as the statistical residue of repeated co-activation.

To try and make this more concrete, I built a simulation where the Hebbian rule updates a small set of neurons based on input. You can watch the wiring happen in real time—see which connections strengthen and which fade as patterns repeat.

{{< simulation src="/simulations/JA_sim.html?v=2" title="Hebbian wiring simulator" height="620" >}}

#### The Landscape Intuition

For simple concepts like "Jennifer Aniston," the Hebbian math works cleanly. But cognition involves far more complex concepts—*justice*, *irony*, *home*—where the picture changes.

In these cases, you're not dealing with a handful of neurons switching on or off. You're dealing with billions of neurons, most of which are *always* active to some degree. The concept isn't "these neurons on, those neurons off." It's a *pattern*—a specific configuration across a vast, always-active network.

This is where simple weight matrices stop being enough. When everything is always firing, what matters is the *geometry* of how activations relate to each other. The concept becomes a region in a high-dimensional space, not a binary state. But critically, the mechanism remains identical—Hebbian learning still carves the structure. What changes is how we visualize it.

This is why we need the landscape metaphor—and a new term: **attractor**.

An attractor is simply a state that a system naturally falls into and stays in. Drop a marble into a bowl, and it rolls to the bottom. That resting point is an attractor. The marble doesn't stay on the rim; it's *attracted* to the lowest point. In neural terms, an attractor is a stable pattern of activity that the network settles into when activated. Once the network reaches that pattern, it stays there—the neural equivalent of the marble at rest.

**Attractor dynamics** describes how the system moves toward these stable states. It's the rolling, not just the resting. When you see half of Jennifer Aniston's face, your neural network doesn't freeze at "half-recognized." It *moves*—activity flows through strengthened connections until the whole pattern completes. The dynamics are the journey; the attractor is the destination.

Think of the network's weights as carving a landscape of hills and valleys. Each pattern you store shapes the terrain—creating a valley that the network naturally falls into. Most critically for our topic, there are ridges between these valleys, and their shape turns out to be philosophically revealing.

- **The weights** are the terrain (fixed after learning)—the grooves carved into the landscape.

- **The state** is a marble rolling on that terrain (changes moment to moment).

- **Memories** are the valleys (stable resting points the marble settles into).

- **A cue** is where you drop the marble.


{{< simulation src="/simulations/attractor-landscape.html" title="Attractor landscape simulator" height="620" >}}

The mathematics is simple. But what it produces is not: a physical system that automatically extracts abstract commonality from concrete experience, stores it as terrain, and retrieves it from partial information.

One thing worth saying out loud: nothing in this picture depends on neurons specifically. The geometry would have the same properties if it were running on silicon, or on some alien chemistry we haven't imagined. What matters is the shape of the valleys, the gradients of the slopes, the saddle points between concepts. Neurons are how *we* happen to run the process. The geometry is the process itself.

This is how meaning gets a physical address.

## 4. The Attraction of Fuzziness

Why does this matter for philosophy?

For many reasons, but let's start with how it might explain why we can never quite define our terms.

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

This explains why so many definitional conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers sometimes treat it as an intellectual surrender—an admission that you can't *really* define the thing. But attractor theory suggests it might be the most honest answer possible. You *do* know it when you see it. Your neural network recognizes when a stimulus falls within a valley. What you can't do is articulate the valley's exact boundary, because there is no boundary—only a gradient where the gravity of the concept gets weaker.

Wittgenstein noticed something similar. His concept of "family resemblance"—the idea that category members share overlapping similarities rather than a single defining feature—is a philosophical description of what attractor valleys produce. But Wittgenstein went further than mere overlap: he insisted that the resemblances are fluid and context-dependent, that the boundaries of a concept shift depending on the language game being played. This maps naturally onto attractor geometry. The landscape isn't static. Context modulates the terrain—priming certain neural populations, adjusting effective connection strengths, reshaping the valley walls in real time. The "same" concept can have different boundaries in different contexts not because the word is ambiguous, but because the attractor geometry is dynamic.

If this picture is right, fuzziness isn't a bug. It's the feature that lets us generalize—to recognize a beanbag as a chair—without learning a new rule for every object in the universe.

## 5. Reductionism?

At this point the reductionist alarm should be ringing. If concepts are attractor dynamics, have we explained them away? Reduced meaning to math, thought to topology?

No. And the reason is simple. Describing the substrate of a concept doesn't eliminate the concept, any more than describing the acoustics of a concert hall eliminates the music. The relationships between concepts—the way they combine, support each other, conflict—are real features of the system, and they operate at their own level. You can't derive a valid argument from the Hebbian learning rule. You can't get ethics from synaptic weights.

What the neural picture *does* change is our expectations. If concepts are attractor valleys with sloped sides, we should stop being surprised when they don't have sharp boundaries. We should stop treating definitional failure as a philosophical crisis and start treating it as a predictable consequence of how concepts get built—in any substrate, by any system that learns by extracting what's common from experience. The emergence is real. But what emerges is constrained by how it emerges.

## 6. Vagueness Revisited: Hills, Mountains, and Transitions

Now we can approach the Sorites Paradox—the Heap Paradox.

- 1 grain of sand is not a heap.

- 2 grains are not a heap.

- ...

- At what exact number does it become a heap?

Logic fails here because it demands a binary switch. Attractor theory might not solve the problem, but it reframes it in a way that may be productive.

Philosophers have already proposed something in this neighborhood: degree theories of vagueness, where predicates like "heap" come in degrees of truth rather than being simply true or false. The attractor picture is sympathetic to this idea, but it offers something richer—not just degrees along a single slider, but a whole landscape with its own shape, one that varies from person to person and context to context.

Imagine two valleys side-by-side. One is "Non-Heap," the other is "Heap." Between them is a ridge—what topologists call a **saddle point**, a place where the landscape curves up in one direction and down in another. It's unstable: a marble perched there could roll either way.

As you add grains of sand, you're pushing the ball up the slope of the "Non-Heap" valley. There's no single point where it switches. There's a **transition zone**—the ridge—where the state is unstable. The neural network might flicker between the two concepts.

What the attractor framing adds beyond standard degree theory is structure: the transition isn't a smooth linear gradient from 0 to 1. It has a specific shape—steep on some axes, shallow on others—determined by the learning history that carved the valleys. Different people, with different experiences, will have differently shaped ridges. The "vagueness" isn't in the word or the world. It's in the geometry, and the geometry varies.

Vagueness, on this account, is the feeling of a neural state traversing a saddle point.

The same logic could apply to other classic puzzles:

- When does a hill become a mountain?

- When does a person become old?

- When does a collection of cells become a person?

I don't want to claim these puzzles are "solved." But they might be less mysterious when reframed this way. They might not be failures of language at all—just accurate descriptions of continuous landscapes being forced into discrete categories.

---

## 7. So What? Questions Worth Asking

If we take this seriously—that knowledge might be topology, not propositions—it opens questions worth pursuing in detail. Let me sketch three.

**Knowledge**

What would it mean to replace "justified true belief" with something like "stable attractor"? The standard philosophical definition of knowledge is a belief that is both true and justified. But if beliefs are valleys, what does "justified" mean? Perhaps it means the valley was carved by reliable processes—consistent experiences that track real patterns in the world. Or perhaps this whole translation is a category error. I'm not sure.

There's also the question of conviction. What makes us *feel* certain? Is certainty the depth of a valley? The steepness of its walls? I don't know, but I'd like to.

**Ethics**

We keep trying to build perfectly consistent ethical systems, and they keep generating paradoxes. The Trolley Problem may be less mysterious—and possibly more interesting—when seen as a topological ridge where conflicting moral attractor valleys meet. "Do no harm" and "minimize total harm" are each stable attractors; the trolley scenario places you on the saddle point between them. The discomfort isn't confusion. It's the instability of a state caught between two basins of attraction. This doesn't resolve the dilemma, but it suggests that searching for a single consistent moral principle may be like searching for a single valley in a landscape that has two.

**Experimental Philosophy?**

Large language models are, in a meaningful sense, synthetic systems with their own attractor landscapes. They form concepts through statistical extraction of invariants from data—structurally analogous to Hebbian learning, even if mechanistically different. We can probe their concept boundaries, map their transition zones, test whether their "vagueness" has the same topological structure as ours. This could constitute a genuine form of experimental philosophy: testing claims about the geometry of concepts in systems we can fully inspect. If LLM concept boundaries show the same saddle-point structure as human concepts, the case for topology-as-epistemology gets stronger—because the substrate is radically different, but the geometry converges.

---

## 8. Situating the Argument

I'm not the first to suggest these connections. The groundwork was laid decades ago, and it's worth being clear about where this essay sits.

The **connectionist** movement of the 1980s (Rumelhart, McClelland) argued that cognition is pattern-matching in neural networks, not symbol manipulation. This was a paradigm-level claim, and it generated fierce debate—but the philosophical implications were largely treated as a problem for cognitive science, not for epistemology proper.

**Paul Churchland's** neurosemantics went further, arguing that knowledge is best understood as a position in a high-dimensional vector space rather than a set of propositions. This is the closest ancestor to what I'm arguing here, and Churchland was largely right. But his framework predated the concept neuron findings and the modern understanding of attractor dynamics, and it was (perhaps unfairly) dismissed alongside eliminative materialism's more radical claims.

**Andy Clark** and the predictive processing framework describe the brain as minimizing "prediction error"—which is another way of describing descent toward an energy minimum. The mathematical connection to attractor dynamics is direct, though Clark's emphasis is on perception and action rather than on the structure of concepts per se.

Philosophy has largely treated these insights as implementation details—interesting neuroscience that doesn't bear on the "real" questions about truth, knowledge, and meaning.

I think that dismissal was premature. Not because neural implementation determines philosophical truth—the geometry, not the substrate, is the point—but because the topology that emerges from any concept-forming system constrains what concepts can do. If concepts are attractor valleys, they have graded boundaries. If they have graded boundaries, the search for necessary and sufficient conditions is not just difficult but misconceived. And if that search is misconceived, then a significant portion of analytic philosophy has been trying to flatten a landscape that is irreducibly curved.

The question I want to leave you with is whether studying the topology of concepts could make progress on puzzles that propositional approaches have been stuck on for centuries.
