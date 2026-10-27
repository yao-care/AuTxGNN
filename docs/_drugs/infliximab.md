---
layout: default
title: Infliximab
parent: Model Prediction Only (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Infliximab: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Crohn's disease, inflammatory bowel disease, ulcerative colitis…"
monitor_inn: "Infliximab"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "hypermobility of coccyx", "anus disease", "Kummell disease", "inflammatory spondylopathy", "bronchitis"]
---

# Infliximab
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

## Infliximab: From Crohn's Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Infliximab is a TNF-alpha blocking antibody, originally used for Crohn's disease, ulcerative colitis, rheumatoid arthritis, ankylosing spondylitis and psoriatic arthritis.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome** (score 90.2%), but there are **no clinical trials and no publications** supporting it. It is most likely a graph-based artefact.
Among the other predictions, those with real support are mostly extensions of existing indications (for example perianal Crohn's disease, spondyloarthritis and polyarticular juvenile arthritis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, ulcerative colitis, rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis (the Australian ARTG entry has no indication text) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome (rank 1) |
| TxGNN Prediction Score | 90.22% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Infliximab is a chimeric monoclonal antibody against TNF-alpha, a pro-inflammatory cytokine. Its efficacy in TNF-driven immune-mediated diseases is well established.

For the top-ranked prediction, **no mechanistic link could be identified**. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an ultra-rare developmental malformation syndrome without a known TNF-driven inflammatory component. The high score is most likely an artefact of the knowledge graph rather than a true signal.

Other highly ranked predictions fall into three groups:
- **Extensions of existing indications (credible):** anus disease (perianal Crohn's disease, rank 5), inflammatory spondylopathy (spondyloarthritis including ankylosing spondylitis, rank 7), polyarticular juvenile rheumatoid arthritis (rank 8) and Crohn disease of the oesophagus (rank 10). These overlap with approved uses or closely related TNF-driven disease.
- **Genuine research question:** rheumatoid vasculitis (rank 3). TNF-alpha is a shared driver with rheumatoid arthritis, but anti-TNF agents have also been linked to paradoxical vasculitis, so the benefit-risk balance is unclear.
- **No rationale:** brachydactyly-syndactyly syndrome, hypermobility of coccyx, Kummell disease and bronchitis, which have no plausible TNF-driven mechanism or supporting evidence.

---

## Clinical Trial Evidence

For the rank 1 prediction, currently no related clinical trials are registered.

For context, the highest-evidence predictions have the following trials (none are specific to the rank 1 prediction):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00036374](https://clinicaltrials.gov/study/NCT00036374) | Phase 3 | Completed | 123 | Infliximab plus methotrexate in polyarticular juvenile rheumatoid arthritis (randomised, double-blind) |
| [NCT02762812](https://clinicaltrials.gov/study/NCT02762812) | Phase 3 | Completed | 199 | BCD-055 (infliximab biosimilar) vs Remicade in ankylosing spondylitis |
| [NCT00844805](https://clinicaltrials.gov/study/NCT00844805) | Phase 3 | Completed | 158 | Infliximab plus naproxen as first-line therapy in early axial spondyloarthritis |
| [NCT00439283](https://clinicaltrials.gov/study/NCT00439283) | Phase 3 | Completed | 240 | Infliximab every 6 weeks vs on demand in ankylosing spondylitis |
| [NCT00202865](https://clinicaltrials.gov/study/NCT00202865) | Phase 3 | Completed | 76 | Low-dose infliximab (3 mg/kg) vs placebo in ankylosing spondylitis |
| [NCT00051623](https://clinicaltrials.gov/study/NCT00051623) | Phase 3 | Completed | 70 | Infliximab in psoriatic arthritis (randomised, double-blind) |
| [NCT00591201](https://clinicaltrials.gov/study/NCT00591201) | Phase 2/3 | Completed | 26 | Infliximab vs placebo in juvenile spondyloarthropathies |
| [NCT01015547](https://clinicaltrials.gov/study/NCT01015547) | Phase 3 | Completed | 60 | Anti-TNF plus methotrexate vs DMARD combination vs methotrexate alone in very early polyarticular JIA |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients (rheumatoid vasculitis prediction; only tangentially related) |

---

## Literature Evidence

For the rank 1 prediction, currently no related literature is available.

Selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17763439](https://pubmed.ncbi.nlm.nih.gov/17763439/) | 2007 | RCT | Arthritis Rheum | Infliximab plus methotrexate in polyarticular-course juvenile rheumatoid arthritis |
| [20237125](https://pubmed.ncbi.nlm.nih.gov/20237125/) | 2010 | Long-term extension | Ann Rheum Dis | Long-term efficacy and safety of infliximab plus methotrexate in polyarticular JRA |
| [25887212](https://pubmed.ncbi.nlm.nih.gov/25887212/) | 2015 | Cochrane review | Cochrane Database Syst Rev | TNF-alpha inhibitors for ankylosing spondylitis |
| [40621455](https://pubmed.ncbi.nlm.nih.gov/40621455/) | 2025 | Network meta-analysis | Front Immunol | Risk of new-onset and recurrent uveitis with different biologics in ankylosing spondylitis |
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic review | Clin Rheumatol | Biological therapy in rheumatoid vasculitis |
| [40874971](https://pubmed.ncbi.nlm.nih.gov/40874971/) | 2026 | Cohort | Am J Gastroenterol | Subcutaneous infliximab for perianal Crohn's disease (BioLap-Rem) |
| [42488031](https://pubmed.ncbi.nlm.nih.gov/42488031/) | 2026 | Review | Ther Adv Gastroenterol | Subcutaneous infliximab in perianal fistulising Crohn's disease |
| [41622053](https://pubmed.ncbi.nlm.nih.gov/41622053/) | 2026 | Retrospective cohort | Dig Liver Dis | Oesophageal, gastric and duodenal Crohn's disease in the biologic era |
| [11907371](https://pubmed.ncbi.nlm.nih.gov/11907371/) | 2002 | Case report | J Clin Gastroenterol | Infliximab for an oesophagobronchial fistula in oesophageal Crohn's disease |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Review/Mechanistic | Scand J Immunol | Cutaneous vasculitis associated with etanercept and infliximab (safety signal) |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10057H | Inflectra | Powder for I.V. infusion 100 mg | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified in total. The main ones include:
  - **Major:** corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone including ophthalmic), deferiprone, and the radiopharmaceuticals iobenguane (I-131), ibritumomab tiuxetan and tositumomab (I-131).
  - **Moderate:** metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin.
  - **Minor:** zinc salts (sulfate, acetate, gluconate).
- **Class considerations noted in the literature:** serious infection risk, tuberculosis reactivation, infusion-related anaphylaxis with anti-infliximab antibodies, and paradoxical vasculitis.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the rank 1 prediction)

**Rationale:**
- The top-ranked prediction has no trials, no literature and no plausible TNF-driven mechanism, so it is most likely a model artefact. Evidence level is L5.
- Predictions that are credible (perianal Crohn's disease, spondyloarthritis, polyarticular juvenile arthritis and oesophageal Crohn's disease) are largely extensions of existing indications and could be assessed as "Proceed with Guardrails". Rheumatoid vasculitis remains a research question.

**To proceed, the following is needed:**
- Re-prioritise the candidate list towards predictions with clinical evidence rather than score rank alone
- Mechanism of action data for infliximab
- Product Information (PI) warnings and contraindications, and the approved indication text for the Australian ARTG entry
- For perianal Crohn's disease: confirmation of Australian approval status for the fistulising indication and subcutaneous formulation
- For polyarticular juvenile arthritis: verification of paediatric approval status in Australia
- For rheumatoid vasculitis: a dedicated benefit-risk review given reports of anti-TNF-associated vasculitis
- Standard guardrails for any progression: TB and hepatitis B screening and infection monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

