"""
Brain & Neuroscience Basics
A Practical Guide to Understanding Your Mind and Using It Better

PDF e-book generator using ReportLab.
Run this script to produce 'brain_neuroscience_basics.pdf'.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    HRFlowable, Table, TableStyle
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY   = HexColor("#1A2B4A")
GOLD   = HexColor("#D4AF37")
DARK   = HexColor("#0D1425")
LGRAY  = HexColor("#CCCCCC")
WHITE  = HexColor("#FFFFFF")
OFFWHT = HexColor("#F8F8F8")

# ── Page geometry ────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

OUTPUT_FILE = "brain_neuroscience_basics.pdf"


# ═══════════════════════════════════════════════════════════════════════════
# Custom canvas – running header / footer on every non-title page
# ═══════════════════════════════════════════════════════════════════════════
class NeuroscienceCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_footer(num_pages)
            super().showPage()
        super().save()

    def _draw_footer(self, page_count):
        page_num = self.__dict__.get("_pageNumber", 1)
        if page_num <= 1:          # skip title page
            return
        self.saveState()
        self.setStrokeColor(GOLD)
        self.setLineWidth(0.8)
        y = MARGIN - 0.5 * cm
        self.line(MARGIN, y, PAGE_W - MARGIN, y)

        self.setFont("Helvetica", 8)
        self.setFillColor(LGRAY)
        self.drawString(MARGIN, y - 0.4 * cm,
                        "Brain & Neuroscience Basics  ·  Yash Sahu")
        self.drawRightString(PAGE_W - MARGIN, y - 0.4 * cm,
                             f"Page {page_num} of {page_count}")
        self.restoreState()


# ═══════════════════════════════════════════════════════════════════════════
# Style sheet
# ═══════════════════════════════════════════════════════════════════════════
def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["title_page_main"] = ParagraphStyle(
        "title_page_main",
        fontSize=36, leading=44, alignment=TA_CENTER,
        textColor=WHITE, fontName="Helvetica-Bold", spaceAfter=12
    )
    styles["title_page_sub"] = ParagraphStyle(
        "title_page_sub",
        fontSize=18, leading=26, alignment=TA_CENTER,
        textColor=GOLD, fontName="Helvetica", spaceAfter=8
    )
    styles["title_page_author"] = ParagraphStyle(
        "title_page_author",
        fontSize=14, leading=20, alignment=TA_CENTER,
        textColor=LGRAY, fontName="Helvetica"
    )

    styles["chapter_heading"] = ParagraphStyle(
        "chapter_heading",
        fontSize=22, leading=30, alignment=TA_LEFT,
        textColor=NAVY, fontName="Helvetica-Bold",
        spaceBefore=18, spaceAfter=8
    )
    styles["section_heading"] = ParagraphStyle(
        "section_heading",
        fontSize=15, leading=22, alignment=TA_LEFT,
        textColor=NAVY, fontName="Helvetica-Bold",
        spaceBefore=14, spaceAfter=6
    )
    styles["subsection_heading"] = ParagraphStyle(
        "subsection_heading",
        fontSize=12, leading=18, alignment=TA_LEFT,
        textColor=GOLD, fontName="Helvetica-Bold",
        spaceBefore=10, spaceAfter=4
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontSize=11, leading=17, alignment=TA_JUSTIFY,
        textColor=black, fontName="Helvetica",
        spaceAfter=8
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontSize=11, leading=17, alignment=TA_LEFT,
        textColor=black, fontName="Helvetica",
        leftIndent=20, bulletIndent=10, spaceAfter=4,
        bulletText="•"
    )
    styles["callout"] = ParagraphStyle(
        "callout",
        fontSize=11, leading=17, alignment=TA_LEFT,
        textColor=NAVY, fontName="Helvetica-BoldOblique",
        leftIndent=20, rightIndent=20,
        spaceBefore=8, spaceAfter=8
    )
    styles["toc_title"] = ParagraphStyle(
        "toc_title",
        fontSize=20, leading=28, alignment=TA_CENTER,
        textColor=NAVY, fontName="Helvetica-Bold", spaceAfter=20
    )
    styles["toc_entry"] = ParagraphStyle(
        "toc_entry",
        fontSize=12, leading=20, alignment=TA_LEFT,
        textColor=black, fontName="Helvetica", leftIndent=10, spaceAfter=4
    )

    return styles


# ═══════════════════════════════════════════════════════════════════════════
# Helper builders
# ═══════════════════════════════════════════════════════════════════════════
def gold_rule():
    return HRFlowable(width="100%", thickness=1.5, color=GOLD, spaceAfter=10)


def chapter_rule():
    return HRFlowable(width="100%", thickness=0.5, color=LGRAY, spaceAfter=6)


def chapter(styles, number, title):
    """Return flowables for a chapter heading (with a page break before it)."""
    return [
        PageBreak(),
        Paragraph(f"Chapter {number}", styles["subsection_heading"]),
        Paragraph(title, styles["chapter_heading"]),
        gold_rule(),
        Spacer(1, 0.3 * cm),
    ]


def section(styles, title):
    return [Paragraph(title, styles["section_heading"])]


def sub(styles, title):
    return [Paragraph(title, styles["subsection_heading"])]


def body(styles, text):
    return Paragraph(text, styles["body"])


def bullet(styles, text):
    return Paragraph(text, styles["bullet"])


def callout(styles, text):
    return [
        Spacer(1, 0.2 * cm),
        Paragraph(f'<i>"{text}"</i>', styles["callout"]),
        Spacer(1, 0.2 * cm),
    ]


def tip_box(styles, label, text):
    """A highlighted tip / exercise box."""
    data = [[Paragraph(f"<b>{label}</b>", styles["subsection_heading"]),
             Paragraph(text, styles["body"])]]
    t = Table(data, colWidths=[3 * cm, PAGE_W - MARGIN * 2 - 3 * cm - 0.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), OFFWHT),
        ("BOX",        (0, 0), (-1, -1), 1, GOLD),
        ("VALIGN",     (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [Spacer(1, 0.3 * cm), t, Spacer(1, 0.3 * cm)]


# ═══════════════════════════════════════════════════════════════════════════
# Title page (drawn directly on the canvas via an onFirstPage callback)
# ═══════════════════════════════════════════════════════════════════════════
def title_page_callback(canvas_obj, doc):
    canvas_obj.saveState()

    # Navy gradient background (approximate with two rectangles)
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    canvas_obj.setFillColor(DARK)
    canvas_obj.rect(0, 0, PAGE_W, PAGE_H * 0.35, fill=1, stroke=0)

    # Gold accent line top
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(3)
    canvas_obj.line(MARGIN, PAGE_H - 1.5 * cm, PAGE_W - MARGIN, PAGE_H - 1.5 * cm)

    # Gold accent line bottom
    canvas_obj.line(MARGIN, 1.5 * cm, PAGE_W - MARGIN, 1.5 * cm)

    # Main title
    canvas_obj.setFillColor(WHITE)
    canvas_obj.setFont("Helvetica-Bold", 38)
    canvas_obj.drawCentredString(PAGE_W / 2, PAGE_H - 5 * cm, "BRAIN &")
    canvas_obj.drawCentredString(PAGE_W / 2, PAGE_H - 6.5 * cm, "NEUROSCIENCE BASICS")

    # Subtitle
    canvas_obj.setFillColor(GOLD)
    canvas_obj.setFont("Helvetica", 18)
    canvas_obj.drawCentredString(
        PAGE_W / 2, PAGE_H - 8.2 * cm,
        "A Practical Guide to Understanding Your Mind"
    )
    canvas_obj.drawCentredString(
        PAGE_W / 2, PAGE_H - 9.2 * cm,
        "and Using It Better"
    )

    # Decorative circle
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(2)
    canvas_obj.circle(PAGE_W / 2, PAGE_H / 2 - 1 * cm, 1.8 * cm, stroke=1, fill=0)
    canvas_obj.setFont("Helvetica-Bold", 28)
    canvas_obj.setFillColor(GOLD)
    canvas_obj.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 2 * cm, "⚙")

    # Author
    canvas_obj.setFillColor(LGRAY)
    canvas_obj.setFont("Helvetica", 16)
    canvas_obj.drawCentredString(PAGE_W / 2, 3.5 * cm, "By Yash Sahu")

    canvas_obj.restoreState()


# ═══════════════════════════════════════════════════════════════════════════
# Table of Contents page
# ═══════════════════════════════════════════════════════════════════════════
TOC_ITEMS = [
    ("Introduction", "How to Use This Book"),
    ("Chapter 1",    "What Is the Brain?"),
    ("Chapter 2",    "Structure of the Brain"),
    ("Chapter 3",    "Neurons and Neural Communication"),
    ("Chapter 4",    "Brain Chemistry — Neurotransmitters"),
    ("Chapter 5",    "Neuroplasticity: How the Brain Changes"),
    ("Chapter 6",    "Memory and Learning"),
    ("Chapter 7",    "Attention and Focus"),
    ("Chapter 8",    "Emotions and the Brain"),
    ("Chapter 9",    "Decision-Making and Behaviour"),
    ("Chapter 10",   "Habits and the Brain"),
    ("Chapter 11",   "Stress and the Nervous System"),
    ("Chapter 12",   "Sleep and Brain Function"),
    ("Chapter 13",   "Practical Applications"),
    ("Conclusion",   "The Adaptable Brain"),
]


def build_toc(styles):
    items = [
        PageBreak(),
        Paragraph("Table of Contents", styles["toc_title"]),
        gold_rule(),
        Spacer(1, 0.4 * cm),
    ]
    for label, title in TOC_ITEMS:
        items.append(
            Paragraph(f"<b>{label}</b>  —  {title}", styles["toc_entry"])
        )
        items.append(Spacer(1, 0.15 * cm))
    return items


# ═══════════════════════════════════════════════════════════════════════════
# Book content
# ═══════════════════════════════════════════════════════════════════════════
def build_content(styles):
    e = []   # accumulator

    # ── INTRODUCTION ────────────────────────────────────────────────────────
    e += [PageBreak()]
    e += [Paragraph("Introduction", styles["chapter_heading"]), gold_rule(),
          Spacer(1, 0.3 * cm)]
    e += callout(styles,
        "Your brain is not just an organ. "
        "It is a prediction machine, a pattern recogniser, "
        "and occasionally, your worst enemy.")
    e.append(body(styles,
        "Neuroscience — the scientific study of the brain and nervous system — "
        "has produced an extraordinary body of knowledge over the past century. "
        "Yet most of that knowledge remains locked inside academic journals, "
        "inaccessible to the very people who could benefit from it most: "
        "curious, motivated individuals who want to understand how they think, "
        "feel, decide, and learn."))
    e.append(body(styles,
        "This book bridges that gap. It presents the core ideas of modern "
        "neuroscience in clear, jargon-free language, without sacrificing "
        "accuracy. Each chapter builds on the last, guiding you from basic "
        "anatomy all the way to evidence-based strategies for improving your "
        "everyday life."))
    e += section(styles, "What You Will Gain")
    for pt in [
        "A scientifically accurate picture of how your brain actually works.",
        "Freedom from common myths and oversimplifications.",
        "Practical tools rooted in neuroscience that you can use immediately.",
        "The vocabulary to keep learning on your own.",
    ]:
        e.append(bullet(styles, pt))
    e += section(styles, "How to Use This Book")
    e.append(body(styles,
        "You do not need any prior scientific knowledge. Read the chapters in "
        "order for the best experience — concepts build progressively — but "
        "each chapter is also designed to stand alone if you prefer to jump "
        "straight to a topic. Pay particular attention to the "
        "<b>Practical Exercises</b> sections; applying what you read is the "
        "fastest way to internalise it."))

    # ── CHAPTER 1 ────────────────────────────────────────────────────────────
    e += chapter(styles, 1, "What Is the Brain?")
    e.append(body(styles,
        "At first glance the brain looks unremarkable: roughly 1.4 kilograms "
        "of pinkish-grey tissue with the consistency of firm jelly. "
        "But packed inside that tissue are approximately 86 billion neurons "
        "and an even larger number of supporting cells called glia — "
        "forming a network so complex that it dwarfs any computing system "
        "ever built."))
    e += section(styles, "Core Functions")
    for pt in [
        "Processing and interpreting sensory input from the outside world.",
        "Orchestrating voluntary and involuntary movement.",
        "Regulating emotion, motivation, and social behaviour.",
        "Making predictions and decisions.",
        "Encoding and retrieving memories.",
    ]:
        e.append(bullet(styles, pt))
    e += section(styles, "The Brain as a Prediction Machine")
    e.append(body(styles,
        "Modern neuroscience has moved away from the idea that the brain is a "
        "passive receiver of sensory data. Instead, it is better understood as "
        "a prediction engine. Rather than waiting for the world to happen and "
        "then reacting, the brain constantly generates predictions about what "
        "is about to happen, then compares those predictions against incoming "
        "signals. Only the <i>difference</i> — the prediction error — "
        "receives heavy processing."))
    e += callout(styles,
        "Key Insight: Your brain does not show you reality. "
        "It creates a model of reality based on past experience.")
    e.append(body(styles,
        "This has profound implications. It explains why eyewitness accounts "
        "are unreliable, why first impressions stick, and why changing a habit "
        "requires deliberate and sustained effort."))
    e += sub(styles, "Practical Takeaway")
    e.append(body(styles,
        "When you feel absolutely certain about something, pause. "
        "Ask yourself: 'Is this what I actually observed, or is it my brain "
        "filling in the gaps?' This single habit can improve the quality of "
        "your decisions enormously."))

    # ── CHAPTER 2 ────────────────────────────────────────────────────────────
    e += chapter(styles, 2, "Structure of the Brain")
    e.append(body(styles,
        "Understanding brain structure is like learning the layout of a city "
        "before you navigate it. You do not need to memorise every street, "
        "but knowing the districts and how they relate saves a great deal of "
        "confusion later."))
    e += section(styles, "The Three Major Divisions")
    e += sub(styles, "1. Cerebrum")
    e.append(body(styles,
        "The cerebrum is the largest part of the brain, accounting for about "
        "85 % of total brain weight. Its deeply folded outer layer — the "
        "cerebral cortex — is where the most sophisticated processing happens: "
        "conscious thought, language, voluntary movement, reasoning, and "
        "abstract planning."))
    e += sub(styles, "2. Cerebellum")
    e.append(body(styles,
        "The cerebellum sits at the back and bottom of the brain. It "
        "coordinates voluntary movement, balance, and posture. Damage here "
        "does not cause paralysis but produces clumsy, uncoordinated movement. "
        "Recent research has also linked the cerebellum to aspects of "
        "cognition and emotion."))
    e += sub(styles, "3. Brainstem")
    e.append(body(styles,
        "The brainstem connects the cerebrum to the spinal cord and regulates "
        "survival-critical automatic functions: breathing, heart rate, blood "
        "pressure, and the sleep–wake cycle. Because these functions are "
        "essential for life, the brainstem is evolutionarily the oldest and most "
        "protected part of the brain."))
    e += section(styles, "The Four Lobes of the Cerebral Cortex")
    lobe_data = [
        ["Frontal Lobe",   "Decision-making, planning, impulse control, "
                           "working memory, personality, voluntary movement."],
        ["Parietal Lobe",  "Sensory integration, spatial awareness, "
                           "body position (proprioception), arithmetic."],
        ["Temporal Lobe",  "Auditory processing, language comprehension "
                           "(Wernicke's area), long-term memory (hippocampus "
                           "lies just below)."],
        ["Occipital Lobe", "Visual processing — nearly a third of the cortex "
                           "is devoted to vision."],
    ]
    for name, desc in lobe_data:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "The Limbic System")
    e.append(body(styles,
        "Beneath the cortex lies a collection of interconnected structures "
        "known collectively as the limbic system. Key components include:"))
    for pt in [
        "<b>Hippocampus</b> — essential for forming new long-term memories "
        "and spatial navigation.",
        "<b>Amygdala</b> — evaluates emotional significance, especially threat. "
        "Central to fear, anxiety, and emotional memory.",
        "<b>Hypothalamus</b> — regulates hunger, thirst, body temperature, "
        "hormones, and the stress response.",
        "<b>Thalamus</b> — the brain's relay station, routing sensory signals "
        "to the appropriate cortical areas.",
    ]:
        e.append(bullet(styles, pt))

    # ── CHAPTER 3 ────────────────────────────────────────────────────────────
    e += chapter(styles, 3, "Neurons and Neural Communication")
    e.append(body(styles,
        "Everything the brain does — every thought, memory, feeling, and "
        "movement — is ultimately the result of neurons communicating with "
        "one another. Understanding how they work is the foundation of "
        "understanding the brain."))
    e += section(styles, "Structure of a Neuron")
    for pt in [
        "<b>Dendrites</b> — branching extensions that receive incoming signals "
        "from other neurons.",
        "<b>Cell body (soma)</b> — integrates all incoming signals and keeps "
        "the neuron alive.",
        "<b>Axon</b> — a long cable that transmits the electrical signal away "
        "from the cell body.",
        "<b>Myelin sheath</b> — a fatty insulating layer around the axon that "
        "dramatically speeds up signal transmission.",
        "<b>Axon terminals</b> — the tips of the axon where chemical signals "
        "are released to the next neuron.",
    ]:
        e.append(bullet(styles, pt))
    e += section(styles, "How Neurons Communicate")
    e += sub(styles, "Step 1 — The Electrical Signal (Action Potential)")
    e.append(body(styles,
        "When a neuron receives enough input, its electrical charge changes "
        "rapidly — a process called an <i>action potential</i>. "
        "This electrical pulse travels down the axon at speeds of up to "
        "120 metres per second (faster in myelinated fibres)."))
    e += sub(styles, "Step 2 — The Chemical Signal (Synapse)")
    e.append(body(styles,
        "At the axon terminal the electrical signal triggers the release of "
        "chemical messengers called <i>neurotransmitters</i> into the tiny "
        "gap between two neurons — the <i>synaptic cleft</i>. "
        "These molecules bind to receptors on the receiving neuron, either "
        "exciting it (making it more likely to fire) or inhibiting it "
        "(making it less likely to fire)."))
    e += callout(styles,
        "\"Neurons that fire together, wire together.\" "
        "— Donald Hebb, 1949")
    e.append(body(styles,
        "This principle, known as Hebbian learning, is the cellular basis of "
        "all learning and memory. Every time two neurons activate together "
        "repeatedly, the synapse between them grows stronger — literally "
        "encoding an association in physical form."))
    e += tip_box(styles, "🔬 Key Idea",
        "Learning is not merely mental effort — it is a physical restructuring "
        "of the brain. Every new skill or memory you form changes the "
        "connectivity of your neural network.")

    # ── CHAPTER 4 ────────────────────────────────────────────────────────────
    e += chapter(styles, 4, "Brain Chemistry — Neurotransmitters")
    e.append(body(styles,
        "If neurons are the wiring of the brain, neurotransmitters are the "
        "signals running through that wiring. These chemical messengers "
        "exert an enormous influence on mood, motivation, cognition, and "
        "behaviour. Popular culture has reduced them to simplistic slogans "
        "('serotonin = happiness') but the reality is far richer."))
    e += section(styles, "Key Neurotransmitters")
    nt_data = [
        ("Dopamine",
         "Widely misunderstood as the 'pleasure chemical', dopamine is more "
         "accurately the <i>anticipation and drive</i> signal. It is released "
         "when the brain expects a reward — not necessarily when it receives "
         "one. Dopamine motivates you to seek, explore, and work towards goals. "
         "Dysregulation is implicated in addiction, ADHD, and Parkinson's "
         "disease."),
        ("Serotonin",
         "Serotonin contributes to mood stability, feelings of well-being, "
         "and social confidence. Low serotonin is associated with depression "
         "and anxiety, though the relationship is far more complex than a "
         "simple deficiency model. Most serotonin is produced in the gut, "
         "illustrating the profound gut–brain connection."),
        ("GABA (γ-aminobutyric acid)",
         "GABA is the brain's primary inhibitory neurotransmitter. "
         "It reduces neuronal excitability, producing calming effects. "
         "Alcohol, benzodiazepines, and many sleep medications work by "
         "enhancing GABA activity."),
        ("Glutamate",
         "The principal excitatory neurotransmitter. Glutamate is essential "
         "for learning and memory — it drives the synaptic strengthening "
         "described in the previous chapter. Excessive glutamate activity "
         "can cause neurotoxicity."),
        ("Acetylcholine",
         "Critical for attention, learning, and memory formation. "
         "In the peripheral nervous system, acetylcholine drives muscle "
         "contraction. Alzheimer's disease involves the early destruction "
         "of acetylcholine-producing neurons."),
        ("Noradrenaline (Norepinephrine)",
         "Regulates alertness, attention, and the 'fight-or-flight' response. "
         "Elevated during stress and danger; plays a key role in focus "
         "and arousal."),
        ("Cortisol",
         "Technically a hormone rather than a neurotransmitter, cortisol is "
         "released by the adrenal glands in response to stress. "
         "Short-term cortisol boosts energy and focus. "
         "Chronically elevated cortisol damages the hippocampus, impairs "
         "memory, and suppresses immune function."),
    ]
    for name, desc in nt_data:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += tip_box(styles, "⚠️ Reality Check",
        "Neurotransmitter systems interact in enormously complex ways. "
        "Statements like 'just boost your dopamine' or 'low serotonin causes "
        "depression' are dangerous oversimplifications. "
        "Treat supplement claims that target single neurotransmitters "
        "with healthy scepticism.")

    # ── CHAPTER 5 ────────────────────────────────────────────────────────────
    e += chapter(styles, 5, "Neuroplasticity: How the Brain Changes")
    e.append(body(styles,
        "For much of the 20th century, scientists believed the adult brain was "
        "fixed — that the neurons you were born with were all you would ever "
        "have and that their connections were essentially permanent. "
        "This idea has been comprehensively overturned."))
    e.append(body(styles,
        "We now know that the brain remains plastic throughout life: "
        "it forms new synaptic connections, strengthens or weakens existing "
        "ones, and can even generate new neurons (neurogenesis) in specific "
        "regions such as the hippocampus."))
    e += section(styles, "Types of Neuroplasticity")
    e += sub(styles, "Synaptic Plasticity")
    e.append(body(styles,
        "The strengthening or weakening of individual synapses based on "
        "activity. This is the micro-level mechanism of learning and memory. "
        "Long-Term Potentiation (LTP) — the synaptic equivalent of 'practice "
        "makes permanent' — is the best-studied form."))
    e += sub(styles, "Structural Plasticity")
    e.append(body(styles,
        "Physical changes in the architecture of the brain: new dendritic "
        "branches grow, axons extend, and neural circuits reorganise. "
        "The famous London taxi-driver study found enlarged hippocampi in "
        "experienced cab drivers compared to controls — a direct structural "
        "consequence of intense spatial navigation."))
    e += sub(styles, "Functional Plasticity")
    e.append(body(styles,
        "One region can take over functions previously performed by a damaged "
        "area. Stroke rehabilitation exploits this property: with targeted "
        "practice, healthy brain tissue can partially compensate for lost "
        "function."))
    e += section(styles, "The Core Rule of Neuroplasticity")
    e += callout(styles, "Repetition + focused attention = stronger neural pathways.")
    e.append(body(styles,
        "Neither repetition alone nor attention alone is sufficient. "
        "Mindless repetition produces weak, shallow learning. "
        "Attention without practice produces no physical change. "
        "Together, they drive the synaptic strengthening that makes "
        "a skill automatic."))
    e += tip_box(styles, "🧠 Practical Exercise",
        "Choose one skill you want to develop. Practise it for 10–20 minutes "
        "daily with full attention (no phone, no background noise). "
        "Do this for four weeks. You will have physically restructured neural "
        "circuits in your brain — not metaphorically, but literally.")

    # ── CHAPTER 6 ────────────────────────────────────────────────────────────
    e += chapter(styles, 6, "Memory and Learning")
    e.append(body(styles,
        "Memory is often imagined as a video recording — a faithful archive "
        "of past events waiting to be played back. "
        "This model is almost entirely wrong. "
        "Memory is <i>reconstructive</i>: every time you recall something, "
        "you partially rebuild it, influenced by your current knowledge, "
        "mood, and expectations. This is why memories change over time "
        "and why two people who witnessed the same event can give "
        "genuinely different accounts."))
    e += section(styles, "Types of Memory")
    mem_types = [
        ("Sensory memory",
         "A very brief (under 1 second) trace of sensory input. "
         "Most of it is discarded immediately."),
        ("Working memory",
         "Your mental whiteboard — holds 4–7 chunks of information for "
         "active use. Limited in capacity; central to reasoning, "
         "comprehension, and problem-solving."),
        ("Short-term memory",
         "A temporary store that can last seconds to hours without rehearsal."),
        ("Long-term memory",
         "Virtually unlimited in capacity. Divided into declarative memory "
         "(facts and events) and procedural memory (skills and habits)."),
        ("Episodic memory",
         "Personal autobiographical memories — 'what happened to me'."),
        ("Semantic memory",
         "General world knowledge — facts, concepts, language."),
    ]
    for name, desc in mem_types:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "How Memory Formation Works")
    for step, desc in [
        ("Encoding", "New information enters working memory. "
                     "Emotional significance, attention, and prior knowledge "
                     "strongly influence how well it is encoded."),
        ("Consolidation", "Over hours and especially during sleep, the "
                          "memory is stabilised and transferred to long-term "
                          "storage. The hippocampus plays a central role."),
        ("Storage", "The memory is distributed across the cortex, "
                    "not stored in any single location."),
        ("Retrieval", "Recalling a memory involves partial reconstruction. "
                      "Context and emotional state at retrieval matter "
                      "enormously."),
    ]:
        e += sub(styles, step)
        e.append(body(styles, desc))
    e += section(styles, "Evidence-Based Learning Strategies")
    e += tip_box(styles, "📚 Spaced Repetition",
        "Review material at increasing intervals rather than cramming. "
        "The 'forgetting curve' means material studied once is rapidly lost. "
        "Spaced repetition exploits the desirable difficulty of near-forgetting "
        "to drive deeper encoding. Apps like Anki automate this process.")
    e += tip_box(styles, "📚 Active Recall",
        "Testing yourself — closing the book and trying to remember — "
        "is far more effective than re-reading. This is the 'retrieval "
        "practice effect'. Every recall attempt strengthens the memory trace.")
    e += tip_box(styles, "📚 Elaborative Encoding",
        "Connect new information to things you already know. "
        "Ask 'How does this relate to what I learned in Chapter 5?' "
        "The more connections, the more retrieval routes, "
        "and the more robust the memory.")
    e += tip_box(styles, "📚 The Feynman Technique",
        "Explain the concept in simple language as if teaching a beginner. "
        "Gaps in your explanation reveal gaps in your understanding, "
        "directing you back to study exactly what you need.")

    # ── CHAPTER 7 ────────────────────────────────────────────────────────────
    e += chapter(styles, 7, "Attention and Focus")
    e.append(body(styles,
        "Attention is the brain's resource-allocation system. "
        "Because the nervous system receives far more sensory information "
        "than it can fully process, attention acts as a selective filter — "
        "determining what gets through to conscious awareness and receives "
        "detailed processing, and what gets suppressed."))
    e += section(styles, "The Attention System")
    attn_types = [
        ("Selective attention",
         "The ability to focus on one stimulus while ignoring others. "
         "Classic demonstration: the 'invisible gorilla' experiment, "
         "in which people focused on counting basketball passes completely "
         "fail to notice a person in a gorilla suit walking through the scene."),
        ("Sustained attention (vigilance)",
         "Maintaining focus over an extended period. "
         "Degrades after 20–45 minutes of intense effort without breaks. "
         "This is why the Pomodoro Technique works."),
        ("Divided attention",
         "The brain cannot truly multitask on complex cognitive work. "
         "What feels like multitasking is rapid task-switching, each switch "
         "incurring a 'residue' — lingering activation from the previous task "
         "that reduces performance on the next."),
        ("Executive attention",
         "Top-down control of attention by the prefrontal cortex. "
         "Allows you to resist distraction, suppress automatic responses, "
         "and deliberately redirect focus."),
    ]
    for name, desc in attn_types:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "The Cost of Distraction")
    e.append(body(styles,
        "Every time you switch away from a task and return to it, "
        "you pay a switching cost. Research by Gloria Mark at UC Irvine "
        "found that after an interruption, it takes an average of "
        "23 minutes to return to the original task at full depth. "
        "In an environment of constant notifications, the cumulative "
        "switching cost is staggering."))
    e += callout(styles,
        "Distractions do not merely steal time — "
        "they weaken the neural circuits responsible for deep focus.")
    e += tip_box(styles, "🎯 Practical Exercise",
        "Schedule two 'deep work' sessions per day of 25–45 minutes each. "
        "Before each session: silence all notifications, set a timer, "
        "and write a single specific goal on paper. "
        "After each session, take a proper break (walk, water, rest eyes). "
        "Treat sustained attention like a muscle: train it progressively, "
        "rest it between sets.")

    # ── CHAPTER 8 ────────────────────────────────────────────────────────────
    e += chapter(styles, 8, "Emotions and the Brain")
    e.append(body(styles,
        "Emotions are often portrayed as the enemy of rational thought — "
        "irrational forces that hijack good judgement. "
        "Modern neuroscience tells a more nuanced story: "
        "emotions are sophisticated, fast, biological signals that have "
        "guided human survival for millions of years. "
        "The problem is not that we have emotions, but that they can "
        "misfire in contexts for which they were not designed."))
    e += section(styles, "Key Brain Structures in Emotion")
    for name, desc in [
        ("Amygdala",
         "Two almond-shaped clusters deep in the temporal lobes, the amygdala "
         "rapidly evaluates incoming stimuli for threat or reward. "
         "It can trigger a fear response before conscious perception is "
         "complete — one reason we can 'startle' before we know why. "
         "The amygdala encodes the emotional significance of memories, "
         "which is why emotionally charged events are remembered more vividly."),
        ("Prefrontal Cortex (PFC)",
         "The prefrontal cortex exerts top-down regulation over the amygdala. "
         "It enables us to evaluate, reappraise, and modulate emotional "
         "responses. Importantly, the PFC is the last region of the brain "
         "to fully mature (not until the mid-20s), which partly explains "
         "adolescent impulsivity."),
        ("Anterior Cingulate Cortex (ACC)",
         "Monitors conflict between emotional impulses and rational goals. "
         "Active when you resist a temptation or notice you are "
         "about to say something impulsive."),
        ("Insula",
         "Involved in interoception — awareness of internal body states "
         "such as heartbeat, hunger, and physical sensations. "
         "Plays a key role in empathy and the feeling of disgust."),
    ]:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "Emotion Regulation")
    e.append(body(styles,
        "The ability to regulate emotions — not suppress them, "
        "but to understand and modulate them — is one of the most "
        "consequential skills a person can develop. "
        "Research consistently links emotion regulation capacity with "
        "mental health, relationship quality, and professional success."))
    e += sub(styles, "Cognitive Reappraisal")
    e.append(body(styles,
        "Changing how you interpret an event ('This setback is information, "
        "not evidence of failure') reduces amygdala activation and shifts "
        "processing back to the PFC. This is the empirical foundation "
        "of Cognitive Behavioural Therapy (CBT)."))
    e += tip_box(styles, "🧘 Practical Exercise",
        "When you feel a strong emotion, before reacting:\n"
        "1. Pause for 5–10 seconds (this allows PFC input to arrive).\n"
        "2. Name the emotion specifically: 'I feel frustrated' rather than "
        "'I feel bad'. Research by Matthew Lieberman shows that labelling "
        "an emotion — affect labelling — measurably reduces amygdala "
        "activation.\n"
        "3. Ask: 'Is this response proportionate to the actual situation, "
        "or is my brain pattern-matching to something from the past?'")

    # ── CHAPTER 9 ────────────────────────────────────────────────────────────
    e += chapter(styles, 9, "Decision-Making and Behaviour")
    e.append(body(styles,
        "How do you decide what to eat for breakfast, whether to trust "
        "a stranger, or whether to accept a job offer? "
        "Decision neuroscience reveals that these apparently different "
        "processes share common underlying mechanisms — "
        "and that our intuitions about how we decide are often wrong."))
    e += section(styles, "Two Systems of Thinking")
    e.append(body(styles,
        "Psychologist Daniel Kahneman popularised a framework — "
        "grounded in decades of cognitive and neural research — "
        "distinguishing two modes of thinking:"))
    for name, desc in [
        ("System 1 (Fast, Automatic)",
         "Fast, automatic, emotional, unconscious, and effortless. "
         "Drives the vast majority of everyday decisions. "
         "Relies heavily on heuristics — mental shortcuts that are usually "
         "efficient but can produce systematic errors (cognitive biases)."),
        ("System 2 (Slow, Deliberate)",
         "Slow, deliberate, logical, and effortful. "
         "Engages the prefrontal cortex and working memory. "
         "Has limited capacity and fatigues quickly (decision fatigue). "
         "Most people believe they use System 2 for important decisions "
         "far more than they actually do."),
    ]:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "Common Cognitive Biases")
    for bias, desc in [
        ("Confirmation bias",
         "Seeking evidence that confirms existing beliefs while ignoring "
         "contradictory evidence."),
        ("Availability heuristic",
         "Judging probability by how easily an example comes to mind. "
         "'Plane crashes feel more dangerous than car crashes' because "
         "plane crashes receive more media coverage."),
        ("Sunk cost fallacy",
         "Continuing an investment (of money, time, or effort) because of "
         "past costs, not future value."),
        ("Dunning-Kruger effect",
         "Those with limited knowledge in a domain overestimate their "
         "competence; experts often underestimate theirs."),
    ]:
        e += sub(styles, bias)
        e.append(body(styles, desc))
    e += tip_box(styles, "🎯 Practical Tip",
        "For any high-stakes decision: write it down, sleep on it, "
        "and actively look for evidence against your preferred option. "
        "This three-step process systematically engages System 2, "
        "reduces emotional bias, and dramatically improves decision quality.")

    # ── CHAPTER 10 ───────────────────────────────────────────────────────────
    e += chapter(styles, 10, "Habits and the Brain")
    e.append(body(styles,
        "Habits are not a sign of laziness or weakness — they are "
        "the brain's elegant efficiency mechanism. "
        "By automating frequently repeated behaviours, the brain frees "
        "up limited conscious resources for novel situations. "
        "This is enormously adaptive: you can drive to work, hold a "
        "conversation, and drink coffee simultaneously, because driving "
        "has become a habit, requiring minimal executive input."))
    e += section(styles, "The Neuroscience of Habits")
    e.append(body(styles,
        "Habits are encoded primarily in the <b>basal ganglia</b> — "
        "a cluster of subcortical structures involved in procedural learning "
        "and reward-based behaviour. "
        "When a behaviour is performed repeatedly in a consistent context, "
        "the basal ganglia begin to 'chunk' the sequence, allowing it "
        "to run automatically without prefrontal oversight."))
    e += section(styles, "The Habit Loop")
    e.append(body(styles,
        "MIT researcher Ann Graybiel identified a three-part cycle underlying "
        "all habitual behaviour:"))
    for part, desc in [
        ("Cue",
         "A trigger in the environment (a time, place, emotional state, "
         "or preceding behaviour) that activates the habit automatically."),
        ("Routine",
         "The habitual behaviour itself — physical, mental, or emotional."),
        ("Reward",
         "A positive outcome (pleasure, relief, satisfaction) that "
         "reinforces the cue-routine link, making the behaviour "
         "more likely to repeat."),
    ]:
        e += sub(styles, part)
        e.append(body(styles, desc))
    e += section(styles, "How to Change a Habit")
    e += callout(styles,
        "You cannot erase a habit. You can only replace it.")
    e.append(body(styles,
        "The basal ganglia never forget an encoded habit loop. "
        "Attempting to simply 'stop' a habit is why willpower-based "
        "approaches fail. The effective strategy is to intercept the "
        "loop at the routine stage:"))
    for step in [
        "Identify the cue for the habit you wish to change.",
        "Choose a new routine that delivers a similar reward.",
        "Repeat the new cue → new routine → same reward loop consistently.",
        "The old routine fades from active use (though never fully disappears).",
    ]:
        e.append(bullet(styles, step))
    e += tip_box(styles, "🔄 Habit Stacking",
        "Link a new desired habit to an existing strong habit: "
        "'After I pour my morning coffee [existing cue], "
        "I will meditate for five minutes [new routine].' "
        "The existing habit provides a reliable, automatic cue.")

    # ── CHAPTER 11 ───────────────────────────────────────────────────────────
    e += chapter(styles, 11, "Stress and the Nervous System")
    e.append(body(styles,
        "Stress is not inherently harmful — it is a biological response "
        "that evolved to mobilise the body's resources in the face of "
        "immediate physical danger. The problem is that in modern life, "
        "this ancient system is activated by psychological threats "
        "(deadlines, social rejection, financial worry) that do not "
        "resolve in the way a physical predator would."))
    e += section(styles, "The Autonomic Nervous System")
    e.append(body(styles,
        "The autonomic nervous system (ANS) regulates involuntary body "
        "functions and has two complementary branches:"))
    for name, desc in [
        ("Sympathetic Nervous System (SNS) — 'Fight or Flight'",
         "Activates in response to perceived threat. "
         "Releases adrenaline and cortisol; increases heart rate, "
         "blood pressure, and blood flow to muscles; suppresses digestion "
         "and immune function. Prepares the body for immediate physical action."),
        ("Parasympathetic Nervous System (PNS) — 'Rest and Digest'",
         "Active during calm, safety, and recovery. "
         "Slows heart rate, promotes digestion, enables immune function, "
         "and facilitates long-term cellular repair. "
         "The vagus nerve is the primary PNS conduit."),
    ]:
        e += sub(styles, name)
        e.append(body(styles, desc))
    e += section(styles, "Acute vs. Chronic Stress")
    e.append(body(styles,
        "Short-term (acute) stress can be beneficial — it sharpens "
        "focus and enhances memory consolidation for the stressed event. "
        "Chronic stress is damaging. Persistently elevated cortisol:"))
    for pt in [
        "Shrinks the hippocampus, impairing memory and learning.",
        "Weakens prefrontal cortex function, degrading decision-making.",
        "Suppresses the immune system, increasing vulnerability to illness.",
        "Disrupts sleep, creating a vicious cycle of stress and fatigue.",
        "Accelerates cellular ageing (shortens telomeres).",
    ]:
        e.append(bullet(styles, pt))
    e += section(styles, "Evidence-Based Stress Regulation Tools")
    e += tip_box(styles, "🌬️ Physiological Sigh",
        "A double inhale through the nose followed by a long exhale through "
        "the mouth. This technique — studied by Andrew Huberman at Stanford — "
        "rapidly activates the parasympathetic system and is the fastest "
        "known method of reducing acute stress in real time.")
    e += tip_box(styles, "🏃 Physical Movement",
        "Even a 10-minute walk reduces cortisol and adrenaline. "
        "Regular aerobic exercise is one of the most potent tools for "
        "building long-term stress resilience by reducing HPA-axis reactivity.")
    e += tip_box(styles, "📵 Stimulus Control",
        "Constant digital stimulation keeps the SNS in a low-grade "
        "activated state. Scheduled periods of reduced stimulation — "
        "no screen, no music, no podcast — allow genuine recovery.")

    # ── CHAPTER 12 ───────────────────────────────────────────────────────────
    e += chapter(styles, 12, "Sleep and Brain Function")
    e.append(body(styles,
        "Sleep is not a passive period of inactivity. "
        "It is an active, tightly regulated biological process during which "
        "the brain performs critical maintenance and consolidation work "
        "that cannot happen while you are awake. "
        "The idea that high performers 'sleep less' is not just false — "
        "it is backwards. Reducing sleep is one of the most reliable ways "
        "to impair almost every cognitive function."))
    e += section(styles, "What Happens During Sleep")
    for phase, desc in [
        ("NREM Stage 1 & 2 (Light Sleep)",
         "Heart rate and body temperature drop. "
         "Sleep spindles appear — bursts of neural activity associated "
         "with the transfer of memories from hippocampus to cortex."),
        ("NREM Stage 3 (Deep / Slow-Wave Sleep)",
         "The body releases growth hormone and repairs tissue. "
         "Deep sleep is critical for declarative memory consolidation "
         "and immune function. The glymphatic system — the brain's "
         "waste-clearance network — is most active here, "
         "flushing out metabolic byproducts including amyloid-beta "
         "(implicated in Alzheimer's disease)."),
        ("REM (Rapid Eye Movement) Sleep",
         "The brain is highly active. Emotional memories are processed "
         "and integrated; procedural and creative memory is consolidated. "
         "Dreams occur. REM sleep increases in later sleep cycles, "
         "which is why cutting sleep short disproportionately "
         "reduces REM sleep."),
    ]:
        e += sub(styles, phase)
        e.append(body(styles, desc))
    e += section(styles, "Consequences of Sleep Deprivation")
    e.append(body(styles,
        "After 17–19 hours awake, cognitive performance is equivalent "
        "to a blood alcohol level of 0.05 %. "
        "Chronic short sleep (under 6 hours) is associated with "
        "increased risk of obesity, cardiovascular disease, diabetes, "
        "mental health disorders, and dementia."))
    e += section(styles, "Sleep Optimisation — Evidence-Based Rules")
    for rule in [
        "Aim for 7–9 hours of sleep per night (most adults need 8).",
        "Maintain a consistent sleep and wake time, including weekends.",
        "Keep your bedroom cool (16–19 °C / 60–67 °F) and dark.",
        "Avoid caffeine after 2 pm; its half-life is ~5–7 hours.",
        "Avoid screens for 60–90 minutes before bed — blue light suppresses melatonin.",
        "Avoid alcohol within 3 hours of sleep; it disrupts REM.",
        "Regular aerobic exercise improves sleep quality significantly.",
    ]:
        e.append(bullet(styles, rule))

    # ── CHAPTER 13 — PRACTICAL APPLICATIONS ──────────────────────────────────
    e += chapter(styles, 13, "Practical Applications")
    e.append(body(styles,
        "This chapter synthesises the preceding 12 chapters into a "
        "coherent set of daily practices. Each practice is drawn directly "
        "from the neuroscience you have now learned, grounded in evidence, "
        "and immediately actionable."))

    e += section(styles, "1. Optimise Learning")
    for step in [
        "<b>Focus fully during study sessions.</b> "
        "Attention + repetition = neural pathway strengthening (Chapter 5).",
        "<b>Use active recall, not passive re-reading.</b> "
        "Close the book and retrieve (Chapter 6).",
        "<b>Space your practice.</b> "
        "Revisit material after 1 day, 3 days, 1 week, 1 month (Chapter 6).",
        "<b>Teach it.</b> The Feynman Technique forces genuine understanding "
        "and reveals gaps (Chapter 6).",
        "<b>Sleep after learning.</b> "
        "Consolidation happens during sleep; study before bed "
        "then sleep on it (Chapter 12).",
    ]:
        e.append(bullet(styles, step))

    e += section(styles, "2. Regulate Emotions")
    for step in [
        "<b>Pause before reacting.</b> "
        "Allow the prefrontal cortex to come online (Chapter 8).",
        "<b>Name the emotion specifically.</b> "
        "Affect labelling reduces amygdala activation (Chapter 8).",
        "<b>Use the physiological sigh</b> to down-regulate the stress "
        "response in real time (Chapter 11).",
        "<b>Practise cognitive reappraisal.</b> "
        "Ask: 'What is a more accurate interpretation of this situation?' "
        "(Chapter 8).",
    ]:
        e.append(bullet(styles, step))

    e += section(styles, "3. Build Lasting Habits")
    for step in [
        "<b>Design your environment.</b> "
        "Make cues for desired habits obvious and cues for unwanted habits "
        "invisible (Chapter 10).",
        "<b>Use habit stacking.</b> "
        "Attach new behaviours to existing strong habits (Chapter 10).",
        "<b>Reward the new routine immediately.</b> "
        "The dopamine system responds to immediate, not delayed, reward "
        "(Chapter 4).",
        "<b>Track your streak.</b> Visual progress reinforces dopaminergic "
        "anticipation of the next iteration (Chapters 4 and 10).",
    ]:
        e.append(bullet(styles, step))

    e += section(styles, "4. Maximise Cognitive Performance")
    for step in [
        "<b>Protect deep work time.</b> "
        "Block 2–4 hours daily for cognitively demanding work free of "
        "interruptions (Chapter 7).",
        "<b>Batch low-value tasks.</b> "
        "Group emails, admin, and routine decisions to protect "
        "System 2 capacity (Chapter 9).",
        "<b>Make important decisions earlier in the day</b> "
        "when prefrontal resources are freshest (Chapter 9).",
        "<b>Exercise regularly.</b> "
        "Aerobic exercise increases BDNF (brain-derived neurotrophic factor), "
        "promotes neurogenesis in the hippocampus, and improves mood, "
        "focus, and stress resilience.",
        "<b>Maintain sleep as non-negotiable.</b> "
        "No cognitive strategy compensates for chronic sleep deprivation "
        "(Chapter 12).",
    ]:
        e.append(bullet(styles, step))

    e += section(styles, "5. Manage Stress Proactively")
    for step in [
        "<b>Build in recovery periods.</b> "
        "The SNS cannot sustain chronic activation without cost. "
        "Scheduled downtime is maintenance, not laziness (Chapter 11).",
        "<b>Reduce background stimulation.</b> "
        "Constant low-level stimulation sustains mild SNS activation. "
        "Regular digital detox periods allow genuine parasympathetic "
        "recovery (Chapter 11).",
        "<b>Move your body daily.</b> "
        "Even 20–30 minutes of walking significantly reduces cortisol "
        "and improves mood (Chapter 11).",
    ]:
        e.append(bullet(styles, step))

    e += section(styles, "A Sample Daily Protocol")
    protocol = [
        ["Time", "Activity", "Neuroscience Rationale"],
        ["6:00–6:30", "Wake, brief exercise or walk",
         "Reduces cortisol; BDNF boost; sets circadian clock."],
        ["6:30–7:00", "No screens; breakfast; review today's single goal",
         "Protects PFC from early-morning dopamine spike."],
        ["7:00–9:00", "Deep work session (most cognitively demanding task)",
         "PFC resources peak; low interruption window."],
        ["9:00–9:15", "Break (walk, water, breathing)",
         "Sustained attention recovery; parasympathetic activation."],
        ["9:15–11:00", "Second deep work or learning session",
         "Spaced repetition; second focus block."],
        ["11:00–12:00", "Email, admin, low-cognition tasks",
         "Batching preserves System 2 for important decisions."],
        ["12:00–12:45", "Lunch; light walk",
         "Cortisol management; hippocampal neurogenesis."],
        ["13:00–14:00", "Creative or collaborative work",
         "Post-lunch alertness window after brief movement."],
        ["14:00–17:00", "Remaining focused tasks; no new caffeine",
         "Avoid caffeine after 14:00 to protect sleep."],
        ["21:00",       "Wind-down: dim lights, no screens",
         "Protect melatonin onset; prepare for consolidation."],
        ["22:00–6:00",  "Sleep (8 hours)",
         "Memory consolidation; glymphatic clearing; recovery."],
    ]
    t = Table(
        protocol,
        colWidths=[2.5 * cm, 5.5 * cm, PAGE_W - MARGIN * 2 - 8.4 * cm]
    )
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 10),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFFWHT, WHITE]),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("GRID",          (0, 0), (-1, -1), 0.5, LGRAY),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    e.append(Spacer(1, 0.4 * cm))
    e.append(t)

    # ── CONCLUSION ────────────────────────────────────────────────────────────
    e += [PageBreak()]
    e += [Paragraph("Conclusion", styles["chapter_heading"]), gold_rule(),
          Spacer(1, 0.3 * cm)]
    e.append(body(styles,
        "You have now covered the essential landscape of modern neuroscience — "
        "from the basic anatomy of the brain to the neural mechanisms that "
        "underlie memory, emotion, habit, decision-making, stress, and sleep. "
        "More importantly, each concept has been linked to actionable "
        "strategies rooted in that science."))
    e += callout(styles,
        "Your brain is adaptable, biased, efficient, and flawed. "
        "You cannot hack it overnight — but you can train it, shape it, "
        "and steadily improve how it works.")
    e.append(body(styles,
        "The gap between people is not, in general, one of raw intelligence. "
        "It is a gap in self-knowledge and in the quality of habits, "
        "decisions, and practices that accumulate over time. "
        "Neuroscience hands you the most powerful possible tool for closing "
        "that gap: an accurate model of how your own mind works."))
    e += section(styles, "Key Principles to Carry Forward")
    for pt in [
        "Your brain predicts reality — challenge your assumptions actively.",
        "Repetition + focused attention physically rewires your brain.",
        "Memory is reconstructive — test yourself, don't just re-read.",
        "Emotions are fast survival signals — label them, don't suppress them.",
        "Most decisions are made automatically — build good defaults.",
        "Habits cannot be erased — replace the routine, keep the reward.",
        "Chronic stress degrades the brain — recovery is non-negotiable.",
        "Sleep is maintenance — protect it with the same seriousness as food.",
    ]:
        e.append(bullet(styles, pt))
    e.append(Spacer(1, 0.5 * cm))
    e.append(body(styles,
        "The brain you have today is not the brain you are stuck with. "
        "It is the brain you have been given as a starting point. "
        "What you do with it — the habits you build, the skills you practise, "
        "the sleep you protect, the stress you manage — determines the "
        "brain you will have tomorrow."))
    e += callout(styles,
        "Begin today. Start small. Be consistent. The neuroscience is clear: "
        "that is enough.")

    return e


# ═══════════════════════════════════════════════════════════════════════════
# Main builder
# ═══════════════════════════════════════════════════════════════════════════
def build_ebook(output_path=OUTPUT_FILE):
    print(f"Building e-book → {output_path}")

    styles = build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN + 1 * cm,   # extra space for footer
        title="Brain & Neuroscience Basics",
        author="Yash Sahu",
        subject="A Practical Guide to Understanding Your Mind and Using It Better",
    )

    # ── Assemble story ────────────────────────────────────────────────────────
    story = []

    # Title page — rendered entirely by the onFirstPage canvas callback.
    # A minimal Spacer forces ReportLab to emit the first page; a PageBreak
    # then starts the TOC on a fresh page.
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # Table of Contents
    story += build_toc(styles)

    # Main content
    story += build_content(styles)

    # ── Build PDF ────────────────────────────────────────────────────────────
    doc.build(
        story,
        onFirstPage=title_page_callback,
        canvasmaker=NeuroscienceCanvas,
    )

    import os
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅  E-book generated successfully!")
    print(f"📄  File  : {output_path}")
    print(f"📦  Size  : {size_mb:.2f} MB")
    return output_path


if __name__ == "__main__":
    build_ebook()
