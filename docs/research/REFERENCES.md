# Complete Reference List

Comprehensive bibliography for the Value-Aligned AI Agent Systems research paper series.

Each entry includes a **Relevance** note explaining why this work informs our methodology.

---

## Primary Sources

### Anthropic Constitutional AI

Anthropic. (2022, December 15). *Constitutional AI: Harmlessness from AI Feedback*. Anthropic Research.
https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

> **Relevance**: Primary comparison point for Paper 3. Demonstrates convergent discovery of value-alignment principles through different methodology (RLAIF vs. axiom-based).

Anthropic. (2023, May 9). *Claude's Constitution*. Anthropic.
https://www.anthropic.com/constitution

> **Relevance**: Early constitution document showing evolution of AI value specification.

Anthropic. (2026, January 22). *Claude's new constitution*. Anthropic News.
https://www.anthropic.com/news/claude-new-constitution

> **Relevance**: The 57-page "soul document" that explains "why" to Claude. Demonstrates parallel emphasis on transparency and explaining reasoning—key convergent discovery with our A3 (Transparency) axiom.

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... & Kaplan, J. (2022). Constitutional AI: Harmlessness from AI Feedback. *arXiv preprint arXiv:2212.08073*.
https://arxiv.org/abs/2212.08073

> **Relevance**: Academic paper detailing RLAIF methodology. Technical foundation for understanding Constitutional AI approach.

### Constitutional AI Tracking

Constitutional.ai. (2026). *Tracking Anthropic's Revolutionary Framework*.
https://constitutional.ai/

> **Relevance**: Community tracking of Constitutional AI evolution.

---

## Foundational Philosophy

### Logic and Formal Methods

Frege, G. (1879). *Begriffsschrift* (Concept Script). Louis Nebert.

> **Relevance**: Father of modern logic. Created predicate calculus that enables formal axiom systems. Our derivation rules (D1-D5) use Fregean logical structure: "IF [premise] THEN [conclusion]".

Frege, G. (1892). Über Sinn und Bedeutung (On Sense and Reference). *Zeitschrift für Philosophie und philosophische Kritik*, 100, 25-50.

> **Relevance**: Distinction between sense (meaning) and reference (what it denotes). Informs how our axioms (sense) derive specific rules (reference) while maintaining consistent meaning.

Hilbert, D. (1899). *Grundlagen der Geometrie* (Foundations of Geometry). Teubner.

> **Relevance**: **Direct inspiration for our axiom-based architecture**. Hilbert's axiomatic method—deriving all theorems from a minimal set of axioms—is the template for our 5-layer deductive system. Our axioms A1-A5 are designed following Hilbert's principles: independence, consistency, completeness.

Hilbert, D. (1928). *Grundzüge der theoretischen Logik* (Principles of Theoretical Logic). Springer. (With Ackermann, W.)

> **Relevance**: Formalization of first-order logic. Our validation constraints (VC1-VC5) implement Hilbert-style consistency checking.

Leibniz, G. W. (1666). *Dissertatio de arte combinatoria*. 

> **Relevance**: Vision of "universal characteristic"—a formal language for all reasoning. Our axiom system attempts something similar: a formal language for AI agent behavior that enables derivation of correct action from first principles.

Leibniz, G. W. (1714). *Monadology*.

> **Relevance**: Concept of monads as fundamental units with internal principles. Each agent in our system is like a monad: internally governed by axioms, externally coordinated through pre-established harmony (shared axiom system).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38, 173-198.

> **Relevance**: Incompleteness theorems remind us that no axiom system can be both complete and consistent for all statements. This is why our VC5 (Halt on Axiom Conflict) routes to human judgment—formal systems have limits.

Tarski, A. (1944). The semantic conception of truth and the foundations of semantics. *Philosophy and Phenomenological Research*, 4(3), 341-376.

> **Relevance**: Formal theory of truth. Our A1 (Verifiability) axiom requires outputs to be verifiable against source—a practical application of Tarski's correspondence theory.

### Epistemology

Descartes, R. (1637). *Discours de la méthode* (Discourse on the Method).

> **Relevance**: Methodic doubt and the pursuit of certainty. Our A1 (Verifiability) axiom embodies Cartesian skepticism: "Don't accept anything as true unless verified." The Grounding Skill implements Cartesian doubt in practice.

Descartes, R. (1641). *Meditationes de Prima Philosophia* (Meditations on First Philosophy).

> **Relevance**: Search for indubitable foundations. Our Layer 0 (Integrity) seeks similarly indubitable axioms from which everything else derives.

Hume, D. (1739). *A Treatise of Human Nature*.

> **Relevance**: The is-ought problem: you cannot derive "ought" from "is." Our architecture addresses this by making the "ought" explicit in axioms, then deriving specific behaviors. We don't pretend values emerge from facts—we state values explicitly.

Hume, D. (1748). *An Enquiry Concerning Human Understanding*.

> **Relevance**: Emphasis on experience and observation. Our Pattern Feedback Skill (inductive learning) is Humean: we observe patterns and generalize, but validate against axioms to avoid Hume's problem of induction.

Quine, W. V. O. (1951). Two Dogmas of Empiricism. *The Philosophical Review*, 60(1), 20-43.

> **Relevance**: Web of belief—knowledge forms an interconnected network. Our layered architecture embodies this: axioms (core beliefs) connect to principles connect to practices connect to technical implementation. Changes propagate through the web.

Quine, W. V. O. (1960). *Word and Object*. MIT Press.

> **Relevance**: Indeterminacy of translation and radical interpretation. Informs our A3 (Transparency): since meaning is underdetermined, we must be explicit about our reasoning to enable correct interpretation.

### Philosophy of Language

Wittgenstein, L. (1922). *Tractatus Logico-Philosophicus*. Kegan Paul.

> **Relevance**: Early Wittgenstein's picture theory of language. Our formal axiom structure attempts to create unambiguous language for values—though we recognize the later Wittgenstein's critique.

Wittgenstein, L. (1953). *Philosophical Investigations*. Blackwell.

> **Relevance**: **Key influence on Paper 2 (Sacred Psychology)**. Language games and meaning-as-use. Our three-layer architecture (sacred internal, professional external, technical implementation) implements different language games for different contexts. Same truth, different expression.

Austin, J. L. (1962). *How to Do Things with Words*. Oxford University Press.

> **Relevance**: Speech act theory—language as action. Our agents don't just describe; they act. Austin's performatives inform how agent communications are themselves actions with consequences.

Carnap, R. (1928). *The Logical Structure of the World* (*Der logische Aufbau der Welt*). University of California Press.

> **Relevance**: Logical constructionism—building complex concepts from simple ones through explicit rules. Our derivation rules (D1-D5) are Carnapian: they explicitly construct specific behaviors from axiomatic foundations.

Carnap, R. (1950). *Logical Foundations of Probability*. University of Chicago Press.

> **Relevance**: Formal approach to inductive logic. Informs our Pattern Feedback Skill's approach to generalizing from observations while maintaining logical rigor.

### Philosophy of Mind and AI

Searle, J. R. (1980). Minds, Brains, and Programs. *Behavioral and Brain Sciences*, 3(3), 417-424.

> **Relevance**: The Chinese Room argument. Raises questions about AI understanding vs. simulation. Our A3 (Transparency) axiom acknowledges this: we don't claim AI "understands" but require it to explain its reasoning, enabling humans to verify.

Searle, J. R. (1995). *The Construction of Social Reality*. Free Press.

> **Relevance**: How collective intentionality creates social facts. Our axiom system creates a "social reality" for agents—shared values that coordinate behavior through collective acceptance.

### Philosophy of Science

Comte, A. (1830-1842). *Cours de philosophie positive* (Course of Positive Philosophy).

> **Relevance**: Founder of positivism and scientific methodology. Our emphasis on verification (A1), empirical observation (Pattern Feedback), and measurable outcomes reflects positivist epistemology applied to AI alignment.

Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson.

> **Relevance**: Falsificationism—good theories are testable and refutable. Our validation constraints (VC1-VC5) implement Popperian testing: rules must be traceable to axioms and potentially refutable.

Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.

> **Relevance**: Paradigm shifts and normal science. Our axiom system defines a paradigm; Layer 0 changes represent paradigm shifts requiring human oversight (VC5).

---

## Ancient Wisdom Traditions

### Chinese Philosophy

Lao Tzu. (c. 6th century BCE). *Tao Te Ching*. (Various translations)

> **Relevance**: **Key influence on Paper 2 (Sacred Psychology)**. Wu Wei (effortless action) informs our approach to system design—systems should work naturally, not through force. Yin-Yang balance informs our handling of competing concerns (e.g., performance vs. simplicity).

Recommended translations:
- Henricks, R. G. (Trans.). (1989). *Lao-Tzu: Te-Tao Ching*. Ballantine Books.
- Ames, R. T., & Hall, D. L. (Trans.). (2003). *Daodejing: A Philosophical Translation*. Ballantine Books.

Confucius. (c. 500 BCE). *The Analects* (*Lunyu*). (Various translations)

> **Relevance**: Virtue ethics and proper relationships. Our A2 (User Primacy) reflects Confucian emphasis on serving others appropriately. The concept of *li* (ritual propriety) informs our practice patterns—regular disciplines that maintain excellence.

Recommended translation:
- Slingerland, E. (Trans.). (2003). *Confucius: Analects*. Hackett Publishing.

Mozi. (c. 400 BCE). *Mozi*. (Various translations)

> **Relevance**: Universal love (*jian ai*) and consequentialism. Our A4 (Non-Harm) axiom reflects Mozi's emphasis on actions that benefit all, not just the in-group. Mozi's anti-war pragmatism informs our preference for solving problems without conflict.

Recommended translation:
- Johnston, I. (Trans.). (2010). *The Mozi: A Complete Translation*. Columbia University Press.

Sun Tzu. (c. 5th century BCE). *The Art of War* (*Sunzi Bingfa*). (Various translations)

> **Relevance**: Strategic thinking for agent coordination. Sun Tzu's principles—"know yourself and know your problem," "win without fighting," "adapt to circumstances"—inform our agent design and problem-solving patterns. Not about war, but about achieving goals with minimal conflict.

Recommended translation:
- Giles, L. (Trans.). (1910). *Sun Tzu on the Art of War*. Luzac and Co.

Zhuangzi. (c. 3rd century BCE). *Zhuangzi*. (Various translations)

> **Relevance**: Philosophical Taoism and perspective relativism. Reminds us that our axiom system is one perspective among many—valuable, but not absolute. Informs our humility about AI alignment.

Ames, R. T. (Ed.). (1998). *Wandering at Ease in the Zhuangzi*. SUNY Press.

### Buddhist Philosophy

Siddhartha Gautama (Buddha). (c. 5th century BCE). *Dhammapada* and Pali Canon. (Various translations)

> **Relevance**: **Key influence on Paper 2 (Sacred Psychology)**. The Four Noble Truths provide a framework for understanding and alleviating suffering—including the suffering caused by poorly designed systems. Mindfulness practice informs our emphasis on careful, present-moment awareness in development.

Recommended translations:
- Easwaran, E. (Trans.). (2007). *The Dhammapada*. Nilgiri Press.
- Bodhi, B. (Trans.). (2005). *In the Buddha's Words*. Wisdom Publications.

Thich Nhat Hanh. (1991). *Peace Is Every Step: The Path of Mindfulness in Everyday Life*. Bantam Books.

> **Relevance**: Applied mindfulness. Demonstrates how ancient wisdom applies to modern life. Our daily practices (P1-P3) reflect this integration of mindfulness into work.

Suzuki, S. (1970). *Zen Mind, Beginner's Mind*. Weatherhill.

> **Relevance**: Beginner's mind (*shoshin*)—approaching problems without preconceptions. Essential for avoiding assumptions (our Grounding Skill) and remaining open to novel solutions.

### Christian Ethics

Jesus of Nazareth. (c. 30 CE). Teachings preserved in the Gospels.

> **Relevance**: **Key influence on Paper 2 (Sacred Psychology)**. The Golden Rule ("treat others as you want to be treated") directly informs our A2 (User Primacy) and user-centered design. Servant leadership ("the greatest among you will be your servant") informs our view of systems as serving users, not the reverse.

Recommended scholarly editions:
- Ehrman, B. D. (2004). *The New Testament: A Historical Introduction*. Oxford University Press.

Lewis, C. S. (1952). *Mere Christianity*. Geoffrey Bles.

> **Relevance**: Accessible articulation of Christian ethics. Lewis's concept of moral law as objective reality parallels our treatment of axioms as foundational truths rather than arbitrary preferences.

Greenleaf, R. K. (1977). *Servant Leadership: A Journey into the Nature of Legitimate Power and Greatness*. Paulist Press.

> **Relevance**: Servant leadership applied to organizations. Directly informs our design philosophy: systems exist to serve users, not to be served. This is a secular application of Jesus's teaching.

### Islamic Philosophy

Al-Ghazali. (c. 1100 CE). *Ihya Ulum al-Din* (Revival of Religious Sciences).

> **Relevance**: **Referenced in Paper 2**. The concept of *Ihsan* (excellence as if God is watching) informs our approach to intrinsic quality motivation. Doing excellent work because excellence itself matters, not for external reward.

---

## Moral Psychology and Sacred Values

Haidt, J. (2012). *The Righteous Mind: Why Good People Are Divided by Politics and Religion*. Vintage Books.

> **Relevance**: **Core theoretical foundation for Paper 2**. Moral foundations theory explains why sacred framing creates stronger commitment than instrumental framing.

Haidt, J., & Graham, J. (2007). When morality opposes justice: Conservatives have moral intuitions that liberals may not recognize. *Social Justice Research*, 20(1), 98-116.
https://doi.org/10.1007/s11211-007-0034-z

> **Relevance**: Identifies moral foundations (care, fairness, loyalty, authority, sanctity) that our sacred psychology approach leverages.

Graham, J., Haidt, J., & Nosek, B. A. (2009). Liberals and conservatives rely on different sets of moral foundations. *Journal of Personality and Social Psychology*, 96(5), 1029-1046.
https://doi.org/10.1037/a0015141

> **Relevance**: Empirical validation of moral foundations theory.

Tetlock, P. E. (2003). Thinking the unthinkable: Sacred values and taboo cognitions. *Trends in Cognitive Sciences*, 7(7), 320-324.
https://doi.org/10.1016/S1364-6613(03)00135-9

> **Relevance**: **Core theoretical foundation for Paper 2**. Shows that sacred values resist trade-offs that ordinary values accept. This is why sacred framing creates stronger commitment.

Tetlock, P. E., Kristel, O. V., Elson, S. B., Green, M. C., & Lerner, J. S. (2000). The psychology of the unthinkable: Taboo trade-offs, forbidden base rates, and heretical counterfactuals. *Journal of Personality and Social Psychology*, 78(5), 853-870.
https://doi.org/10.1037/0022-3514.78.5.853

> **Relevance**: Detailed empirical work on sacred values and taboo cognitions.

---

## Ethics and Virtue

Aristotle. (c. 350 BCE). *Nicomachean Ethics*. (Various translations)

> **Relevance**: Virtue ethics—character matters, not just actions. Our approach treats AI systems as having "character" (values, habits, virtues) rather than just following rules. The concept of *phronesis* (practical wisdom) informs our emphasis on judgment, not just compliance.

Recommended translation:
- Ross, W. D. (Trans.). (2009). *Nicomachean Ethics*. Oxford University Press.

MacIntyre, A. (1981). *After Virtue: A Study in Moral Theory*. University of Notre Dame Press.

> **Relevance**: Revival of virtue ethics for modern context. MacIntyre's critique of emotivism and call for return to tradition-based ethics informs our use of ancient wisdom traditions.

Kant, I. (1785). *Grundlegung zur Metaphysik der Sitten* (Groundwork of the Metaphysics of Morals).

> **Relevance**: The categorical imperative as universal moral law. Our axioms function similarly: universal principles that should apply to all agents in all situations.

---

## Organizational Behavior and Culture

Cameron, K. S., & Quinn, R. E. (2011). *Diagnosing and changing organizational culture: Based on the competing values framework* (3rd ed.). Jossey-Bass.

> **Relevance**: **Cited in Paper 2**. Shows that organizations with higher purpose outperform those without. Supports our emphasis on Layer 1 (Purpose) as foundational.

Schein, E. H. (2010). *Organizational Culture and Leadership* (4th ed.). Jossey-Bass.

> **Relevance**: Three levels of culture (artifacts, espoused values, basic assumptions). Our 5-layer architecture parallels this: visible artifacts (Layer 4), stated principles (Layer 2), and deep axioms (Layer 0).

Collins, J. C., & Porras, J. I. (1994). *Built to Last: Successful Habits of Visionary Companies*. Harper Business.

> **Relevance**: "Core ideology" as foundation for enduring organizations. Our axiom system provides this ideological foundation for AI agent systems.

---

## Behavioral Economics

Ariely, D. (2012). *The honest truth about dishonesty: How we lie to everyone—especially ourselves*. Harper.

> **Relevance**: **Cited in Paper 2**. Shows that moral framing prevents dishonest behavior more effectively than financial incentives. Supports sacred psychology approach.

Ariely, D., & Gneezy, U. (2009). Pay enough or don't pay at all. *Quarterly Journal of Economics*, 124(4), 1639-1677.

> **Relevance**: Intrinsic vs. extrinsic motivation. Our sacred framing leverages intrinsic motivation rather than external enforcement.

Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

> **Relevance**: System 1/System 2 thinking. Our axiom system creates System 2 (deliberate) guardrails for System 1 (intuitive) agent behavior.

Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale University Press.

> **Relevance**: Choice architecture and libertarian paternalism. Our axiom system is a form of choice architecture for AI agents—guiding toward good outcomes while preserving flexibility.

---

## AI Safety and Alignment

Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.

> **Relevance**: Defines the AI alignment problem. Our axiom-based architecture is one approach to the control problem Russell identifies.

Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. *arXiv preprint arXiv:1606.06565*.

> **Relevance**: Taxonomy of AI safety problems. Our axioms address several: avoiding negative side effects (A4), reward hacking prevention (A1), scalable oversight (VC5).

Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.

> **Relevance**: Long-term AI alignment concerns. Our axiom system is designed to be stable under capability increases.

Christian, B. (2020). *The Alignment Problem: Machine Learning and Human Values*. W. W. Norton & Company.

> **Relevance**: Accessible overview of alignment challenges. Provides context for our approach.

Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds and Machines*, 30(3), 411-437.
https://doi.org/10.1007/s11023-020-09539-2

> **Relevance**: Philosophical analysis of what AI alignment means. Informs our definition of value alignment.

---

## Software Engineering

Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.

> **Relevance**: Craftsmanship approach to software. Our "craft practices" (P4-P6) extend this to AI-assisted development.

Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.

> **Relevance**: Dependency inversion and architecture patterns. Informs our layered architecture design.

Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.

> **Relevance**: Incremental improvement without changing behavior. Our Pattern Feedback Skill implements similar continuous improvement.

Beck, K. (2002). *Test Driven Development: By Example*. Addison-Wesley.

> **Relevance**: Tests as specification. Our A1 (Verifiability) axiom treats verification as foundational, similar to TDD.

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

> **Relevance**: Reusable patterns for common problems. Our pattern library extends this concept to AI agent behavior.

---

## Agent Systems and Multi-Agent Coordination

Wooldridge, M. (2009). *An Introduction to MultiAgent Systems* (2nd ed.). Wiley.

> **Relevance**: Foundational text on agent systems. Provides theoretical basis for our agent architecture.

Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

> **Relevance**: Comprehensive AI textbook including agent architectures. Standard reference.

Shoham, Y., & Leyton-Brown, K. (2008). *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge University Press.

> **Relevance**: Formal foundations for multi-agent systems. Informs our understanding of agent coordination.

---

## Religion and Psychology

Koenig, H. G., & Cohen, H. J. (Eds.). (2002). *The link between religion and health: Psychoneuroimmunology and the faith factor*. Oxford University Press.

> **Relevance**: Empirical research on psychological effects of religious practice. Supports the psychological mechanisms behind sacred framing.

Pargament, K. I. (1997). *The Psychology of Religion and Coping: Theory, Research, Practice*. Guilford Press.

> **Relevance**: How religious frameworks help people cope. Informs our understanding of why sacred framing creates resilience under pressure.

Hood, R. W., Hill, P. C., & Spilka, B. (2009). *The Psychology of Religion: An Empirical Approach* (4th ed.). Guilford Press.

> **Relevance**: Comprehensive empirical psychology of religion. Provides scientific basis for sacred psychology claims.

---

## Mindfulness and Focus

Kabat-Zinn, J. (1994). *Wherever You Go, There You Are: Mindfulness Meditation in Everyday Life*. Hyperion.

> **Relevance**: Secular mindfulness practice. Informs our daily practices (P1-P3) that cultivate present-moment awareness.

Newport, C. (2016). *Deep Work: Rules for Focused Success in a Distracted World*. Grand Central Publishing.

> **Relevance**: Deep focus as competitive advantage. Supports our emphasis on deliberate practice and focused development.

---

## Excellence and Craftsmanship

Sennett, R. (2008). *The Craftsman*. Yale University Press.

> **Relevance**: Craftsmanship as ethical practice. Informs our "craft practices" and view of code as craft.

Crawford, M. B. (2009). *Shop Class as Soulcraft: An Inquiry into the Value of Work*. Penguin Press.

> **Relevance**: Meaning through skilled work. Supports our emphasis on meaningful, purposeful development.

---

## Related Online Resources

### Augmented Coding Patterns
Lexler. (n.d.). *Augmented Coding Patterns*.
https://lexler.github.io/augmented-coding-patterns/

> **Relevance**: AI collaboration patterns that influenced our agent design. Active Partner, Check Alignment patterns.

### Cursor Agent Factory
Cursor Agent Factory Project. (2026). GitHub Repository.
https://github.com/gitwalter/cursor-agent-factory

> **Relevance**: Primary implementation of the axiom-based architecture.

### ai-dev-agent Project
ai-dev-agent. (2025-2026). GitHub Repository.
https://github.com/gitwalter/ai-dev-agent

> **Relevance**: Sister project containing sacred psychology implementation and ancient wisdom design patterns.

---

## Citation Formats

### APA 7th Edition (used in papers)

Author, A. A. (Year). Title of work: Capital letter also for subtitle. Publisher.

Author, A. A., & Author, B. B. (Year). Title of article. *Title of Periodical*, volume(issue), pages. https://doi.org/xxxxx

### BibTeX Entries

```bibtex
@article{bai2022constitutional,
  title={Constitutional AI: Harmlessness from AI Feedback},
  author={Bai, Yuntao and Kadavath, Saurav and Kundu, Sandipan and others},
  journal={arXiv preprint arXiv:2212.08073},
  year={2022}
}

@book{russell2019human,
  title={Human Compatible: Artificial Intelligence and the Problem of Control},
  author={Russell, Stuart},
  year={2019},
  publisher={Viking}
}

@article{haidt2007morality,
  title={When morality opposes justice},
  author={Haidt, Jonathan and Graham, Jesse},
  journal={Social Justice Research},
  volume={20},
  number={1},
  pages={98--116},
  year={2007},
  publisher={Springer}
}

@book{hilbert1899grundlagen,
  title={Grundlagen der Geometrie},
  author={Hilbert, David},
  year={1899},
  publisher={Teubner}
}

@article{frege1879begriffsschrift,
  title={Begriffsschrift},
  author={Frege, Gottlob},
  year={1879},
  publisher={Louis Nebert}
}

@book{wittgenstein1953investigations,
  title={Philosophical Investigations},
  author={Wittgenstein, Ludwig},
  year={1953},
  publisher={Blackwell}
}
```

---

## Acknowledgments

We acknowledge the contributions of many researchers, developers, and thinkers whose work has informed this research series. Special thanks to:

- The Anthropic team for pioneering Constitutional AI and publishing their work openly
- The broader AI safety and alignment research community
- The developers and contributors to the Cursor Agent Factory and ai-dev-agent projects
- The ancient wisdom traditions—Taoist, Confucian, Buddhist, Christian, Islamic—that provide universal grounding for our approach to values and ethics
- The philosophical tradition from Frege and Hilbert through Wittgenstein and Quine that enables rigorous formalization of values

---

*This reference list is part of the Value-Aligned AI Agent Systems research series.*
*Last updated: January 2026*
