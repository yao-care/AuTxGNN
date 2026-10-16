---
layout: default
title: Gabapentin
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gabapentin: predicted new indication Myofascial pain syndrome (evidence level L5). Approved use: Restless legs syndrome"
monitor_inn: "Gabapentin"
predicted_indications: ["acne (disease)", "adolescent/adult onset autosomal dominant epilepsy with auditory features", "epilepsy with generalized tonic-clonic seizures", "myofascial pain syndrome", "visual epilepsy", "active cochlear Meniere disease", "active cochleovestibular Meniere disease", "active vestibular Meniere disease", "trigeminal nerve neoplasm", "osteoarthritis susceptibility"]
---

# Gabapentin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Gabapentin: From Restless Legs Syndrome and Postherpetic Neuralgia to Myofascial Pain Syndrome

## One-Sentence Summary

Gabapentin is an oral anticonvulsant originally used for restless legs syndrome and postherpetic neuralgia. The TxGNN model predicts it may be effective for **myofascial pain syndrome**, the highest-ranked prediction with meaningful supporting evidence. Support currently comes from **4 clinical trials** (all in the related condition fibromyalgia) and **9 publications**, including one RCT in chronic masticatory muscle pain.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Restless legs syndrome; postherpetic neuralgia (the ARTG entry in the data compiled for this report has no approved indication text) |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 92.97% |
| Evidence Level | L1 as scored in the data compiled for this report. This is generous: the trials are in fibromyalgia, not myofascial pain syndrome, so the effective level for the predicted indication is closer to L2-L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on the other predictions:** The top-ranked prediction, acne (score 98.5%), has no trials or literature and no plausible mechanism, so it is likely a knowledge-graph artefact (Hold). Other predictions (epilepsy subtypes, Meniere disease subtypes, trigeminal nerve neoplasm, osteoarthritis susceptibility) have no direct supporting evidence and are rated Hold or Research Question. Myofascial pain syndrome is the only prediction with a clinical-trial base, so this report focuses on it.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Gabapentin is generally understood to bind the alpha-2-delta subunit of voltage-gated calcium channels, which reduces excitatory neurotransmitter release and dampens central sensitisation. This is the same pharmacology that underpins its use in postherpetic neuralgia.

Myofascial pain syndrome is a chronic regional muscle pain condition with trigger points and features of central sensitisation. Its pain biology overlaps with the neuropathic pain that gabapentin already treats, which makes symptomatic benefit mechanistically plausible.

The direct evidence is limited. Most trials are in fibromyalgia, a related but distinct condition. The most relevant direct study is a 12-week RCT in chronic masticatory muscle pain (PMID 17030096), plus an open-label study of stepped treatment with tricyclic antidepressants and gabapentin in myofascial pain.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00057278](https://clinicaltrials.gov/study/NCT00057278) | Phase 2/3 | Completed | 150 | Gabapentin for pain in primary fibromyalgia (GIFT); safety and effectiveness assessed |
| [NCT01107574](https://clinicaltrials.gov/study/NCT01107574) | Phase 3 | Completed | 41 | Gabapentin and/or osteopathic manipulative medicine for fibromyalgia symptoms, tender points and quality of life |
| [NCT05384210](https://clinicaltrials.gov/study/NCT05384210) | Not applicable | Unknown | 75 | Milnacipran vs gabapentin vs combination in fibromyalgia |
| [NCT02052414](https://clinicaltrials.gov/study/NCT02052414) | Not applicable | Completed | 34 | Open-label, non-randomised study of Gralise (extended-release gabapentin) in fibromyalgia pain |

None of these trials enrolled patients with myofascial pain syndrome. No ANZCTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17030096](https://pubmed.ncbi.nlm.nih.gov/17030096/) | 2007 | RCT | Pain | 12-week RCT (n=50) of gabapentin for chronic masticatory myalgia, assessing analgesic effect |
| [25905532](https://pubmed.ncbi.nlm.nih.gov/25905532/) | 2015 | Cohort (open study) | J Oral Facial Pain Headache | Response to stepped treatment with tricyclic antidepressants and gabapentin in persistent myofascial pain |
| [40110636](https://pubmed.ncbi.nlm.nih.gov/40110636/) | 2025 | Review | Muscle & Nerve | Update on clinical features, pathogenesis, diagnosis and treatment of myofascial pain syndrome |
| [9303258](https://pubmed.ncbi.nlm.nih.gov/9303258/) | 1997 | Review | Clin J Pain | Effect of gabapentin on neuropathic pain scores and opiate use |
| [37142285](https://pubmed.ncbi.nlm.nih.gov/37142285/) | 2023 | Case report | BMJ Case Reports | Levator ani syndrome (a myofascial pain condition) presenting with vaginal pain |
| [32627323](https://pubmed.ncbi.nlm.nih.gov/32627323/) | 2020 | Case report | Am J Med Genet A | Benefit of gabapentin in two children with Noonan syndrome and early-onset neuropathic pain |
| [25794224](https://pubmed.ncbi.nlm.nih.gov/25794224/) | 2015 | Case report | Pain Physician | Peripheral nerve stimulation for temporomandibular joint pain |
| [24849638](https://pubmed.ncbi.nlm.nih.gov/24849638/) | 2014 | Case report | BMJ Case Reports | Temporomandibular joint pain unresponsive to gabapentin and other drugs, treated with stellate ganglion block |

Several of these papers are only loosely related to the predicted indication, and one case report describes gabapentin failing to help.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1834M | Neurontin | Capsule 300 mg (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified, with the examples below drawn from the list provided.
  - **Major:** morphine (including liposomal morphine), most likely additive central nervous system and respiratory depression.
  - **Moderate:** dronabinol, nabilone, metoclopramide, opium and sibutramine.
  - **Minor:** cimetidine and antacids containing magnesium or aluminium (magnesium oxide, magnesium hydroxide, magnesium carbonate, aluminium hydroxide, magaldrate).
- **Disease-related cautions (from the knowledge graph, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease and pyoureter. Gabapentin is renally cleared, so kidney function needs attention.

Please refer to the TGA-approved Product Information (PI) for key warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Myofascial pain syndrome is the only prediction with a clinical-trial base, and gabapentin is a well-established neuropathic pain drug with a plausible mechanism. However, the trials are in fibromyalgia and only one RCT, in chronic masticatory myalgia, is closer to the target condition. The evidence is supportive but indirect.

**To proceed, the following is needed:**
- Trials or systematic review evidence specifically in myofascial pain syndrome
- Retrieval of TGA Product Information (warnings, contraindications, approved indications for ARTG 1834M)
- Mechanism of action data (MOA)
- Safety monitoring plan, particularly for renal impairment, concurrent opioids and other CNS depressants
- A dosing and renal-adjustment plan appropriate for the Australian setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

