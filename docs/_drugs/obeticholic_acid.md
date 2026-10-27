---
layout: default
title: Obeticholic Acid
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Obeticholic Acid: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the data compiled for this report (the literature descr…"
monitor_inn: "Obeticholic acid"
predicted_indications: ["rheumatoid arthritis", "conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "heart disease", "orofacial clefting syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "Jeune syndrome situs inversus"]
---

# Obeticholic Acid
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

## Obeticholic Acid: From Primary Biliary Cholangitis to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Obeticholic acid is a farnesoid X receptor (FXR) agonist, registered in Australia as Ocaliva 5 mg tablets. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and only **one directly relevant preclinical study** (in rats). The evidence is therefore very early-stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the literature describes obeticholic acid as a treatment for primary biliary cholangitis) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 (preclinical only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on the published literature, obeticholic acid is a potent FXR agonist, and it is used as second-line therapy for primary biliary cholangitis (PBC).

FXR activation has anti-inflammatory effects, including suppression of NF-κB signalling and pro-inflammatory cytokines. This provides a plausible link to autoimmune arthritis. A single 2026 rat study reports that obeticholic acid attenuated Complete Freund's Adjuvant-induced arthritis through FXR-mediated modulation of TGF-β/TAK1/MKK3/p38 MAPK signalling, inflammation and oxidative stress.

This link is hypothesis-generating only. The other retrieved papers concern PBC, autoimmune hepatitis models and FXR protection against liver injury from *Tripterygium wilfordii*. They are indirect and do not demonstrate efficacy in rheumatoid arthritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42758264](https://pubmed.ncbi.nlm.nih.gov/42758264/) | 2026 | Preclinical (rat model) | Inflammopharmacology | Obeticholic acid attenuated adjuvant-induced arthritis via FXR-mediated modulation of TGF-β/TAK1/MKK3/p38 MAPK signalling, inflammation and oxidative stress |
| [32299307](https://pubmed.ncbi.nlm.nih.gov/32299307/) | 2020 | Review | United European Gastroenterol J | Diagnosis and treatment of PBC (indirect; background on the original disease area) |
| [35903109](https://pubmed.ncbi.nlm.nih.gov/35903109/) | 2022 | Review | Front Immunol | Animal models of autoimmune hepatitis (indirect) |
| [33704005](https://pubmed.ncbi.nlm.nih.gov/33704005/) | 2021 | Preclinical (mouse) | Xenobiotica | FXR activation prevented liver injury from *Tripterygium wilfordii* preparations used for RA (indirect; relates to liver safety of RA therapy) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12623J | Ocaliva | Tablet 5 mg (oral) | Not listed in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 50 potential interactions were identified. Among those listed, one is classed as **Major** (grazoprevir). Most others are **Moderate**, including:
  - Bile acid sequestrants: cholestyramine, colesevelam, colestipol
  - Methylxanthines: theophylline, aminophylline, caffeine
  - Anticoagulants: anisindione, dicoumarol
  - Psychotropics: clozapine, clomipramine, duloxetine, asenapine
  - Others: lidocaine, alosetron, anagrelide, bendamustine, cyclobenzaprine, flutamide

  Esomeprazole is classed as Minor.
- **Literature-based considerations**: The pooled safety analysis (PMID 36757421, 1,878 individuals with chronic liver disease) and related papers describe the safety profile in liver disease. Pruritus and hepatotoxicity in advanced cirrhosis are recognised concerns. Obeticholic acid can also raise LDL-C and lower HDL-C. These would need weighing in an RA population that is often exposed to hepatotoxic DMARDs.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications, as these were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only direct support is a single animal study, and no human trials exist. Obeticholic acid also carries liver-related and lipid safety concerns that matter in RA patients.

**To proceed, the following is needed:**
- The TGA-approved PI, to obtain the approved indication, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Replication of the rat arthritis findings in additional preclinical models, with safety and dose assessment
- A defined RA population and a safety plan covering hepatic monitoring, lipid effects and interactions with concurrent DMARDs
- A phase 1/2 proof-of-concept study design if preclinical results are confirmed

### Note on other predicted indications

Other top-ranked predictions are not recommended for progression at this stage:
- **Heart disease** (score 98.99%, L4): The evidence is preclinical or indirect (cardiac dysfunction in NASH mice, cisplatin cardiotoxicity and diabetic cardiomyopathy models). The label is too broad, and the LDL-C/HDL-C effects are a potential concern. A specific cardiac phenotype should be defined first.
- **Conjunctivitis** and the remaining rare congenital or genetic syndromes (L5): These are model predictions only, with no supporting trials or relevant literature, and no plausible FXR-mediated mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

