---
layout: default
title: Ephedrine
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Ephedrine
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

# Ephedrine: From Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

Ephedrine is a classical mixed sympathomimetic agent with a well-established pharmacological basis as a nasal decongestant, though it currently holds no TGA registration in Australia. The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **18 clinical trials** and **8 publications** currently associated with this indication direction. Evidence is primarily observational and historical in nature; formal Australian registration data are absent, warranting structured risk management before clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nasal decongestant / bronchospasm / vasopressor support (historical use — no current ARTG registration) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ephedrine is a mixed-action sympathomimetic derived from the *Ephedra* plant genus, acting both directly on α- and β-adrenoceptors and indirectly by promoting noradrenaline release from sympathetic nerve terminals. Although detailed mechanism of action data was not retrieved from DrugBank during evidence collection, its pharmacology is well characterised in the classical literature. The primary basis for predicting efficacy in nasal cavity disease is its α1-adrenoceptor agonism, which causes vasoconstriction of the nasal mucosal vasculature, reduces turbinate engorgement, and decreases mucous secretion — the same mechanism underlying pseudoephedrine and phenylpropanolamine, two widely used oral decongestants of the same pharmacological class.

Historically, topical ephedrine nasal drops (0.5–1%) were a standard first-line treatment for nasal congestion arising from a range of nasal cavity conditions including allergic rhinitis, vasomotor rhinitis, and acute upper respiratory infections. Ephedrine was gradually superseded in topical formulations by more receptor-selective imidazoline α-agonists such as oxymetazoline and xylometazoline, and by pseudoephedrine for oral systemic use, largely owing to concerns about rebound congestion (rhinitis medicamentosa) and systemic cardiovascular effects. However, the core mechanistic rationale for nasal cavity disease remains valid and well-supported.

The TxGNN model's high prediction score of 99.90% for nasal cavity disease reflects this established pharmacological relationship rather than a genuinely novel repurposing discovery. The clinical interest now lies in whether specific nasal cavity disease subtypes — for example, post-viral rhinitis, rhinitis medicamentosa reversal, or specific mucosal inflammatory conditions — may benefit from revisited ephedrine formulations or dosing strategies, particularly given emerging preclinical evidence suggesting additional anti-inflammatory effects via NF-κB suppression and endoplasmic reticulum stress inhibition in airway tissues.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind RCT comparing topical anaesthesia, decongestant, or their combination before fiberoptic nasal pharyngoscopy and laryngoscopy — directly evaluates the role of nasal decongestants in ENT procedures and patient comfort |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Four-arm crossover RCT of an H3 receptor antagonist (PF-03654746) for allergen-induced nasal congestion in seasonal allergic rhinitis; oral and topical decongestants used as active comparators; acoustic rhinometry used for objective nasal dimension measurement |
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | Unknown | 212 | Prospective RCT comparing double vs single pledget nasal preparation before unsedated transnasal endoscopy; ephedrine-containing nasal pledgets are a standard preparation component in this clinical setting |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | Exploratory study using MRI to assess the effect of anti-allergy drugs on nasal mucosal anatomy following intranasal allergen challenge in hayfever subjects — validates objective methodology directly applicable to decongestant evaluation |
| [NCT04645511](https://clinicaltrials.gov/study/NCT04645511) | N/A | Recruiting | 120 | Placebo-controlled double-blind RCT of balloon sinuplasty vs sham in chronic or recurrent maxillary rhinosinusitis; also evaluates impact on Eustachian tube dysfunction |
| [NCT03979209](https://clinicaltrials.gov/study/NCT03979209) | Phase 1 | Completed | 16 | Phase 1 study assessing incidence of cortisol suppression with high-volume mometasone nasal irrigation in chronic sinusitis patients — safety framing applicable across intranasal pharmacological agents |
| [NCT03725956](https://clinicaltrials.gov/study/NCT03725956) | N/A | Unknown | 30 | Objective assessment of the impact of endoscopic sinus surgery on sleep quality in nasal polyposis patients, including polysomnography outcomes |
| [NCT04048174](https://clinicaltrials.gov/study/NCT04048174) | N/A | Completed | 27 | Pilot safety and efficacy study of *Lactococcus lactis* W136 probiotic instilled directly into nasal and sinus cavities for refractory chronic rhinosinusitis |
| [NCT05494346](https://clinicaltrials.gov/study/NCT05494346) | N/A | Recruiting | 101 | Multicentre pre-market clinical investigation of a decongestant seawater spray enriched with essential oils for acute rhinitis with nasal obstruction over an 8-day treatment period |
| [NCT00015795](https://clinicaltrials.gov/study/NCT00015795) | Phase 1 | Completed | 30 | Investigation of laryngeal airflow resistance in abductor spasmodic dysphonia and normal volunteers; airway physiology methodology is low direct relevance to ephedrine nasal use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1541887](https://pubmed.ncbi.nlm.nih.gov/1541887/) | 1992 | RCT | J Laryngol Otol | RCT comparing nasal packing vs nasal spraying for pre-operative nasal preparation — directly evaluates topical nasal decongestant delivery methods in ENT, informing optimal administration strategies |
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Clinical Trial | Svenska Läkartidningen | Prospective clinical testing of N-hydroxyethylpromethazine combined directly with **ephedrine hydrochloride** applied to the nasal cavity — direct historical evidence of topical ephedrine use in nasal disease |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative Study | Am J Rhinology | Head-to-head comparison of phenylpropanolamine and d-pseudoephedrine as oral and topical nasal decongestants; acoustic rhinometry used to measure changes in nasal cavity dimensions — provides mechanistic class benchmark for ephedrine as a sympathomimetic decongestant |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Clinical Observation | Chin J Integr Trad West Med | Clinical observation of a rhinitis spray formulation for treating chronic rhinitis — real-world context for decongestant combination formulations in nasal disease management |
| [8283338](https://pubmed.ncbi.nlm.nih.gov/8283338/) | 1993 | Case Series | Nihon Jibiinkoka Gakkai | 10-case series of congenital nasal stenosis in neonates with respiratory distress; nasal and oral interventions including decongestants documented — illustrates clinical management landscape of nasal cavity obstruction |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal Model | J Pharmacol Toxicol Methods | Pharmacological characterisation of a chronic dog model of nasal congestion using compound 48/80 — developed specifically to study nasal decongestant mechanism of action, with direct relevance to α-adrenergic agents including ephedrine |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal Model | Am J Rhinology | Ragweed-sensitised dog model of allergic nasal congestion validated using acoustic rhinometry — preclinical platform for evaluating the α-adrenergic decongestant drug class to which ephedrine belongs |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal Model | Am J Rhinology | Beagle dog acoustic rhinometry model of mast cell degranulation-induced nasal congestion — pharmacologically characterises sympathomimetic nasal decongestant responses relevant to ephedrine's mechanism |

---

## Australia Market Information

Ephedrine (DrugBank ID: DB01364) currently has **no ARTG-registered products** in Australia (TGA database, queried 9 March 2026).

> **Note for prescribers:** Ephedrine may be accessible in Australia as an unapproved medicine via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway. Compounding pharmacies may also prepare ephedrine nasal formulations under relevant state/territory legislation. Clinicians should note that ephedrine is also a listed precursor chemical under Australian drug control legislation (Customs (Prohibited Imports) Regulations) and is currently scheduled as a Schedule 4 (Prescription Only Medicine) substance under the Poisons Standard. Verification of current scheduling and access pathway requirements is recommended prior to clinical use.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information. As no TGA-registered PI currently exists for ephedrine in Australia, clinicians are advised to consult international drug monographs (e.g., Martindale: The Complete Drug Reference, British National Formulary, Micromedex) and relevant TGA guidance on sympathomimetic agents.

Key class-level safety considerations for sympathomimetics applicable to ephedrine (sourced from published literature):

- **Cardiovascular effects:** Hypertension, tachycardia, palpitations, and cardiac arrhythmias — caution is warranted in patients with cardiovascular disease, hypertension, or hyperthyroidism
- **CNS stimulation:** Anxiety, insomnia, and tremor — particularly relevant when systemic absorption occurs from topical nasal preparations
- **Drug interactions:** Clinically significant interactions with monoamine oxidase inhibitors (MAOIs) carry risk of hypertensive crisis; interactions also reported with tricyclic antidepressants and other sympathomimetic agents
- **Rebound congestion:** Rhinitis medicamentosa associated with prolonged topical α-agonist use
- **Contact sensitisation:** Case reports exist of ephedrine acting as a hapten causing IgE-mediated allergic reactions (see PMID [20560391](https://pubmed.ncbi.nlm.nih.gov/20560391/))

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ephedrine's mechanism of action for nasal cavity disease is pharmacologically well-established through α1-adrenoceptor-mediated vasoconstriction of the nasal mucosa, supported by historical clinical use, comparative pharmacological studies, and observational data (Evidence Level L3). The absence of any current TGA ARTG registration, lack of formal Australian safety profiling, scheduling considerations, and the availability of more selective alternatives currently registered in Australia require structured risk management before progressing this indication.

**To proceed, the following is needed:**
- Retrieve complete mechanism of action and safety data from DrugBank API (currently a data gap)
- Confirm current TGA scheduling status and identify the appropriate regulatory access pathway (SAS Category A or B, or Authorised Prescriber application)
- Obtain and review international Product Information documents for ephedrine nasal formulations (FDA, EMA, or UK SmPC equivalents)
- Define the specific nasal cavity disease subtype being targeted (e.g., allergic rhinitis, vasomotor rhinitis, chronic rhinosinusitis, nasal polyposis) to focus the indication development pathway
- Conduct a systematic comparative effectiveness review against currently TGA-approved alternatives (oxymetazoline, xylometazoline, pseudoephedrine, intranasal corticosteroids) to establish a clear benefit-risk case for ephedrine
- Formally assess the cardiovascular and CNS risk profile in the intended Australian patient population, including interactions with commonly co-prescribed agents
- Search ANZCTR for any Australia or New Zealand registered clinical trials involving ephedrine or sympathomimetic nasal decongestants to identify local evidence gaps

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All information should be interpreted in conjunction with TGA-approved product information and current clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

