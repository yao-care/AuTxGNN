---
layout: default
title: Morphine
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morphine: From Pain Management to Myofascial Pain Syndrome

## One-Sentence Summary

Morphine is a mu-opioid receptor agonist long established for moderate-to-severe pain. The TxGNN model predicts it may be effective for **Myofascial Pain Syndrome (MPS)**, with **33 clinical trials** and **17 publications** identified, though the evidence is largely class-level (opioids in chronic pain generally) rather than morphine-specific trials in MPS.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe pain (opioid analgesic) — no matching TGA/ARTG licence text was returned by this query |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed TGA-registered mechanism-of-action data is not available for this candidate (data gap). Based on established pharmacology, morphine is a mu-opioid receptor agonist that produces analgesia through spinal and supraspinal inhibition of nociceptive transmission — a broad-spectrum analgesic mechanism rather than a disease-specific one.

Myofascial Pain Syndrome is itself a chronic pain condition involving muscle trigger points and central sensitisation, so there is a plausible mechanistic extension from morphine's general analgesic action to MPS. However, the identified evidence base largely consists of studies on opioids in chronic non-cancer pain as a drug class (e.g., long-term opioid therapy registries, opioid-sparing strategies after surgery) and trigger-point-focused procedural trials, rather than trials testing morphine specifically against MPS as a primary endpoint.

Given that opioids are not recommended as first-line therapy for chronic non-cancer pain conditions such as MPS under most current clinical guidelines, this prediction should be regarded as a research hypothesis for further mechanistic and clinical investigation rather than an established therapeutic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Phase 2 | Completed | 11 | Trigger point injections immediately post-TKA vs sham, evaluating pain scores and opioid use; notes correlation between soft-tissue manipulation and myofascial pain |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Phase 4 | Recruiting | 60 | Trigger point injections vs traditional therapy for postsurgical cervical myofascial pain after anterior cervical spine surgery |
| [NCT03161795](https://clinicaltrials.gov/study/NCT03161795) | N/A | Completed | 258 | Multicentre South Korean observational study on risks of long-term opioid therapy in chronic non-cancer pain, including opioid-related chemical coping |
| [NCT03271151](https://clinicaltrials.gov/study/NCT03271151) | Phase 4 | Completed | 160 | Double-blind RCT of duloxetine's effect on opioid consumption after total knee arthroplasty |
| [NCT04504812](https://clinicaltrials.gov/study/NCT04504812) | Phase 3 | Completed | 1937 | Large effectiveness trial comparing treatments to reduce opioid reliance and improve pain/function in knee osteoarthritis |
| [NCT06533345](https://clinicaltrials.gov/study/NCT06533345) | N/A | Recruiting | 120 | Chronic pain research clinic examining neuropathic, structural and nociplastic (e.g., fibromyalgia-type) pain mechanisms and treatment |
| [NCT05069363](https://clinicaltrials.gov/study/NCT05069363) | N/A | Recruiting | 20 | Feasibility trial of whole-body photobiomodulation for chronic pain, referencing morphine as a current but often inadequate treatment option |
| [NCT04862845](https://clinicaltrials.gov/study/NCT04862845) | Phase 1 | Completed | 90 | Multimodal analgesia (duloxetine + pregabalin) to reduce opioid reliance after liposuction surgery |
| [NCT04090099](https://clinicaltrials.gov/study/NCT04090099) | N/A | Completed | 93 | Regional nerve blocks vs opioid-based analgesia after cardiac surgery, highlighting opioid-related adverse effects |
| [NCT05050656](https://clinicaltrials.gov/study/NCT05050656) | Phase 4 | Completed | 70 | Duloxetine premedication and its effect on postoperative pain control after ACL repair under spinal anaesthesia |

Note: Most trials returned by the underlying knowledge-graph search relate to opioids as a drug class in chronic/postoperative pain, or to non-pharmacological/procedural MPS treatments (dry needling, trigger point injection), rather than morphine tested specifically against MPS. Several additional low-relevance trials (e.g., rTMS, tDCS, cryoanalgesia device studies unrelated to opioid pharmacology) were excluded from this table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine Journal | Double-blind RCT comparing dexmedetomidine + morphine vs plain ropivacaine for myofascial infiltration in thoracolumbar spinal fusion |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Cohort | Journal of Anesthesia | Cervical facet joint injections added to multimodal treatment for long-standing cervical myofascial pain syndrome |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Practice | Structured stretching exercise programme and its effect on resolving myofascial pain and reducing opioid use in "legacy pain" patients |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Cohort | Der Schmerz | Altered pain thresholds during and after opioid withdrawal in patients with chronic low back pain |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Review of long-term opioid use in chronic temporomandibular joint dysfunction |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Review | J Oral Maxillofac Surg | Arthrocentesis with intra-articular morphine infusion for refractory TMJ pain dysfunction syndrome |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | Comparative trial | European Journal of Pain | Epidural analgesia vs intercostal nerve cryoanalgesia for post-thoracotomy pain control |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Descriptive study | Rev Assoc Med Bras | Therapeutic approach in 56 patients with failed back surgery pain syndrome |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Study (type pending) | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for perioperative pain after botulinum toxin injection for myofascial pelvic pain |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Use of oral medications, infusions and injections in differential diagnosis of orofacial pain |

---

## Australia Market Information

No ARTG entries were returned for this candidate in the current dataset (0 licences; market status: not marketed). This is a data gap in the underlying regulatory query rather than confirmation that no morphine products exist on the Australian market — morphine is a Schedule 8 (Controlled Drug) opioid with a long history of clinical use, and TGA/ARTG records should be checked directly to confirm current registered products, formulations and approved indications before any repurposing evaluation proceeds.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications or drug interaction data were returned in this evidence pack (DDI query: not found).

As general clinical context worth flagging: several of the trials and literature above indicate that opioids are associated with dependence risk, opioid-induced hyperalgesia, and are generally positioned as third-line or adjunct therapy — not first-line — in chronic non-cancer pain conditions similar to MPS. This should be weighed heavily in any Australian PI safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the supporting evidence is class-level (opioids broadly in chronic/postoperative pain) rather than morphine-specific trials for MPS, and the underlying scoring itself flags this as a "Research Question" at an early evaluation stage (L3/S1). Given morphine's opioid dependence and misuse risk, and that current guidelines do not support opioids as first-line MPS therapy, clinical progression is not warranted on the present evidence.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) — currently a blocking data gap for safety assessment
- Confirmed mechanism-of-action documentation (DrugBank or TGA source) — currently a data gap
- A dedicated trial testing morphine (or opioids as a class) specifically against MPS outcomes, rather than general chronic-pain opioid-use data
- Confirmation of current ARTG registration status and available formulations in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

