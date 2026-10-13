---
layout: default
title: Amphotericin B
parent: Moderate Evidence (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 10
---

# Amphotericin B
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Amphotericin B: From Fungal and Bacterial Infections to Paranasal Sinus Neoplasm

## One-Sentence Summary

Amphotericin B is a polyene antifungal, originally used for candidiasis and other fungal infections.
The TxGNN model's top-ranked prediction is **paranasal sinus neoplasm**, but the evidence does not support it: there are **0 clinical trials** and **8 publications**, all describing invasive fungal sinus infections in patients with cancer or immunosuppression, not tumour treatment.
The best-supported prediction in this set is **chronic rhinosinusitis** (1 Phase 3 RCT, multiple meta-analyses), but results are largely negative or inconsistent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Candidiasis (cutaneous, oral, oesophageal) and other infections (from the knowledge graph; the Australian licence record has no indication text) |
| Predicted New Indication | Paranasal sinus neoplasm |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amphotericin B is a polyene antifungal, and its efficacy in invasive fungal infections is well established.

For **paranasal sinus neoplasm**, there is no anti-neoplastic mechanism. The retrieved literature concerns mucormycosis and aspergillosis of the sinuses in patients with cancer or immunosuppression, where amphotericin B is used as an antifungal. The high score likely reflects an association between sinus disease and fungal infection, not a treatment effect on tumours.

Other predictions follow a similar pattern. Several (bacterial pneumonia, meningococcal infection, bacterial arthritis) appear to be ontology artefacts, because amphotericin B has no antibacterial activity. Pneumocystosis is also unlikely, as Pneumocystis lacks ergosterol in its membrane.

The most plausible alternative is **chronic rhinosinusitis**. The hypothesis is that an exaggerated immune response to fungi drives the disease, so topical amphotericin B might help. Trial results, however, have been largely negative.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication, paranasal sinus neoplasm. Currently no related clinical trials registered.

For context, the most relevant trial across the other predictions (chronic rhinosinusitis, rank 2) is:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00425620](https://clinicaltrials.gov/study/NCT00425620) | Phase 3 | Completed | 300 | Randomised, double-blind, placebo-controlled study of intranasal amphotericin B in refractory postsurgical chronic sinusitis; the primary outcome was complete resolution of key symptoms over 16 weeks. Outcomes should be verified, as the published RCT literature is mostly null. |

## Literature Evidence

The table below covers the top-ranked indication, paranasal sinus neoplasm.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31181136](https://pubmed.ncbi.nlm.nih.gov/31181136/) | 2019 | Systematic Review | J Pediatric Infect Dis Soc | 10-year review of paediatric mucormycosis cases (clinical features, management, outcomes) |
| [27832748](https://pubmed.ncbi.nlm.nih.gov/27832748/) | 2016 | Cohort (epidemiologic) | BMC Infect Dis | Registry-based study of invasive mucormycosis in children |
| [30338581](https://pubmed.ncbi.nlm.nih.gov/30338581/) | 2019 | Cohort (retrospective) | Mycoses | Invasive mucormycosis in children with cancer (Italian network) |
| [12229280](https://pubmed.ncbi.nlm.nih.gov/12229280/) | 2002 | Case series | Invest Clin | Three mucormycosis cases, including rhinocerebral disease in diabetes |
| [12218600](https://pubmed.ncbi.nlm.nih.gov/12218600/) | 2002 | Case report | J Pediatr Hematol Oncol | Long-term survival of rhinocerebral mucormycosis in a boy with relapsed leukaemia on systemic antifungals |
| [10595472](https://pubmed.ncbi.nlm.nih.gov/10595472/) | 1999 | Case report | Clin Nucl Med | Ga-67 SPECT monitoring of invasive sphenoid sinus aspergillosis |
| [10340559](https://pubmed.ncbi.nlm.nih.gov/10340559/) | 1999 | Case report | Surv Ophthalmol | Orbital apex syndrome in a lung cancer patient on chemoradiation |
| [8567925](https://pubmed.ncbi.nlm.nih.gov/8567925/) | 1995 | Case report | J Clin Microbiol | Cutaneous Alternaria infection in an immunosuppressed patient with neoplastic disease; in vitro amphotericin B activity |

None of these studies shows tumour treatment benefit; all concern fungal infections.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2931G | Fungilin | Lozenge 10 mg | Not recorded in the data compiled for this report |

Only an oral lozenge is registered. Topical, nasal or intravenous formulations were not identified, so route compatibility with any predicted indication has not been established.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not label text): kidney disease, pyoureter, liver disease, gallbladder disease, potassium deficiency, *Clostridium difficile* colitis, perinatal necrotising enterocolitis.
- **Drug interactions:** 100 interactions were identified. Those classed as **Major** include foscarnet, gallium nitrate, amiodarone and arsenic trioxide. Moderate interactions include zidovudine, acetazolamide, hydrocortisone, furosemide, hydrochlorothiazide, ganciclovir and amikacin. Corticosteroids and diuretics are of particular note, given the risk of hypokalaemia.

Please also refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (paranasal sinus neoplasm) has no mechanistic basis and no clinical trials. The supporting literature concerns fungal infections, not tumour treatment. The model score appears to reflect a disease association rather than therapeutic benefit.
- The best-evidenced alternative, chronic rhinosinusitis, has a Phase 3 RCT and meta-analyses, but results are largely negative or inconsistent. It is better treated as a research question than a repurposing candidate.

**To proceed, the following is needed:**
- Mechanism of action data
- For chronic rhinosinusitis: review of the NCT00425620 results and subgroup studies (e.g. nasal polyps, allergic fungal rhinosinusitis)
- Confirmation of an appropriate formulation and route, since only an oral lozenge is registered in Australia
- Product Information review for warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

