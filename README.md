# Retriva — Antigravity SDD Pack for PoC v0.1.1

This pack bootstraps **Spec-Driven Development (SDD)** for the first implementation of **Retriva**.

## Scope
- Q&A-only chatbot
- local static **`wget` mirror** as the primary tested input
- Python + Streamlit
- OpenAI-compatible chat + embeddings
- dense retrieval only
- grounded answers with citations and explicit fallback

## What changed in this name-corrected pack
The project name is set consistently to **Retriva** in:
- repository-level instructions
- constitution and skills
- workflows
- specs and architecture notes
- Python package path examples (`src/retriva/`)

## Suggested Antigravity flow
1. `/define Finalize specs/001-qa-only-poc using docs/mirror-contract.md.`
2. `/architect Prepare the implementation plan for specs/001-qa-only-poc.`
3. `/execute Implement only the approved tasks in specs/001-qa-only-poc/tasks.md.`
4. `/verify Validate specs/001-qa-only-poc against its acceptance criteria.`

## Setup & Run Instructions (v0.1.1)

1. **Bootstrap local environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Setup environment variables**:
   Create a `.env` file containing `OPENAI_API_KEY=sk-...` and ensure your `MIRROR_BASE_PATH` defaults to your `wget` extraction directory (`./mirror`).
3. **Ingest the mirror**:
   ```bash
   python -m src.retriva.cli ingest
   ```
4. **Boot the Streamlit User Interface**:
   ```bash
   streamlit run src/retriva/ui/streamlit_app.py
   ```

## Smoke Tests Verification (Acceptance Criteria)

Once your UI boots up, you can verify the functional ACs using the following targeted prompts:

- **English Test** (AC3 & AC5): *"What is the main topic of the mirrored website?"* -> System must answer in English and provide the underlying context block locally.
- **Italian Test** (AC6): *"Qual è l'argomento principale di questo sito?"* -> System must answer exclusively in Italian and link citations gracefully.
- **Fallback Test** (AC4): *"What is the airspeed velocity of an unladen swallow?"* -> System must cleanly issue the exact explicit fallback instruction: *"I do not have sufficient evidence in my knowledge base to answer this question."*
