# Example feature spec: Export my tasks

**Status:** Draft — review before implementation.

## Problem and outcome
Users need a portable copy of their own tasks for offline analysis. Success means an authenticated user can download a CSV containing only tasks they are authorized to see.

## In scope
- Export initiated from the user's task list.
- UTF-8 CSV with header `id,title,status,created_at` in that order.
- Standard CSV quoting for commas, quotes and newlines.
- Only tasks belonging to the authenticated user.
- Empty list produces header-only CSV.
- Filename `tasks.csv`; no hidden personal information or secrets.

## Out of scope
Scheduled exports, Excel-specific formats, imports, and shared-team tasks.

## Acceptance criteria
1. **Given** an authenticated user with two tasks, **when** export is selected, **then** a CSV is downloaded containing the header and exactly those two records.
2. **Given** a task title containing a comma, quote or newline, **when** exported, **then** CSV escaping preserves the original value.
3. **Given** an empty task list, **when** exported, **then** the file contains only the header.
4. **Given** a request without authentication, **when** export is requested, **then** access is denied without disclosing tasks.
5. **Given** another user's tasks, **when** exporting, **then** none of those tasks appear.

## Constraints
- Enforce authorization server-side, not only by hiding UI controls.
- Avoid spreadsheet formula injection when exported CSV may be opened in spreadsheet software; define and test a safe escaping policy.
- Meet application accessibility and error-reporting conventions.
- Do not log exported task content.

## Questions for product/security review
- Maximum export size and performance target?
- Expected ordering and timestamp timezone?
- Policy for potentially dangerous spreadsheet formula prefixes?
- How should network failures appear to users?

## Suggested agent tasks
1. Inspect current authorization and task storage behavior.
2. Resolve the open questions with the human reviewer.
3. Implement server-side export and CSV serialization.
4. Add authorization, empty-list, quoting, injection and error tests.
5. Verify acceptance criteria and review diff with a human.

## Evidence checklist
- [ ] All five acceptance criteria mapped to checks
- [ ] Authorization verified independently
- [ ] CSV edge cases tested
- [ ] Accessibility and errors checked
- [ ] Diff and test results reviewed
