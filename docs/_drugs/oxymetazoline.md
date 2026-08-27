---
layout: default
title: Oxymetazoline
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
---

# Oxymetazoline
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

Using the report prompt exactly as specified. A few data-fidelity notes before the report: `taiwan_regulatory.licenses` is empty (0 ARTG entries, "未上市"/Not Marketed) and `drug.original_moa` / `original_indications` are marked as data gaps, so I've drawn the mechanistic description from the `repurposing_rationale.mechanistic_link` field that *is* present in the pack (oxymetazoline as an α1A/α2-adrenergic agonist / decongestant), rather than inventing an indication. I've also flagged, transparently, that several "matching" trials/papers in the evidence pack were retrieved on anatomical co-occurrence (nasal cavity) rather than direct drug testing — this matters for a pharmacist reader.

---

# Oxymetazoline: From Topical Nasal Decongestion to Nasal Cavity Disease

## One-Sentence Summary

> Oxymetazoline is a well-known topical α1A/α2-adrenergic agonist used as a nasal vasoconstrictor (decongestant); this evidence pack does not contain a formal TFDA/ARTG-sourced "original indication" record, but its known pharmacology is decongestant/vasoconstrictor action on nasal mucosa.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **17 clinical trials** and **5 publications** retrieved, though only a minority directly test oxymetazoline itself — the rest were retrieved because they concern the same anatomical site.
> Because the predicted indication overlaps heavily with oxymetazoline's already-established decongestant use, this candidate is better read as a confirmation of known pharmacology than a genuinely novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded via ARTG/TFDA licence data in this pack; pharmacologically known as a topical nasal decongestant (vasoconstrictor) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (per evidence-pack scoring; direct oxymetazoline evidence within the retrieved set is limited — see caveats below) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is marked as a data gap in this pack. However, the repurposing rationale attached to the top prediction describes oxymetazoline as a selective **α1A/α2-adrenergic receptor agonist** that acts directly on nasal mucosal vascular smooth muscle, producing vasoconstriction and reducing mucosal congestion and swelling — this is the well-established core mechanism of oxymetazoline as a nasal decongestant.

Read against that mechanism, the predicted indication — "Nasal Cavity Disease" — sits very close to oxymetazoline's already-recognised use rather than representing a distinct new disease area. The presence of Phase 2 and Phase 4 trials involving nasal decongestant pharmacology in the evidence set (see below) is consistent with this: it looks like the model is reinforcing an existing pharmacological relationship rather than surfacing an unexpected one.

That said, some of the retrieved evidence points to a more specific and genuinely useful application: procedural use of oxymetazoline as a pre-operative decongestant/haemostatic agent (e.g., before endoscopic sinus surgery), which is a narrower, better-defined clinical scenario than "nasal cavity disease" as a broad label. It's worth noting the pack also surfaced lower-ranked, lower-evidence candidates (e.g., headache disorder and trigeminal autonomic cephalalgia, via sphenopalatine ganglion blockade) that may be of separate research interest but are not part of this primary candidate assessment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Direct comparison of topical 0.05% oxymetazoline vs 1:1000 epinephrine before endoscopic sinus surgery, assessing blood loss and surgical field visualisation — the strongest direct evidence for oxymetazoline in this pack. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomised, double-blind, double-dummy, four-way crossover study of an H3-receptor antagonist against nasal-allergen-induced congestion; representative of decongestant pharmacodynamic trial design, but the active comparator tested was not oxymetazoline itself. |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (tetracaine + oxymetazoline nasal mist) vs injected articaine for dental pulpal anaesthesia — a combination product containing oxymetazoline, but for a dental rather than nasal-cavity-disease indication; withdrawn before enrolling participants. |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Same Kovanaze vs articaine comparison, terminated early with only 3 participants enrolled. |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Compared topical anaesthetic and/or decongestant pretreatment for comfort during fibreoptic nasal pharyngoscopy/laryngoscopy; consistent with oxymetazoline-type decongestant use, though the specific agent used is not confirmed in the summary provided. |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Compared co-phenylcaine nasal spray (a different decongestant/anaesthetic combination) with nasal nebulisation before rigid nasoendoscopy; relevant to decongestant use in nasal procedures but does not test oxymetazoline directly. |

**Note:** the search retrieved 17 trials in total for this indication. The 11 not listed above (e.g., acoustic rhinometry device validation, spasmodic dysphonia physiology, sleep apnoea airflow studies, sinus/lacrimal surgical technique comparisons, and a trial of xylometazoline rather than oxymetazoline) were graded low-relevance or unrelated and are excluded here as anatomical-site false positives rather than genuine drug evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal Study | Annals of Otology, Rhinology & Laryngology | In a rabbit model of induced acute maxillary sinusitis, topical oxymetazoline nose drops were compared against placebo — the only paper in this set that directly tests oxymetazoline. |
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Cohort | Annals of the New York Academy of Sciences | Investigated olfactory function during acute rhinitis using chemosensory evoked potentials and acoustic rhinometry; describes nasal cavity disease physiology but does not test oxymetazoline. |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohort | Journal of Plastic Surgery and Hand Surgery | Used acoustic rhinometry to assess nasal patency after cleft lip/palate repair; relevant to nasal cavity anatomy but not a drug study. |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case Series | American Journal of Rhinology & Allergy | Describes endoscopic coblation treatment of nasal telangiectasias in hereditary haemorrhagic telangiectasia; a nasal cavity disease report unrelated to oxymetazoline. |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case Report | Global Pediatric Health | Case report of rhinoscleroma (a rare bacterial granulomatous nasal disease) in a child; unrelated to oxymetazoline treatment. |

**Note:** only 1 of these 5 papers actually studies oxymetazoline; the remaining 4 were retrieved because they concern nasal cavity disease generally, not because they evaluate the drug. Relevance grading for this literature set has not yet been completed in the evidence pack (marked "pending").

## Australia Market Information

No ARTG entries were found for oxymetazoline in this evidence pack (0 licences recorded; market status "Not Marketed"). No dosage form, product name, or approved-indication text is available to tabulate.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- One direct Phase 4 trial (NCT03228914) and one animal study support a specific, well-defined use of topical oxymetazoline as a pre-operative decongestant/haemostatic agent in sinus surgery, consistent with its known vasoconstrictor mechanism. However, most of the 17 trials and 4 of the 5 papers retrieved for "Nasal Cavity Disease" are anatomically co-located rather than drug-specific, and the predicted indication substantially overlaps with oxymetazoline's already-recognised decongestant use rather than identifying a clearly novel therapeutic niche.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information, including warnings, contraindications, and drug interaction data (currently a blocking data gap — DG001)
- A confirmed DrugBank mechanism-of-action record (currently a data gap — DG002), to replace the pharmacology summary drawn only from the repurposing rationale
- Clarification of whether "Nasal Cavity Disease" represents a distinct new clinical use-case (e.g., a defined procedural/haemostatic indication) or simply restates oxymetazoline's existing decongestant indication
- Confirmation of Australian market/ARTG status, since this pack currently records 0 licences and "Not Marketed"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

