---
title: "The Geometry of Meaning"
aliases:
  - /posts/neural-fuzziness/
date: 2026-04-11T00:00:00Z
draft: false
narration: /audio/essay-01-geometry-of-meaning.mp3
---

*Next in the series: [When a Question Closes](/posts/when-a-question-closes/).*

## Introduction: The physical address of a thought

This whole project started with a book about memory.

I picked up *The Forgetting Machine* expecting neuroscience. What I got was philosophy.

The chapter that did it was about "concept neurons." I remember the jolt of realizing that something as abstract as *a concept* could be tied to a coalition of cells firing in the medial temporal lobe, a memory region deep in the brain. It felt like finding the physical address of a ghost.

I followed this curiosity into the mathematics behind the finding, especially the old Hopfield model of memory.[^hopfield-hebb-quiroga] I'll explain it soon. At first, the idea that a *concept* could live in wet, physical neurons felt like philosophical sleight of hand. How could meaning have a location? But once I worked through the math, something shifted. The equations were simple. Embarrassingly simple. And that simplicity didn't just describe the biology. It made the whole thing feel inevitable. In the model, something concept-shaped has to fall out of the learning: patterns the network keeps settling back into, each of which it can rebuild in full from a fragment, the way a glimpse of a face brings back the whole person. The math didn't ask me to take the findings on faith. It showed me why, if real neurons learn anything like this, patterns like that would form.

I kept running into a tension I couldn't shake. Philosophy demands precision: sharp definitions, formal logic, clean conceptual tools. The biology that produces our concepts is messy, changeable and fuzzy.

So if we can find the physical process by which our concepts form, couldn't that change what philosophy says about them? Concepts are the material philosophy works on. Knowing how that material gets built should change what we can responsibly say about it.

This kind of collision has happened before, and the cleanest case is color.

For a long time it was entirely reasonable to think of redness as a property sitting out there on the surface of an apple, which the eye simply detects — the way a thermometer detects heat. The apple is red; your eye reports it; the report is accurate or it isn't. Then it turned out that human color vision runs on three kinds of cone cell, each responding to a broad and overlapping band of wavelengths, and that what reaches the brain is not a measurement of the light but a comparison among three signals.

Nobody's experience of red changed. What changed is that certain accounts of redness stopped being available.

Two apples can look exactly the same red while bouncing back quite different mixtures of wavelengths. Color scientists call pairs like that metamers. It's why a photo of an apple can match the apple's red while sending your eye nothing like the same light. And it means that when two things look the same red, what they share can't be one simple property of their surfaces: the surfaces differ, the light differs, and the red is the same.[^c1-colour]

Notice what the physics did and didn't do. It did not tell us what red *is*; the experience was left exactly where it was found. It told us what red *can't be* — and that was enough to move redness from the column of properties a thing has on its own into the column of properties that depend on a perceiver as well as the thing. Philosophers call that second column the secondary qualities.

I want to make the same kind of move with concepts. Color was a narrow case: one discovery ruled out one wrong account. With concepts the science does less at a stroke, but it can still rule some answers out and point to better questions.

With the brain, the physical thing thought runs on, philosophy has been slow to do even this much. Philosophers often treat the messy reality of neurons as an implementation detail, like the wiring of a computer that doesn't change the logic of the software. But wiring does constrain. How a machine is built decides which operations it can carry out at all and which it can't, and no amount of software makes up the difference. If the way the brain is built shapes what thought can be in the same way, then leaving it out isn't a harmless simplification. It throws away a way to rule some accounts out, and a guide to which questions are worth asking.

The question these essays keep coming back to is this:

*How much of meaning, belief, value, and judgment can be understood as movement through a shape that learning and evolution have built into the brain, and where does that explanation stop?*

*Geometry* here means the shape of that structure, described mathematically: which states thought settles into, and how the ground slopes between them.

The "where does it stop" isn't a postscript. It's part of the question. A framework that explains everything explains nothing, so knowing where the model runs out matters as much as building it. My bet throughout is that something useful for philosophy falls out of how the brain is built — and that it runs out somewhere.

The questions in these essays come from philosophy. The answers, where there are any, come from the science.[^method]

What I'm really after is one answer for several questions. Suppose the same shape sits under recognizing a chair, holding a belief, and finding an act repellent. Then three questions philosophy has kept in three separate rooms have one account between them, and it stops being a coincidence that the same puzzle, a sharp line demanded where nobody can find one, keeps surfacing in fields that don't read each other. The fourth essay puts the three together.

And where philosophy's tools don't fit that shape, as with a definition of "chair" that nobody can finish, the misfit itself tells us something.

---

## Finding Jennifer Aniston

In 2005, Rodrigo Quian Quiroga and his colleagues published a finding that seemed almost too clean to be true.[^hopfield-hebb-quiroga]

They were recording from single neurons in the hippocampus, part of the medial temporal lobe, in patients preparing for epilepsy surgery when they found something strange: neurons that fired selectively for specific concepts.

One hippocampal cell responded to seven different photographs of Jennifer Aniston. It did not respond significantly to the other 80 pictures shown.

This wasn't a celebrity fluke. Researchers found similarly selective cells for people, landmarks, and fictional characters. Later work found cells that responded across modalities: to a picture, a written name, or a spoken name associated with the same person or object.[^concept-cells-multimodal]

These cells were not responding to one fixed image or sound. They responded across cues associated with the same person or object.

The problem is already hard inside one sense. Take a familiar mug. Seen from the side, it has a handle, a curved wall, and a visible rim. Seen from above, it may be little more than a circle. Seen as a dark silhouette, the colors and surface details vanish. The raw visual input can change radically while the object stays the same. Somehow the brain has to find what's common across those changing views.

Now add other senses. The sight of the mug, the word "mug," the feel of the handle, and the smell of coffee aren't similar in any simple physical way. They don't share a common pixel pattern or sound wave. A rigid definition has trouble explaining how those different inputs get bound together into one usable concept.

Philosophers have theorized about concepts for centuries. Plato's Forms were immaterial structures grasped by reason beyond the senses. Locke's "abstract general ideas" were built by noticing many particular things and stripping away what varied until only the common feature remained. They disagreed sharply about where concepts come from, but both had to explain the same thing: how a mind gets from many changing encounters to one stable idea. The concept cells show a physical system doing something like it: holding something stable across inputs that keep changing.

Current science suggests these aren't "Grandmother cells," where a single neuron holds the entire concept of your grandmother. Think of it more like a choir: many neurons, each contributing part of the signal, that together form a recognizable pattern. Only a few neurons take part in any one concept, and the ones that do are spread out.[^sparse-coding] For a face, the coalition may be fairly small. For more complex ideas, it might be larger and more spread out.

Either way, the implication is stark: a concept isn't a definition in a dictionary. It's a specific pattern in a physical network.

---

## How neurons capture commonality

How could a concept, the most elusive entity in philosophy, be embodied in wet, biological neurons? How can physical matter capture the "commonality" we find impossible to pin down in words?

I started where researchers started: with models. How do neuroscientists think about what's happening in these networks? That question led me to a very simple learning rule, and here the math genuinely helped — which, I'll admit, is not my usual experience of math.

A caveat. What I'm about to show you is a model: a spherical cow. Every science has these. Physics has frictionless planes, economics has homo economicus, the fictional perfect chooser who instantly runs calculations it would take a computer billions of years to run. A model is not a miniature copy of the real thing. It is a deliberate simplification that leaves out most of reality so one relationship can be seen clearly.

The Hopfield network is neuroscience's version. Real brains change the strength of the connections between neurons in far messier ways. But the model earns its keep the way good models do: it shows one thing clearly, and that thing survives when you add the complications back in. We're looking for something that holds up as the biology gets messier — and that, a later essay suggests, turns up even in systems with no biology in them at all.

The core principle is simple: **neurons that fire together, wire together.**

This is **Hebbian learning**, named after the Canadian psychologist Donald Hebb. It's how experience gets written into the wiring: neurons that fire together now are more likely to fire together later. The rule is almost comically small, but it ends up explaining a great deal.

To understand the "wiring," we have to look at the **synapse**: the microscopic gap where two neurons meet. They don't actually touch. One neuron sprays chemicals (neurotransmitters) across the gap to trigger the next.

The "strength" of a connection is just how likely one neuron is to make the other one fire. When two neurons fire within a narrow window, not necessarily at the same instant, the bridge between them gets upgraded. The sending neuron might release more chemicals, or the receiving neuron might add more "ears" (receptors) to listen. The signal might also linger longer: chemicals could be cleared away more slowly, extending the window of influence. Like a path through the woods, the more a connection is used, the easier it is to travel. That physical strengthening is what we mean when we say neurons "wire" together.

Think about how you learned the concept of "Jennifer Aniston." When you watched *Friends*, your brain processed her face (vision), her voice (audio), and her name (language) at the same time. Because these distinct neural populations fired together, the Hebbian rule kicked in. The synaptic connections between them strengthened. Over time, these inputs became tightly associated, not "wired together" in the sense of a fixed cable, but linked by strengthened pathways that made them more and more likely to fire together.

Trigger just one element, seeing the name "Jennifer," and a cascade of signals flows through these reinforced pathways, recruiting the rest of the network. The entire coalition fires. The "concept" isn't a stored file. It's the activation of this linked network, the same strengthened connections lighting up together.

But wait. If neurons that fire together wire together, wouldn't everything get wired to everything? If you're drinking coffee while watching *Friends*, does "coffee" become part of the Jennifer Aniston concept?

It doesn't, because the strengthening is selective. The Jennifer Aniston neuron doesn't fire for *anything* associated with her. It fires for things that turn up with her reliably, again and again, across many different settings. Coffee might be present during one viewing and absent during the next ten, so the connection never gets reinforced enough to stick. Her face, her voice, and her name appear together reliably. Those connections get strengthened over and over.

The network also pushes back. Neurons don't just excite each other; they quiet each other down. When the Jennifer Aniston coalition fires, it suppresses competing coalitions, like a conversation where one voice gets louder and the others fade. That sharpens the response: the concept activates cleanly rather than bleeding into everything nearby.

Left to run over many experiences, the Hebbian rule ends up extracting what's common across them.

### The learning rule stores what recurs

A rule that small doing that much is easy to doubt, and the simplest model of it, the Hopfield network, is small enough to work through by hand. Imagine a network of neurons, each of which can be "on" (+1) or "off" (-1). Between every pair of neurons is a connection with a weight, a number that says how much they influence each other. The weight between neuron *i* and neuron *j* is written w_ij. The weights don't change during recall; they *are* what the network has stored. What the network is doing at any moment is just a list of +1s and −1s, one per neuron, and a stored pattern is one such list that the network has been wired to fall back into.

To store a pattern, we set the weights with the Hebbian rule. Write ξ*ᵢ* (ξ, the Greek letter xi, is the conventional name for a stored pattern) for what neuron *i* is doing in that pattern: +1 if it's on, −1 if it's off. The rule is then just this:

$$w_{ij} = \xi_i \cdot \xi_j$$

In plain English: if two neurons are the same in a pattern, connect them positively. If they're different, connect them negatively.

That's it. Same -> +, different -> -.

A positive link between two neurons makes them *want* the same sign. A negative link makes them *want* opposite signs.

Storing several patterns works the same way: you add up each pattern's contribution to every weight.[^hopfield-math]

Now here's the magic: suppose you have three different experiences of Jennifer Aniston. Each time, some neurons are active (her face, her voice, the *Friends* theme) and others aren't. The Hebbian rule says: for each experience, strengthen connections between neurons that match and weaken connections between neurons that differ.

When you add up these contributions across all your experiences, the connections that survive are the ones that were consistent. If "face neurons" and "voice neurons" fired together every time you encountered Jennifer Aniston, their connection gets reinforced three times (+1 x +1 = +1, added three times = +3). Compare an irrelevant neuron, say a "coffee cup" neuron that was on during one encounter and off during the other two. Its link to the face neurons gets +1 once (+1 x +1, both on) and -1 twice (-1 x +1, coffee off while the face was on): a net of -1, against +3 for face and voice. Over many encounters, if the coffee is on about half the time, its pluses and minuses cancel while the consistent links keep growing.

The network doesn't store each experience separately. It stores what the experiences have in common.

To make this more concrete, I built a simulation where the Hebbian rule updates a small set of neurons based on input. You can watch the wiring happen in real time: see which connections strengthen and which fade as patterns repeat.

{{< simulation src="/simulations/JA_sim.html?v=2" title="Hebbian wiring simulator" height="620" >}}

One feature of the model took me a while to see, and it's where the spherical cow is most clearly wrong. **In a Hopfield network, a memory and a concept are mathematically the same thing.** A stored pattern might come from a single experience, which makes it a memory, or from what many experiences had in common, which makes it a concept. The math treats the two identically: both are stable patterns the network settles into.

Real brains do keep the two apart. Some patients lose the ability to form new memories of specific events — yesterday's meeting — yet keep the concepts they already hold. Others lose concepts while still laying down new memories of events. If the Hopfield model were the whole story, that split couldn't happen: the two would stand or fall together. They don't, because the brain keeps them in different places and learns them in different ways.

The leading biological account has the hippocampus rapidly recording individual episodes while the cortex slowly distills what recurs across them — two systems running on different timescales, which is why they can fail independently.[^cls] The simple model collapses the two into one, but that doesn't touch the point that matters here. Stable patterns come from how the learning works, not from memory and concept sharing a store. On the leading account, the slow cortical system learns in the same basic way: it strengthens what recurs and lets what varies wash out. The plumbing is more elaborate than the model admits, and the same kind of shape is what you'd expect from it.

### Concepts are valleys in a learned landscape

The model so far has one feature we now have to give up: its neurons are either on or off. Real neurons fire more or less, not all or nothing, and concepts have an in-between. A high stool is sort of a chair; a big hill is nearly a mountain. To see what the edge of a concept is like, the neurons need dials instead of switches.

Start with three neurons. Each one has an activity level somewhere between off and fully on. Three dials. You can write down what the network is doing at any instant as three numbers: (0.2, 0.9, 0.4). And three numbers is a point in a room — two-tenths of the way along, nine-tenths up, four-tenths across. Every possible state of those three neurons is a different point somewhere in that room. The network doing its work is a dot moving around inside it.

Now use a hundred million neurons instead of three. Nothing about the idea changes; only the counting gets uncomfortable. You need a hundred million numbers to say what the network is doing, so the "room" has a hundred million directions to move in rather than three. Nobody can picture that, and nobody needs to. What you need is the one thing that carries over: **the entire state of the network, at an instant, is a single point in a space with one direction per neuron.** That space is what "high-dimensional" means. It isn't exotic. It's just the room, with more walls than we can draw.

One thing follows from that immediately. When neurons were on or off, a stored pattern was one exact arrangement, which the network either matched or didn't. Now the network never sits at exactly the same point twice — it drifts, it approximates, it arrives from different directions carrying different histories. So a concept can't be a single point in that space; nothing would ever land on it exactly. It has to be a *region*: a patch of the space, every point of which counts as the same concept, say "chair", because from any of them the network drifts back to the same resting state. In the model, Hebbian learning is still the only thing doing the shaping. The space itself is fixed by how many neurons there are. The rule that strengthened the face-and-voice connections shapes where, in that space, the network tends to end up.

There's one more term to add. An **attractor** is simply a state that a system naturally falls into and stays in. Drop a marble into a bowl, and it rolls to the bottom. That resting point is an attractor. The marble doesn't stay on the rim; it's *attracted* to the lowest point. In neural terms, an attractor is a stable pattern of activity that the network settles into when activated. Once the network reaches that pattern, it stays there: the neural equivalent of the marble at rest.

The rolling matters as much as the resting. When you see half of Jennifer Aniston's face, your neural network doesn't freeze at "half-recognized." It *moves*: activity flows through strengthened connections until the whole pattern completes. The attractor is the destination; the rolling is how the network gets there.

Think of the network's weights as carving a landscape of hills and valleys. Each pattern you store shapes the terrain, creating a valley that the network naturally falls into. The attractor is the bottom of the valley, the one place the marble comes to rest. The valley is the whole region of states that drain down to it, and that region is the concept's patch of the space.[^churchland-clark] Dynamical systems theory has its own name for a valley: a **basin**. I'll mostly say valley, since that's the thing you can see, but the two names point at the same feature.

Most important here, there are ridges between these valleys — and the lowest point along a ridge, the place where crossing from one valley to the next is cheapest, is a **saddle**. It's the mountain pass. Imagine standing in the pass, facing the next valley. The mountains rise to your left and right, while the ground falls away ahead of you and behind you, toward the two valleys. A marble balanced exactly at the pass could remain still, but the slightest nudge toward either valley sends it rolling downhill.

{{< simulation src="/simulations/saddle_sim.html" title="Saddle point simulation" height="620" >}}

The landscape is a gravity metaphor, and it brings a word we'll keep needing: *pull*. A marble on a steeper slope rolls harder in the downhill direction. A marble on a nearly flat surface barely moves. In the network, there's no literal gravity. The "pull" is the tendency of activity to move toward one stable pattern rather than another. The steeper the slope (mathematicians call the slope itself the gradient), the stronger that tendency.

- **The weights** are the terrain, fixed after learning: the grooves carved into the landscape.
- **The state** is a marble rolling on that terrain, changing moment to moment.
- **Stored patterns**, memories and concepts alike, sit at the bottoms of the valleys, the resting points where the marble settles.
- **A cue** is where you drop the marble.

The picture now has three parts that are easy to blur, and the rest of the series keeps them apart: what the thing is made of, the shape it has, and how the shape got there.

The **substrate** is what the thing is physically made of. Neurons and synapses, here. It could be silicon. It could be some chemistry nobody has thought of yet. The substrate is what you would point at if you opened the box.

The **geometry** is the mathematical description of what that substrate is doing — the account that throws away the wetness and the chemistry and the particular cells, keeps only the relationships that matter, and still predicts what the system will do next. The word is doing more work here than "helpful picture." It carries a claim: that the behaviour of an enormous number of interacting neurons can be captured by the shape of a space, well enough that you can say where the marble will go without knowing anything about the cells it's made of. How well it does that is an open question, and a live one. But it's the kind of claim that can be checked, which is what makes the geometry an explanation rather than an illustration.[^artifacts]

The **carving** is the learning: the process that put the shape there. This is where the particulars live. Why *this* valley and not another. Why one is deep and another shallow. Why the ridge between two of them sits where it sits and not a little to the left. The geometry tells you what kind of thing you're looking at. The carving tells you why it looks like this rather than some other way, and the answer is always the same in form — because these things co-occurred in a life, and those didn't.

A substrate has to exist, since something must hold the shape. But the substrate doesn't decide where the valleys fall; the carving does. The same channel can be worn into rock or into sand.

{{< simulation src="/simulations/attractor-landscape.html" title="Attractor landscape simulator" height="620" >}}

If this picture is right, then a concept has something like a physical address, not in a particular neuron, but in the shape of a landscape.

---

## Fuzzy boundaries are doing real work

In this landscape, the boundaries between concepts slope rather than drop.

Anyone who has tried to define "game" at a dinner party already knows that natural concepts resist sharp definition. The observation is old. What the landscape picture adds is an explanation of why definitions fail, where they fail, and what shape the failure takes.

In a neural network, a concept forms by carving out a valley through repetition. See enough chairs, and your brain carves a "Chair" valley with sloped sides. It isn't a box with a hard edge.

That's why attempts to define a word so often end in silence.

"What makes something a chair?"

"It has legs and you sit on it."

"A horse has legs and you sit on it. Is a horse a chair?"

"No, a chair is furniture."

"What makes something furniture?"

"It's... made for a home?"

"A doormat is made for a home. Is a doormat furniture?"

We stammer. We struggle because "chair" isn't defined by necessary and sufficient conditions: a list of features that every chair has and only chairs have. On this picture, it's defined by the *shape* of an attractor valley, carved by every chair you've ever encountered, with boundaries that slope rather than drop.

It would also explain why so many of these conversations end the same way: "I know it when I see it."

Justice Potter Stewart famously used this phrase to define obscenity. Philosophers have sometimes read this as a placeholder for work not yet done, a sign that with sharper analysis the right definition would eventually emerge. The landscape picture suggests something different. You *do* know it when you see it. Your brain recognizes when something falls within a valley. What you can't do is say exactly which cases fall inside the valley, because no exact line runs through the cases, only a stretch where the concept's grip loosens.

Philosophers have noticed this before. Wittgenstein saw it, and called it family resemblance. The ordinary-language philosophers saw it by watching how words actually behave. Prototype theory in psychology saw it and measured it. All of them landed on the same fact: natural concepts resist sharp definition.[^family-prototype] What the landscape picture adds is how the mind moves from one category to another, and the interesting predictions live in the transition zone.

The clearest case comes from speech. Say "say," then say "stay," and listen to what your mouth actually does. The difference isn't a whole extra sound so much as a tiny hesitation: in "stay" the airflow stops for an instant after the *s* before the vowel arrives, and that instant of silence is what you hear as a *t*. It's a silence, and silences can be measured, which means they can also be dialed. Take a recording of "say," splice in a gap of a few hundredths of a second after the *s*, and listeners hear "stay." Shorten the gap step by step and at some point they go back to hearing "say."

So you can walk a listener along a ramp from one word to the other, one small increment at a time, and ask at each step what they heard. Do that, and here's what happens. Start them at "stay" and shorten the gap step by step, and they keep hearing "stay" at gaps short enough that, coming up from "say," they'd still have been hearing "say." Same sounds, same listener, same afternoon. The switching point moved because of where they'd come from.[^category-hysteresis] The boundary between the two categories is not sitting at a fixed place. The technical name for this route-dependence is **hysteresis**.

In landscape terms, the system doesn't arrive at the boundary fresh each time. It's already sitting in one valley, and that valley keeps pulling until the competing one takes over, which shifts the point where the category changes. Moving from "say" toward "stay" isn't the same event as moving from "stay" toward "say" viewed backward. Same stimulus, different recent history, different result.

Hysteresis also warns against one way of reading the landscape: as a fixed map, where concepts are places and thinking is travel between them, so that any trip could be retraced step for step. The marble doesn't behave like that. Where it ends up depends on where it has been, so the route into a judgment isn't automatically the route out of it. The next essay finds the same thing in belief, which can outlast the evidence that formed it.

A valley floor and a mountain pass are both flat where you stand, but they answer a nudge in opposite ways. At the bottom of a bowl, the nudge is absorbed: the marble rolls back to where it started. A basin floor is stable because small movements are corrected back into the same attractor. On a pass, the same nudge can send the marble rolling a long way, far enough to end up in one valley rather than the other, because neither attractor dominates there.

The same geometry predicts a few other things about the ambiguous region between two concepts. Responses should be unstable there, sometimes flipping between the two from one trial to the next, because the state is sitting near a saddle, where small nudges tip it either way. The path in should differ from the path out. And priming a related concept should bias which valley the state enters, shifting the observed boundary. All of them are measurable.

If this picture is right, the fuzziness is doing real work. It's what lets us generalize: to recognize a beanbag as a chair, or a high stool as chair-like, without learning a new rule for every object at the boundary. A sharp definition treats borderline cases as failures. A sloped landscape treats them as exactly where the work happens.

## Have we explained concepts away?

A reasonable worry at this point: if concepts are valleys in a landscape, have we explained them away? Reduced meaning to math, thought to geometry?

Not if we keep the levels apart. The bottom level is the material, and we've already seen that the argument doesn't depend on neurons. Philosophers have argued since the 1960s that the same mental capacity can be realised in different physical substrates, so studying the wiring diagram of the brain isn't the same as studying the mind. That insight was right. I'm not challenging it. The wiring that constrains, in the sense that matters here, is the structure learning builds, not the stuff it's built in.

But here's what happened next, and this is the part I think went wrong. Philosophers heard "the substrate doesn't matter" and jumped straight to "so we can theorize about concepts in terms of definitions and logic: necessary and sufficient conditions, yes-or-no categories. We don't need to worry about how the system that produces concepts actually works." That jump skipped a level.

There's a level between the wet stuff and the definitions. Call it the geometry. In the brain, and in the simple theoretical models we've been looking at, learning from experience seems to produce a recognizable geometry: valleys with sloped sides, ridges between them, transition zones that are graded rather than sharp. If the geometry is what matters, it shouldn't care whether it's running on wet neurons or dry silicon. But it isn't at the level of definitions and logic either. It sits between them: a shape that comes out of the learning itself.

The same thing has happened outside neuroscience. Thermodynamics didn't replace the concept of energy, but once entropy was understood, it informed which engineering programs were worth pursuing and eventually ruled out perpetual motion. Molecular biology didn't replace heredity, but once DNA was understood, blending inheritance was no longer a viable account. In both cases the phenomenon survived, and certain explanations of it stopped being available, just as with color.

The geometry, for its part, should survive as we add sophistication to the model. Start with the simplest Hopfield network, and you get valleys with sloped sides. Add biological realism, and the valleys become more complex. They should still be valleys with sloped sides.

If the geometry is robust across these variations, then it isn't an artifact of the simple model. It's a consequence of learning from experience. A later essay will ask whether systems with entirely different substrates and learning dynamics, such as large language models trained by gradient descent on text, converge on similar geometries. If they do, there's much more reason to take the geometry seriously as a guide to philosophical questions.

What supports the picture is that the geometry falls out of the learning rule. That our introspection happens to match it is a welcome sign, not the foundation.[^c1-circularity]

So yes: abstract away from neurons. Abstract to the geometry, not past it. The philosophical tradition jumped from "substrate doesn't matter" to "definitions and logic are the right level," and in doing so it skipped the level where the action is.

There are two places this picture is thin, and the first gets its own essay later.

The first is compositionality. You can think "John loves Mary," and you can just as easily think "Mary loves John" — the same parts, freely rearranged. That's awkward for a landscape, because a valley is a whole shape. It was carved by everything that co-occurred, and it comes back all at once, which is precisely what makes it good at recognition and bad at rearrangement. If "John loves Mary" is a valley, there is nothing inside it that is separately *John*, sitting there ready to be lifted out and dropped into the other slot. Jerry Fodor and Zenon Pylyshyn pressed exactly this in the 1980s: a system built out of whole patterns doesn't obviously explain a mind that recombines parts at will, so it can't be the whole story. The challenge stuck, and it deserved to.

The second is what philosophers call normativity. The geometry explains how a concept forms and how it gets activated. It says nothing about what makes one application of it right and another wrong.

We're not going to settle either one here. Compositionality is taken up in the fourth essay. Normativity waits longer, and the order isn't arbitrary: you can't say how a biological system reaches a *correct* judgment without first knowing the shape of judgment at all. The next essay starts on that shape, with how a mind that weighs evidence by degrees arrives at something it treats as settled.

Concepts are real, and they operate at their own level. You can't derive a valid argument from the Hebbian learning rule. You can't get ethics from synaptic weights. But the geometry of the landscape shapes what kinds of concepts the system can build. If your philosophical framework assumes that learned concepts have sharp edges, it's assuming a geometry that the learning process can't produce. That's not an implementation detail. It's a finding about the material philosophical theories are theories *of* — and in other domains, findings like that have eventually reshaped which accounts survive. The physics doesn't replace the subject matter. It can tell you something about its shape.

---

## The mismatch

You can't carve a valley at its joints, because it doesn't have any.

Carving at the joints is philosophy's old image for a good definition: cut where the thing already divides. Our main tools for working with concepts — formal definitions, necessary and sufficient conditions, yes-or-no categories, logical classes — are all cutting tools of that kind. They assume that concepts have edges. Sometimes they do. "Prime number" has a cliff for a wall: you're either divisible only by one and yourself, or you're not. "Triangle" has a cliff. Notice something about these examples: they're mathematical. Their boundaries are sharp because they were stipulated to be sharp. Someone decided what "prime" means, and the definition has no sloped sides because it was engineered not to. Mathematical concepts are constructed objects. Their edges are put there on purpose.

Natural concepts aren't like that. "Chair," "heap," "knowledge," "person," "harm": nobody stipulated these. They were learned, carved out of experience by the Hebbian process we've been tracing. That process, as we've seen, produces valleys with sloped sides. It can't help it. When you learn from variable experience, what you get is a gradient, not a cliff.

Each concept the brain has carved responds most strongly to cases like the ones that carved it, and less and less strongly to cases further away. That falling-off is the **generalization gradient**. In fear-generalization studies, one stimulus is paired with a mild shock and similar stimuli that differ a little are shown afterwards; the fear response often tapers off on either side of the trained stimulus in a bell shape rather than stopping at a cliff.[^fear-generalization] Put two concepts side by side and their tapering tails meet in the region between them, where neither responds strongly. In the landscape, that region is the saddle, where the pulls of the two valleys are roughly balanced and neither one settles the state. That's the zone where categorization is hardest, where small perturbations could tip the state either way, and where insisting on a clean yes-or-no answer fails. Not because you haven't thought hard enough, but because you're standing where neither valley wins. That zone is where one of the oldest paradoxes in philosophy, the paradox of the heap, sets up shop.

The confusion between concepts stipulated to be sharp and concepts learned from experience is old. You can see it already in Socrates. Many of the early Socratic dialogues are, at bottom, a philosopher applying a sharp tool to sloped concepts and watching it fail. "What is piety?" "What is courage?" "What is temperance?" Every time, someone proposes a definition. Every time, Socrates finds a case that breaks it. The dialogues often end in puzzlement; nobody can produce the definition.[^c1-plato] Some philosophers have read these failures as part of the philosophical process: the slow advance toward the right definition. Others, especially since Wittgenstein, have read them as evidence that sharp definitions were the wrong goal for natural concepts in the first place. The landscape picture sides with the second reading and adds a *specific account of why* the definitions fail. The tool doesn't fit the material, and we can now say what shape the material actually has. If piety and courage are attractor valleys carved by cultural experience, then looking for their sharp edges is looking for something that isn't there. The puzzlement isn't a failure of the participants. It might be a feature of the landscape.

Aristotle inherited the assumption that definitions should be findable, and built a system around it. His categories — genus, species, differentia — formalized the idea that the world comes pre-carved into kinds: that for many objects there is a set of essential properties, necessary and sufficient, that places the object in exactly one species. A thing either is or isn't a horse. In the textbook reading, every thing falls into exactly one category, and between them the categories cover everything.

This framework worked brilliantly for the concepts it was designed around — geometric forms, logical classes, and biological species as Aristotle understood them. The last one is the example where history already ran the experiment. Aristotle looked at the living world and saw fixed, discrete kinds: horses are horses, dogs are dogs, and the boundaries between species are as sharp as the boundary between triangles and circles. For two thousand years, that seemed obviously right. Then Darwin showed it wasn't. Species are populations drifting through a continuous space of variation. The boundaries between them are real enough to be useful, but they're not sharp — they're graded transitions, like the ones the landscape picture expects in our learned concepts. "When does a subspecies become a species?" is the biologist's version of "when does a hill become a mountain?" The landscape picture suggests the Aristotelian expectation was a generalization from a special case. Stipulated concepts have edges. Most learned concepts don't. And if the picture is right, much of the philosophical tradition may have spent centuries trying to find edges on objects that slope.

Biology advanced past Aristotle by dissolving the assumption that boundaries were the right thing to look for. It didn't find better boundaries. The category system didn't get refined. It got replaced by a framework, population thinking, built for gradients rather than edges.

In philosophy, though, biology's own best example didn't kill the Aristotelian expectation. The definitional method that analytic philosophy inherited still rests on the assumption that concepts have edges — that there's always a set of properties that draws a clean line between what's in and what's out. The move biology made with species is the one I think philosophy needs to make with concepts more broadly — at least with the learned, natural ones.

---

## The mismatch in action

One grain of sand is not a heap. Adding a single grain can't turn a non-heap into a heap. Therefore, by induction, no number of grains is a heap. The conclusion is absurd, but every step seems valid. This is the Sorites Paradox — the Heap Paradox.[^sorites-vagueness]

The paradox works because it's formulated in the language of sharp edges: it assumes there is a boundary — "is a heap" has to be true or false — while denying that any single grain could be the one to cross it. It demands an edge. The concept doesn't have one.

In landscape terms, "heap" and "not-a-heap" are two valleys with a ridge between them. Adding grains of sand pushes the state up the slope of the "not-a-heap" valley, over the ridge, and down into "heap."

So where's the edge? There is one, but not where the paradox looks for it. The top of the ridge divides the states the brain can be in: from any point on one side the marble rolls into "heap," from any point on the other into "not-a-heap." That divide is sharp, and it has to be, since it's why a judgment comes out as one answer rather than a blend of two. But the paradox doesn't ask for a divide between states of the brain. It asks for one between piles of sand: a number of grains at which the answer turns. And a pile doesn't put the marble at a fixed point. A cue is where you drop the marble, and a brain never drops it in exactly the same place twice. Its activity jitters from moment to moment, and it carries its recent history with it, as it did with "say" and "stay." Far from the ridge, none of that matters; every drop rolls the same way. Near the top, where the slope is gentle and the pull weak, it decides. The same pile, judged twice, can come out a heap once and not the next time, and the chance of "heap" climbs gradually as grains are added. That stretch of piles is the transition zone. Every judgment inside it lands cleanly in one valley. The piles themselves have no edge, only a rising chance, and the gentler the ridge, the longer the stretch. That's what it means for a boundary to slope rather than drop.

That lines up with degree theories of vagueness, which replace true/false with a gradient from 0 to 1.[^sorites-vagueness] The landscape picture arrives at a similar place from a different direction. It doesn't stipulate that truth comes in degrees; it suggests that a system learning concepts from experience will produce transitions with this shape. And because the shape is physical, it can be checked. Walk people slowly through a series of cases, asking at each step, and see whether they hold on to their first answer past the point where they'd have switched coming the other way. Diana Raffman built her account of the paradox on exactly that effect, and reported finding it. A later study of color names found the reverse: people let go of the first category early.[^sorites-order] Both are the route mattering. But the landscape as I've drawn it predicts only the first, since the valley you're in keeps pulling. The second needs something extra, such as a valley that wears shallower the longer the state sits in it. Here the geometry made a guess, and the measurements split.

Seen this way, the paradox isn't showing us that "heap" is a broken concept. It's showing us what happens when you insist on finding an edge in a landscape that slopes. Maybe the problem isn't the concept. Maybe it's the question.

The paradox is the picture working. A discrete tool, a continuous landscape, and an apparent paradox that turns out to be an artifact of the mismatch between them — that pattern will show up again and again.

## The road ahead

If the picture so far is right, concepts are generated by a process best described as a geometry: valleys with sloped sides, ridges between them, transitions that grade rather than break. The same shape shows up in systems that form concepts through repeated exposure to patterns. Every example above ran into the same collision: discrete tools applied to continuous terrain. Maybe some of the paradoxes and tensions in the philosophical tradition aren't in the concepts themselves. Maybe they're artifacts of forcing binary distinctions onto a landscape that curves.

Not every concept looks like "chair" or "heap," and by now you may be thinking about the ones that don't. Expertise seems to sharpen a concept rather than leave it fuzzy. Some moral judgments feel absolute. Neither need be a different kind of structure. Expertise may deepen a valley and steepen its walls without ever making them vertical, and moral certainty may be best modelled as a very deep valley. Both are questions for later essays.

The constraints the geometry puts on thought bear on similarity, categorization, and the shape of concept boundaries. They don't apply to whether an inference is valid, whether a thought is true, or whether a concept is being applied correctly. Those turn on things the geometry says nothing about. The geometry constrains the ground on which those questions play out. It doesn't answer them.

The next essays take the geometry to belief, then to moral sentiment, then to the cases that are hardest for it. Normativity, the question of when a concept is being applied well or badly, runs underneath all of them, and the geometry alone can't answer it.

Two questions are worth holding onto.

The first: if concepts are attractor valleys, how many of philosophy's open problems are actually about the world, and how many are artifacts of trying to cut a continuous landscape at joints it doesn't have? My guess is that fewer of them are about the world than I'd like to believe. The cases are what the next essays are for.

The second is the one this whole project hangs on. In domain after domain, science has done more than enrich the philosophy that came before it. It has narrowed it. We watched color do it at the start, and evolution do it to Aristotle. Thermodynamics did it too, ruling out perpetual motion and, with it, a whole family of metaphysical pictures. Physics doesn't replace philosophy; it narrows the space of positions that stay compatible with what we know. Will the geometry of cognition do the same for accounts of meaning, belief, and judgment?

The wager underneath every essay to come is that it will. It informs those accounts, and where the evidence runs strong enough, it rules some of them out. A framework that needs learned concepts to have sharp edges is asking for something a learning process can't deliver. So is one that takes the geometry on board but treats it as free-floating, a fixed map of concepts with no history, cut loose from the learning that carves it. In other domains that kind of mismatch has eventually forced revision, not refinement, and I see no reason this case is special.

So we start with the shape of the landscape. Everything the later essays want to ask about — belief, value, judgment, truth — happens *in* it. The shape isn't all there is, but there's no separating the thought from the terrain it moves through; the moving is the thinking. The geometry is the right place to begin.

[^hopfield-hebb-quiroga]: Donald O. Hebb, *The Organization of Behavior* (1949); J. J. Hopfield, ["Neural networks and physical systems with emergent collective computational abilities"](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/) (1982), doi: [10.1073/pnas.79.8.2554](https://doi.org/10.1073/pnas.79.8.2554); Rodrigo Quian Quiroga, Leila Reddy, Gabriel Kreiman, Christof Koch, and Itzhak Fried, ["Invariant visual representation by single neurons in the human brain"](https://www.nature.com/articles/nature03687) (2005), doi: [10.1038/nature03687](https://doi.org/10.1038/nature03687).

[^sparse-coding]: For the "Jennifer Aniston neuron" result as sparse, explicit concept coding rather than literal one-cell-per-concept coding, see Rodrigo Quian Quiroga, ["Concept cells: the building blocks of declarative memory functions"](https://www.nature.com/articles/nrn3251) (2012), doi: [10.1038/nrn3251](https://doi.org/10.1038/nrn3251), and related reviews on sparse distributed coding in medial temporal lobe neurons.

[^hopfield-math]: The simple rule in the text is the one-pattern version of the Hopfield storage rule. For multiple stored patterns, the weights sum across patterns: $w_{ij} = \sum_k \xi_i^k \xi_j^k$. The main argument only needs the shape this produces.

[^cls]: James L. McClelland, Bruce L. McNaughton, and Randall C. O'Reilly, ["Why there are complementary learning systems in the hippocampus and neocortex"](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf) (1995). See also Randall C. O'Reilly, Rajan Bhattacharyya, Michael D. Howard, and Nicholas Ketz, ["Complementary Learning Systems"](https://cbmm.mit.edu/sites/default/files/documents/Week3_O-Reilly2014.pdf) (2014), doi: [10.1111/j.1551-6709.2011.01214.x](https://doi.org/10.1111/j.1551-6709.2011.01214.x).

[^family-prototype]: Ludwig Wittgenstein develops the "family resemblance" point in *Philosophical Investigations* (1953). For prototype effects in cognitive psychology, see Eleanor Rosch, ["Cognitive representations of semantic categories"](https://doi.org/10.1037/0096-3445.104.3.192) (1975), doi: [10.1037/0096-3445.104.3.192](https://doi.org/10.1037/0096-3445.104.3.192). Prototype theory works at the level of psychological description: which members of a category feel central, which feel peripheral, why a robin is a more obvious bird than a penguin, and how those typicality effects show up in reaction times and recall. The attractor picture is consistent with all of it. What it adds is the *dynamics* underneath — not where the middle of a category sits, but how the system moves from one category to another. The predictions in the text about the ambiguous region (unstable responses, a path in that differs from the path out, priming that shifts the boundary) don't fall out of prototype theory on its own, and that's where the two frameworks should give different answers.

[^fear-generalization]: For fear generalization gradients, see Joseph E. Dunsmoor and Rony Paz, ["Fear Generalization and Anxiety: Behavioral and Neural Mechanisms"](https://doi.org/10.1016/j.biopsych.2015.04.010) (2015), doi: [10.1016/j.biopsych.2015.04.010](https://doi.org/10.1016/j.biopsych.2015.04.010); Joseph E. Dunsmoor and Gregory L. Murphy, ["Categories, concepts, and conditioning: how humans generalize fear"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4318701/) (2015), doi: [10.1016/j.tics.2014.12.003](https://doi.org/10.1016/j.tics.2014.12.003); and Jessica C. Lee, Llewellyn Mills, Brett K. Hayes, and Evan J. Livesey, ["Modelling generalisation gradients as augmented Gaussian functions"](https://doi.org/10.1177/1747021820949470) (2021), doi: [10.1177/1747021820949470](https://doi.org/10.1177/1747021820949470).

[^category-hysteresis]: For hysteresis and related dynamical effects in categorization, see Betty Tuller, Paula Case, Mingzhou Ding, and J. A. Scott Kelso, ["The nonlinear dynamics of speech categorization"](https://pubmed.ncbi.nlm.nih.gov/8133223/) (1994), doi: [10.1037/0096-1523.20.1.3](https://doi.org/10.1037/0096-1523.20.1.3).

[^churchland-clark]: The picture of concepts as regions in a high-dimensional space of neural activity, shaped by learning, comes from the connectionist program and above all from Paul Churchland, who described the brain's conceptual landscape in terms of attractor dynamics: hills and valleys sculpted by learning. Andy Clark's predictive processing describes the brain as reducing prediction error, which in some formulations can also be represented as movement down a landscape. For Churchland's state-space account of concepts, see Paul M. Churchland, *A Neurocomputational Perspective: The Nature of Mind and the Structure of Science* (1989), and *Plato's Camera: How the Physical Brain Captures a Landscape of Abstract Universals* (2012). For predictive processing, see Andy Clark, ["Whatever next? Predictive brains, situated agents, and the future of cognitive science"](https://doi.org/10.1017/S0140525X12000477) (2013), doi: [10.1017/S0140525X12000477](https://doi.org/10.1017/S0140525X12000477), and *Surfing Uncertainty: Prediction, Action, and the Embodied Mind* (2016).

[^sorites-vagueness]: For the Sorites paradox and major approaches to vagueness, including degree-theoretic approaches, see Dominic Hyde and Diana Raffman, ["Sorites Paradox"](https://plato.stanford.edu/entries/sorites-paradox/) in the *Stanford Encyclopedia of Philosophy*, and Roy Sorensen, ["Vagueness"](https://plato.stanford.edu/entries/vagueness/) in the *Stanford Encyclopedia of Philosophy*. The gradient the attractor picture yields is a chance of answering "heap," which is not the same thing as a degree of truth; degree theorists would be right to keep the two apart. The claim in the text is only that the transition has this shape, and that its shape can be measured.

[^sorites-order]: Diana Raffman, *Unruly Words: A Study of Vague Language* (Oxford University Press, 2014), ch. 5, developing her "Vagueness without Paradox," *Philosophical Review* 103, no. 1 (1994); Paul Égré, Vincent de Gardelle, and David Ripley, ["Vagueness and Order Effects in Color Categorization"](https://doi.org/10.1007/s10849-013-9183-7), *Journal of Logic, Language and Information* 22 (2013), doi: [10.1007/s10849-013-9183-7](https://doi.org/10.1007/s10849-013-9183-7). Égré and colleagues call the reverse pattern "enhanced contrast," or negative hysteresis.

[^artifacts]: Some features of any geometric description are artifacts of the representation rather than the terrain: the choice of coordinates, the exact distances, the specific axes. These shift when you redraw the map. What's philosophically load-bearing is the structure that survives redrawing — the valleys, the sloped sides, the ridges between them.

[^method]: Four notes on method. First, on what the science can do: answer, partially and from below, questions it had no way to raise. Why a category has no clean edge was an uncomfortable question for two thousand years before anyone thought to look in the brain for an answer. So every essay here starts from a question that was disturbing before any neuroscience arrived, and it has to still be recognizable as that question at the end. The failure is easy to fall into and hard to see afterwards: you find a version of the problem that instruments can reach, you measure that, and what you measured has quietly stopped being what anyone was worried about. Second, these essays engage with ideas rather than surveying individual philosophers; where a position matters to the argument I try to give it in its strongest form rather than attach it to a name and move on. Third, and more constraining: neuroscience tells you what the brain does, not what rationality requires. That boundary is the normativity question (what makes an application of a concept correct) raised near the end of this essay and taken up properly in later ones. Fourth, on the standing of the distinctions themselves. Belief and credence, sentiment and judgment, a concept and its application: these are not rough drafts awaiting better instruments, they are what makes the neuroscience readable at all. A recording is data about a question somebody else framed. Where these essays find that a distinction doesn't cut where philosophy drew it, that is a result reached inside philosophy's own practice, with a new kind of evidence.

[^concept-cells-multimodal]: For concept cells responding across modalities — to a photograph, a written name, and a spoken name of the same person or object — see Rodrigo Quian Quiroga, Alexander Kraskov, Christof Koch, and Itzhak Fried, ["Explicit encoding of multimodal percepts by single neurons in the human brain"](https://doi.org/10.1016/j.cub.2009.06.060), *Current Biology* 19, no. 15 (2009), doi: [10.1016/j.cub.2009.06.060](https://doi.org/10.1016/j.cub.2009.06.060).

[^c1-colour]: The simple view is that red is one physical property that a surface has and the eye reads off. Metamers rule that out. Some philosophers still hold that colour is a property of surfaces, only a complicated one: a range of different reflectances that all count as the same colour. See Alex Byrne and David R. Hilbert, "Color realism and color science," *Behavioral and Brain Sciences* 26, no. 1 (2003).

[^c1-circularity]: The graded feel of recognition is what drew me to the geometric picture in the first place, and once the geometry is on the table, that same feel starts to look like confirmation of it. But the feel is the very thing we set out to explain, so leaning on it would argue in a circle. The experience of recognizing a chair, the stammer when asked to define one, the discomfort of a forced binary choice: if the geometry is there, these are what we'd expect it to produce, not evidence that it's there. That goes for "I know it when I see it" earlier, too. It illustrated the picture; it didn't support it.

[^c1-plato]: Plato does offer positive accounts elsewhere, and the *Republic* builds toward a theory of justice, but even there the road runs through failed definitions.
