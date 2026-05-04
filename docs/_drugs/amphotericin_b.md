---
layout: default
title: Amphotericin B
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Amphotericin B
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

# Amphotericin B: From Systemic Fungal Infections to Paranasal Sinus Neoplasm

## One-Sentence Summary

Amphotericin B is a well-established polyene antifungal agent used as a cornerstone treatment for serious and life-threatening fungal infections, including invasive aspergillosis, candidiasis, and mucormycosis.
The TxGNN model predicts it may have relevance for **Paranasal Sinus Neoplasm** with a score of 97.45%, however **0 clinical trials** and **12 publications** have been identified — none of which directly investigate Amphotericin B as a treatment for paranasal sinus tumours.
The available evidence strongly suggests this is a knowledge graph topology artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious systemic fungal infections (invasive aspergillosis, candidiasis, mucormycosis and related) |
| Predicted New Indication | Paranasal Sinus Neoplasm |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amphotericin B is a polyene macrolide antifungal that acts by binding to ergosterol — a sterol found specifically in fungal cell membranes but absent in mammalian cells (which contain cholesterol). This binding creates pores in the fungal membrane, leading to leakage of cellular contents and fungal cell death. Ergosterol-targeting is the basis of its broad-spectrum antifungal activity against Candida, Aspergillus, Mucor, Cryptococcus, and related organisms. Importantly, **Amphotericin B has no known antitumour mechanism of action**.

The high TxGNN score (97.45%) for paranasal sinus neoplasm does not reflect genuine mechanistic plausibility. It is most likely an artefact of anatomical co-location within the knowledge graph: Amphotericin B has well-documented associations with rhinocerebral and paranasal sinus fungal infections (particularly mucormycosis and invasive aspergillosis). In the knowledge graph, the drug–disease node for "paranasal sinus fungal infection" sits in close proximity to "paranasal sinus neoplasm," causing score propagation — a phenomenon known as **false positive propagation**. The two disease entities share anatomical location but differ fundamentally in aetiology, pathophysiology, and therapeutic approach.

All 12 retrieved publications are case reports, retrospective cohort studies, or systematic reviews of rhinocerebral mucormycosis or invasive fungal sinusitis. Not a single study examines Amphotericin B as a treatment for — or in any direct relationship to — paranasal sinus tumours. A biological rationale for this repurposing direction is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> **Important context:** All publications below concern fungal infections of the paranasal sinuses (primarily rhinocerebral mucormycosis and aspergillosis), **not** paranasal sinus neoplasm. Their retrieval reflects the knowledge graph overlap described above.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31181136](https://pubmed.ncbi.nlm.nih.gov/31181136/) | 2019 | Systematic Review | J Pediatric Infect Dis Soc | Systematic review of paediatric mucormycosis (2008–2017); Amphotericin B identified as cornerstone therapy; survival improving with combined antifungal and surgical management |
| [30338581](https://pubmed.ncbi.nlm.nih.gov/30338581/) | 2019 | Retrospective Cohort | Mycoses | Invasive mucormycosis in paediatric oncology patients; Amphotericin B-based regimens used; mortality remains 22–59% despite treatment |
| [27832748](https://pubmed.ncbi.nlm.nih.gov/27832748/) | 2016 | Retrospective Cohort | BMC Infect Dis | Registry-based study of paediatric mucormycosis across European and non-European centres; AmB central to treatment protocols |
| [23058177](https://pubmed.ncbi.nlm.nih.gov/23058177/) | 2013 | Review | J Cranio-Maxillofac Surg | Surgical management of rhinocerebral mucormycosis in immunocompromised patients; AmB combined with aggressive debridement |
| [12229280](https://pubmed.ncbi.nlm.nih.gov/12229280/) | 2002 | Case Series | Investigacion Clinica | Three cases of mucormycosis (predominantly diabetic patients); rhinocerebral form with paranasal sinus involvement treated with AmB |
| [12218600](https://pubmed.ncbi.nlm.nih.gov/12218600/) | 2002 | Case Report | J Pediatr Hematol Oncol | Long-term survival of a child with rhinocerebral mucormycosis during ALL relapse; sustained systemic AmB therapy achieved chronic disease course |
| [2195371](https://pubmed.ncbi.nlm.nih.gov/2195371/) | 1990 | Case Report/Review | Neuro-Chirurgie | Aspergillus granuloma simulating meningioma; associated paranasal sinus fungal infection; AmB therapy discussed alongside surgical biopsy |
| [7689184](https://pubmed.ncbi.nlm.nih.gov/7689184/) | 1993 | Case Report | Neurol Med Chir | Rhinocerebral mucormycosis in a 74-year-old diabetic male with orbital apex mass extending into paranasal sinuses and cavernous sinus |
| [10340559](https://pubmed.ncbi.nlm.nih.gov/10340559/) | 1999 | Case Report | Surv Ophthalmol | Lung cancer patient on chemoradiation developed orbital apex fungal infection without paranasal sinus disease; AmB used for fungal component |
| [1057138](https://pubmed.ncbi.nlm.nih.gov/1057138/) | 1975 | Case Report | Oral Surg Oral Med | Early description of rhinocerebral mucormycosis with oral findings; AmB treatment outlined; high morbidity and mortality noted |

---

## Australia Market Information

Amphotericin B is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no approved products listed in Australia as of the data cut-off date (5 April 2026).

Clinicians in Australia requiring access to Amphotericin B (including lipid formulations such as liposomal Amphotericin B, AmBisome®) for seriously ill patients may need to apply through the **TGA Special Access Scheme (SAS Category B or C)** or via the **Authorised Prescriber** pathway for unapproved therapeutic goods.

---

## Safety Considerations

As Amphotericin B is not registered in Australia and formal safety data (warnings, contraindications, and drug interaction records) were not available in this evidence pack, please refer to:

- International prescribing information (e.g., the FDA-approved label or EMA SmPC for AmBisome® or Fungizone®)
- Published clinical guidelines, such as the ESCMID antifungal guidelines or the Infectious Diseases Society of America (IDSA) guidelines
- The TGA Special Access Scheme documentation applicable to the specific formulation being considered

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN score (97.45%), this prediction has no mechanistic basis — Amphotericin B targets fungal ergosterol and has no known antitumour activity. All 12 retrieved publications concern rhinocerebral mucormycosis or invasive fungal sinusitis, and none relate to paranasal sinus tumour treatment. This is a classic knowledge graph false positive arising from anatomical co-location of "fungal sinusitis" and "paranasal sinus neoplasm" nodes.

**To reconsider this indication, the following would be needed:**

- Preclinical evidence (in vitro or animal model) demonstrating any direct or indirect effect of Amphotericin B on paranasal sinus tumour cell lines or tumour biology
- A plausible mechanistic hypothesis beyond antifungal activity (e.g., immunomodulatory, toll-like receptor stimulation, or anti-angiogenic effects that have been proposed for polyene compounds in some early research)
- Clarification of whether the TxGNN disease label "paranasal sinus neoplasm" may be mapping to "paranasal sinus fungal disease" in the underlying knowledge graph, and correction of this ontology mapping error
- TGA Special Access Scheme assessment for any Australian clinical use context

---

*This report is produced for research reference only and does not constitute medical advice. Drug repurposing candidates identified by computational models require independent clinical validation prior to any patient application. All content should be interpreted in conjunction with current clinical guidelines and specialist judgement.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

