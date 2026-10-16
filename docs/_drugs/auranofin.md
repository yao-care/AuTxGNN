---
layout: default
title: Auranofin
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Auranofin: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Auranofin"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "osteoarthritis susceptibility", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "cholangiocarcinoma, susceptibility to", "arthropathy", "osteoarthritis"]
---

# Auranofin
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

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is an oral gold-based anti-rheumatic drug, originally used to treat rheumatoid arthritis.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, an ultra-rare developmental disorder, but there are **0 clinical trials** and **0 publications** supporting it. The score most likely reflects knowledge-graph proximity rather than biology.

Note: the more biologically plausible candidates in the data compiled for this report are **arthropathy** (including gouty and psoriatic arthritis) and **osteoarthritis**. They are discussed below as context, but they remain preclinical or indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally recorded for this drug. From the published literature, auranofin is a gold(I) compound that inhibits thioredoxin reductase, increases cellular oxidative stress, and suppresses inflammatory signalling such as NF-κB and the NLRP3 inflammasome. Its exact mechanism in rheumatoid arthritis is still not fully understood.

For the top-ranked prediction, **no plausible mechanistic link was identified**. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an ultra-rare developmental disorder, and nothing in auranofin's redox or anti-inflammatory pharmacology suggests it could correct such a condition. The high score (rank 5,468 in the model's output) likely reflects proximity in the knowledge graph rather than a real biological relationship. The next two predictions (brachydactyly-syndactyly syndrome, 99.24%; osteoarthritis susceptibility, 91.79%) share the same weakness. The first is a congenital limb malformation, and the second is a genetic susceptibility label rather than a treatable clinical entity.

Lower-ranked predictions are more biologically credible:
- **Arthropathy (62.81%)**: This overlaps largely with the existing rheumatoid arthritis indication. A 2025 preclinical study reported that auranofin reduced gouty inflammation by suppressing NLRP3 activation and neutrophil migration. This is a possible new direction at the preclinical stage.
- **Osteoarthritis (61.93%)**: A 2022 preclinical study found that inhibiting TXNRD1 (auranofin's primary target) protected cartilage matrix through Nrf2 activation. This is hypothesis-generating only, with no human efficacy data.
- **Cholangiocarcinoma susceptibility (64.11%)**: Auranofin has general preclinical anticancer activity, but nothing specific to cholangiocarcinoma was retrieved.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, nor for any of the 10 predicted indications reviewed.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For context, the table below lists the most relevant publications retrieved for the arthropathy and osteoarthritis predictions. They support the general pharmacology of auranofin, not the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10796461](https://pubmed.ncbi.nlm.nih.gov/10796461/) | 2000 | Systematic Review | Cochrane Database Syst Rev | Auranofin versus placebo in rheumatoid arthritis; use has declined, partly because of conflicting study results |
| [10796328](https://pubmed.ncbi.nlm.nih.gov/10796328/) | 2000 | Systematic Review | Cochrane Database Syst Rev | Interventions for psoriatic arthritis, including auranofin |
| [1977391](https://pubmed.ncbi.nlm.nih.gov/1977391/) | 1990 | Meta-analysis | Arthritis Rheum | Comparative efficacy and toxicity of second-line drugs in rheumatoid arthritis, including auranofin |
| [41090769](https://pubmed.ncbi.nlm.nih.gov/41090769/) | 2025 | Preclinical | Cells | Auranofin reduced gouty inflammation by suppressing NLRP3 activation and neutrophil migration via the IL-33/ST2-CXCL1 axis |
| [36308906](https://pubmed.ncbi.nlm.nih.gov/36308906/) | 2022 | Preclinical | Biochem Biophys Res Commun | TXNRD1 inhibition prevented cartilage matrix degeneration via Nrf2 in osteoarthritis |
| [34731781](https://pubmed.ncbi.nlm.nih.gov/34731781/) | 2021 | Review | Int Immunopharmacol | Auranofin past and present; anti-inflammatory effects and repurposing |
| [37071737](https://pubmed.ncbi.nlm.nih.gov/37071737/) | 2023 | Review | Chem Rev | Gold drugs and repurposing of auranofin in cancer, parasitic and microbial infections |
| [33642497](https://pubmed.ncbi.nlm.nih.gov/33642497/) | 2021 | Review | Yakugaku Zasshi | Potential anticancer activity of auranofin |
| [34630379](https://pubmed.ncbi.nlm.nih.gov/34630379/) | 2021 | Review | Front Immunol | Auranofin's anti-inflammatory, redox and antiviral properties in the context of COVID-19 |
| [6426923](https://pubmed.ncbi.nlm.nih.gov/6426923/) | 1984 | Review | Drugs | Pharmacology and use of auranofin in rheumatoid arthritis; efficacy appears to approach sodium aurothiomalate |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1095P | Ridaura | Tablet 3 mg (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease graph links, not from product label text, and should be checked against the Product Information):
- Blood disorders: haematologic disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia
- Kidney and liver disease, hepatitis, gallbladder disease
- Skin conditions: exanthem, exfoliative dermatitis, urticaria, angioedema, atopic eczema, dermatitis
- Lung conditions: pulmonary fibrosis, post-inflammatory pulmonary fibrosis
- Gastrointestinal conditions: colitis, necrotizing enterocolitis
- Autoimmune and other conditions: systemic lupus erythematosus (including paediatric), Sjögren syndrome, dry eye syndrome
- Metabolic and vascular conditions: diabetes mellitus, diabetic ketoacidosis, hypertension and hypertensive disorder, pyoureter

**Drug Interactions**: 86 interactions were identified. The main ones with a recorded severity are:
- **Major**: deferiprone, proguanil, chloroquine
- **Moderate**: metronidazole, tinidazole, rosuvastatin, simvastatin, benznidazole, disulfiram
- Other listed interactions have unclassified severity, including warfarin, prednisone, prednisolone, omeprazole, pantoprazole, lansoprazole, ranitidine, misoprostol, clarithromycin, calcitriol and folic acid.

Please refer to the TGA-approved Product Information (PI) for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is based on model score alone. It has no trials, no literature and no plausible mechanism linking auranofin to this ultra-rare developmental syndrome. The knowledge-graph contraindication list, notably the blood, kidney, liver and lung disorders, adds a safety concern for any new use.

**To proceed, the following is needed:**
- A documented mechanistic rationale linking thioredoxin reductase or inflammatory pathways to the predicted disease
- Preclinical disease-model data for the predicted indication
- Confirmation of the approved indication text and safety warnings from the TGA Product Information (the label data was unavailable)
- If a repurposing direction is pursued, redirect effort to the better-supported candidates: gouty inflammation (arthropathy) and osteoarthritis, both currently at the preclinical research-question stage
- For the cancer-related prediction (cholangiocarcinoma), disease-specific preclinical data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

