"""
ebook_content.py
Full textual content for "Religion Weaponized: The Dark Side of Faith"
by Yash Sahu.

Each chapter is a list of (element_type, text) tuples:
  - ('heading', text)      – chapter title
  - ('subheading', text)   – section sub-heading
  - ('body', text)         – regular paragraph
  - ('quote', text)        – pull-quote / block-quote
  - ('bullet', text)       – bullet-list item
"""

BOOK_METADATA = {
    "title": "Religion Weaponized",
    "subtitle": "The Dark Side of Faith",
    "author": "Yash Sahu",
    "publisher": "Independent Publication",
    "year": "2024",
    "language": "en",
    "description": (
        "An unflinching examination of how religious systems can be "
        "twisted into instruments of control, manipulation, and harm—and "
        "how survivors can reclaim their lives and spirituality."
    ),
    "keywords": [
        "religion", "religious trauma", "cult", "spiritual abuse",
        "religious manipulation", "healing", "recovery", "faith",
    ],
    "isbn": "",
    "rights": "All rights reserved.",
}

CHAPTERS = [
    {
        "number": 0,
        "title": "Introduction",
        "content": [
            ("body",
             "Religion has been one of the most powerful forces in human history. "
             "It has inspired great art, sustained communities through hardship, "
             "and offered billions of people a framework for meaning, morality, "
             "and transcendence. Yet the same institutions and belief systems that "
             "elevate the human spirit can, in the wrong hands, become weapons."),
            ("body",
             "This book is not an attack on faith. It is an examination of a "
             "troubling pattern that has repeated across cultures and centuries: "
             "the deliberate—or sometimes unconscious—use of sacred texts, "
             "rituals, leaders, and communities to exercise control over "
             "individuals, suppress dissent, and cause lasting harm."),
            ("body",
             "The pages that follow draw on historical case studies, psychological "
             "research, and the lived experiences of survivors. They are intended "
             "for anyone who has felt confused, hurt, or silenced within a "
             "religious context, as well as for those who love such a person and "
             "want to understand what they went through."),
            ("quote",
             "\"The first step toward healing is understanding what actually "
             "happened.\""),
            ("body",
             "Each chapter addresses a different dimension of religious weaponization: "
             "historical roots, modern tactics, the psychology of control, the path "
             "toward healing, and ultimately the possibility of a healthier "
             "relationship with spirituality."),
            ("body",
             "If any section feels personally familiar, you are not alone. "
             "Millions of people around the world carry the hidden wounds of "
             "spiritual abuse. This book is for you."),
        ],
    },
    {
        "number": 1,
        "title": "Chapter 1: The Weaponization of Faith",
        "content": [
            ("subheading", "What Does It Mean to Weaponize Religion?"),
            ("body",
             "To weaponize something is to repurpose a neutral or positive tool "
             "so that it causes harm. A scalpel that saves lives in a surgeon's "
             "hands becomes lethal in the hands of an attacker. Faith, similarly, "
             "contains the raw material for both liberation and oppression."),
            ("body",
             "Religious weaponization occurs when doctrines, rituals, community "
             "structures, or leadership authority are deliberately or systematically "
             "used to: control behavior through fear of divine punishment; "
             "silence critical thinking; exploit financial or emotional "
             "vulnerability; or justify violence, discrimination, and abuse."),
            ("subheading", "Three Core Mechanisms"),
            ("bullet",
             "Doctrinal Control: Convincing followers that one interpretation "
             "of sacred text is the only acceptable one, and that deviation "
             "leads to eternal damnation or divine abandonment."),
            ("bullet",
             "Social Control: Using the threat of shunning, excommunication, "
             "or community rejection to keep individuals in line."),
            ("bullet",
             "Psychological Control: Exploiting existential fears—death, "
             "meaninglessness, unworthiness—to keep followers dependent on "
             "religious leadership for reassurance."),
            ("body",
             "These mechanisms rarely operate in isolation. They reinforce "
             "one another, creating a closed system where questioning any "
             "single element is experienced as an attack on the entire "
             "spiritual identity of the community."),
            ("quote",
             "\"Power without accountability is dangerous in any domain. "
             "In religion, the claim that authority comes directly from God "
             "removes every normal check.\""),
            ("subheading", "Who Weaponizes Religion?"),
            ("body",
             "It would be comforting to think that religious abuse is always the "
             "work of obvious villains—charismatic fraudsters or extremist "
             "fringe groups. The reality is more complex. Weaponization can occur "
             "at every level of a religious institution: in the family home, "
             "in a local congregation, in national denominations, and in global "
             "movements. It can be perpetrated by deeply sincere believers who "
             "have never examined their assumptions, as well as by cynical "
             "manipulators who exploit faith for personal gain."),
            ("body",
             "Understanding this spectrum is essential for identifying harm, "
             "because the sincerity of the perpetrator does not reduce the damage "
             "done to the survivor."),
        ],
    },
    {
        "number": 2,
        "title": "Chapter 2: Historical Patterns of Religious Control",
        "content": [
            ("subheading", "Ancient Roots"),
            ("body",
             "The fusion of religious authority with political power is as old as "
             "recorded civilization. In ancient Egypt, the Pharaoh was considered "
             "a living deity; to disobey him was to sin against the cosmic order. "
             "In Mesopotamia, temple priests controlled vast agricultural resources "
             "in the name of the gods, a convenient arrangement that concentrated "
             "wealth and power in few hands."),
            ("body",
             "This is not to say that ancient religion was nothing but manipulation. "
             "Temples also served as hospitals, archives, and centers of learning. "
             "But the same institutions that preserved knowledge also enforced "
             "compliance through the language of divine will."),
            ("subheading", "The Medieval Inquisitions"),
            ("body",
             "Few historical episodes illustrate religious weaponization more "
             "starkly than the Inquisitions of medieval and early modern Europe. "
             "Established to stamp out heresy, these ecclesiastical courts "
             "prosecuted hundreds of thousands of people, using torture, exile, "
             "and execution to enforce doctrinal conformity."),
            ("body",
             "The Inquisitions are a case study in how the fear of supernatural "
             "consequences—eternal hellfire—can be leveraged to justify extreme "
             "earthly violence. The victim was told that her suffering was an act "
             "of mercy: better to be burned in this life than to burn forever in "
             "the next."),
            ("quote",
             "\"When suffering is reframed as divine mercy, abuse becomes "
             "invisible even to the abused.\""),
            ("subheading", "Colonial Religious Imperialism"),
            ("body",
             "The colonization of the Americas, Africa, and Asia was routinely "
             "justified in religious terms. Missionaries accompanied conquistadors. "
             "Indigenous spiritual traditions were outlawed. Children were taken "
             "from their families and placed in religious boarding schools designed "
             "to 'kill the Indian and save the man.' The psychological damage to "
             "entire communities has persisted for generations."),
            ("body",
             "Understanding this history is necessary not to assign collective "
             "guilt but to recognize a recurring pattern: the conflation of "
             "religious truth with cultural domination, and the resulting harm "
             "to those whose traditions are labeled inferior or demonic."),
            ("subheading", "Twentieth-Century Religious Violence"),
            ("body",
             "The twentieth century produced some of the most extreme examples "
             "of religious weaponization in history, from the Holocaust's "
             "exploitation of centuries-old Christian antisemitism to the mass "
             "suicides at Jonestown, where over 900 people—including hundreds "
             "of children—died after years of calculated psychological control "
             "under the religious leadership of Jim Jones."),
            ("body",
             "Jonestown in particular remains a landmark case in the study of "
             "cultic manipulation. Jones used the vocabulary of social justice "
             "and Christian scripture to build a community that became "
             "progressively more isolated, more controlled, and ultimately "
             "lethal. Survivors described how the slow escalation of control "
             "made each step feel normal until escape had become almost "
             "unthinkable."),
        ],
    },
    {
        "number": 3,
        "title": "Chapter 3: Modern Religious Manipulation Tactics",
        "content": [
            ("subheading", "Love Bombing"),
            ("body",
             "One of the most effective recruitment and retention tools in "
             "high-control religious groups is the practice known as love "
             "bombing: overwhelming a newcomer with warmth, attention, and a "
             "sense of instant belonging. For someone who is lonely, grieving, "
             "or searching for meaning, the experience can feel like finally "
             "coming home."),
            ("body",
             "The warmth is not necessarily fake. Members of high-control groups "
             "are often genuinely enthusiastic and caring within the bounds of "
             "the community. The manipulation lies in what comes next: as the "
             "newcomer becomes more embedded, boundaries are gradually tightened, "
             "outside relationships are discouraged, and critical thinking is "
             "labeled as spiritual weakness or demonic influence."),
            ("subheading", "Information Control"),
            ("bullet",
             "Restricting access to outside media, books, or internet content."),
            ("bullet",
             "Labeling critical information as 'apostate literature' or "
             "'spiritually dangerous.'"),
            ("bullet",
             "Creating an in-group vocabulary that makes communication with "
             "outsiders difficult."),
            ("bullet",
             "Discouraging or punishing members who research the group's history "
             "or doctrine independently."),
            ("body",
             "Information control is central to maintaining doctrinal authority. "
             "If members encounter contradictory evidence, the system must "
             "provide an explanation. In high-control groups, the standard "
             "answer is that the source of the contradiction is corrupted, "
             "biased, or spiritually compromised."),
            ("subheading", "Thought-Stopping Techniques"),
            ("body",
             "High-control groups frequently teach specific mental practices "
             "that interrupt critical thinking. These include: repetitive "
             "prayer or chanting that crowds out analytical thought; the "
             "doctrine that doubt is itself sinful, a trick of the devil, "
             "or evidence of insufficient faith; confession practices that "
             "place private thoughts under communal scrutiny; and the "
             "constant reframing of negative emotions as spiritual failure."),
            ("quote",
             "\"The most effective cage is one where the prisoner sincerely "
             "believes the bars are there for their protection.\""),
            ("subheading", "Financial Exploitation"),
            ("body",
             "Financial manipulation in religious contexts ranges from aggressive "
             "tithing expectations enforced through shame and spiritual threat "
             "to outright fraud. Members may be pressured to give beyond their "
             "means, told that financial sacrifice demonstrates faith, or "
             "promised that divine blessing will compensate for their "
             "contributions. Leadership often lives lavishly while ordinary "
             "members struggle financially."),
            ("subheading", "Sexual Abuse and Cover-Up"),
            ("body",
             "The sexual abuse scandals that have emerged from Catholic dioceses, "
             "independent Protestant ministries, Orthodox Jewish communities, "
             "and countless other religious bodies around the world share "
             "a common thread: institutional protection of abusers and "
             "systematic re-traumatization of victims who came forward. "
             "The theological language of forgiveness, humility, and not "
             "bringing 'shame on the body of Christ' (or equivalent formulations "
             "in other traditions) has been weaponized to silence survivors and "
             "protect perpetrators."),
        ],
    },
    {
        "number": 4,
        "title": "Chapter 4: Recognizing Religious Abuse",
        "content": [
            ("subheading", "Warning Signs in Institutions"),
            ("body",
             "Not every strict or demanding religious community is abusive, "
             "and not every warm and welcoming one is safe. The following "
             "warning signs are not a checklist for instant diagnosis, but "
             "rather indicators that warrant closer examination."),
            ("bullet",
             "Absolute authority: Leadership claims to speak directly for God "
             "with no accountability to outside bodies or internal dissent."),
            ("bullet",
             "Us versus them: The world outside the community is uniformly "
             "corrupt, dangerous, or spiritually contaminated."),
            ("bullet",
             "Loaded language: A specialized vocabulary that outsiders find "
             "hard to understand and that insiders use to preempt critical "
             "discussion."),
            ("bullet",
             "Punishment for doubt: Questioning is met not with engagement "
             "but with social penalties, spiritual threats, or accusations "
             "of faithlessness."),
            ("bullet",
             "Boundary violations: Personal privacy—in thoughts, relationships, "
             "finances, or sexuality—is routinely overridden in the name of "
             "communal accountability."),
            ("bullet",
             "Escalating demands: What began as a modest commitment has grown "
             "into something that consumes virtually all of one's time, money, "
             "and social relationships."),
            ("subheading", "Warning Signs in Individuals"),
            ("body",
             "Religious abuse also occurs in personal relationships: a parent "
             "who terrorizes a child with images of hell, a spouse who uses "
             "scripture to justify domestic violence, a pastor who uses "
             "counseling relationships to establish inappropriate emotional "
             "or sexual power. Signs may include:"),
            ("bullet",
             "Constant guilt, shame, or unworthiness that is linked to religious "
             "teachings or the expectations of a specific person."),
            ("bullet",
             "Fear of eternal punishment that is disproportionate or used "
             "instrumentally to control behavior."),
            ("bullet",
             "Being told that one's religious status depends on obedience to "
             "a particular human authority."),
            ("bullet",
             "Sexual contact or content framed as spiritually meaningful or "
             "required."),
            ("quote",
             "\"Healthy religion builds people up. Abusive religion tears "
             "people down and then blames them for the damage.\""),
            ("subheading", "The Spectrum of Harm"),
            ("body",
             "Religious harm exists on a spectrum from overt violence to "
             "subtle but pervasive psychological damage. The less dramatic "
             "end of the spectrum—shame-based theology, excessive guilt, "
             "suppressed identity—is often invisible to those outside the "
             "community and even to survivors themselves, who may spend "
             "years not recognizing that what happened to them was a "
             "form of abuse."),
        ],
    },
    {
        "number": 5,
        "title": "Chapter 5: The Psychology of Cult Behavior",
        "content": [
            ("subheading", "Defining a Cult"),
            ("body",
             "The word 'cult' carries significant baggage, often conjuring images "
             "of bizarre rituals and obviously deluded followers. This popular "
             "image obscures the reality: high-control groups recruit intelligent, "
             "educated, and psychologically healthy people. They are not "
             "necessarily small or fringe; some operate on a massive scale within "
             "mainstream religious bodies."),
            ("body",
             "Researchers like Robert Lifton, Margaret Singer, and Steven Hassan "
             "have identified behavioral and structural characteristics that "
             "distinguish high-control groups from healthier religious "
             "communities, regardless of the group's stated beliefs or size. "
             "The key factors relate to how the group treats its members "
             "rather than what it teaches about God."),
            ("subheading", "Lifton's Eight Criteria"),
            ("bullet", "Milieu Control: The group controls the environment and communication."),
            ("bullet", "Mystical Manipulation: Spontaneous events are engineered to appear as divine signs."),
            ("bullet", "Demand for Purity: Members are taught to constantly judge themselves and others against an impossibly high standard."),
            ("bullet", "Confession: Personal information is shared in group settings and can later be used as leverage."),
            ("bullet", "Sacred Science: The group's doctrine is presented as ultimate truth, beyond question."),
            ("bullet", "Loading the Language: A specialized vocabulary short-circuits critical thinking."),
            ("bullet", "Doctrine over Person: Personal experience is subordinated to the group's official narrative."),
            ("bullet", "Dispensing of Existence: The group alone determines who is spiritually valid or worthy of respect."),
            ("subheading", "Why People Stay"),
            ("body",
             "One of the most common and harmful misconceptions about cult "
             "membership is that people who stay must be weak, gullible, or "
             "stupid. In reality, leaving a high-control group means losing "
             "your community, your worldview, your sense of identity, and "
             "often your family. The psychological cost of leaving can be "
             "higher than the psychological cost of staying, at least in "
             "the short term."),
            ("body",
             "Leaving also means confronting the disorienting possibility that "
             "one was deceived, that years of devotion and sacrifice may have "
             "been misdirected, and that trusted authorities were not what they "
             "claimed to be. These realizations arrive not all at once but in "
             "waves, often accompanied by grief, rage, and profound "
             "disorientation."),
            ("quote",
             "\"Leaving a cult is not like quitting a club. It is more like "
             "emigrating from the only country you have ever known.\""),
            ("subheading", "The Role of Identity"),
            ("body",
             "High-control groups are effective in part because they offer "
             "a complete identity package: answers to every meaningful question, "
             "a clear place in a cosmic hierarchy, and the deep comfort of "
             "belonging to something larger than oneself. When that package "
             "is removed—or when one removes oneself from it—the resulting "
             "emptiness is not a sign of weakness. It is a natural response "
             "to the loss of an entire framework for understanding reality."),
        ],
    },
    {
        "number": 6,
        "title": "Chapter 6: Healing from Religious Trauma",
        "content": [
            ("subheading", "Religious Trauma Syndrome"),
            ("body",
             "Dr. Marlene Winell coined the term Religious Trauma Syndrome (RTS) "
             "to describe the complex symptoms that can follow the harmful "
             "experience of leaving a religious group or recovering from "
             "religious abuse. RTS shares features with PTSD and complex "
             "trauma but has specific dimensions related to existential and "
             "identity loss: grief over lost beliefs, difficulty trusting "
             "one's own perceptions, and deep confusion about morality and "
             "meaning."),
            ("body",
             "RTS is not yet an official diagnostic category in the DSM, but "
             "it is increasingly recognized by therapists who work with "
             "ex-religious clients. Recognition matters because survivors "
             "who do not understand why they are suffering may blame "
             "themselves, or may receive unhelpful treatment from clinicians "
             "who do not understand the religious dimension of their "
             "experience."),
            ("subheading", "The Stages of Recovery"),
            ("bullet",
             "Awareness: Recognizing that what happened was harmful, "
             "not normal or acceptable, even if it was framed as loving."),
            ("bullet",
             "Grief: Mourning not only the community and relationships lost "
             "but the belief system that once provided certainty and comfort."),
            ("bullet",
             "Anger: Allowing appropriate anger to surface without suppressing "
             "it through residual religious guilt."),
            ("bullet",
             "Rebuilding: Constructing a new framework for meaning, ethics, "
             "and identity that is genuinely one's own."),
            ("bullet",
             "Integration: Coming to a place where the past is neither "
             "denied nor entirely defining—where it is part of one's story "
             "without consuming it."),
            ("subheading", "Therapeutic Approaches"),
            ("body",
             "Effective therapeutic approaches for religious trauma typically "
             "combine elements from several traditions: "
             "trauma-informed cognitive behavioral therapy to address "
             "thought patterns instilled by the group; EMDR or somatic "
             "therapies to address the body-level responses that persist "
             "after the intellectual processing is done; and existential or "
             "narrative therapy to help survivors construct a coherent "
             "life story that includes but is not defined by their experience."),
            ("body",
             "Finding a therapist who is both trauma-informed and "
             "non-judgmentally familiar with religious systems is important. "
             "A therapist who is deeply embedded in any religious tradition "
             "may unintentionally re-impose the frameworks the client is "
             "trying to examine. Equally, a therapist who dismisses "
             "spirituality entirely may not be able to honor the genuine "
             "value that faith once held in the client's life."),
            ("quote",
             "\"Healing is not forgetting. It is the gradual reclaiming "
             "of your own mind, your own story, and your own future.\""),
            ("subheading", "Community and Peer Support"),
            ("body",
             "For many survivors, the most powerful healing resource is "
             "not professional but communal: finding others who have "
             "had similar experiences and can offer validation, shared "
             "humor about their past, and concrete advice. Online "
             "communities for ex-members of specific groups have proliferated "
             "in the social media era, providing connection that can be "
             "life-saving for someone in geographic isolation or recently "
             "estranged from their entire social network."),
        ],
    },
    {
        "number": 7,
        "title": "Chapter 7: Reclaiming Spirituality",
        "content": [
            ("subheading", "Beyond Binary Thinking"),
            ("body",
             "Survivors of religious abuse often feel pressure toward one "
             "of two equally unsatisfying positions: returning to the "
             "belief system that harmed them, or abandoning all "
             "spirituality entirely. Both can be reactive responses to "
             "trauma rather than genuine choices."),
            ("body",
             "A third path exists: the careful, gradual, and genuinely "
             "autonomous exploration of what, if anything, one actually "
             "believes and values. This path has no required destination. "
             "Some survivors ultimately find their way to a new and "
             "healthier religious community. Some develop a rich secular "
             "humanism. Some find meaning in nature, art, or philosophy. "
             "What matters is that the path is freely chosen."),
            ("subheading", "Markers of Healthy Spirituality"),
            ("bullet",
             "Questions are welcomed, not suppressed."),
            ("bullet",
             "Authority is accountable to the community it serves."),
            ("bullet",
             "Diversity of belief and practice is respected."),
            ("bullet",
             "Boundaries—physical, emotional, financial—are consistently "
             "honored."),
            ("bullet",
             "Doubt is treated as a normal part of the spiritual journey, "
             "not evidence of failure or sin."),
            ("bullet",
             "The community builds people up and supports their "
             "flourishing in the broader world."),
            ("subheading", "Building a Personal Practice"),
            ("body",
             "A personal spiritual practice—if one chooses to maintain "
             "one—can be built incrementally, on one's own terms. This "
             "might mean: exploring multiple traditions with the "
             "curiosity of a student rather than the commitment of a "
             "convert; keeping a journal of genuine questions and "
             "evolving answers; finding contemplative practices such as "
             "meditation or mindfulness that do not require doctrinal "
             "commitment; or connecting with nature, art, or community "
             "service as sources of meaning."),
            ("body",
             "The key distinction is between a practice chosen freely and "
             "revised over time versus one imposed by external authority "
             "and maintained through fear."),
            ("quote",
             "\"Your spiritual life belongs to you. No institution, "
             "leader, or doctrine has the right to claim it entirely.\""),
            ("subheading", "A Note on Forgiveness"),
            ("body",
             "Forgiveness is often presented within religious contexts as "
             "an obligation, a spiritual requirement with dire "
             "consequences for non-compliance. Survivors of religious "
             "abuse may find this framing itself abusive: being told "
             "to forgive before they are ready, or to forgive in a way "
             "that requires minimizing what happened."),
            ("body",
             "A healthier understanding of forgiveness, drawn from "
             "psychological rather than doctrinal sources, sees it as "
             "a process, not an event—something that happens on the "
             "survivor's timeline and for the survivor's benefit, not "
             "for the perpetrator's absolution. Forgiveness in this "
             "sense does not require reconciliation or contact with "
             "the person or institution that caused harm. It is the "
             "survivor's private decision to release the weight of "
             "resentment when, and if, they are ready."),
        ],
    },
    {
        "number": 8,
        "title": "Conclusion",
        "content": [
            ("body",
             "Religion is neither inherently good nor inherently bad. Like "
             "any powerful human institution, it reflects the full range "
             "of human capacity: for compassion and cruelty, for liberation "
             "and control, for truth-seeking and self-deception."),
            ("body",
             "The goal of this book has not been to diminish faith but to "
             "illuminate a pattern of abuse that has been hidden for too "
             "long behind the language of the sacred. Naming that pattern "
             "clearly is the first step toward preventing it, addressing "
             "it when it occurs, and supporting those who have been harmed "
             "by it."),
            ("body",
             "If you are a survivor, you deserve to have your experience "
             "named, witnessed, and taken seriously. What happened to you "
             "was not your fault. You were not too sensitive, too faithless, "
             "or too weak. You encountered a system designed—however "
             "consciously—to override your own judgment, and you survived it."),
            ("body",
             "If you are a leader, educator, or family member who wants "
             "to understand this issue better, thank you for your "
             "willingness to look honestly at the potential for harm "
             "within the structures you love. That willingness is the "
             "foundation of genuine accountability."),
            ("body",
             "The work of building religious communities that are truly "
             "safe—communities where doubt is honored, authority is "
             "accountable, and the flourishing of every individual is "
             "the highest goal—is ongoing and never complete. But it "
             "is possible. And it is necessary."),
            ("quote",
             "\"Faith that cannot survive honest questioning was never "
             "truly strong. Faith that welcomes honest questioning "
             "may last a lifetime.\""),
        ],
    },
    {
        "number": 9,
        "title": "Resources & Further Reading",
        "content": [
            ("subheading", "Books"),
            ("bullet", "Winell, Marlene. Leaving the Fold: A Guide for Former Fundamentalists and Others Leaving Their Religion."),
            ("bullet", "Hassan, Steven. Combating Cult Mind Control."),
            ("bullet", "Singer, Margaret T. Cults in Our Midst."),
            ("bullet", "Lifton, Robert Jay. Thought Reform and the Psychology of Totalism."),
            ("bullet", "Van der Kolk, Bessel. The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma."),
            ("bullet", "Engle, Beverly. It Wasn't Your Fault: Freeing Yourself from the Shame of Childhood Abuse."),
            ("subheading", "Organizations & Online Resources"),
            ("bullet", "Recovery from Religion Foundation – recoveringfromreligion.org"),
            ("bullet", "Cult Education Institute – culteducation.com"),
            ("bullet", "SNAP (Survivors Network of those Abused by Priests) – snapnetwork.org"),
            ("bullet", "International Cultic Studies Association – icsa home.com"),
            ("bullet", "Open Minds Foundation – openmindsfoundation.org"),
            ("subheading", "Crisis & Support Lines"),
            ("bullet",
             "If you are in immediate danger, call your local emergency services (911 in the US)."),
            ("bullet",
             "National Domestic Violence Hotline (US): 1-800-799-7233 | thehotline.org"),
            ("bullet",
             "Crisis Text Line (US/UK/Ireland/Canada): Text HOME to 741741"),
            ("bullet",
             "SAMHSA National Helpline (US, mental health & substance abuse): "
             "1-800-662-4357"),
            ("subheading", "A Note on Seeking Therapy"),
            ("body",
             "When seeking a therapist for religious trauma, look for someone "
             "who is: trauma-informed; non-judgmental about religious or "
             "irreligious identities; familiar with high-control groups or "
             "willing to learn; and respectful of your autonomy in the "
             "healing process. Psychology Today's therapist finder "
             "(psychologytoday.com/us/therapists) allows filtering by "
             "specialty, including trauma and religious issues."),
        ],
    },
]
