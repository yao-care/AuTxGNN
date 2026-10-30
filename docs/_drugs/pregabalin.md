---
layout: default
title: Pregabalin
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: predicted new indication Tendinitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pregabalin: Tendinitis (top-ranked); osteoarthritis has the strongest supporting evidence (tendinitis)
{: .text-alpha }

## One-Sentence Summary

Pregabalin is a gabapentinoid originally used for anxiety disorder, fibromyalgia, myofascial pain syndrome and postherpetic neuralgia.
The TxGNN model's top-ranked prediction is **tendinitis**, but it has **no registered clinical trials** and only **indirect literature**. Better-supported predicted directions are **osteoarthritis** (9 relevant trials, 1 meta-analysis), **headache disorder** and **migraine disorder**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tendinitis (top-ranked); osteoarthritis has the strongest supporting evidence (tendinitis) |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 for tendinitis (L1 for osteoarthritis and headache disorder; L2 for migraine disorder) |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold for tendinitis; Proceed with Guardrails is worth considering for osteoarthritis pain |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Pregabalin is generally understood to bind the alpha2-delta subunit of voltage-gated calcium channels. This reduces excitatory neurotransmitter release and dampens neuropathic and central-sensitisation pain signalling. This is consistent with its established use in postherpetic neuralgia and fibromyalgia.

For **tendinitis**, the link is indirect. Tendinitis is mainly inflammatory and mechanical, so pregabalin could plausibly help only with neuropathic pain components, such as nerve impingement. The very high TxGNN score is not supported by direct clinical data. The retrieved literature consists of a fluoroquinolone-associated disability report, an editorial on piriformis syndrome, a case report of nerve impingement after a marathon and two perioperative rotator cuff repair studies (one RCT, one retrospective cohort). None test pregabalin as a treatment for tendinitis itself.

The other predictions are more plausible:

- This would be symptom control, not disease modification.
- **Migraine and headache disorders:** Preclinical work shows pregabalin raises the threshold for cortical spreading depression, a plausible basis for migraine prophylaxis.
- **Myositis fibrosa, idiopathic granulomatous myositis, inclusion body myositis, osteoarthritis susceptibility and atrophoderma vermiculata:** These are prediction-only, with no supportive evidence. Any role would be limited to symptomatic pain relief at most.

## Clinical Trial Evidence

There are **no registered clinical trials** for tendinitis. Findings are summarised from registry descriptions only, and results have not been verified.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00442546](https://clinicaltrials.gov/study/NCT00442546) | Phase 3 | Completed | 307 | Multicentre, double-blind, placebo-controlled study of pregabalin for post-operative pain after total knee arthroplasty |
| [NCT04532684](https://clinicaltrials.gov/study/NCT04532684) | Phase 4 | Completed | 66 | Duloxetine vs pregabalin in knee osteoarthritis with mixed-type pain |
| [NCT00581685](https://clinicaltrials.gov/study/NCT00581685) | Phase 3 | Completed | 31 | Pregabalin plus celecoxib around total hip arthroplasty; small perioperative study |
| [NCT05447364](https://clinicaltrials.gov/study/NCT05447364) | Phase 4 | Completed | 82 | 75 mg vs 150 mg pregabalin for pain after total knee arthroplasty |
| [NCT03604354](https://clinicaltrials.gov/study/NCT03604354) | Phase 4 | Completed | 95 | Tapentadol vs pregabalin for post-operative pain after knee arthroplasty |
| [NCT05322681](https://clinicaltrials.gov/study/NCT05322681) | NA | Unknown | 90 | Pregabalin for neuropathic pain after knee arthroplasty in patients without central sensitisation |
| [NCT05254652](https://clinicaltrials.gov/study/NCT05254652) | NA | Unknown | 90 | Pregabalin in centrally sensitised patients treated with duloxetine after knee arthroplasty |
| [NCT06328062](https://clinicaltrials.gov/study/NCT06328062) | NA | Recruiting | 80 | Mirogabalin vs pregabalin after knee arthroplasty |
| [NCT07598474](https://clinicaltrials.gov/study/NCT07598474) | NA | Recruiting | 35 | Pregabalin hydrogel phonophoresis with calf muscle technique in Grade III knee OA |

Other predicted indications with trials:

  - [NCT06271486](https://clinicaltrials.gov/study/NCT06271486): Phase 3, completed, n=75. Pregabalin as an alternative to epidural blood patch for postdural puncture headache.
  - [NCT03910088](https://clinicaltrials.gov/study/NCT03910088): Phase 4, completed, n=30. Pregabalin vs hydrocortisone for postdural puncture headache.
- **Migraine disorder:** [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) (Phase 3, n=70, pregabalin vs sodium valproate) was **withdrawn**, so it yields no efficacy data.

## Literature Evidence

No literature directly addresses pregabalin for tendinitis. The most relevant publications for the better-supported indications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42481863](https://pubmed.ncbi.nlm.nih.gov/42481863/) | 2026 | Systematic review/Meta-analysis | Inflammopharmacology | Effect of pregabalin on pain and function in knee osteoarthritis (RCT meta-analysis) |
| [23918578](https://pubmed.ncbi.nlm.nih.gov/23918578/) | 2013 | RCT | Yonsei Med J | Meloxicam plus pregabalin for knee osteoarthritis pain |
| [35442367](https://pubmed.ncbi.nlm.nih.gov/35442367/) | 2022 | Comparative clinical study | Rev Assoc Med Bras | Duloxetine vs pregabalin on pain and function in knee osteoarthritis |
| [29066930](https://pubmed.ncbi.nlm.nih.gov/29066930/) | 2017 | Randomised clinical study | J Pain Res | Pregabalin or duloxetine vs placebo for hand osteoarthritis pain |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network meta-analysis | JAMA Netw Open | Preventive medications in paediatric migraine |
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iran J Child Neurol | Pregabalin vs sodium valproate in paediatric migraine prophylaxis |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Med Iran | Propranolol vs pregabalin for childhood migraine prophylaxis |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | Preclinical | PNAS | Pregabalin inhibits cortical spreading depression in vivo |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative pregabalin vs interscalene block after rotator cuff repair (tendon-related, postoperative pain) |
| [39688824](https://pubmed.ncbi.nlm.nih.gov/39688824/) | 2024 | Clinical study | Pain Physician | Prednisolone vs pregabalin for post-dural puncture headache |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2335X | Lyzalon | Capsule 75 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications from the knowledge graph:** The TxGNN knowledge graph lists drug-disease contraindication links, which are not drawn from label text. They include thrombocytopenia, several forms of angioedema, myopathy and other muscle diseases (including rhabdomyolysis), impaired renal function and atrioventricular block. Some of these may reflect warnings and precautions, so they should be checked against the PI.
- **Drug interactions:** The interaction screen returned 100 records. The **Major** interactions identified are with **morphine** (including liposomal morphine), which is consistent with additive central nervous system and respiratory depression. **Moderate** interactions include diphenoxylate, difenoxin, dronabinol, nabilone, opium, metoclopramide, sibutramine and the thiazolidinediones (pioglitazone, rosiglitazone, troglitazone).
- Sexual dysfunction and abuse potential have also been described.

For label warnings and contraindications, please refer to the TGA-approved Product Information (PI).

## Conclusion and Next Steps

**Decision: Hold (tendinitis)**

**Rationale:**
- The tendinitis prediction has the highest TxGNN score (0.9971) but no registered trials and only indirect literature. The mechanistic link is limited to possible neuropathic pain components.
- Their evidence concerns symptom control in specific settings, so they would need cautious, guarded evaluation.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA Product Information (including approved indications, warnings and contraindications), both currently missing
- For tendinitis, a focused literature review or a pilot trial in tendinopathy with neuropathic features
- A plan for managing opioid co-prescribing and renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

