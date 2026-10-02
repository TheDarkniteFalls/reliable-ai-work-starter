# Reliable AI Work Starter

Start one recurring job with an AI assistant and a small set of files you can
read and edit. Keep your copy private: this is where you name the job, choose
its sources, and say what the assistant must ask before doing.

For example, you could try drafting a weekly project update from notes you
choose to provide. The starter gives you a place to keep those choices and
review the saved result in a later session. It does not run the assistant or
enforce its permissions.

You do not need to build an app or connect a collection of services to begin.
Create your copy, use the setup prompt below, then try one job from start to
finish.

## Create your private copy

[Create a private repository from this starter](https://github.com/new?template_owner=TheDarkniteFalls&template_name=reliable-ai-work-starter&visibility=private),
then open the new repository in Codex.

If you prefer a local folder, use GitHub's **Code → Download ZIP** action and
extract it somewhere private. Keep real source material in your own copy, not
in a public issue or pull request.

## Set up your first job

Open a fresh Codex session in your copied starter and paste this prompt.
Review the proposed setup before approving changes to the three named files:

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

<!-- toolkit-trust-card:placement -->

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

## Find your way around the files

- `WORKING_AGREEMENT.md` names the job, trusted sources, permitted
  actions, and checks needed before calling the work done.
- `TODAY.md` keeps the current job, next steps, blockers, and
  results waiting for your review in one place.
- `SOURCE_SHELF.md` records which questions each source can answer,
  how old it is, and when you should check it again.
- `REVIEW_LOG.md` records whether you used, changed or rejected an
  important result, and what you learned.
- `context/` holds short notes with their sources and confidence labels.
- `outputs/` holds results you want to keep and reuse.

Keep these files short. Save what the next session needs to continue the job;
you do not need to copy every conversation into them.

## Try one complete workflow

Once the setup is agreed:

1. Use a fresh session that can see only this workspace and sources you
   deliberately add.
2. Run the one agreed job and save its output.
3. Check that the result names its sources, uncertainty, checks performed,
   next action, and the person responsible for that action.
4. Record whether the result was used, edited, rejected, or superseded.
5. Stop if the workflow needs hidden state, broad access, an unsafe external
   action, or more setup than the expected result is worth.

For your first-use test, success means a fresh session completes one useful
job using the files and sources you named. Review the actual output before
deciding whether to keep using the workflow.

## What this starter does

- **Time to first setup:** about 10 minutes.
- **Runtime:** no code required; Python is used only for the optional structural
  check.
- **Model and network:** this repository calls neither.
- **Writes:** the setup prompt permits changes only to three named local files.
- **External authority:** sending, publishing, purchasing, deleting, deploying,
  or changing shared state always requires a separate decision.

## What the structural check tells you

If you have Python, run this optional check from the starter folder:

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

These five passes confirm the expected files, agreement sections, setup
boundary, safety wording and template links are present. They do not run an
agent, enforce permissions, inspect your sources, or show whether the workflow
will be useful. That needs the first-use test above.

## Share feedback if you want to

After one real first use, you may optionally submit a
[structured first-use report](https://github.com/TheDarkniteFalls/reliable-ai-work-starter/issues/new?template=first-use-report.yml).
The form asks for generalized or synthetic details only. The public
`USAGE_EVIDENCE.md` ledger records only what reporters chose to share and
separates evidence-backed corrections from maintainer judgement.

## Keep private material in your own copy

Never add private messages, credentials, personal records, customer data,
internal links, connector exports, raw model logs, or unpublished material to
a public copy or public issue. Generalize or substitute synthetic details.

## License

MIT. See `LICENSE`.
