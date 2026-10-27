---
layout: default
title: Chloramphenicol
parent: Moderate Evidence (L3-L4)
nav_order: 152
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Chloramphenicol: predicted new indication Conjunctivitis (evidence level L3). Approved use: Typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Chloramphenicol"
predicted_indications: ["conjunctivitis", "diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis", "chronic rhinosinusitis"]
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Chloramphenicol: From Systemic Bacterial Infections to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is a broad-spectrum antibiotic, originally used for infections such as typhoid fever, meningococcal infection and rickettsial diseases.
The TxGNN model predicts it may be effective for **conjunctivitis**, supported by **no registered clinical trials** but **20 publications**, mostly reviews, commentaries and small comparative studies.
This is better described as an extension of its existing anti-infective use than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, paratyphoid fever, meningococcal infection, streptococcal meningitis, rickettsial diseases and others (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Chloramphenicol is a well-known bacteriostatic antibiotic that inhibits the bacterial 50S ribosomal subunit, and its efficacy against a range of bacterial infections is established. Mechanistically, this is directly relevant to bacterial conjunctivitis.

The original indications (typhoid fever, meningitis, skin and ear infections) are all bacterial infections, and conjunctivitis of bacterial origin is a natural extension. Topical chloramphenicol is already used routinely for conjunctivitis in several countries, including the UK, and an eye-drop product is already marketed in Australia (Chlorsig). The prediction is therefore plausible, but it largely reflects existing practice rather than a new therapeutic direction.

Other predicted indications (diffuse scleroderma, post-infectious conditions, Chagas cardiomyopathy, and others) have little or no supporting evidence. The scleroderma signal is probably an artefact, as chloramphenicol acetyltransferase is commonly used as a reporter gene in laboratory studies of the fibroblast gene regulation described in the literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for conjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Cochrane systematic review | Cochrane Database Syst Rev | Interventions for preventing ophthalmia neonatorum (neonatal conjunctivitis) |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative clinical study | Curr Ther Res | Moxifloxacin compared with chloramphenicol for bacterial eye infections |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | Randomised, single-blind comparison | Acta Ophthalmol | Fusidic acid vs chloramphenicol eye drops in acute purulent conjunctivitis: clinical success 84% vs 81%; more stinging and discomfort with chloramphenicol (14% vs 5%) |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | Open, randomised comparison | Acta Ophthalmol | In Tanzania, clinical success was 93% with fusidic acid, 48% with chloramphenicol and 74% with framycetin, linked to in vitro resistance differences |
| [1448311](https://pubmed.ncbi.nlm.nih.gov/1448311/) | 1992 | Comparative clinical study | Pediatr Infect Dis J | Oral rifampin vs topical chloramphenicol for eradicating conjunctival carriage of *H. influenzae* biogroup aegyptius (Brazilian purpuric fever) |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Review (safety) | Drug Saf | Debated link between ocular chloramphenicol and aplastic anaemia |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | Comparative review of 16 topical ophthalmic antibacterial preparations |
| [7498557](https://pubmed.ncbi.nlm.nih.gov/7498557/) | 1995 | Commentary | Eye (Lond) | Topical chloramphenicol: use or abuse? |
| [25833086](https://pubmed.ncbi.nlm.nih.gov/25833086/) | 2015 | Commentary | Clin Exp Ophthalmol | Over-the-counter chloramphenicol |
| [7153511](https://pubmed.ncbi.nlm.nih.gov/7153511/) | 1982 | Clinical/laboratory study | J Hyg | Chloramphenicol drops delayed and reduced signs of chlamydial neonatal conjunctivitis, but 85% of treated infants remained culture-positive |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11112W | Chlorsig | Eye drops 5 mg per mL, 10 mL | Not available in the data compiled for this report |

Only an ophthalmic formulation is registered, which fits the predicted conjunctivitis indication.

---

## Safety Considerations

- **Contraindications and warnings (from the knowledge graph, not label text):** The knowledge graph links chloramphenicol with caution in kidney disease, liver disease, gallbladder disease, peripheral neuropathy, optic neuritis, acute intermittent porphyria and paroxysmal nocturnal haemoglobinuria. It also flags blood disorders, including aplastic anaemia, anaemia, thrombocytopenia, agranulocytosis and neutropenia (including congenital forms).
- **Haematological concern:** The literature debates a possible link between topical ocular chloramphenicol and aplastic anaemia. This is a key reason for guardrails.
- **Drug interactions (DDInter; 100 recorded in total, examples below):**
  - Major: cisapride, naloxegol
  - Moderate: sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide), repaglinide, saxagliptin, simvastatin, rosuvastatin, metronidazole, budesonide, aprepitant, iron, eliglustat, nitisinone, naldemedine, balsalazide

  These interactions mainly concern systemic exposure and are likely of limited relevance to eye drops, but they matter if systemic use were considered.

For label-based warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Topical chloramphenicol for bacterial conjunctivitis is supported by several comparative studies, reviews and established clinical practice, and an ophthalmic product is already marketed in Australia. The evidence is mostly older or low-tier (L3), no trials are registered, and the haematological safety debate requires caution. The other predicted indications remain at Hold (L4–L5).

**To proceed, the following is needed:**
- Review of the TGA-approved PI for Chlorsig, including approved indications, warnings and contraindications
- Mechanism of action data from DrugBank for completeness
- Comparison with current Australian guidance on topical antibiotics for conjunctivitis, including resistance patterns
- A safety plan covering patients with prior blood disorders or bone marrow suppression, and limits on duration of use
- Updated comparative evidence, as most of the supporting studies are decades old
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

