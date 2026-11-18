import pytest
from render import depth_of_field as mod

CASES = [
    ("coc_focus", "m.circle_of_confusion(2.0, 2.0, 1.0) == approx(0.0)"),
    ("coc_near", "m.circle_of_confusion(1.0, 2.0, 1.0) == approx(1.0)"),
    ("coc_far", "m.circle_of_confusion(4.0, 2.0, 1.0) == approx(2.0)"),
    ("focus_average", "m.focus_point([1.0, 3.0]) == approx(2.0)"),
    ("focus_single", "m.focus_point([2.0]) == approx(2.0)"),
    ("upsample_sum", "m.upsample_weight(1.0, 2.0) + m.upsample_weight(2.0, 1.0) == approx(1.0)"),
    ("upsample_near", "m.upsample_weight(1.0, 2.0) > m.upsample_weight(2.0, 1.0)"),
    ("bokeh_grow", "m.bokeh_kernel(2.0) > m.bokeh_kernel(1.0)"),
    ("hdr_keep", "m.preserve_hdr(10.0) == approx(10.0)"),
    ("hdr_floor", "m.preserve_hdr(-1.0) == approx(0.0)"),
    ("sign_far", "m.near_far_sign(3.0, 2.0) == 1"),
    ("sign_near", "m.near_far_sign(1.0, 2.0) == -1"),
    ("hold_full", "m.focus_hold(1.0, 3.0, 1.0, 1.0) == approx(3.0)"),
    ("transition_end", "m.transition_alpha(1.0) == approx(1.0)"),
    ("stereo_mid", "m.stereo_focus(1.0, 3.0) == approx(2.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
