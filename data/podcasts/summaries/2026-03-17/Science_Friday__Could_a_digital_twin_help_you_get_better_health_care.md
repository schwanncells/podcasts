---
podcast: Science Friday
date: 2026-03-17
source_transcript: data/podcasts/transcripts/Science_Friday/2026-03-17_Could_a_digital_twin_help_you_get_better_health_care.md
---

# Science Friday — "Could a 'digital twin' help you get better health care?"

**Host:** Flora Lichtman. **Guest:** Dr. Caroline Chung (radiation oncologist; co-director, Institute for Data Science in Oncology, UT MD Anderson Cancer Center; researcher at the forefront of digital twin development in medicine).

## TL;DR

- **A medical digital twin is more than a data dashboard** — it requires an ongoing feedback loop: model predicts outcomes, patient acts on that information, new data flows back to update the model, repeating over time.
- **The concept originated in aerospace engineering** — NASA and aircraft manufacturers built digital replicas of vehicles to pressure-test failure scenarios without risking physical prototypes.
- **Human biology is far harder to model than mechanical systems** — physical laws governing fluid dynamics and heart mechanics are well understood, but many molecular mechanisms in cancer biology remain undiscovered.
- **Chung's team is designing radiation treatment using digital twins** — the goal is to identify which sub-regions of a tumor need higher doses and which healthy tissues can be spared, then adapt treatment early in the course of therapy.
- **Simulations have shown chemotherapy scheduling matters** — the same total drug dose delivered on a personalized schedule yielded better outcomes for breast cancer patients than the standard uniform schedule, without additional drug costs.
- **Cardiology digital twins can predict who needs early follow-up** — by modeling blood flow from imaging data, clinicians could safely tell lower-risk patients they don't need a retest for three years.
- **Ownership and accountability remain unresolved** — even if a patient nominally "owns" their digital twin, accessing it without the supporting software infrastructure may be practically impossible.
- **Chung warns that the drive for speed undermines critical thinking** — she argues that well-designed interfaces need to build in deliberate "pause" to prevent over-reliance on algorithmic outputs.

---

**Origins: From Aerospace to the Clinic**

Digital twins originated in the aerospace and spacecraft industries, where engineers needed to test how vehicles would behave under extreme conditions without building and destroying costly physical models. By creating digital replicas, they could simulate all possible failure scenarios and identify the most promising designs before committing to physical construction. Chung describes this as "a continuous bridging between the physical and the digital world." Translating that concept to medicine introduces a fundamental challenge: while the physical laws governing, say, fluid dynamics in a beating heart are well established, molecular biology still has large knowledge gaps. Many cellular and tumor mechanisms remain poorly understood, meaning medical digital twins must be built on incomplete foundations.

**What a True Digital Twin Actually Is**

Chung distinguishes between the popular conception of a digital twin — a visual representation or dashboard aggregating a patient's medical records — and the more rigorous engineering definition. A true digital twin is a living simulation that continuously interacts with real-world data: the model predicts what will happen, the clinician or patient acts on that prediction, new outcomes are measured, and the model updates accordingly. It "journeys with you through time," in Chung's phrase, rather than representing a static snapshot.

**Radiation Oncology: Personalizing Treatment in Real Time**

Chung's own research focuses on one of the most precise and consequential decisions in oncology: how to distribute radiation dose across a tumor. Her team is building digital twins that can identify which sub-regions contain more aggressive or treatment-resistant cells, allowing clinicians to boost dose where it matters most while reducing exposure to surrounding healthy tissue. The aim is to detect whether a treatment is working early enough during a course of therapy to modify it — rather than waiting until the end to assess outcomes. Clinical trials along these lines have been run by her colleague Dr. Heiko Enderling at MD Anderson, and Chung's team is actively designing new trials.

**Cardiology and Chemotherapy: Two Other Applications**

Beyond oncology, digital twins have been built in cardiology to model blood flow from imaging data. Chung describes these models identifying individual patients at lower risk of a cardiac event, allowing clinicians to confidently extend the interval before the next test — a benefit both for patients who avoid unnecessary procedures and for health systems managing costs. In chemotherapy, simulations have already shown that the same total drug dose can produce meaningfully different outcomes depending on timing and scheduling. For women with breast cancer, a personalized schedule calibrated to an individual's physiology and tumor biology outperformed the standard uniform schedule — without adding drug costs.

**The Whole-Body Digital Twin: Ambition and Limits**

There is a global research community — convening at a "Virtual Human Global Symposium" — that aspires to integrate all organ-system-level digital twins into a single comprehensive model of an entire person. Chung acknowledges this aspiration but argues that a digital twin "needs to be fit for purpose." For a specific clinical question, connecting every biological system is unnecessary and creates more surface area for error. For basic science discovery, a full-body model may be worth the investment. She also notes that a complete digital twin of a single individual becomes highly identifying — potentially unique in a way that creates serious privacy exposure.

**Ownership, Accountability, and the Human-Machine Interface**

Chung raises two unresolved legal and ethical questions. First: who owns the digital twin? Even if the answer is the patient, exercising that ownership may be practically impossible without access to the proprietary software stack that keeps the model running. Second: when a digital twin's prediction is wrong and a patient suffers a bad outcome, how is responsibility assigned? Her answer is that digital twins are a "frame of information," and final clinical decisions must remain a joint deliberation between clinician and patient, weighted against social and personal factors that no model captures.

On the question of algorithmic bias, Chung identifies two failure modes: clinicians who defer uncritically to machine outputs, and those who reflexively reject them in favor of human intuition. She argues the real challenge is interface design — presenting information in a way that "creates pause" and supports critical reasoning. She sees the current cultural premium on speed as the primary threat, noting that "the pause is probably the critical piece that will allow us to be discerning."
