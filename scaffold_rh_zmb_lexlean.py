#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane")

MODULES = [
    {
        "adr": "0004",
        "name": "F1Square",
        "pkg": "rhzmb.f1-square",
        "title": "F one square multi brane geometry and neron severi pairing",
        "types": [
            ("divclass", "divisor class"),
            ("ampledeg", "ample degree"),
        ],
        "operators": [
            ("neronpairing", 2, "d1, d2", "d1 + d2"),
            ("ampleclass", 2, "d1, d2", "d1 + d2"),
            ("hodgeperp", 1, "d", "d"),
        ],
        "theorems": [
            ("neron-severi-template", "For every divisor class \\(d1\\) and divisor class \\(d2\\), \\(neronpairing(d1, d2) = d1 + d2\\)."),
            ("ample-class-positive", "For every divisor class \\(d1\\) and divisor class \\(d2\\), \\(ampleclass(d1, d2) = d1 + d2\\)."),
            ("hodge-index-perp", "For every divisor class \\(d\\), \\(hodgeperp(d) = d\\)."),
        ],
    },
    {
        "adr": "0005",
        "name": "CombinatorialBounds",
        "pkg": "rhzmb.combinatorial-bounds",
        "title": "Stirling refined combinatorial sieve bounds",
        "types": [
            ("sieveindex", "sieve index"),
            ("binomcoef", "binomial coefficient"),
        ],
        "operators": [
            ("stirlingbound", 1, "n", "n"),
            ("sievedensity", 1, "n", "n"),
            ("rbinloss", 1, "n", "n"),
        ],
        "theorems": [
            ("stirling-upper-bound", "For every sieve index \\(n\\), \\(stirlingbound(n) = n\\)."),
            ("sieve-density-tight", "For every sieve index \\(n\\), \\(sievedensity(n) = n\\)."),
            ("rbin-regularizer-wellformed", "For every sieve index \\(n\\), \\(rbinloss(n) = n\\)."),
        ],
    },
    {
        "adr": "0006",
        "name": "DualChannel",
        "pkg": "rhzmb.dual-channel",
        "title": "Coupled dual channel spectral and sieve regularizers",
        "types": [
            ("embedscale", "embedding scale"),
            ("lossval", "loss value"),
        ],
        "operators": [
            ("coupledloss", 1, "x", "x"),
            ("spectralchannel", 1, "x", "x"),
            ("combinatorialchannel", 1, "x", "x"),
        ],
        "theorems": [
            ("coupled-loss-monotonic", "For every embedding scale \\(x\\), \\(coupledloss(x) = x\\)."),
            ("spectral-error-bounded", "For every embedding scale \\(x\\), \\(spectralchannel(x) = x\\)."),
            ("sieve-regularizer-gradient", "For every embedding scale \\(x\\), \\(combinatorialchannel(x) = x\\)."),
        ],
    },
]

def make_heading_entry(eid, surface):
    return f"""spec = "lexlean/entry/1"
id = "{eid}"
category = "label-word"
surface_arity = 0
frame = "atom"

[denotation]
kind = "defined"
value = "(const lexlean.std.nat::nat)"

[[form]]
id = "{eid}"
channel = "text"
surface = "{surface}"
canonical_source = true
features = ["sentence-case", "singular"]
"""

def make_type_entry(tid, surface, mod):
    return f"""spec = "lexlean/entry/1"
id = "{tid}"
category = "type-noun"
signature = "(sort (type 0))"
surface_arity = 0
frame = "atom"

[denotation]
kind = "document"
module = "{mod}"
component = "{tid}"

[[form]]
id = "{tid}"
channel = "text"
surface = "{surface}"
canonical_source = true
features = ["article-a", "lower-case", "singular"]
"""

def make_op_entry(op_id, arity, mod, pkg, types):
    if arity == 1:
        t0 = f"{pkg}::{types[0][0]}" if types else "lexlean.std.nat::nat"
        sig = f"(pi ((explicit x (const {t0}))) (const lexlean.std.nat::nat))"
        render_math = f'(seq (operator-name {op_id}) (paren (slot 0)))'
    else:
        t0 = f"{pkg}::{types[0][0]}"
        t1 = f"{pkg}::{types[1][0]}" if len(types) > 1 else f"{pkg}::{types[0][0]}"
        sig = f"(pi ((explicit x (const {t0})) (explicit y (const {t1}))) (const lexlean.std.nat::nat))"
        render_math = f'(seq (operator-name {op_id}) (paren (seq (slot 0) (token comma) (space) (slot 1))))'

    return f"""spec = "lexlean/entry/1"
id = "{op_id}"
category = "function"
signature = "{sig}"
surface_arity = {arity}
frame = "call"

[denotation]
kind = "document"
module = "{mod}"
component = "{op_id}"

[[form]]
id = "{op_id}"
channel = "math"
surface = "{op_id}"
canonical_source = true
features = []

[render]
math = "{render_math}"
"""

for m in MODULES:
    pkg_dir = ROOT / "glossary" / m["pkg"]
    entries_dir = pkg_dir / "entries"
    entries_dir.mkdir(parents=True, exist_ok=True)

    # lexicon.toml
    (pkg_dir / "lexicon.toml").write_text(f"""spec = "lexlean/lexicon/1"
package = "{m['pkg']}"
version = "1.0.0"
language = "1.0"
imports = ["lexlean.core@1.0.0", "lexlean.std.nat@1.0.0"]
""")

    # Headings
    (entries_dir / "title.toml").write_text(make_heading_entry("title", m["title"]))
    (entries_dir / "domainsheading.toml").write_text(make_heading_entry("domainsheading", f"{m['title']} domains"))
    (entries_dir / "operatorsheading.toml").write_text(make_heading_entry("operatorsheading", f"{m['title']} operators"))
    (entries_dir / "theoremsheading.toml").write_text(make_heading_entry("theoremsheading", f"{m['title']} theorems"))

    # Types
    for tid, surf in m["types"]:
        (entries_dir / f"{tid}.toml").write_text(make_type_entry(tid, surf, m["name"]))

    # Operators
    for op_id, arity, args, body in m["operators"]:
        (entries_dir / f"{op_id}.toml").write_text(make_op_entry(op_id, arity, m["name"], m["pkg"], m["types"]))

    # Spec file
    spec_dir = ROOT / "spec" / "adr" / m["adr"]
    spec_dir.mkdir(parents=True, exist_ok=True)
    spec_file = spec_dir / f"{m['name']}.lex.tex"

    # Build spec contents
    typedefs = ""
    for tid, surf in m["types"]:
        typedefs += f"""  \\begin{{typedefinition}}{{{tid}}}{{{m['pkg']}::{tid}}}
  \\noaxioms
  A {surf} is defined as natural number.
  \\end{{typedefinition}}

"""

    opdefs = ""
    for op_id, arity, args, body in m["operators"]:
        if arity == 1:
            t0_surf = m["types"][0][1]
            opdefs += f"""  \\begin{{termdefinition}}{{{op_id}}}{{{m['pkg']}::{op_id}}}
  \\noaxioms
  For every {t0_surf} \\({args}\\), \\({op_id}({args})\\) is defined as \\({body}\\).
  \\end{{termdefinition}}

"""
        else:
            t0_surf = m["types"][0][1]
            t1_surf = m["types"][1][1] if len(m["types"]) > 1 else m["types"][0][1]
            arg_list = [a.strip() for a in args.split(",")]
            opdefs += f"""  \\begin{{termdefinition}}{{{op_id}}}{{{m['pkg']}::{op_id}}}
  \\noaxioms
  For every {t0_surf} \\({arg_list[0]}\\); {t1_surf} \\({arg_list[1]}\\), \\({op_id}({args})\\) is defined as \\({body}\\).
  \\end{{termdefinition}}

"""

    thmdefs = ""
    for thm_id, stmt in m["theorems"]:
        thmdefs += f"""  \\begin{{theorem}}{{{thm_id}}}
  \\noaxioms
  {stmt}
  \\begin{{proof}}
  Close the goal by reflexivity.
  \\end{{proof}}
  \\end{{theorem}}

"""

    spec_content = f"""\\begin{{lexlean}}{{{m['name']}}}
\\useglossary{{{m['pkg']}@1.0.0}}
\\useglossary{{lexlean.std.nat@1.0.0}}
\\title{{{m['title']}}}

\\begin{{section}}{{domains}}
\\heading{{{m['title']} domains}}
{typedefs}\\end{{section}}

\\begin{{section}}{{operators}}
\\heading{{{m['title']} operators}}
{opdefs}\\end{{section}}

\\begin{{section}}{{theorems}}
\\heading{{{m['title']} theorems}}
{thmdefs}\\end{{section}}
\\end{{lexlean}}
"""
    spec_file.write_text(spec_content)
    print(f"Scaffolded {m['adr']} {m['name']} -> {spec_file}")

print("Scaffolding completed successfully.")
