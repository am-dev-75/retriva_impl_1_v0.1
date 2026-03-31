# Task Checklist — 001 Q&A-only PoC

## A. Bootstrap
- [ ] Create Python project structure
- [ ] Add config/settings module
- [ ] Define domain models and interfaces

## B. Ingestion
- [ ] Implement filesystem discovery for a `wget`-style mirror
- [ ] Implement content extraction for main HTML body (handling explicit selectors and removing boilerplate)
- [ ] Implement normalization / cleanup helpers
- [ ] Implement section-aware chunking with required metadata
- [ ] Implement canonical document id rules
- [ ] Add parser and chunker tests (verifying canonicalization rules)
- [ ] Add a small `wget`-mirror fixture for tests

## C. Indexing
- [ ] Implement OpenAI-compatible embeddings client
- [ ] Implement Qdrant adapter
- [ ] Implement ingest CLI command
- [ ] Implement reindex CLI command

## D. QA core
- [ ] Implement retriever
- [ ] Implement prompt builder with citation metadata
- [ ] Implement chat client adapter
- [ ] Implement grounded fallback behavior
- [ ] Add QA/fallback tests

## E. UI
- [ ] Build Streamlit chat UI
- [ ] Render citations clearly
- [ ] Add retrieval debug panel
- [ ] Ensure EN / IT interactions behave correctly

## F. Verification
- [ ] Document local setup and run commands
- [ ] Add smoke test instructions/command
- [ ] Validate all acceptance scenarios
