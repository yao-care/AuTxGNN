---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Piroxicam: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome . Most plau… (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "Piroxicam"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis"]
---

# Piroxicam
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

# Piroxicam: From Rheumatoid Arthritis and Osteoarthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a non-steroidal anti-inflammatory drug (NSAID) originally used to treat rheumatoid arthritis and osteoarthritis.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, but this has no credible mechanistic link and no supporting studies. The most clinically plausible prediction in the data compiled for this report is **juvenile idiopathic arthritis (JIA)**, which has **0 clinical trials** and **10 publications** (including 2 small piroxicam-specific paediatric comparisons from the 1980s).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome (rank 1; no credible mechanistic link). Most plausible candidate: juvenile idiopathic arthritis (rank 10) |
| TxGNN Prediction Score | 99.996% (rank 1); 99.927% (JIA) |
| Evidence Level | L5 (rank 1); L3 (JIA) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails limited to JIA as a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, piroxicam is a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation and pain, which underpins its use in rheumatoid arthritis and osteoarthritis.

**Top-ranked predictions (ranks 1–8).** The highest-scoring predictions are mostly rare genetic skeletal, limb or developmental syndromes (for example brachydactyly-syndactyly syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia, pseudoachondroplasia) plus WHIM syndrome. A COX inhibitor cannot correct these developmental or genetic defects. The high scores most likely reflect knowledge-graph proximity, such as shared skeletal or connective tissue nodes, rather than a therapeutic rationale. At most, an NSAID might give symptomatic joint pain relief in some of these conditions. No trials or literature were found for any of them.

**Rheumatoid nodulosis (rank 9).** This is related to rheumatoid arthritis, so symptomatic NSAID effects are conceivable. However, it is a distinct nodule-forming condition and no efficacy evidence was found.

**Juvenile idiopathic arthritis (rank 10).** This has the strongest rationale. JIA is an inflammatory arthritis for which NSAIDs are an established symptomatic therapy. Piroxicam-specific paediatric data exist, but they are old and concern symptom control rather than disease modification. Piroxicam is not a first-line JIA therapy in current practice, which favours disease-modifying antirheumatic drugs (DMARDs) and biologics.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no ClinicalTrials.gov, ANZCTR or ICTRP entries were found for any predicted indication).

---

## Literature Evidence

The following is for juvenile idiopathic arthritis (rank 10). No literature was found for the other nine predicted indications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic review / network meta-analysis | World J Clin Cases | Compares different NSAIDs for JIA; the optimal NSAID approach has not been established |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic review / network meta-analysis | Indian Pediatr | Compares the efficacy and safety of nine NSAIDs in JIA |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Randomised clinical study | Eur J Rheumatol Inflamm | 26 patients (aged 3–25) randomised to piroxicam or naproxen in juvenile rheumatoid arthritis; painful and swollen joint counts decreased significantly |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | Double-blind crossover study | Br J Rheumatol | Piroxicam vs naproxen in 47 children with seronegative juvenile chronic arthritis over 8 weeks; no significant difference between the two treatments reported; also discusses problems in paediatric NSAID trials |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic study | Eur J Clin Pharmacol | 10 children with rheumatoid arthritis given about 0.4 mg/kg once daily; mean half-life about 32.6 hours |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Long-term toxicity study | Clin Rheumatol | Describes long-term toxicity of antirheumatic and anti-inflammatory drugs in 117 children followed for a mean of 8.6 years |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderarztl Prax | Drug therapy of juvenile chronic arthritis; piroxicam is described as a newer option |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review (indirect) | Crit Rev Ther Drug Carrier Syst | NSAID drug delivery systems in arthritis |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review (indirect) | Drugs | Nabumetone in osteoarthritis and rheumatoid arthritis; not piroxicam-specific |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review (indirect) | Drugs | Pirprofen review; piroxicam appears only as a comparator |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1897W | APO-Piroxicam | Capsule 10 mg | Not available in the data compiled for this report |

---

## Safety Considerations

**Contraindications / conditions of concern (from knowledge-graph drug-disease contraindication links, not label text):**
- Cardiovascular and cerebrovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke, cerebral infarction, thrombotic disease, cardiovascular disease
- Renal and hepatic: kidney disease, liver disease, acute liver failure, hepatitis, drug-induced liver injury, gallbladder disease
- Gastrointestinal: active peptic ulcer disease
- Haematological: blood coagulation disease, anaemia, haemoglobinopathy
- Other: substance abuse/dependence, vision disorder/blindness, pyoureter

**Drug Interactions** (100 interactions recorded; examples from the 20 listed):
- **Moderate:** acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, aprepitant, potassium citrate and bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes
- **Minor:** famotidine, ranitidine, cimetidine, linaclotide

Please refer to the TGA-approved Product Information (PI) for official warnings and contraindications. The label data for this product was not available.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (colobomatous microphthalmia-rhizomelic dysplasia syndrome) and the other predictions of ranks 2–8. **Proceed with Guardrails** (as a research question only) for juvenile idiopathic arthritis.

**Rationale:**
- The top-ranked predictions have no mechanistic link and no clinical or literature support. The high TxGNN scores likely reflect graph-topology artefacts.
- JIA has a plausible mechanism and limited, dated piroxicam-specific paediatric data (L3). Piroxicam is not first-line in current practice, and the evidence concerns symptom control only.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- TGA Product Information with warnings, contraindications and approved indications for APO-Piroxicam
- Review of piroxicam against current JIA guidelines and alternative NSAIDs, including paediatric dosing and safety
- Cardiovascular, gastrointestinal and renal risk assessment for the target population
- Any new clinical trial registration (ANZCTR or ClinicalTrials.gov) before further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

