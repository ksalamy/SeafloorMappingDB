# Issue #293 Revert Investigation Plan

## Current state

Branch `fix/issue-293-revert-investigate` is at **a6399dc** (pre-#293 code).

## Known breakage (in #293)

**Label placement on zoom out** – Labels become evenly spaced / nowhere near nav_track. **Root cause: #293 styling** (iconSize/iconAnchor + #293 CSS). Test A proved: #293 placement + pre-#293 styling works. Test B proved: pre-#293 placement + #293 styling breaks. **Fix:** Keep Test A (commit d2bae69).

## Must-keep (non-negotiable)

**Bidirectional hover styling** – Track ↔ label ↔ table row. When the user hovers any of these, all three highlight together (`.smdb-hover`). This must be preserved when re-applying #293.

## #293 commits (in order, for re-apply)

| Order | Commit   | Description |
|-------|----------|-------------|
| 1     | 4521eda  | Bidirectional hover link between nav tracks and mission names |
| 2     | ec0175c  | Include mission labels in hover link; offset labels beside track |
| 3     | ac64b74  | Missions map: label placement and styling |
| 4     | 0d9ba69  | tests: remove failing measure tests, fix flaky nav-track hover wait |
| 5     | aa2f483  | Plain labels by default, hover-only styling; 500/2000 per_page; scroll row into view |

## Workflow

### Phase 1: Find the issue

1. **Verify baseline** – Run tests, use Missions page. Confirm whether the bug exists at this pre-#293 state.
2. **If bug exists here** – It predates #293; fix it on this branch, then re-apply #293.
3. **If bug does NOT exist here** – It was introduced by #293; re-apply commits one by one until it appears.

### Phase 2: Fix the bug

- Fix the bug on this branch (with or without #293 code, depending on Phase 1).
- Commit the fix.

### Phase 3: Re-apply #293 (if reverted)

Cherry-pick in order, testing after each:

```bash
git cherry-pick 4521eda
# Test; if OK, continue
git cherry-pick ec0175c
# Test
git cherry-pick ac64b74
# Test
git cherry-pick 0d9ba69
# Test
git cherry-pick aa2f483
# Test
```

If a cherry-pick introduces the bug, either:
- Fix it in that commit (amend or fix-up), or
- Skip that commit and re-implement the desired behavior differently.

### Phase 4: Merge

- Open PR from `fix/issue-293-revert-investigate` into `develop`.
- After merge, `feature/issue-293-track-name-hover-link` can be updated or retired.

## Stash to restore later

```
stash@{0}: WIP before issue-293 revert investigation: .gitignore, local.py, mission_filter.html (?v=293)
```

Restore with: `git stash pop`
