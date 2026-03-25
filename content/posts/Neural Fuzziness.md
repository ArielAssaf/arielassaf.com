# Neural Fuzziness, Concepts, and the Epistemology of Logic

## 1. Introduction: The Physical Address of a Thought

My interest in the intersection of neuroscience and philosophy started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

I was reading about "concept neurons"—and I remember the jolt of realizing that something as abstract as *the concept of a specific person* could be pinned to a specific coalition of cells firing in the medial temporal lobe. It felt like finding the physical address of a ghost.

I followed this curiosity into the underlying mathematics—Hopfield networks, attractor dynamics. At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But when I worked through the math, something shifted. The equations were simple—embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. If neurons work this way, then *of course* concepts emerge. The math didn't ask me to accept the findings on faith. It showed me why they had to be true.

This highlighted a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. But the biological matter that generates these concepts is messy, plastic, and inherently fuzzy.

This has happened before. Relativity dissolved the absolute space and time that philosophy had taken for granted. Evolution showed that species don't have fixed essences—that sharp category boundaries are things we impose on a continuous process. Quantum mechanics made randomness fundamental, not a sign of ignorance. Each time, new physics forced new philosophy—not as an optional upgrade, but as a correction.

Yet when it comes to the "wetware" of the brain—the physical machinery (substrate) that actually produces thought—philosophy has been remarkably slow to absorb the implications. We treat the messy reality of neurons as a mere implementation detail—like the wiring of a computer that doesn't change the logic of the software. But if our concepts are physically instantiated in this messy, fuzzy way, shouldn't that change our philosophies of truth and logic?

This essay is the foundation for a series. I'll walk through the neuroscience and the mathematics, and arrive at a claim I think has teeth: that concepts are attractor valleys with sloped sides, not boxes with sharp edges—and that a surprising number of philosophy's classic puzzles come from ignoring that shape. Subsequent essays will push this into vagueness, epistemology, ethics, and what large language models might teach us about concept geometry.

---

## 2. The Neurology: Finding Jennifer Aniston

In 2005, Quiroga et al. made a discovery that sounded like science fiction.

They were recording from single neurons in the human hippocampus (in patients preparing for epilepsy surgery) when they found something strange: neurons that fired selectively for specific concepts.

One neuron fired furiously when the patient saw a photo of Jennifer Aniston. But this wasn't just a visual response. The same neuron lit up for the written text of her name. It fired for the sound of her voice. It fired for related audio cues. It even responded to her specific haircut.

It didn't fire for Julia Roberts, or the Eiffel Tower, or anything else.

This wasn't a celebrity fluke. They found similar neurons for the Sydney Opera House, for Luke Skywalker, and even for the researcher himself. One neuron fired consistently whether the patient saw the researcher's face or simply heard his voice.

These neurons weren't coding for light or sound waves. They were coding for **meaning**—extracting an invariant concept that held steady regardless of whether it arrived via eyes, ears, or text.

Philosophers have theorized about the nature of concepts for centuries—from Plato's immaterial Forms, apprehended by pure reason beyond the senses, to Locke's "abstract general ideas," constructed by observing particulars and stripping away the circumstances of time, place, and individual difference to leave only what is common. These traditions disagreed—sharply—about where concepts come from. But they agreed on what concepts have to *do*: capture the invariant behind variable experience. What the concept neuron findings give us is a look at the machinery behind that end product—the mechanism that actually produces the stable, cross-modal representations that both traditions were trying to account for.

Current science suggests these aren't "Grandmother cells"—where a single neuron holds the entire concept of your grandmother. Instead, they are sparse, distributed populations. For a simple object like a face, a small cluster of neurons fires in sync. For more complex ideas, the coalition might be larger and more spread out.

But the implication is stark: a concept is not a definition in a dictionary. It's a specific pattern in a physical network.

---

## 3. The Mechanism: How Neurons Capture Commonality

How could a concept—the most elusive entity in philosophy—be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

To understand this, I started where researchers started: with models. How do neuroscientists think about what's happening in these networks? That question led me deep into Hebbian learning—and the math really helped my intuition, something it should always do, but does not often enough in my case.

The core principle is simple: **Neurons that fire together, wire together.**

This is known as **Hebbian learning**, named after psychologist Donald Hebb. It is the brain's primary way of turning experience into structure.

To understand the "wiring," we have to look at the **synapse**. This is the microscopic gap where two neurons meet. They don't actually touch; instead, one neuron sprays chemicals (neurotransmitters) across the gap to trigger the next one.

The "strength" of a connection is simply how likely one neuron is to make the other one fire. When two neurons fire at the same time, the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen. The signal might also linger longer—the chemicals could be cleared away more slowly, extending the window of influence. This is **synaptic plasticity**. Like a path through the woods, the more a connection is used, the easier it is to travel. This physical strengthening is what we mean when we say they "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watch *Friends*, your brain processes her face (vision), her voice (audio), and her name (language) simultaneously. Because these distinct neural populations fire at the same time, the Hebbian rule kicks in. The synaptic connections between them strengthen. Over time, these inputs become physically linked.

Trigger just one element—seeing the name "Jennifer"—and a cascade of signals flows through these reinforced pathways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the activation of this linked network—the same strengthened connections lighting up together.

But wait. If neurons that fire together wire together, wouldn't everything get wired to everything? If you're drinking coffee while watching *Friends*, does "coffee" become part of the Jennifer Aniston concept?

This is where the system's selectivity matters. The Jennifer Aniston neuron doesn't fire for *anything* associated with her—it fires for stimuli that reliably and repeatedly co-occur with the concept across many different contexts. Coffee might be present during one viewing, but absent during the next ten. The connection never gets reinforced enough to stick. Meanwhile, her face, her voice, and her name appear together reliably. Those connections get strengthened over and over.

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

$$w\_{ij} = \sum\_{k=1}^{p} \xi_i^k \cdot \xi_j^k$$

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

We stammer. We struggle because "chair" isn't defined by necessary and sufficient conditions. It's defined by the *shape* of an attractor valley—carved by every chair you've ever encountered, with boundaries that slope rather than drop.


This explains why so many definitional conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers sometimes treat it as an intellectual surrender—an admission that you can't *really* define the thing. But attractor theory suggests it might be the most honest answer possible. You *do* know it when you see it. Your neural network recognizes when a stimulus falls within a valley. What you can't do is articulate the valley's exact boundary, because there is no boundary—only a gradient where the gravity of the concept gets weaker.

Wittgenstein noticed something similar. His concept of "family resemblance"—the idea that category members share overlapping similarities rather than a single defining feature—is a philosophical description of what attractor valleys produce. But Wittgenstein went further than mere overlap: he insisted that the resemblances are fluid and context-dependent, that the boundaries of a concept shift depending on the language game being played. This maps naturally onto attractor geometry. The landscape isn't static. Context modulates the terrain—priming certain neural populations, adjusting effective connection strengths, reshaping the valley walls in real time. The "same" concept can have different boundaries in different contexts not because the word is ambiguous, but because the attractor geometry is dynamic.

If this picture is right, fuzziness isn't a bug. It's the feature that lets us generalize—to recognize a beanbag as a chair—without learning a new rule for every object in the universe.

## 5. Reductionism?

At this point a reasonable worry: if concepts are attractor dynamics, have we explained them away? Reduced meaning to math, thought to topology?
No. But the reason is more specific than the usual anti-reductionist move, and I want to be careful about what I'm claiming — and what I'm not.
Start with what I'm not claiming. I'm not claiming that neurons are the key. Neurons are how we happen to run this process, but the argument doesn't depend on them. You could swap the neurons for silicon or for some alien chemistry and the argument would go through unchanged. Philosophy has known since the 1960s that the same mental function can run on different physical substrates — that studying the wiring diagram of the brain isn't the same as studying the mind. That insight was right. I'm not challenging it.
But here's what happened next, and this is the part I think went wrong. Philosophers heard "the substrate doesn't matter" and jumped straight to "so we can theorize about concepts at the level of propositions — definitions, necessary and sufficient conditions, binary predicates — without worrying about how the system that produces concepts actually works." And that jump skipped a level.
There's an explanatory level between substrate and proposition. Call it the geometry. When any system forms concepts by extracting statistical regularities from experience — neurons, transistors, whatever — it produces a specific topology: valleys with sloped sides, ridges between them, transition zones that are graded rather than sharp. That topology isn't the substrate. It doesn't care whether it's running on wet neurons or dry silicon. But it isn't at the level of definitions and logic either. It sits between them — a structure that emerges from the learning process and constrains what the phenomenology can look like.
This is the claim that matters: the geometry shapes the phenomenology. The feeling of recognizing a chair, the stammer when asked to define one, the ease of border cases and the discomfort of forced binary choices — these are experiences of navigating the landscape. You feel the slopes. You feel the valley floor. You feel the saddle points. If the geometry has graded boundaries, then the phenomenology will have them too — not because neurons are messy (they are, but that's beside the point), but because gradients are built into the topology itself.
So yes — abstract away from neurons. But abstract to the geometry, not past it. The philosophical tradition jumped from "substrate doesn't matter" to "propositions are the right level," and in doing so it skipped the level where the constraints actually live. Concepts are real, and they operate at their own level. You can't derive a valid argument from the Hebbian learning rule. You can't get ethics from synaptic weights. But the topology of the landscape constrains what kinds of concepts the system can build. And if your philosophical framework assumes that learned concepts have sharp edges, it's assuming a geometry that the learning process can't produce. That's not an implementation detail. That's a constraint the philosophy has to respect.

## 6. The Mismatch

Here's the pattern worth naming: continuous landscapes resist discrete dissection. You can't carve a valley at its joints because it doesn't have joints.

But our primary tools for working with concepts—formal definitions, necessary and sufficient conditions, binary predicates, logical categories—are all dissection tools. They assume that concepts have edges. Sometimes they do. "Prime number" has a cliff for a wall—you're either divisible only by one and yourself, or you're not. "Triangle" has a cliff. But notice something about these examples: they're mathematical. Their boundaries are sharp because they were stipulated to be sharp. Someone decided what "prime" means, and the definition has no sloped sides because it was engineered not to. Mathematical concepts are constructed objects. Their edges are put there on purpose.

Natural concepts aren't like that. "Chair," "heap," "knowledge," "person," "harm"—nobody stipulated these. They were learned, carved out of experience by the Hebbian process we've been tracing. And that process, as we've seen, produces valleys with sloped sides. It can't help it. When you learn from variable experience, what you get is a gradient, not a cliff.

And "experience" here extends further than it might seem. Some of our deepest attractor valleys — fear of snakes, face detection, basic intuitions about physical objects — look hardwired. But they were carved by experience too, just not *yours*. Natural selection is Hebbian learning at an evolutionary timescale: organisms that responded to snakes survived and reproduced; those that didn't were selected out; and over millions of iterations, the "snake = danger" attractor got carved into the genome rather than into individual synapses. The valley is just as sloped — innate snake fear generalizes to garden hoses and coiled ropes, exactly as you'd predict from a graded attractor. The mismatch between discrete tools and continuous landscapes isn't a quirk of individual learning. It's a feature of any system — personal or evolutionary — that builds concepts by statistical extraction.

The confusion between these two kinds of concepts is old—and it has a name. Aristotle's system of categories (genus, species, differentia) was built on the assumption that nature comes pre-carved into kinds: that every object belongs to exactly one species, defined by a set of essential properties that are both necessary and sufficient. A thing either is or isn't a mammal. It either is or isn't a substance. The categories are exhaustive—everything fits somewhere—and mutually exclusive—nothing fits in two places at once. 

This framework worked brilliantly for the concepts it was designed around—geometric forms, logical classes, and biological species as Aristotle understood them. That last one is worth pausing on, because it's the example where history already ran the experiment. Aristotle looked at the living world and saw fixed, discrete kinds: horses are horses, dogs are dogs, and the boundaries between species are as sharp as the boundary between triangles and circles. For two thousand years, that seemed obviously right. Then Darwin showed it wasn't. Species are populations drifting through a continuous space of variation. The boundaries between them are real enough to be useful, but they're not sharp—they're exactly the kind of graded transitions that attractor geometry predicts. "When does a subspecies become a species?" is the biologist's version of "when does a hill become a mountain?" The attractor picture suggests this expectation was a generalization from a special case. Stipulated concepts have edges. Most learned concepts don't. And the philosophical tradition has spent centuries trying to find edges on objects that slope.

What matters for our argument is not just that Aristotle was wrong about species—it's how biology advanced past him. It didn't find better boundaries. It dissolved the assumption that boundaries were the right thing to look for. The category system didn't get refined. It got replaced by a framework—population thinking—that was built for gradients rather than edges. That's exactly the kind of move I'm suggesting philosophy needs to make with concepts more broadly. 

And yet the Aristotelian expectation survived its own best example. The definitional method that analytic philosophy inherited still rests on the assumption that concepts have edges—that there's always a set of properties that draws a clean line between what's in and what's out. Biology moved on. Philosophy, in this respect, hasn't.


## 7. Situating the Argument

I should be clear: none of this is new. The groundwork was laid decades ago, and it matters where this essay sits relative to it.

The **connectionist** movement of the 1980s (Rumelhart, McClelland) argued that cognition is pattern-matching in neural networks, not symbol manipulation. This was a paradigm-level claim, and it generated fierce debate—but the philosophical implications were largely treated as a problem for cognitive science, not for epistemology proper.

**Paul Churchland's** neurosemantics went further, arguing that knowledge is best understood as a position in a high-dimensional vector space rather than a set of propositions. Churchland was closer to what I'm arguing here, and I think he was largely right. But his framework predated the concept neuron findings and the modern understanding of attractor dynamics, and it was (perhaps unfairly) dismissed alongside eliminative materialism's more radical claims.

**Andy Clark** and the predictive processing framework describe the brain as minimizing "prediction error"—which is another way of describing descent toward an energy minimum. The mathematical connection to attractor dynamics is direct, though Clark's emphasis is on perception and action rather than on the structure of concepts per se.

Something like: "The dismissal followed the pattern we traced in section 5 — substrate doesn't matter, so the findings were filed under implementation details.

I think that dismissal was premature—but I also think the connectionists made it easy. They won an important argument: that cognition is pattern-matching in networks, not symbol manipulation. But they fought the battle on cognitive science's turf, not philosophy's. They described a substrate—small artificial networks—and showed it could do pattern-recognition. What they didn't do is extract the general geometric consequence: that any system forming concepts through statistical extraction from experience will produce attractor valleys with graded boundaries. That's a claim about the topology of concepts, not about neurons—and it's the claim that bears on epistemology. The connectionists opened the door but stopped on the threshold. This series tries to walk through it.

## 8. The Mismatch in Action

To see the pattern concretely, consider the oldest example.

The Sorites Paradox—the Heap Paradox—goes like this. One grain of sand is not a heap. If something is not a heap, adding a single grain cannot make it a heap. Therefore, by induction, no number of grains is a heap. The conclusion is absurd, but every step seems valid.

The paradox works because it's formulated in the language of sharp edges: a predicate ("is a heap") that has to be true or false, and a principle (one grain can't flip it) that exploits the absence of any boundary to flip at. It demands an edge. The concept doesn't have one.

In attractor terms, "heap" and "not-a-heap" are two valleys. Between them is a ridge—a transition zone where the landscape is nearly flat and a small perturbation could tip the state either way. There is no cliff between the valleys. There is a saddle. Adding grains of sand pushes the state up the slope of the "not-a-heap" valley, across the ridge, and down into "heap"—but the crossing is gradual, and the exact point where gravity switches depends on the shape of the terrain, which varies from person to person and context to context.

This might sound like the degree theories of vagueness, which replace true/false with a gradient from 0 to 1. The attractor picture is sympathetic but says something different — the transition isn't a smooth linear slide. It has a specific shape, carved by learning, that varies between people. More on that distinction in the next essay.

So the paradox isn't showing us that "heap" is a broken concept. It's showing us what happens when you insist on finding an edge in a landscape that slopes. The problem isn't the concept. It's the question.

The next essay develops this properly—including how the saddle-point picture differs from existing responses to Sorites (degree theories, supervaluationism). But the point for now is just to see the pattern: a discrete tool, a continuous landscape, and an apparent paradox that's really an artifact of the mismatch. That same pattern, I'll argue, shows up again and again.

## 9. The Road Ahead

So here's where we are. Concepts are attractor valleys with sloped sides — in any system that forms them through repeated exposure to patterns. And what we've been watching, in every example so far, is the same collision: discrete tools applied to continuous terrain. The paradoxes and tensions aren't in the concepts themselves. They're artifacts of forcing binary distinctions onto a landscape that curves.

I should say what I think this framework *doesn't* do, because the absence might give the wrong impression. Not every concept looks like "chair" or "heap." Some seem to sharpen with expertise rather than staying fuzzy. Some moral judgments feel absolute. I don't think these are counterexamples — expertise deepens valleys and steepens walls without creating vertical cliffs, and moral certainty is a very deep valley, not a different kind of structure. But those claims need their own arguments, and I'll make them in later essays rather than assert them here.

The next essays push this framework into specific philosophical problems: vagueness and the Sorites paradox, where the saddle-point geometry makes testable predictions about the shape of transition zones; the relationship between belief and credence, where attractor depth might explain why continuous confidence feels binary; Humean ethics, where moral sentiments look like culturally carved attractors with overlapping boundaries; and the question of substrate-generality — whether systems that form concepts through entirely different mechanisms (large language models, say) converge on the same representational geometry. That last question is important, because if the topology holds even when the dynamics differ, then the geometric constraints on concepts are deeper than neuroscience. They're structural consequences of learning from experience, full stop.

The question I keep coming back to is simple, and maybe a little unsettling: how many of philosophy's open problems are actually about the world, and how many are artifacts of trying to cut a continuous landscape at joints it doesn't have?
