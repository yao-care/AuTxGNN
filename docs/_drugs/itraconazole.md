---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Systemic fungal infections"
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal originally used for systemic fungal infections such as candidiasis, aspergillosis, histoplasmosis, blastomycosis and sporotrichosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, with a very high score (99.3%), but **no clinical trials** and **no publications showing itraconazole efficacy against Pneumocystis** were found.
The prediction is best treated as a model signal rather than an evidence-backed lead. Of the other ten predictions, Cryptococcal meningitis, penicilliosis and neonatal candidiasis are more clinically plausible (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic fungal infections (esophageal candidiasis, candidemia, histoplasmosis, aspergillosis, blastomycosis, coccidioidomycosis, sporotrichosis, fusariosis and others; Australian ARTG indication text not available in the data compiled) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Itraconazole is a triazole antifungal; this class inhibits CYP51 (lanosterol 14-alpha-demethylase), blocking ergosterol synthesis in fungal cell membranes. This is general class knowledge rather than data from the compiled record.

For pneumocystosis, the mechanistic link is weak. *Pneumocystis jirovecii* is fungal, but its membrane contains very little ergosterol (cholesterol is the main sterol), so the azole target is poorly relevant. The high TxGNN score most likely reflects the drug's antifungal class and network proximity in the knowledge graph rather than a validated mechanism. The retrieved literature consists of general reviews on prophylaxis in transplant, HIV and neutropenic populations and histoplasmosis papers; none shows itraconazole efficacy against Pneumocystis.

By contrast, the lower-ranked predictions are mechanistically more coherent, because the pathogens are ergosterol-containing fungi (see the table of other predictions in the Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pneumocystosis.

For reference, the second-ranked prediction (cryptococcal meningitis) has two registered trials; neither clearly tests itraconazole as the intervention under study:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000639](https://clinicaltrials.gov/study/NCT00000639) | NA | Completed | 400 | Amphotericin B with flucytosine vs amphotericin B alone in AIDS-associated cryptococcal meningitis, followed by a fluconazole vs itraconazole comparison |
| [NCT00012467](https://clinicaltrials.gov/study/NCT00012467) | Phase 2 | Completed | 60 | Interferon-gamma 1b added to standard antifungal therapy; the agents in standard therapy cannot be confirmed from the truncated title |

---

## Literature Evidence

The most relevant publications retrieved for pneumocystosis are listed below. None demonstrates efficacy of itraconazole against Pneumocystis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Randomised placebo-controlled trial (Phase III) | HIV Medicine | Itraconazole capsules for prevention of deep fungal infections in immunodeficient HIV patients; the abstract excerpt does not report a Pneumocystis outcome |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clin Infect Dis | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against Pneumocystis pneumonia |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clin Evid | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including Pneumocystis |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplant Proc | Invasive fungal infections after kidney transplantation |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Clinical review | Medicine | Disseminated histoplasmosis in AIDS |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and review | Front Immunol | *T. marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10732W | Lozanoc | Capsule 50 mg (oral) | Not available in the data compiled |

Only one registered product was identified, and the identifier is as recorded in the data compiled for this report (it should be verified against the ARTG).

---

## Safety Considerations

Safety text from the Australian Product Information was not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

**Disease associations flagged in the knowledge graph (not label text):** long QT syndrome and torsades de pointes, congestive heart failure, cardiomyopathy and other myocardial disorders, coronary artery disease, liver disease and drug-induced liver injury, kidney disease, chronic obstructive pulmonary disease, peripheral neuropathy, hearing loss and vision disorders, and potassium deficiency. These should be verified against the PI.

**Drug interactions (DDInter, 100 interactions recorded; selected examples):**
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, alosetron, aprepitant
- **Minor:** metformin, pioglitazone, chlorpropamide, amphotericin B

Itraconazole is a CYP3A4 inhibitor, so extensive interactions are expected. Acid-suppressing drugs can also reduce absorption of some formulations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, pneumocystosis, has no clinical trials and no supporting literature. It also has a weak mechanistic basis, because *Pneumocystis* has little ergosterol. Evidence level is L5.
- The score appears to reflect the drug's antifungal class rather than a real therapeutic signal.

**Other predictions in the data compiled:**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Cryptococcal meningitis | 93.7% | L2 | Biologically plausible, but fluconazole and amphotericin B regimens are standard and itraconazole has limited CNS penetration; at most a niche or step-down role |
| 3 | Penicilliosis (talaromycosis) | 89.0% | L3 | Already used for step-down and secondary prophylaxis after amphotericin B; supported by case series and reviews |
| 4 | Trichosporonosis | 89.0% | L4 | Limited and variable activity; voriconazole preferred |
| 5 | Hyalohyphomycosis | 89.0% | L4 | Fusariosis is already an original indication; poor or variable susceptibility for the broader group |
| 6 | Geotrichosis | 89.0% | L4 | Case reports only; itraconazole used within multi-drug regimens |
| 7 | Maple bark strippers' lung | 88.8% | L5 | Immune-mediated hypersensitivity pneumonitis; antifungal role not established |
| 8 | Leprosy | 87.5% | L5 | Bacterial, no ergosterol; likely a false-positive retrieval |
| 9 | Candida glabrata | 85.0% | L4 | Frequent azole resistance; echinocandins preferred |
| 10 | Neonatal candidiasis | 85.0% | L3 | Limited infant data; safety concerns (hepatotoxicity, CYP3A4 interactions, variable absorption); fluconazole, amphotericin B and echinocandins are standard |

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for any activity against *Pneumocystis* (or a decision to redirect the evaluation to penicilliosis or cryptococcal meningitis)
- Verification of the intervention arms in NCT00012467 and NCT00000639
- The Australian PI warnings, contraindications and approved indication text for ARTG 10732W
- A formal literature review of the penicilliosis evidence, which is the most clinically coherent lead
- A cardiac, hepatic and drug-interaction risk assessment before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

