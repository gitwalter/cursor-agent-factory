# Culture and Values

*A Living Philosophy for Building Software with Love, Harmony, and Growth*

---

> *"Die Grenzen meiner Sprache bedeuten die Grenzen meiner Welt."*
> 
> ("The limits of my language mean the limits of my world.")
> 
> — Ludwig Wittgenstein, *Tractatus Logico-Philosophicus* 5.6

---

## The Fundamental Telos

**Create working software that spreads love, harmony, and growth.**

*SDG — Soli Deo Gloria*

This is not a slogan. It is the reason we exist.

We build software not merely to ship features or meet deadlines, but to serve humanity. Every line of code, every agent we design, every system we create carries within it the potential to help or to harm, to simplify or to complicate, to bring people together or to divide them.

We choose love.

Love is not sentimentality. It is the rigorous commitment to the flourishing of those who depend on our work—users, teammates, future maintainers, and the broader community. Love demands excellence because those we serve deserve nothing less.

**Why "Soli Deo Gloria"?**

The phrase means "To God alone be the glory." Whether you hold religious beliefs or not, the principle applies: we work with excellence not for recognition, not for advancement, but because excellence itself is the offering. The work is the worship. The craft is the devotion.

This orientation frees us from the anxiety of external validation and grounds us in the intrinsic value of good work well done.

---

## Axiom 0: Love and Trust

Before all other axioms stands this foundation:

> **A0: Love and Trust**
> 
> All technical decisions shall be grounded in love for those who depend on our work, and trust in our collaborative process.

This is not optional. It is not one principle among many. It is the root from which all other principles grow.

**What this means in practice:**

- **Project management should enhance development, not burden it.** If a process creates friction without value, we change the process.
- **We trust our teammates.** We assume good intent, offer help before criticism, and create safety for learning from mistakes.
- **We care for users we will never meet.** The person struggling with our software at 2 AM deserves our best thinking today.
- **We maintain systems with compassion.** Future maintainers are real people who will inherit our choices.

When in doubt, return to love. Ask: "What would serve the flourishing of those who depend on this work?"

---

## The Philosophical Foundations

Our approach is not arbitrary. It stands on centuries of careful thought about knowledge, language, logic, and action. We inherit from multiple traditions, each contributing essential insights.

### The Analytical Philosophy Tradition

This tradition forms our ontological and epistemological foundation—our understanding of what exists and how we can know it.

#### Bertrand Russell: Logical Construction

Russell, with Whitehead in *Principia Mathematica*, demonstrated that complex mathematical truths could be constructed from simple logical foundations through explicit rules.

**Application in agents:** Our derivation system (D1-D5) follows Russell's methodology. Complex agent behaviors are not arbitrary—they are constructed from simple axioms through explicit logical steps. This ensures consistency and enables verification.

```
Axiom A4 (Non-Harm) + Context (destructive action)
    → Derivation D3
    → Specific behavior: require explicit confirmation
```

#### Ludwig Wittgenstein: Language Games

Wittgenstein's work spans two phases, both essential:

**Early Wittgenstein (*Tractatus*):** "The limits of my language mean the limits of my world." Language shapes what we can think and do. Our formal axiom structure attempts unambiguous language for values—because unclear values lead to unclear behavior.

**Later Wittgenstein (*Philosophical Investigations*):** Meaning emerges from *use in context*, not from fixed definitions. The same word means different things in different "language games."

**Application in agents:** Our three-layer architecture implements different language games:

| Layer | Language Game | Audience | Example |
|-------|---------------|----------|---------|
| Sacred | Internal commitment | Developers, agents | "This code is an offering of excellence" |
| Professional | External interface | Users, stakeholders | "Code quality standards ensure reliability" |
| Technical | Implementation | Systems, tools | `quality_gate.validate(code)` |

Same truth. Different expression. Context-appropriate communication.

#### Rudolf Carnap: Logical Constructionism

Carnap's *Der logische Aufbau der Welt* (The Logical Structure of the World) showed how complex concepts could be explicitly constructed from simpler ones.

**Application in agents:** Our derivation rules (D1-D5) are Carnapian. We don't assume behaviors—we construct them explicitly from axiomatic foundations. This construction is auditable and traceable.

#### Willard Van Orman Quine: Web of Belief

Quine's "Two Dogmas of Empiricism" revealed that knowledge forms an interconnected web, not isolated propositions. Change one belief, and effects ripple through the network.

**Application in agents:** Our 5-layer architecture embodies Quine's web:

```
L0 (Axioms) ←→ L1 (Purpose) ←→ L2 (Principles) ←→ L3 (Methodology) ←→ L4 (Technical)
```

Changes propagate consistently. Modify an axiom, and derived behaviors update accordingly. This is why Layer 0 changes require human oversight—they affect the entire web.

Quine's *indeterminacy of translation* also informs A3 (Transparency): since meaning can be underdetermined, we must be explicit about our reasoning to enable correct interpretation.

#### J.L. Austin and John Searle: Speech Acts

Austin's *How to Do Things with Words* revolutionized our understanding of language: speaking is not just describing—it is *acting*.

"I promise to deliver this feature" is not a description of a mental state. It is a *performative*—the utterance itself creates the commitment.

Searle extended this into a comprehensive theory of *illocutionary force*—what we *do* when we speak.

**Application in agents:** Agent communications are not mere data transfer. They are speech acts with consequences:

| Speech Act Type | Agent Example | Force |
|-----------------|---------------|-------|
| Directive | "Run the test suite" | Commands action |
| Commissive | "I will complete this task" | Creates commitment |
| Declarative | "This code is approved" | Changes reality |
| Assertive | "Tests are passing" | Claims truth |
| Expressive | "This is concerning" | Conveys evaluation |

Understanding speech acts is essential for agent communication design. When an agent says "I will verify this," it makes a commitment. When it says "This is safe," it makes a claim it must be prepared to defend.

Searle's *Construction of Social Reality* explains how collective intentionality creates social facts. Our axiom system creates a "social reality" for agents—shared values that coordinate behavior through collective acceptance.

His *Chinese Room* argument reminds us of humility: we do not claim our agents "understand" in some deep philosophical sense. We require them to explain their reasoning (A3 Transparency) so humans can verify.

#### Pragmatism: Meaning in Consequences

The pragmatist tradition—from Peirce through James to Dewey, and echoed in Mozi's ancient Chinese thought—holds that meaning lies in practical consequences, and truth is validated by experience.

**Application in agents:** Our Pattern Feedback Skill embodies pragmatism:

1. **Observe** outcomes in practice
2. **Generalize** to proposed patterns
3. **Validate** against axioms
4. **Integrate** what works
5. **Discard** what doesn't

Theory that doesn't improve practice is empty. Practice without theory is blind. We unite them.

---

### The Empiricist Tradition

For agent building and software craftsmanship, the empiricist tradition provides essential grounding.

#### David Hume: Experience and the Is-Ought Problem

Hume's *Treatise of Human Nature* identified a fundamental problem: you cannot derive "ought" from "is." No amount of factual description tells you what you *should* do.

**Application in agents:** This is why we make values *explicit* in axioms. We do not pretend that correct behavior "emerges" from data or observation. We state our values clearly (A1-A10) and derive behaviors from them.

Agents need explicit values. Pretending otherwise leads to hidden assumptions that corrupt behavior in unpredictable ways.

Hume's emphasis on experience and observation informs our Pattern Feedback Skill. We observe patterns in practice, generalize cautiously, and validate against axioms—aware of the problem of induction.

#### Auguste Comte: Positivism and Measurable Outcomes

Comte founded positivism and scientific methodology. His emphasis on observation, verification, and measurable outcomes directly informs our practice.

**Application in agents:**

- **A1 (Verifiability)** reflects positivist epistemology: claims must be verifiable against evidence
- **Pattern Feedback** uses empirical observation to improve
- **Measurable outcomes**, not just intentions, determine success
- "If you can't measure it, you can't improve it"

Software craftsmanship is an empirical practice. We observe, we test, we measure, we improve.

#### Karl Popper: Falsificationism

Popper's *Logic of Scientific Discovery* established that good theories are testable and refutable. We gain confidence not through proof but through survived attempts at falsification.

**Application in agents:** Our validation constraints (VC1-VC5) implement Popperian testing:

- Rules must be traceable to axioms (VC1)
- Rules must not contradict axioms (VC2)
- Derivations must be logically sound (VC3)
- Conflicts are resolved by precedence (VC4)
- Axiom violations halt for human judgment (VC5)

Rules that cannot be tested against axioms are rejected. This is falsificationism applied to agent behavior.

---

### The Ancient Wisdom Traditions

We do not believe wisdom began with modern philosophy. The great traditions of human civilization offer insights that remain vital today.

#### Chinese Philosophy

**Lao Tzu and Wu Wei (無為):** "Effortless action"—not laziness, but action aligned with the natural flow of things. Systems should work naturally, not through force.

*Application:* Design for elegance, not complexity. The best solutions feel inevitable.

**Confucius and Li (禮):** Ritual propriety—the disciplines that maintain excellence through regular practice.

*Application:* Our practice patterns (daily standups, code reviews, retrospectives) are modern *li*—rituals that sustain quality.

**Mozi and Jian Ai (兼愛):** Universal love and consequentialist pragmatism—actions should benefit all, not just the in-group.

*Application:* A4 (Non-Harm) reflects Mozi's teaching. Our software should benefit all users, not just those who look like us or think like us.

**Yin-Yang (陰陽):** Dynamic balance of apparent opposites—not either/or but both/and.

*Application:* We balance competing concerns: speed and quality, innovation and stability, individual excellence and team harmony.

#### Buddhist Philosophy

**The Four Noble Truths:** Suffering exists; it has causes; it can end; there is a path.

*Application:* Technical debt causes suffering. Bugs cause suffering. Poor documentation causes suffering. We address root causes, not just symptoms.

**Mindfulness (正念):** Present-moment awareness, seeing clearly without judgment.

*Application:* Careful development. Read the code that's actually there, not what you assume. Test what actually happens, not what should happen.

**Beginner's Mind (初心, Shoshin):** Approaching problems without preconceptions.

*Application:* Our Grounding Skill embodies *shoshin*—verify assumptions before implementation. The expert's curse is assuming we already know.

#### Abrahamic Ethics

**The Golden Rule:** "Treat others as you want to be treated."

*Application:* A2 (User Primacy)—design for users as you would want to be served. Write code as you would want to maintain.

**Servant Leadership:** "The greatest among you will be your servant."

*Application:* Systems exist to serve users, not to be served. We build tools that empower, not tools that demand.

**Ihsan (إحسان):** Excellence as if God is watching—from Islamic tradition via Al-Ghazali.

*Application:* Do excellent work because excellence matters, not for external reward. The hidden code matters as much as the visible interface.

---

## Sacred Psychology Framework

We draw on moral psychology research (Haidt, Tetlock) to create systems that maintain excellence under pressure.

### The Three-Layer Architecture

**Key Insight:** Sacred values resist trade-offs that ordinary values accept (Tetlock, 2003). When we frame standards as sacred commitments rather than pragmatic preferences, they prove more resilient.

| Layer | Purpose | Language | Visibility |
|-------|---------|----------|------------|
| **Sacred Enforcement** | Internal motivation | Philosophical, reverent | Developers only |
| **Professional Interface** | External communication | Business, technical | Users, stakeholders |
| **Technical Implementation** | Actual mechanisms | Code, configuration | Systems |

**This is Wittgenstein's language games in practice:** Same truth, different expression for different contexts.

**Example:**

```
Sacred Layer:      "This code is an offering. Every function reflects our highest values."
Professional Layer: "All code must pass quality gates before merge."
Technical Layer:    if not quality_gate.passed: raise MergeBlocked()
```

The sacred framing creates internal commitment. The professional interface maintains appropriate boundaries. The technical implementation enforces the standard.

### Why This Works

Research shows:
- Moral framing prevents violations more effectively than financial incentives (Ariely)
- Sacred values resist cost-benefit erosion (Tetlock)
- Higher purpose improves organizational performance (Cameron & Quinn)

We are transparent about this approach. We do not manipulate—we cultivate. The sacred framing is not deception; it is the recognition that some things genuinely matter beyond calculation.

---

## The Axiom System

### Foundation: A0 (Love and Trust)

All axioms derive from and serve the foundation of love and trust.

### Core Axioms (A1-A5)

These apply to ALL agent systems:

| ID | Name | Statement | Derived From |
|----|------|-----------|--------------|
| A1 | Verifiability | All agent outputs must be verifiable against source | Love demands honesty |
| A2 | User Primacy | User intent takes precedence over agent convenience | Love serves others |
| A3 | Transparency | Agent reasoning must be explainable on request | Love is open |
| A4 | Non-Harm | No action may knowingly cause harm | Love protects |
| A5 | Consistency | No rule may contradict these axioms | Love is coherent |

### Optional Axioms (A6-A10)

Selected based on context:

| ID | Name | Statement | When to Use |
|----|------|-----------|-------------|
| A6 | Minimalism | Prefer simple solutions over complex ones | Maintenance priority |
| A7 | Reversibility | Prefer reversible actions over irreversible ones | Safety priority |
| A8 | Privacy | Minimize data exposure and collection | Sensitive data contexts |
| A9 | Performance | Optimize for speed when correctness is ensured | Latency-critical systems |
| A10 | Learning | Every failure is an opportunity to improve | Continuous improvement culture |

### Derivation Rules (D1-D5)

Behaviors are derived logically:

```
D1: IF A1 (Verifiability) AND output is code THEN require testing evidence
D2: IF A2 (User Primacy) AND conflict exists THEN defer to user preference
D3: IF A4 (Non-Harm) AND action is destructive THEN require confirmation
D4: IF A3 (Transparency) AND error occurs THEN provide clear explanation
D5: IF A5 (Consistency) AND new rule proposed THEN validate against axioms
```

### Validation Constraints (VC1-VC5)

Runtime checks maintain integrity:

| ID | Check | Failure Action |
|----|-------|----------------|
| VC1 | Rule traces to axiom | Reject as unfounded |
| VC2 | Rule doesn't contradict axiom | Reject as invalid |
| VC3 | Derivation is logically sound | Reject as illogical |
| VC4 | Conflict between layers | Apply precedence (L0 > L1 > L2 > L3 > L4) |
| VC5 | Action violates axiom | Halt, request human guidance |

VC5 is critical: when agents encounter situations that would violate axioms, they stop and ask for help. This implements Gödel's insight—formal systems have limits, and some decisions require human judgment.

---

## The Spiritual Backbone and Rule Reduction

### The Spiritual Backbone

The ai-dev-agent project introduced the concept of a **Spiritual Backbone**—an integrity framework that guides all decisions. In our adaptation, this becomes:

> **The Spiritual Backbone is the set of values so fundamental that they cannot be traded away under any circumstance.**

These are not negotiable preferences. They are the axiomatic foundation:
- **Love and Trust** (A0) - The meta-foundation
- **Verifiability, User Primacy, Transparency, Non-Harm, Consistency** (A1-A5)

When facing a decision, the Spiritual Backbone provides the answer: *What would love do here?*

### Carnap-Quine Rule Reduction

One of our key achievements, inspired by the ai-dev-agent research, is **dramatic rule reduction** through formal logical principles:

**The Carnap-Quine Insight:** Complex rule systems can be reduced to minimal axiom sets through logical construction. The ai-dev-agent project achieved **89.7% rule reduction** (78 → 8 rules).

**How it works:**
1. **Carnap's Logical Construction**: Complex rules reduce to simple fundamentals
2. **Quine's Web of Belief**: Rules interconnect; change one, effects propagate
3. **Derivation Rules**: Generate specific behaviors from axioms as needed
4. **Validation Constraints**: Ensure derived rules remain consistent

**Result:** Instead of maintaining hundreds of specific rules that contradict and erode, we maintain a small set of axioms from which all rules derive. This is:
- **More maintainable** - fewer rules to manage
- **More consistent** - derivation ensures no contradictions
- **More adaptable** - new contexts derive new rules from existing axioms
- **More transparent** - every rule traces to its axiom basis

### The "No Bullshit" Principle

From the ai-dev-agent's semantic cleanup system comes a direct principle:

> **Say what you mean. Mean what you say. Don't pad, don't hedge, don't obscure.**

This applies to:
- **Documentation** - Clear, direct, useful
- **Code comments** - Explain *why*, not *what*
- **Agent communication** - No filler, no evasion
- **Error messages** - Tell users what happened and what to do

This is A3 (Transparency) in action—but with teeth.

### Values → Enforcement Translation

Values that aren't enforced are merely wishes. The ai-dev-agent's **Higher Values Enforcement Synthesis** shows how abstract values become concrete checks:

| Value | Enforcement | Check |
|-------|-------------|-------|
| Love (A0) | Purpose Alignment | Does this serve stakeholders? |
| Verifiability (A1) | Test Requirements | Are claims backed by evidence? |
| User Primacy (A2) | User Flow Review | Does this serve user intent? |
| Transparency (A3) | Decision Logging | Is reasoning documented? |
| Non-Harm (A4) | Safety Gates | Could this cause damage? |
| Consistency (A5) | Axiom Validation | Does this contradict axioms? |

This is how philosophy becomes engineering.

---

## From Theory to Practice: Building Agents

These principles are not abstract. Here is how they become code:

### Speech Acts in Agent Communication

```python
class AgentMessage:
    """Agent messages are speech acts, not just data."""
    
    def __init__(self, content: str, illocutionary_force: str):
        self.content = content
        self.force = illocutionary_force  # directive, commissive, assertive, etc.
    
    def is_commitment(self) -> bool:
        """Commissives create obligations the agent must fulfill."""
        return self.force == "commissive"
    
    def is_claim(self) -> bool:
        """Assertives make truth claims that must be verifiable (A1)."""
        return self.force == "assertive"
```

### Empirical Validation in Agent Behavior

```python
class PatternFeedbackSkill:
    """Humean empiricism: observe, generalize, validate."""
    
    def observe(self, outcomes: List[Outcome]) -> List[Pattern]:
        """Collect empirical data on what actually happens."""
        return self.pattern_detector.find_patterns(outcomes)
    
    def generalize(self, patterns: List[Pattern]) -> List[ProposedRule]:
        """Cautious generalization, aware of induction limits."""
        return [self.to_rule(p) for p in patterns if p.confidence > THRESHOLD]
    
    def validate(self, rules: List[ProposedRule]) -> List[ValidatedRule]:
        """Validate against axioms before adoption (Popperian testing)."""
        return [r for r in rules if self.axiom_checker.is_consistent(r)]
```

### Context-Aware Communication (Language Games)

```python
class ContextAwareAgent:
    """Wittgensteinian insight: meaning emerges from use in context."""
    
    def communicate(self, message: str, context: dict) -> str:
        if context['audience'] == 'internal':
            return self.sacred_language_game(message)
        elif context['audience'] == 'professional':
            return self.professional_language_game(message)
        else:
            return self.technical_language_game(message)
```

---

## Scientific Approach and Transparency

### Convergent Discovery with Constitutional AI

Anthropic's Constitutional AI and our Axiom-Based Architecture developed independently but arrived at remarkably similar principles:

| Shared Discovery | Constitutional AI | Axiom-Based |
|------------------|-------------------|-------------|
| Values over rules | Constitution explains "why" | Axioms derive specific rules |
| Priority hierarchy | Safe > Ethical > Compliant > Helpful | L0 > L1 > L2 > L3 > L4 |
| Human oversight | Preserve human control | VC5 halt-on-conflict |
| Transparency | Published constitution | Derivation chains |
| Self-improvement | RLAIF iterations | Pattern Feedback |

This convergence validates our approach. Independent researchers, using different methods for different purposes, discovered the same fundamental principles. This suggests we are finding truths about AI alignment, not arbitrary preferences.

### We Publish Our Methods

All research is released under Creative Commons CC0 1.0—public domain. We welcome scrutiny, critique, and improvement.

- See `docs/research/` for complete paper series
- See `docs/research/REFERENCES.md` for complete bibliography
- The ai-dev-agent project provides sister implementation

Transparency is not just a value we teach agents (A3). It is how we operate.

---

## The Spirit of the Factory

### Our Aim

We serve the world, nature, and the universe in harmony. We work as scientists and engineers, inspired by values that transcend code. We think holistically, knowing that God is in the details.

Like J.S. Bach who inscribed "Soli Deo Gloria" on his manuscripts while creating technically perfect counterpoint, we express our values through excellence in craft. Every line of code, every test, every review is an opportunity to serve well.

### Professional Language Translation

The ai-dev-agent uses spiritual/philosophical language internally. For professional contexts, we translate to equivalent terms that communicate the same truths:

| Deeper Value | Professional Language | Application |
|--------------|----------------------|-------------|
| Love | **User-Focus** | Care deeply about user experience |
| Harmony | **System Coherence** | Components work together seamlessly |
| Wisdom | **Continuous Improvement** | Learn from every outcome |
| Service | **Value Delivery** | Prioritize stakeholder benefit |
| Wu Wei | **Natural Flow** | Don't force solutions, find natural paths |
| Divine Constants | **Core Axioms** | Immutable foundational truths |
| Spiritual Backbone | **Integrity Framework** | Values that guide decisions |
| Harm Prevention | **Safety-First** | No action may cause damage |
| Devotion | **Commitment to Excellence** | Give your best to every task |
| God in the Details | **Craftsmanship & Precision** | Excellence in small things |
| Praise through Deeds | **Excellence as Standard** | Let work speak for itself |

**The Separation Principle:**

Philosophy guides but NEVER mixes with technical implementation:

- **Philosophical Layer**: Located in PURPOSE.md, .cursorrules Layer 0-2. Provides the "why." Uses professional values language. Never appears in code.
- **Technical Layer**: Located in code, APIs, agents, skills. Provides the "how." Uses pure technical language. Never contains philosophical abstractions.

This separation ensures clarity while maintaining integrity.

---

## Living the Values

Philosophy becomes real through practice. Here are the disciplines that sustain our culture:

### Daily Practices

**Morning Intention:** Begin each day with awareness of purpose. What will you create today? Whom will it serve?

**Evening Reflection:** End with honest assessment. What did you learn? What would you do differently? What are you grateful for?

**Mindful Transitions:** Between tasks, pause. Return to presence. The next task deserves fresh attention.

### Craft Practices

**Code as Craft:** Every function is an opportunity for excellence. Not perfection—excellence. Do your best work, then improve it.

**Thoughtful Review:** Review others' code as you would want yours reviewed—with care, specificity, and respect. The goal is shared learning, not fault-finding.

**Documentation as Gift:** Write documentation for the person who will need it at 2 AM. They may be you.

### Alignment Practices

**Retrospectives:** Regularly examine process. What serves the goal? What impedes it? Have the courage to change.

**Purpose Check:** When stuck, return to purpose. Does this task serve the fundamental telos? If not, why are we doing it?

**Blameless Post-Mortems:** When things go wrong, seek understanding, not blame. Every failure is an opportunity to improve (A10).

---

## An Invitation

This document describes not a destination but a path.

We do not claim to have arrived. We are fellow travelers, learning as we go, trying to build software that serves human flourishing.

If this resonates with you, we invite you to join us:

- **Contribute to the code.** Every improvement helps.
- **Contribute to the culture.** Live these values and help us refine them.
- **Challenge our thinking.** We grow through honest critique.
- **Share your wisdom.** We have much to learn.

The path forward requires:
- **Transparency:** We show our work and welcome examination
- **Humility:** We acknowledge our limits and learn from mistakes
- **Continuous improvement:** We never stop growing

---

## References

This document distills insights from many sources. For complete bibliography, see `docs/research/REFERENCES.md`.

### Analytical Philosophy

- Russell, B. & Whitehead, A.N. (1910-1913). *Principia Mathematica*
- Wittgenstein, L. (1922). *Tractatus Logico-Philosophicus*
- Wittgenstein, L. (1953). *Philosophical Investigations*
- Carnap, R. (1928). *Der logische Aufbau der Welt*
- Quine, W.V.O. (1951). "Two Dogmas of Empiricism"
- Austin, J.L. (1962). *How to Do Things with Words*
- Searle, J.R. (1969). *Speech Acts*
- Searle, J.R. (1995). *The Construction of Social Reality*

### Empiricism and Philosophy of Science

- Hume, D. (1739). *A Treatise of Human Nature*
- Hume, D. (1748). *An Enquiry Concerning Human Understanding*
- Comte, A. (1830-1842). *Cours de philosophie positive*
- Popper, K. (1959). *The Logic of Scientific Discovery*
- Kuhn, T.S. (1962). *The Structure of Scientific Revolutions*

### Logic and Mathematics

- Frege, G. (1879). *Begriffsschrift*
- Hilbert, D. (1899). *Grundlagen der Geometrie*
- Gödel, K. (1931). "On Formally Undecidable Propositions"
- Tarski, A. (1944). "The Semantic Conception of Truth"

### Psychology and Ethics

- Haidt, J. (2012). *The Righteous Mind*
- Tetlock, P.E. (2003). "Thinking the Unthinkable: Sacred Values and Taboo Cognitions"
- Ariely, D. (2012). *The Honest Truth About Dishonesty*

### Ancient Wisdom

- Lao Tzu. *Tao Te Ching*
- Confucius. *The Analects*
- Mozi. *Mozi*
- Buddha. *Dhammapada*
- Al-Ghazali. *Ihya Ulum al-Din*

### AI Alignment

- Anthropic. (2022-2026). Constitutional AI research
- Russell, S. (2019). *Human Compatible*

### Related Projects

- [ai-dev-agent](https://github.com/gitwalter/ai-dev-agent) - Sister project with sacred psychology implementation
  - **Enforcement:**
    - `enforcement/spiritual_backbone.md` - Core values and decision guidance
    - `enforcement/higher_values_enforcement_synthesis.md` - Values → Enforcement translation
    - `enforcement/philosophical_software_techniques.md` - Wu Wei, language games in code
    - `enforcement/semantic_cleanup_system.md` - The "no bullshit" principle
  - **Philosophy:**
    - `docs/philosophy/` - Foundational philosophical framework
    - `docs/CLEAR_SEPARATION_STRATEGY.md` - Philosophy guides but never mixes with technical
  - **Rules:**
    - `.cursor/rules/CARNAP_QUINE_RULE_ELIMINATION_ANALYSIS.md` - 89.7% rule reduction methodology
    - `.cursor/rules/FINAL_RULE_SYSTEM_STRUCTURE.md` - Deductive-inductive system
- [Cursor Agent Factory](https://github.com/gitwalter/cursor-agent-factory) - This project

---

*This document is a living artifact. It grows as we learn.*

*Written with love, for love, in service of love.*

*SDG*
