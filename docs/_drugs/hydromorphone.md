---
layout: default
title: Hydromorphone
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Hydromorphone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Hydromorphone: From Pain Management to Pharyngitis

## One-Sentence Summary

Hydromorphone is a potent semi-synthetic opioid analgesic used for the management of moderate-to-severe pain. The TxGNN model predicts it may be effective for **Pharyngitis** — primarily post-tonsillectomy pharyngeal pain — with **6 clinical trials** (including 1 directly relevant completed RCT) and **no published literature** currently supporting this specific direction. Notably, among all 10 predicted indications in this pack, the strongest evidence base was identified for **Headache Disorder (Rank 5)**, where a completed Phase 4 RCT directly evaluating IV hydromorphone for acute migraine in the emergency setting provides Level L2 evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe pain management (opioid analgesic) |
| Predicted New Indication | Pharyngitis (post-tonsillectomy pharyngeal pain) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank for this assessment. Based on well-established clinical pharmacology, hydromorphone is a potent semi-synthetic μ-opioid receptor agonist approximately 5–10 times more potent than morphine on a weight-for-weight basis. It suppresses pain transmission by binding to μ-opioid receptors in the central nervous system and peripheral tissues, inhibiting ascending nociceptive signals and modulating the affective-emotional response to pain.

The mechanistic link to pharyngitis is anatomically and clinically plausible, but context-dependent. Surgical trauma to the pharyngeal mucosa during tonsillectomy or adenotonsillectomy produces a clearly defined acute nociceptive pain signal. As a high-potency opioid, hydromorphone is pharmacologically well-suited to manage this type of acute postoperative pain originating in the pharyngeal region. The TxGNN model most likely captures this **post-tonsillectomy pharyngeal pain scenario** rather than infectious pharyngitis, for which hydromorphone has no antibacterial or antiviral mechanism.

It is important to contextualise the clinical novelty of this prediction. Opioid analgesics are already used in the perioperative setting as standard of care. The meaningful research question here is not whether opioids can be used, but whether hydromorphone offers a specific clinical advantage — in efficacy, safety profile, or recovery outcomes — over comparators such as fentanyl in the post-tonsillectomy paediatric population. A completed head-to-head RCT (NCT04230681) has already explored this question, and its published results would be critical to evaluate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | **[Grade A — Most relevant]** Direct RCT comparing hydromorphone vs fentanyl for postoperative pain control following tonsillectomy or adenotonsillectomy in children and adolescents. The anatomical site of pain (pharynx) is directly relevant to this indication. |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | **[Grade B — Indirect]** Compares long-acting methadone vs short-acting opioids (including fentanyl/hydromorphone) for post-tonsillectomy pain management in paediatric patients. Hydromorphone used as a comparator arm; provides indirect Phase 4-level support. Estimated completion June 2029. |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | **[Grade B — Indirect]** Methadone pilot study for post-tonsillectomy pain optimisation. Hydromorphone serves as the short-acting opioid comparator, reinforcing clinical feasibility of opioids in pharyngeal surgical pain. |

> **Note:** Three further trials retrieved (NCT00109031, NCT00189488, NCT02996591) were assessed as not relevant — these involve palifermin for chemotherapy-related oral mucositis and anaesthesia comparisons for lower-limb surgery, respectively. They have been excluded from the table above.

---

## Literature Evidence

Currently no related literature available for the pharyngitis indication.

> See **Conclusion and Next Steps** for a discussion of the stronger literature evidence base identified for the secondary indication, Headache Disorder.

---

## Australia Market Information

Hydromorphone is currently **not registered with the Therapeutic Goods Administration (TGA)** and has no entries in the Australian Register of Therapeutic Goods (ARTG).

It is not available as a marketed product through standard TGA regulatory channels in Australia. Any clinical use would require access via:

- **TGA Special Access Scheme (SAS Category B or C)**, or
- An approved clinical trial protocol with HREC oversight

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) and relevant international prescribing information for complete safety data. At the time of this assessment, no local TGA safety data, contraindications, or drug interaction data were available for automated review.

> **⚠️ Important flags identified in this Evidence Pack:**
> - **Allergic urticaria (Rank 2) and Cold urticaria (Rank 7):** TxGNN predictions for these indications carry **reverse mechanism warnings**. Opioids, including hydromorphone, are established inducers of non-immunological histamine release via mast cell degranulation — they are a known *cause* of urticaria, not a treatment. These predictions almost certainly reflect misinterpretation of drug–adverse-effect edges in the knowledge graph. These indications should be treated as **contraindicated directions**, not repurposing opportunities.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Pharyngitis/post-tonsillectomy pain, Rank 1) is mechanistically plausible, but the available clinical trial evidence reaches only Level L3 — one completed Early Phase 1 RCT (NCT04230681) and two indirect comparator studies. This is insufficient to support a formal repurposing recommendation, and the clinical scenario (perioperative opioid use) does not represent novel drug repurposing in the traditional sense.

**Across all 10 predicted indications, the following priority actions are recommended:**

- **Headache Disorder (Rank 5) deserves priority review:** Evidence level L2, supported by a completed Phase 4 RCT (NCT02389829 / PMID 29046364) directly comparing IV hydromorphone vs IV prochlorperazine + diphenhydramine for acute migraine in the emergency department, plus 17 publications including a 2025/2026 AHS clinical guideline update (PMID 41321235). Clinical positioning is as a **rescue therapy** when first-line agents fail, with the caveat that trials show inferior efficacy vs standard dopamine antagonist therapy and risk of medication overuse headache. Recommended decision for this indication: **Proceed with Guardrails**.

- **Discontinue evaluation for urticaria indications (Ranks 2 and 7):** Reverse mechanism confirmed — hydromorphone is a precipitant, not a treatment, for allergic and cold urticaria. These should be flagged as adverse effect associations in the knowledge graph review.

- **Hold on Ranks 3, 4, 6, 8, 9, 10:** Insufficient mechanistic rationale or no evidence available. Ranks 3, 4, 6, and 8 represent either broad diagnostic categories without specificity or conditions with superior established therapies. Rank 9 (cervical disc degeneration) reflects existing opioid use rather than a novel indication.

**To proceed with any indication, the following is needed:**

- Retrieve and review published results from NCT04230681 (hydromorphone vs fentanyl, tonsillectomy) to assess whether a meaningful efficacy or safety advantage exists over existing agents
- Obtain DrugBank MOA and pharmacodynamic profile data (Data Gap DG002) to complete mechanism linkage analysis
- Review international prescribing information (US FDA label, EMA SmPC) for full contraindication and warning profile in the absence of TGA PI (Data Gap DG001)
- For headache disorder: review the 2025/2026 AHS guideline update (PMID 41321235) to determine whether hydromorphone retains any recommended role as rescue therapy under current evidence
- Consult TGA Special Access Scheme pathways if any indication progresses to a formal clinical use proposal in Australia

---

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require formal clinical validation before any clinical application. Refer to current TGA-approved prescribing information and clinical guidelines for patient care decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

