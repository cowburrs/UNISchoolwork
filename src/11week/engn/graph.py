from graphviz import Digraph

dot = Digraph(
    graph_attr={
        "rankdir": "TB",
        "splines": "ortho",
        "nodesep": "0.7",
        "ranksep": "1.1",
        "bgcolor": "white",
        "fontname": "Aporetic Sans",
        "pad": "0.5",
    },
    node_attr={
        "fontname": "Aporetic Sans",
        "fontsize": "11",
    },
    edge_attr={
        "fontname": "Aporetic Sans",
        "fontsize": "9",
        "color": "#555555",
    },
)

entry = {
    "shape": "box",
    "style": "filled,rounded",
    "fillcolor": "#FFD966",
    "color": "#B8960A",
    "penwidth": "2",
}
decision = {
    "shape": "diamond",
    "style": "filled",
    "fillcolor": "#A8D8D8",
    "color": "#3A8A8A",
    "penwidth": "1.5",
}
action = {
    "shape": "box",
    "style": "filled,rounded",
    "fillcolor": "#D9EAD3",
    "color": "#5A8A5A",
    "penwidth": "1.5",
}
terminal = {
    "shape": "box",
    "style": "filled,rounded",
    "fillcolor": "#F4CCCC",
    "color": "#C07070",
    "penwidth": "1.5",
}

dot.node("loop_start", "loop()", **entry)
dot.node("read_sensors", "readSideSensor(20)\nreadFrontSensor(20)", **action)
dot.node("cond_even1", "movenumber%2==0\n&& front>10\n&& noSideWall(side)?", **decision)
dot.node("turn_left_1", "turnLeft(turnleftdelta)\nstop(100)", **action)
dot.node("reread_sensors", "Re-read front & side sensors", **action)
dot.node("cond_A", "movenumber%2==0\n&& front<10\n&& noSideWall(side)?", **decision)
dot.node(
    "moveUntil_A", "moveUntil(target)\nmovenumber=0\nturnLeft(turnleftdelta)", **action
)
dot.node("check45_A", "check45()?", **decision)
dot.node(
    "move_fwd_A", "moveForward(...)\nstop(100)\npdMoveForward(...)\nstop(100)", **action
)
dot.node("turn_right_2x", "turnRight x2\nwith stop(100)", **action)
dot.node("cond_B", "movenumber%2==0?", **decision)
dot.node("cond_front", "front < 10?", **decision)
dot.node(
    "moveUntil_B",
    "moveUntil(target)\nmovenumber=0\nturnRight(turnrightdelta)\nstop(100)",
    **action,
)
dot.node("cond_45", "check45()?", **decision)
dot.node(
    "turn_move_fwd",
    "turnRight(turnrightdelta)\nstop(100)\nmoveForward x2\nstop(100) each",
    **action,
)
dot.node("pd_even", "pdMoveForward(...)\nmovenumber++\nstop(100)", **action)
dot.node("pd_odd", "pdMoveForward(...)\nmovenumber++\nstop(100)", **action)
dot.node("loop_end", "→ next loop()", **terminal)

dot.edge("loop_start", "read_sensors")
dot.edge("read_sensors", "cond_even1")
dot.edge("cond_even1", "turn_left_1", label="Yes")
dot.edge("cond_even1", "reread_sensors", label="No")
dot.edge("turn_left_1", "reread_sensors")
dot.edge("reread_sensors", "cond_A")
dot.edge("cond_A", "moveUntil_A", label="Yes")
dot.edge("moveUntil_A", "check45_A")
dot.edge("check45_A", "move_fwd_A", label="No")
dot.edge("check45_A", "turn_right_2x", label="Yes")
dot.edge("move_fwd_A", "loop_end")
dot.edge("turn_right_2x", "loop_end")
dot.edge("cond_A", "cond_B", label="No")
dot.edge("cond_B", "cond_front", label="Yes (even)")
dot.edge("cond_front", "moveUntil_B", label="Yes")
dot.edge("cond_front", "cond_45", label="No")
dot.edge("cond_45", "turn_move_fwd", label="Yes")
dot.edge("cond_45", "pd_even", label="No")
dot.edge("moveUntil_B", "loop_end")
dot.edge("turn_move_fwd", "loop_end")
dot.edge("pd_even", "loop_end")
dot.edge("cond_B", "pd_odd", label="No (odd)")
dot.edge("pd_odd", "loop_end")

dot.render("loop_flowchart", format="png", view=False, cleanup=True)
print("Done! loop_flowchart.png generated.")
