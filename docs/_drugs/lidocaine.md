---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Dermatitis, neuralgia, postherpetic neuralgia, haemorrhoids…"
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Lidocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lidocaine: From Dermatitis and Neuralgia to Conjunctival Disorder

## One-Sentence Summary

Lidocaine is a local anaesthetic originally used for conditions such as dermatitis, neuralgia (including postherpetic neuralgia), haemorrhoids and scabies or lice infestations.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but this has no supporting trials or publications. The best-supported prediction is **conjunctival disorder** (rank 6), with **2 clinical trials** and **20 publications**. These mainly describe procedural anaesthesia rather than disease treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis, neuralgia, postherpetic neuralgia, haemorrhoids, scabies and lice infestations (from the knowledge graph; no approved indication text is listed for the ARTG entry) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (rank 1); conjunctival disorder (rank 6) is the best-evidenced prediction |
| TxGNN Prediction Score | 99.99% (rank 1); 99.84% (conjunctival disorder) |
| Evidence Level | L5 for rank 1 (model prediction only); L3 for conjunctival disorder |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1); Research Question for conjunctival disorder |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lidocaine is a well-known sodium channel blocker that stops nerve signals, which explains its use for pain and itch. Its original indications (neuralgia, dermatitis, haemorrhoids) are largely about relieving nerve-mediated symptoms rather than treating an underlying disease process.

For the top prediction, punctate epithelial keratoconjunctivitis, the link is weak. Lidocaine might ease ocular surface pain, but the data does not support any effect on the disease itself. Topical anaesthetics are also known to impair corneal epithelial healing, so the prediction is questionable.

For conjunctival disorder, the evidence is more relevant but still indirect. It concerns anaesthesia during eye surgery (mainly pterygium excision) and lidocaine use in neuralgiform headaches with conjunctival injection (SUNCT/SUNA), where eye redness is a symptom. This largely reflects the existing anaesthetic profile rather than a new disease-modifying use. There is also indirect preclinical support for atopic conjunctivitis (rank 5), suggesting sensory nerve involvement in allergic responses, but no clinical trials.

## Clinical Trial Evidence

Trials below relate to the predicted indication "conjunctival disorder". No trials were found for the top-ranked prediction.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine Ophtesic gel vs subconjunctival lidocaine injection in pterygium excision, aiming to reduce injection pain |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | N/A | Completed | 34 | Postoperative pain with two local anaesthesia types in conjunctival Müllerectomy for drooping eyelid (tangential relevance) |

## Literature Evidence

Selected publications for "conjunctival disorder" (rank 6), prioritising trials and clinical studies. Where the data lists no study type, the type is described from the title.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye (London) | Lidocaine 2% gel vs tetracaine 1% drops as sole topical anaesthetic for primary pterygium surgery |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Pilot study | Cornea | Subconjunctival injection vs 2% vs 5% lidocaine gel in pterygium surgery |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical study | Acta Ophthalmol Scand | Efficacy of lidocaine 2% gel as topical anaesthetic in pterygium surgery |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical study | Ophthalmologica | Viscous lidocaine for pain relief after pterygium surgery |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT and SUNA (headache disorders with conjunctival injection) |
| [23330822](https://pubmed.ncbi.nlm.nih.gov/23330822/) | 2013 | Clinical study | Curr Eye Res | Efficacy of different anaesthetics and topical anti-inflammatories for pain after intravitreal injection |
| [10696746](https://pubmed.ncbi.nlm.nih.gov/10696746/) | 2000 | Clinical study | Retina | Topical anaesthesia as an alternative to peribulbar or retrobulbar block in posterior vitrectomy |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review (safety) | Cephalalgia | Neuropsychiatric side effects of lidocaine in headache treatment; side effects occurred in all 20 patients in the authors' series |
| [34003160](https://pubmed.ncbi.nlm.nih.gov/34003160/) | 2021 | Review | Neurology India | Update on SUNCT and SUNA |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Preclinical mechanistic study | JCI Insight | Nerve-goblet cell association promotes allergic conjunctivitis through rapid antigen passage (supports atopic conjunctivitis, rank 5) |

For other predictions, the only literature retrieved was not evidence of efficacy:
- **Exposure keratitis (rank 4):** a case series of keratitis in methamphetamine abusers (PMID 8862924), likely a keyword match.
- **Nephrotic syndrome (rank 7):** pharmacokinetic work showing altered lidocaine protein binding in renal disease (PMID 7037263), and a case report of methaemoglobinaemia (PMID 41995267).
- **Non-human animal disease (rank 8):** a veterinary report of seizures in macaques (PMID 19858165). This is a safety signal, not an indication.
- **Tinea corporis (rank 9):** a general review of chronic pruritus (PMID 38809527).

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10209H | Lignocaine Injection (Bridgewest) | Injection containing lidocaine hydrochloride monohydrate 50 mg in 5 mL | Not listed in the data compiled for this report |

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** the graph links lidocaine to a range of conditions, including hypertension, liver failure, liver disease, cirrhosis, kidney disease, epilepsy, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, herpes simplex keratitis, psychotic disorders, and several infectious and skin conditions. These are graph-derived associations and need verification against the approved Product Information.

**Drug Interactions:** 100 interactions were identified. Selected examples from the data:
- **Major:** bupropion
- **Moderate:** aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol 3350 with electrolytes, picosulfuric acid, sodium sulfate
- **Minor:** dexamethasone, kanamycin, neomycin, omeprazole, streptomycin, troglitazone

**Additional signals from the literature:**
- Topical anaesthetic misuse can cause keratopathy, and topical anaesthetics may impair corneal epithelial healing.
- Neuropsychiatric and cardiac side effects were common with intravenous lidocaine in refractory headache.
- Methaemoglobinaemia was reported in a child receiving topical lidocaine with other methaemoglobin-inducing drugs.
- Lidocaine plasma protein binding is altered in renal disease.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** (top prediction, punctate epithelial keratoconjunctivitis); **Research Question** for conjunctival disorder.

**Rationale:**
- The top-ranked prediction rests on model output alone (L5), with no trials or literature, and a plausible counter-mechanism (impaired corneal healing).
- The evidence for conjunctival disorder (L3) shows procedural anaesthesia in eye surgery, which overlaps with existing anaesthetic use and does not demonstrate treatment of a disease.
- None of the 10 predictions has evidence of lidocaine treating the underlying condition.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product, to complete the safety screen
- Mechanism of action data
- Approved indication text for the ARTG entry
- Controlled trials showing disease-modifying benefit (not only procedural anaesthesia) in a defined conjunctival or ocular surface condition
- Assessment of ocular safety, particularly corneal epithelial toxicity with repeated topical use
- Confirmation of route compatibility, as the only registered Australian product is an injection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

