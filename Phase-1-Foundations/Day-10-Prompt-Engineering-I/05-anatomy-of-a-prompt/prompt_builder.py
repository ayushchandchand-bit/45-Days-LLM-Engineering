"""
Anatomy of a good prompt -- assemble the four pieces into one (no API key needed).

Today's techniques are not rivals; they STACK:
  role (system) + clear task (zero-shot) + examples (few-shot) + reasoning (CoT).

This script builds a message list from those parts and prints it, so you can see
the shape of a solid prompt before you send it. It makes no API call -- it just
shows the structure. Drop the returned 'messages' straight into Groq.

Run:
    python prompt_builder.py
"""


def build_messages(role, task, examples, final_input, ask_reasoning=False):
    """Stack the four prompt-engineering pieces into a Groq-ready message list."""
    system = role + " " + task
    if ask_reasoning:
        system += " Think step by step, then put the final answer on the last line."

    messages = [{"role": "system", "content": system}]

    # few-shot: each example becomes a user turn + the ideal assistant turn
    for example_in, example_out in examples:
        messages.append({"role": "user", "content": example_in})
        messages.append({"role": "assistant", "content": example_out})

    # the real task input goes last
    messages.append({"role": "user", "content": final_input})
    return messages


# Build a tiny support-router prompt out of the four pieces.
messages = build_messages(
    role="You route customer messages to a team.",
    task="Reply with only one of: ORDER, REFUND, DELIVERY, OTHER.",
    examples=[
        ("Where is my package?", "DELIVERY"),
        ("I want my money back.", "REFUND"),
    ],
    final_input="Can I change the size on my order?",
    ask_reasoning=False,
)

print("Assembled messages (this is what you'd pass to Groq):")
print("-" * 60)
for turn in messages:
    print(f"[{turn['role']:>9}]  {turn['content']}")

print()
print("The 5-point prompt checklist:")
for item in (
    "1. ROLE      -- who is the assistant? (system)",
    "2. TASK      -- what exactly to do + allowed outputs (zero-shot)",
    "3. EXAMPLES  -- 2-5 worked input->output pairs if format matters (few-shot)",
    "4. REASONING -- 'think step by step' for multi-step problems (CoT)",
    "5. FORMAT    -- pin the output shape so your code can use it",
):
    print("  " + item)
