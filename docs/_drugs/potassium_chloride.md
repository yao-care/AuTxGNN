---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
---

# Potassium Chloride
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

# Potassium Chloride: From Electrolyte Replacement to a Possible Role in Renal Tubular Acidosis

## One-Sentence Summary

Potassium chloride (DrugBank DB00761) is an electrolyte agent generally used to correct or prevent potassium deficiency (hypokalaemia); this evidence pack does not contain a documented TGA-approved indication for it, as the product is currently **not marketed in Australia**. The TxGNN model's top prediction for this drug is **Renal Tubular Acidosis (RTA)**, supported by **9 clinical trials** and **19 publications**, though on close review none of the trials test potassium chloride itself, and the mechanistic case only partly holds up.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Electrolyte replacement / management of hypokalaemia (general pharmacological role; no TGA-approved indication text is available in this evidence pack) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Australia Market Status | Not currently marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for potassium chloride in this evidence pack (data gap DG002). Based on known pharmacology, potassium chloride is a simple electrolyte salt used to replace potassium losses; it has no alkalinising or acid-base buffering activity of its own.

Distal renal tubular acidosis (dRTA) — the RTA subtype most represented in the supporting evidence — is frequently accompanied by hypokalaemia because the distal nephron's impaired hydrogen-ion handling drives compensatory urinary potassium loss. Potassium replacement is a recognised part of supportive management in this setting, which is the mechanistic thread TxGNN is likely picking up on.

However, this thread only partially supports potassium **chloride** specifically. Clinical practice in RTA generally favours potassium **citrate** or potassium **bicarbonate**, because the citrate/bicarbonate anion provides the alkalinising effect needed to correct the underlying acidaemia, whereas chloride does not — and administering additional chloride may work against acid-base correction. Potassium chloride alone addresses only the hypokalaemia component of RTA, not the acidosis itself, and would need to be combined with (or substituted by) an alkalinising potassium salt for that reason. This nuance is reflected in the underlying evidence: the one dRTA-specific interventional trial identified (ADV7103) is itself a potassium-citrate/bicarbonate combination product, not potassium chloride.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | Randomised withdrawal study of ADV7103 (a potassium citrate/bicarbonate combination, not KCl) vs placebo in dRTA; terminated after enrolling only 3 subjects. |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Recruiting | 43 | Crossover trial of exogenous ketone bodies (Ketone-IQ) on proteinuria/renal function in polycystic and proteinuric kidney disease; no KCl arm. |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Terminated | 7 | Oral sodium bicarbonate "alkali therapy" in sickle cell disease, assessing effects on bicarbonate and potassium; not a KCl intervention. |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Terminated | 36 | Spironolactone for prevention of electrolyte abnormalities during Amphotericin B therapy; different drug and mechanism. |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Unknown | 40 | Oral sodium bicarbonate to alkalinise serum/urine in paediatric topiramate-induced RTA; not a KCl trial. |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Unknown | 31 | Eplerenone safety study in cyclosporine-treated transplant recipients; unrelated drug class. |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Planned study of potassium **citrate** (not chloride) in children with hypercalciuria/urolithiasis; withdrawn before enrolment, no data generated. |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Not yet recruiting | 130 | SGLT2 inhibitor for acute cardiorenal syndrome; unrelated to KCl or RTA. |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Recruiting | 33 | Methodology study comparing urinary aldosterone measurement days for diagnosing primary aldosteronism; diagnostic, not a treatment trial. |

**None of the 9 identified trials directly investigate potassium chloride as a treatment for RTA.** The closest trial (ADV7103) tests an alkalinising potassium-citrate/bicarbonate product instead, consistent with the mechanistic caveat above.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos españoles de urología | Overview of RTA diagnosis and management, including alkali/potassium replacement as standard supportive therapy. |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Archives of Internal Medicine | Classic review of RTA pathophysiology and diagnostic approach, including electrolyte disturbance patterns. |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocrine Journal | Reclassifies pseudohypoaldosteronism type II as type IV RTA; discusses hyperkalaemic (not hypokalaemic) acidosis phenotype. |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Medica Indonesiana | General approach to hypokalaemia, including renal (RTA-related) causes and replacement principles. |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype correlation of dRTA (SLC4A1/ATP6V0A1/ATP6V1B1 mutations) with hypokalaemia and hypocitraturia. |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | Journal of Clinical Investigation | In classic RTA patients, sustained acidosis correction was achieved with oral potassium **bicarbonate** (not chloride), assessing renal sodium/chloride handling. |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Medical Bulletin (Ann Arbor) | Early general review of RTA. |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | Journal of Nephrology | Case of dRTA with hypokalaemic periodic paralysis during pregnancy. |
| [36081958](https://pubmed.ncbi.nlm.nih.gov/36081958/) | 2022 | Case Report | Cureus | Late-onset hypokalaemic periodic paralysis in an adult with type 2 (proximal) RTA. |
| [28509102](https://pubmed.ncbi.nlm.nih.gov/28509102/) | 2015 | Case Report | CEN Case Reports | Paediatric Sjögren syndrome with distal RTA and hypokalaemia. |

No RCT-level literature was identified; the highest available tier is review/cohort evidence describing RTA-associated hypokalaemia and its management, largely with citrate/bicarbonate potassium salts rather than chloride.

---

## Australia Market Information

Potassium chloride (this DrugBank entry) currently has **no ARTG entries** and is recorded as **not marketed** in Australia in this evidence pack. No product-level information (brand name, dosage form, approved indication) is therefore available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for formal safety information — the `key_warnings`, `contraindications`, and drug-interaction fields for this entry are all data gaps (DG001, Blocking severity), so no formal warnings can be reported here.

One relevant signal did surface elsewhere in this evidence pack and is worth flagging even though it sits outside the formal safety fields: literature retrieved under other TxGNN-predicted "indications" for this drug (dyspepsia, gastroduodenitis, stomach disease) consistently describes potassium chloride — particularly solid oral formulations — as a **cause of pill-induced gastric/GI mucosal injury and ulceration** (e.g. PMID 10022656, 6514589, 6690174, 2857932). This is very likely an adverse-effect association that the knowledge graph has picked up as a false-positive "treatment" signal, not a genuine repurposing opportunity — see note below.

---

## Other TxGNN Signals for This Drug (Lower Priority)

The evidence pack scored 9 additional candidate indications for potassium chloride beyond RTA. None reached a recommendation better than "Hold," and most have no supporting trials or literature at all:

- **HELIX syndrome, Alström syndrome, Senior-Loken syndrome, congenital prothrombin deficiency, NAD(P)HX dehydratase deficiency** — Evidence Level L5, no clinical trials, little to no literature; these appear to be knowledge-graph artefacts with no discernible mechanistic link to potassium chloride.
- **Pendred syndrome** — Evidence Level L4; case-report literature shows SLC26A4 (pendrin) dysfunction can cause hypokalaemia (especially with thiazide co-therapy), giving a plausible but very low-tier mechanistic rationale.
- **Dyspepsia, gastroduodenitis, stomach disease** — Evidence Level L5; the literature for these actually documents potassium chloride **causing** GI mucosal injury, i.e. a likely reverse-causality/adverse-effect confound rather than a treatment signal (see Safety Considerations above).

None of these warrant further work ahead of the RTA signal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The RTA signal has a biologically coherent but incomplete mechanistic basis — hypokalaemia is a recognised feature of RTA, but standard practice corrects it with potassium citrate/bicarbonate rather than chloride, since chloride offers no alkalinising benefit. No clinical trial identified tests potassium chloride itself in RTA, and the evidence base tops out at review/cohort-level literature (L3), so this should be treated as a hypothesis-generating signal rather than a near-term repurposing candidate.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) for this drug — currently a Blocking data gap (DG001), required before any S1 safety assessment.
- Formal mechanism-of-action documentation (DG002) via DrugBank API query, to confirm there is no additional pharmacology beyond simple potassium replacement.
- Clarification of whether the intended clinical use is potassium chloride specifically, or whether potassium citrate/bicarbonate (the salts actually used in RTA management) should be the real candidate — the current signal may be partly an artefact of TxGNN not distinguishing between potassium salts.
- If pursued, since the drug is not currently marketed in Australia (0 ARTG entries), a route-to-market/registration assessment would be needed alongside clinical evidence generation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

