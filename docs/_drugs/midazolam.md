---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Midazolam
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam (DrugBank DB00683) is an ultra-short-acting benzodiazepine internationally used for procedural sedation, anaesthesia induction, and status epilepticus; a formal record of its originally licensed indication is not present in this evidence pack, as the drug is not currently TGA-registered in Australia. The TxGNN model predicts it may be effective for **Insomnia**, with **32 clinical trials** and **11 publications** identified in the search, though most trials studied midazolam as a peri-procedural sedative rather than as a chronic insomnia treatment. Evidence level is **L2** (one completed Phase 2/3-type RCT with direct relevance), and a **Blocking** data gap on TFDA/TGA product-information warnings currently prevents a full safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Taiwan/Australia registration on file); internationally documented use is procedural sedation / anaesthesia induction |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, midazolam is a short-acting benzodiazepine and positive allosteric modulator of the GABA-A receptor — the same receptor family targeted by established hypnotics (e.g. flurazepam, temazepam). This shared receptor mechanism gives the TxGNN prediction a plausible pharmacological basis: benzodiazepine-class GABA-A modulation is a validated route to sedative-hypnotic effect.

However, the drug-level rationale in the evidence pack flags an important limitation: midazolam's elimination half-life (~2 hours) makes it well suited to inducing sleep onset but poorly suited to maintaining sleep through the night, which is the core requirement for chronic insomnia therapy. Most of the supporting clinical trial evidence reflects this — the majority of identified studies use midazolam as a peri-procedural or ICU sedative (dental sedation, endoscopy, mechanical ventilation) where sleep/delirium outcomes were secondary endpoints, not as a purpose-designed insomnia treatment.

The strongest direct support comes from four older RCTs (1981–1990) that specifically evaluated oral midazolam for insomnia and found it an efficacious, well-tolerated hypnotic in short-term use, comparable to or better tolerated than reference comparators such as flurazepam and Vesparax. This is consistent with — but does not fully validate — the TxGNN prediction, since these trials are decades old, generally short-duration, and predate current insomnia treatment paradigms (e.g. orexin antagonists such as lemborexant).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Compared IV dexmedetomidine vs midazolam for postoperative sleep quality after TURP; direct midazolam sedation-sleep comparison. |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam in patients with sleep disturbance/anxiety undergoing laparoscopic colorectal cancer resection; primary endpoint is postoperative pain, not chronic insomnia. |
| [NCT01343095](https://clinicaltrials.gov/study/NCT01343095) | NA | Terminated | 8 | ICU overnight noise-reduction trial measuring sedative use and sleep quality; terminated early, underpowered. |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Phase 4 | Completed | 90 | Studied short-term sedation effects (dexmedetomidine vs standard sedation, which may include midazolam) on sleep and inflammation in critically ill ALI/ARDS patients. |
| [NCT06041711](https://clinicaltrials.gov/study/NCT06041711) | NA | Completed | 66 | Compared general vs regional anaesthesia effects on perioperative sleep quality in hip arthroplasty patients. |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | NA | Terminated | 5 | Directly compared dexmedetomidine vs midazolam on sleep quality/quantity (24h polysomnography) and delirium incidence in ventilated ICU patients; terminated, very small sample. |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Compared dexmedetomidine vs midazolam sedation efficacy in critically ill ventilated children. |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | NA | Completed | 131 | Compared remimazolam vs propofol+midazolam general anaesthesia in cancer surgery. |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Randomised, double-blind comparison of dexmedetomidine vs midazolam for facilitating extubation in ICU patients. |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Phase 4 | Completed | 100 | Pilot RCT of a dexmedetomidine-focused nocturnal sedation/sleep protocol vs usual care (which may include midazolam) on delirium incidence in critically ill patients. |

*Note: none of the identified trials were designed as pivotal chronic-insomnia registration trials; most are peri-procedural/ICU sedation studies where sleep or delirium was a secondary outcome.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind trial in 30 women with insomnia secondary to neuromuscular disease: midazolam 15 mg was an effective hypnotic, better tolerated than Vesparax, without hangover effect. |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Multicenter RCT of 14-day midazolam vs flurazepam in chronic insomniacs; examined sleep, performance, and plasma levels. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT (dose-finding) | Arzneimittel-Forschung | Multicenter pilot study (n=75) established optimal oral dose range (10–30 mg) for midazolam in mild-to-moderate insomnia secondary to musculoskeletal/nerve disorders and allergies. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT (multicenter) | Journal of Clinical Psychopharmacology | Executive summary of the multicenter 14-day flurazepam vs midazolam chronic insomnia trial (companion paper to PMID 2121802). |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Reviews clinical use of hypnotics including benzodiazepines, discussing pharmacokinetic/pharmacodynamic profile differences relevant to insomnia subtypes. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review/Mechanistic | Orvosi Hetilap | General review of insomnia pathogenesis and cerebral hypoperfusion; mechanistic background rather than midazolam-specific data. |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Pilot study | Journal of Clinical Medicine | Evaluates lemborexant (not midazolam) for insomnia in high-delirium-risk patients, noting benzodiazepines are traditionally used for insomnia but may increase delirium risk — relevant as a safety counterpoint. |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Preclinical | Psychopharmacology | Studies zolpidem (a related GABA-A hypnotic, not midazolam) on sedation, anxiety, and memory; supports GABA-A mechanism relevance to insomnia but is drug-analog, not direct evidence. |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preclinical (mouse) | Pain | Mouse neuropathic pain model shows sleep disturbance is linked to altered GABAergic transmission, supporting the GABA-A mechanistic rationale for benzodiazepine effect on sleep. |
| [36912148](https://pubmed.ncbi.nlm.nih.gov/36912148/) | 2024 | Case report | American Journal of Hospice & Palliative Care | Describes symptom management (including sedative use) at end of life in COVID-19 patients; only tangentially relevant to insomnia. |

---

## Australia Market Information

No ARTG entries were found for midazolam in this evidence pack — the drug's `market_status` is recorded as **Not Marketed** with **0** licenses on file, so a product/dosage-form table cannot be produced. This may reflect either genuine non-registration under this brand/INN or a gap in the query source (TFDA lookup returned 0 results); this should be confirmed directly against the ARTG before any decision is finalised.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack has no key warnings, contraindications, or drug interaction data on file for midazolam — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (GABA-A receptor modulation) is plausible and is supported by several older RCTs specifically testing midazolam as a short-term hypnotic, giving an evidence level of L2. However, the drug is not currently registered in Australia (0 ARTG entries), and the TFDA/TGA product-information data needed for even an initial safety screen is a **Blocking** gap. Most of the surrounding trial evidence is peri-procedural sedation data rather than chronic insomnia therapy data, and midazolam's short half-life limits its suitability for sleep maintenance — this is a mechanistic caution, not just a data gap.

**To proceed, the following is needed:**
- TGA/TFDA-approved Product Information — key warnings and contraindications (Blocking, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High priority, DG002)
- Confirmation of Australian registration status/ARTG entry (or absence thereof) directly against the TGA database
- Clarification of the drug's originally licensed indication, since this evidence pack contains no record of it
- A dedicated assessment of whether midazolam's short half-life is compatible with a chronic (rather than sleep-onset-only) insomnia indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

