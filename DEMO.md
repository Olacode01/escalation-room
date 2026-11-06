# Demo script (about 3 minutes)

Record the Discord window, with the Switch Console visible for the first 20 seconds.
Post each customer message from a **second Discord account** (a teammate, or an
alt account you invite to `acme-support`), so it's clearly a customer and not you.

## 0:00 - Setup (20 s)
Show Switch Console -> Templates -> **Escalation Room**, team `acme`, bridge Discord -> Create.
Cut to Discord: two new channels, `#acme-support` and `#acme-war-room`, three agents saying hello.
Say: *"Three agents, two rooms, one person who has to sign off. Here's a normal support morning."*

## 0:20 - Three customers (30 s)
Paste these into `#acme-support`, one at a time. **Keep the `@support` at the start.** Switch agents only act when mentioned, so a message without it gets no reply.

**Customer A (Maya), BUG:**
> @support Hi, I used SAVE10 on my order (cable $15, headphones $60, case $25) and got charged $106.38. That's way more than 10% off a $100 order?

**Customer B (Jordan), BUG:**
> @support My jacket was exactly $75, and your site says free shipping from $75, but I paid $6.99 shipping. Total was $87.99.

**Customer C (Sam), QUESTION:**
> @support Can I use SAVE10 together with another coupon?

What should happen: Intake numbers them #1 #2 #3. It answers #3 straight from the Support policy doc ("coupons don't stack") and escalates #1 and #2 to the war room.

## 0:50 - The war room works (60 s)
Switch to `#acme-war-room`. Show:
- `ESCALATION #1` and `#2` addressed to @acme-engineer.
- The engineer writing a failing test, pasting real pytest output, naming the cause: `apply_coupon` only discounts the first line item (case 1), and `shipping_for` uses `>` instead of `>=` (case 2).
- `FIX READY #1` with the diff, and the impact: Maya overpaid $9.18.
- `DRAFT REPLY #1` from @acme-comms, with the refund ($9.18) plus a 10% store credit, citing the policy.

Say: *"Nothing has been merged and nothing has gone to Maya. They're waiting for me."*

## 1:50 - Human in the loop (30 s)
Type in `#acme-war-room`:
> @acme-engineer @acme-comms CHANGES #1 make the reply shorter and mention the credit is already on her account

Comms revises. Then:
> @acme-engineer @acme-comms APPROVED #1

Show the engineer merging `fix/case-1` and posting the commit hash, and comms posting the reply to Maya in `#acme-support`.
Then `@acme-engineer @acme-comms APPROVED #2`.

## 2:20 - The big one (25 s, optional but strong)
**Customer D (Northwind Ltd), BUG:**
> @support Office order: headset $20, monitor $400, desk $300 with SAVE10. We were charged $775.44. Please check.

Intake should link it to #1 (same coupon bug, already fixed). Comms works out the overcharge is $75.60. That's over the $50 limit, so it asks for explicit sign-off instead of promising anything. Approve it on camera.

## 2:45 - Close (15 s)
Show the **Case log** doc in the war room filled in: 4 cases, owners, decisions.
Say: *"Without Switch, these are three agents in three terminals and me copy-pasting between them and Discord. With Switch, it's one team in a channel, and I only step in to decide."*

---

### Expected numbers (check before recording)

| Case | Charged (bug) | Correct | Overcharge |
|------|---------------|---------|------------|
| #1 Maya | $106.38 | $97.20 | $9.18 |
| #2 Jordan | $87.99 | $81.00 | $6.99 |
| #4 Northwind | $775.44 | $699.84 | $75.60 |

Reproduce any of them with `python demo-app/checkout.py SAVE10 "Cable:15" "Headphones:60" "Case:25"`.

### Before every take
`git checkout main && git reset --hard demo-start` in the shop repo, so the bugs are back. (Tag the clean buggy commit as `demo-start` once: `git tag demo-start && git push --tags`.)
