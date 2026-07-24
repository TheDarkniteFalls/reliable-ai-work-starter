# Reliable AI Work Starter

<!-- toolkit-trust-card:start -->
> **Public contract:** Experimental starter · about 10 min · No code; Python optional · no model · no network
>
> **Operation:** Edits three named local files after approval
>
> **A pass establishes:** The declared starter files, setup boundary, template links, and public-safety text pass deterministic structural checks.
>
> **It does not establish:** The starter does not run an agent, enforce permissions, inspect sources, or prove that a live workflow is useful.
>
> **First check:** `python3 -B check_starter.py`
<!-- toolkit-trust-card:end -->

A private-by-default, file-based starting point for one useful AI-assisted
workflow.

This repository is for people who want Codex or a similar file-and-tool agent
to help with recurring work without first building an app, granting broad
connector access, or moving important decisions into chat history.

## Create Your Copy

[Create a private repository from this starter](https://github.com/new?template_owner=TheDarkniteFalls&template_name=reliable-ai-work-starter&visibility=private),
then open the new repository in Codex.

If you prefer a local folder, use GitHub's **Code → Download ZIP** action and
extract it somewhere private. Keep real source material in your own copy, not
in a public issue or pull request.

## Start In One Prompt

Paste this into a fresh Codex session opened in your copied starter:

```text
Help me personalize this minimum assistant workspace.

Do not add an app, database, automation, broad connector access, or new daily
interface. Ask me no more than three questions:
1. What recurring job should this workspace improve first?
2. Which sources should it trust for that job?
3. What must it never do without asking me?

Then update only WORKING_AGREEMENT.md, TODAY.md, and SOURCE_SHELF.md. Keep the
files short. Explain the first workflow, its visible proof, what remains
unconfigured, and one exact prompt I can use to run it. Do not take any
external action.
```

## What The Files Do

- `WORKING_AGREEMENT.md` defines purpose, sources, authority, output rules, and
  completion proof.
- `TODAY.md` holds current focus, next moves, blockers, waiting items, and
  outputs needing review.
- `SOURCE_SHELF.md` records what each source is authoritative for, its date,
  limitations, and review timing.
- `REVIEW_LOG.md` records what happened to material outputs and what was
  learned.
- `context/` holds small source-backed notes with visible confidence states.
- `outputs/` holds reusable results outside chat.

Do not fill these files with every fact, task, or conversation. Preserve only
the minimum state that helps a later session do better work.

## First-Use Test

Before adding more machinery:

1. Use a fresh session that can see only this workspace and sources you
   deliberately add.
2. Run one bounded workflow through to a saved output.
3. Confirm that the result names its sources, uncertainty, validation, next
   action, and owner.
4. Record whether the result was used, edited, rejected, or superseded.
5. Stop if the workflow needs hidden state, broad access, an unsafe external
   action, or more setup than the expected result is worth.

The starter passes when a fresh session completes one useful workflow from the
declared files and sources alone. A polished folder structure is not proof.

## Public Contract

- **Time to first setup:** about 10 minutes.
- **Runtime:** no code required; Python is used only for the optional structural
  check.
- **Model and network:** this repository calls neither.
- **Writes:** the setup prompt permits changes only to three named local files.
- **External authority:** sending, publishing, purchasing, deleting, deploying,
  or changing shared state always requires a separate decision.

The structural check proves that the declared starter files and public-safety
boundaries are present. It does not run an agent, enforce permissions, inspect
your sources, or prove that the workflow will be useful.

## Check The Starter

```sh
python3 -B check_starter.py
```

Expected result:

```text
PASS starter_shape
PASS working_agreement
PASS setup_boundary
PASS public_safe_text
PASS template_links
```

## Share Public-Safe Feedback

After one real first use, you may optionally submit a
[structured first-use report](https://github.com/TheDarkniteFalls/reliable-ai-work-starter/issues/new?template=first-use-report.yml).
The form asks for generalized or synthetic details only. The public
`USAGE_EVIDENCE.md` ledger records only what reporters chose to share and
separates evidence-backed corrections from maintainer judgement.

## Public-Safe Use

Never add private messages, credentials, personal records, customer data,
internal links, connector exports, raw model logs, or unpublished material to
a public copy or public issue. Generalize or substitute synthetic details.

## License

MIT. See `LICENSE`.
