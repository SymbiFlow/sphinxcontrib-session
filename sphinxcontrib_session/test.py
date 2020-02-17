#!/usr/bin/env python3

import unittest

from sphinxcontrib_session import rewrite_spans

class TestCase(unittest.TestCase):
    maxDiff=None

    def testRewrite(self):
        TEST_CASES = [
            ("""
<span class="gp">&gt;&gt;&gt; </span><span class="n">h</span> <span class="o">=</span> <span class="s1">&#39;hello&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;hello&#39;</span><span class="p">)</span>
<span class="go">hello</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">hello</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="go">h</span>
<span class="go">e</span>
<span class="go">l</span>
<span class="go">l</span>
<span class="go">o</span>
<span class="go">&gt;&gt;&gt;</span>
""", """
<span class="gp" data-content="&gt;&gt;&gt; "></span><span class="n">h</span> <span class="o">=</span> <span class="s1">&#39;hello&#39;</span>
<span class="gp" data-content="&gt;&gt;&gt; "></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;hello&#39;</span><span class="p">)</span>
<span class="go" data-content="hello
"></span><span class="gp" data-content="&gt;&gt;&gt; "></span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">hello</span><span class="p">:</span>
<span class="gp" data-content="... "></span>    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="go" data-content="h
"></span><span class="go" data-content="e
"></span><span class="go" data-content="l
"></span><span class="go" data-content="l
"></span><span class="go" data-content="o
"></span><span class="go" data-content="&gt;&gt;&gt;
"></span>"""),
]

        for before, expected_after in TEST_CASES:
            actual_after = rewrite_spans(before)
            self.assertMultiLineEqual(expected_after, actual_after)


if __name__ == "__main__":
    unittest.main()
